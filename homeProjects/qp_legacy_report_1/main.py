import pandas
import xml.etree.ElementTree as ET
import re


INPUT_FILE_PATH_1 = "../confidential_resources/quick_prolong_apr11_to_may10.json"
INPUT_FILE_PATH_2 = "../confidential_resources/quick_prolong_mar11_to_apr10.json"
TEMP_FILE_PATH = "temp_file.xml"
OUTPUT_FILE_PATH_TARIFFS = "output_file_tariffs.csv"
OUTPUT_FILE_PATH_VAS = "output_file_vas.csv"
SYLIUS_RATEPLAN_CONFIG_PATH = "../confidential_resources/rateplan_config.txt"
MVP_RATEPLAN_CONFIG_PATH = "../confidential_resources/mvp_rateplans.txt"


def extract_siebel_codes(text):
    # Define the regular expression pattern
    pattern = r'\b(?:RP|SC|HW)\d{4}\b'

    # Use re.findall() to extract all substrings that match the pattern
    siebel_codes = re.findall(pattern, text)

    return siebel_codes


def remove_namespace_prefixes(root):
    for elem in root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}')[-1]


def extract_rp_substrings(text):
    # Define the regular expression pattern to match 'RP' followed by four digits
    pattern = r'\bRP\d{4}\b'

    # Use re.findall() to extract all substrings that match the pattern
    rp_matches = re.findall(pattern, text)

    # Concatenate the matched substrings with a dash as a delimiter
    rp_substr = '-'.join(rp_matches)

    return rp_substr


def extract_rp_names(text):
    # Define the regular expression pattern to match 'RP' followed by four digits
    pattern = r'\bRP\d{4}\b'

    # Use re.findall() to extract all substrings that match the pattern
    lines = text.split('\n')
    matched_lines = ""

    for line in lines:
        # Check if the line contains the pattern
        if re.search(pattern, line):
            # If the pattern is found, add the line to the matched_lines list
            index_of_equal_sign = line.find('=')
            line = line[:index_of_equal_sign].strip()
            matched_lines += (line + ' - ')

    return matched_lines[:-2].strip()


def aggregated_rp_desc(name, mvp, sylius):
    if mvp:
        mvp_text = ''
    else:
        mvp_text = '|NotMVP'

    if sylius:
        sylius_text = ''
    else:
        sylius_text = '|NotSylius'

    return name + mvp_text + sylius_text


def create_data_frame_tariffs():
    # Define column names
    columns = ['tariffId', 'tariffDesc', 'isMvp', 'isSylius', 'router', 'stb']

    # Create an empty DataFrame with specified columns
    df = pandas.DataFrame(columns=columns)

    return df


def create_data_frame_vas():
    # Define column names
    columns = ['vasId', 'vasDesc', 'count']

    # Create an empty DataFrame with specified columns
    df = pandas.DataFrame(columns=columns)

    return df


def count_tv_hw(multiline_string):
    # Define the pattern to match dash followed by exactly one number followed by 'x'
    pattern = r'-(\d)x'

    # Find all matches of the pattern in the multiline string
    matches = re.findall(pattern, multiline_string)

    # Convert the matched numbers to integers and sum them up
    total = sum(int(match) for match in matches)

    return total


def update_vas_dict(vas_dict, text):
    # Define the regular expression pattern to match 'SC' followed by four digits and optional suffix
    pattern = r'\b(?:SC)\d{4}(?:_\d)?\b'

    # Use re.findall() to extract all substrings that match the pattern
    lines = text.split('\n')

    for line in lines:
        # Check if the line contains the pattern
        if re.search(pattern, line):
            # If the pattern is found, add the line to the matched_lines list
            index_of_equal_sign = line.find('=')
            line = line[:index_of_equal_sign].strip()
            if line in vas_dict:
                vas_dict[line] += 1
            else:
                vas_dict[line] = 1


tariff_output_df = create_data_frame_tariffs()
vas_dict = {}

sylius_rateplan_config = pandas.read_csv(SYLIUS_RATEPLAN_CONFIG_PATH).to_dict('list')['sylius_code']
mvp_rateplan_config = pandas.read_csv(MVP_RATEPLAN_CONFIG_PATH).to_dict('list')['sylius_code']

for i in range(2):
    if i == 0:
        df_json = pandas.read_json(INPUT_FILE_PATH_1)
    else:
        df_json = pandas.read_json(INPUT_FILE_PATH_2)

    for hit in df_json.hits.hits:
        xml_ore = hit['_source']['rest']['tibcoRequest']['data']
        with open(TEMP_FILE_PATH, 'w', encoding='utf-8') as file:
            file.write(xml_ore)

        # Parse the XML file using the custom parser
        tree = ET.parse(TEMP_FILE_PATH)

        # Get the root element
        root = tree.getroot()
        remove_namespace_prefixes(root)

        # Use findall() with an XPath expression to get all elements with the tag name 'orderRequestAttributes/value'
        value_element = root.findall('.//orderRequestAttributes/value')

        # Print the text content of the first 'orderRequestAttributes/value' element found
        if value_element:
            order_note = value_element[0].text

            rp_substrings = extract_rp_substrings(order_note)

            # Split the multi-line string into lines
            order_note_lines = order_note.split('\n')

            # Iterate through each line and find the one that contains substrings of interest
            router_line = None
            for line in order_note_lines:
                if 'router' in line or 'Wow' in line:
                    router_line = line
                    index_of_equal_sign = router_line.find('=')
                    router_line = router_line[:index_of_equal_sign].strip()
                    break

            isMvp = rp_substrings in mvp_rateplan_config
            isSylius = rp_substrings in sylius_rateplan_config

            new_line = {'tariffId': rp_substrings,
                        'tariffDesc': aggregated_rp_desc(extract_rp_names(order_note), isMvp, isSylius),
                        'isMvp': isMvp, 'isSylius': isSylius,
                        'router': router_line, 'stb': count_tv_hw(order_note)}
            new_df = pandas.DataFrame([new_line])
            tariff_output_df = pandas.concat([tariff_output_df, new_df], ignore_index=True)
            update_vas_dict(vas_dict, order_note)
        else:
            print("No 'orderRequestAttributes/value' elements found")

tariff_output_df.to_csv(OUTPUT_FILE_PATH_TARIFFS, sep=';', index=False)

vas_df = pandas.DataFrame(list(vas_dict.items()), columns=['Key', 'Value'])
vas_df.to_csv(OUTPUT_FILE_PATH_VAS, sep=';', index=False)

