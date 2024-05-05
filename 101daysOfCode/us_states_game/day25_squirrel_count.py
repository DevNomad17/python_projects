from urllib.parse import urlencode
import pandas

# example URL with params : "https://data.cityofnewyork.us/resource/vfnx-vebw.json?$limit=50&$offset=150"

# Base URL
base_url = "https://data.cityofnewyork.us/resource/vfnx-vebw.json"
record_count = 900
i = 0
merged_count_table = pandas.Series()

# Parameters as a dictionary


while True:
    params = {
        "$limit": record_count,
        "$offset": i * record_count
    }

    i += 1

    # Encode parameters and append them to the base URL
    url_with_params = base_url + "?" + urlencode(params)

    # Read batch of json data from url with pandas
    data = pandas.read_json(url_with_params)
    if data.empty:
        break

    # Count unique fur color values
    count_table = data.primary_fur_color.value_counts()

    # Merge count of this batch with count of previous batches
    merged_count_table = merged_count_table.add(count_table, fill_value=0)

print(merged_count_table)


