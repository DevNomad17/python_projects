# import csv
import pandas

FILE_PATH = "weather_data.csv"

# data = []
#
# with open(FILE_PATH, "r") as file:
#     for line in file:
#         data.append(line.strip())
#
# print(data)

# with open(FILE_PATH, "r") as data_file:
#     temperatures = []
#     data = csv.reader(data_file)
#     next(data)
#     for line in data:
#         temperatures.append(int(line[1]))

# print(temperatures)

data = pandas.read_csv(FILE_PATH)
print(f"Average temperature: {data['temp'].mean():.2f}")
print(f"Maximum temperature: {data['temp'].max()}")

print(data[data.temp == data['temp'].max()])
