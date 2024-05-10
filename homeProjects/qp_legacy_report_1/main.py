import pandas
import xml.etree.ElementTree as ET
import re


def extract_siebel_codes(text):
    # Define the regular expression pattern
    pattern = r'\b(?:RP|SC|HW)\d{4}\b'

    # Use re.findall() to extract all substrings that match the pattern
    siebel_codes = re.findall(pattern, text)

    return siebel_codes


def remove_namespace_prefixes(root):
    """
    Removes namespace prefixes from element tags in the XML tree.

    Args:
    - root: The root element of the XML tree.
    """
    for elem in root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}')[-1]


def extract_rp_substrings(text):
    """
    Extracts all substrings that have the prefix 'RP' followed by four digits
    from the input text and concatenates them with a dash as a delimiter.

    Args:
    - text (str): The input text to search for substrings.

    Returns:
    - rp_substrings (str): A string containing all matched substrings concatenated with a dash.
    """
    # Define the regular expression pattern to match 'RP' followed by four digits
    pattern = r'\bRP\d{4}\b'

    # Use re.findall() to extract all substrings that match the pattern
    rp_matches = re.findall(pattern, text)

    # Concatenate the matched substrings with a dash as a delimiter
    rp_substr = '-'.join(rp_matches)

    return rp_substr


def create_data_frame():
    # Define column names
    columns = ['tariffId', 'isMvp', 'isSylius', 'router', 'stb', 'otherVas']

    # Create an empty DataFrame with specified columns
    df = pandas.DataFrame(columns=columns)

    return df


INPUT_FILE_PATH = "quick_prolong_1day.json"
TEMP_FILE_PATH = "temp_file.xml"
OUTPUT_FILE_PATH = "output_file.csv"
SYLIUS_RATEPLAN_CONFIG_PATH = "rateplan_config.txt"
MVP_RATEPLAN_CONFIG_PATH = "mvp_rateplans.txt"

output_df = create_data_frame()

sylius_rateplan_config = pandas.read_csv(SYLIUS_RATEPLAN_CONFIG_PATH).to_dict('list')['sylius_code']
mvp_rateplan_config = pandas.read_csv(MVP_RATEPLAN_CONFIG_PATH).to_dict('list')['sylius_code']

df_json = pandas.read_json(INPUT_FILE_PATH)

xml_ore = df_json.hits.hits[4]['_source']['rest']['tibcoRequest']['data']

with open(TEMP_FILE_PATH, 'w', encoding='utf-8') as file:
    file.write(xml_ore)

# Parse the XML file using the custom parser
tree = ET.parse(TEMP_FILE_PATH)

# Get the root element
root = tree.getroot()
remove_namespace_prefixes(root)

# Use findall() with an XPath expression to get all elements with the tag name 'orderRequestSalesOrderItem'
value_element = root.findall('.//orderRequestAttributes/value')

# Print the text content of the first 'orderRequestSalesOrderItem' element found
if value_element:
    order_note = value_element[0].text
    # print(order_note)
    siebel_codes_list = extract_siebel_codes(order_note)
    rp_substrings = extract_rp_substrings(order_note)
    new_line = {'tariffId': rp_substrings, 'isMvp': rp_substrings in mvp_rateplan_config,
                'isSylius': rp_substrings in sylius_rateplan_config, 'router': 'premium',
                'stb': 1, 'otherVas': siebel_codes_list}
    new_df = pandas.DataFrame([new_line])
    output_df = pandas.concat([output_df, new_df], ignore_index=True)
else:
    print("No 'orderRequestSalesOrderItem' elements found")

output_df.to_csv(OUTPUT_FILE_PATH, sep=';', index=False)
