import pandas
import xml.etree.ElementTree as ET
from getAssetsResponse import GetAssetsResponse
from asset import Asset
from aggregatedResponse import AggregatedResponseWithFilter

INPUT_FILE_PATH_RAW = "../confidential_resources/getAssets_kibana_max_magenta.json"
INPUT_FILE_PATH_JSON = "../confidential_resources/getAssets_kibana_max_magenta_trimmed.json"
TEMP_FILE_PATH = "temp_file.xml"
OUTPUT_FILE_PATH = "aggregated_responses.json"


def remove_namespace_prefixes(root):
    for elem in root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}')[-1]


def print_tree(asset_param, level=0):
    indent = "  " * level
    print(f"{indent}Asset: {asset_param.asset_id}, Product Code: {asset_param.product_code}")
    for child in asset_param.children:
        print_tree(child, level + 1)


# convert(INPUT_FILE_PATH_RAW, INPUT_FILE_PATH_JSON) # needs to be done only once

df_json = pandas.read_json(INPUT_FILE_PATH_JSON)
responseArray = []

for hit in df_json.hits.hits:
    restResponseBody = hit['_source']['rest.responseBody']
    with open(TEMP_FILE_PATH, 'w', encoding='utf-8') as file:
        file.write(restResponseBody)

    # Parse the XML file using the custom parser
    tree = ET.parse(TEMP_FILE_PATH)

    # Get the root element
    root = tree.getroot()
    remove_namespace_prefixes(root)

    # Use findall() with an XPath expression to get all elements with the tag name 'getAssetsResponseParameters'
    getAssetsResponseXml = root.find('.//getAssetsResponseParameters')

    # Initialize the GetAssetsResponse object
    response = GetAssetsResponse()

    # Parse each asset in the XML
    for asset_elem in getAssetsResponseXml.findall("asset"):
        asset_id = asset_elem.find("id").text
        product_code = asset_elem.find("product/productNumber").text
        parent_asset_elem = asset_elem.find("parentAsset/id")
        parent_asset_id = parent_asset_elem.text if parent_asset_elem is not None else None

        # Create an Asset object
        asset = Asset(asset_id, product_code, parent_asset_id)
        response.add_asset(asset)

    # Build the logical tree structure
    response.build_tree()
    responseArray.append(response)

# Product codes to filter by
product_codes_to_filter = {}  # Replace with your desired product codes e.g. {"SX0074", "SC1688"}

aggregator = AggregatedResponseWithFilter(OUTPUT_FILE_PATH)

for response in responseArray:  # Replace with actual array of GetAssetsResponse objects
    aggregator.add_response(response)

# Write filtered groups to file
aggregator.write_filtered_responses(product_codes_to_filter)
