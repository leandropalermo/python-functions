import csv
import pandas


#### Reading a csv file using csv library

# temperatures = []
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

#### Reading a csv file using pandas
pandasDataFrameObject = pandas.read_csv("weather_data.csv")
print(pandasDataFrameObject)
print(type(pandasDataFrameObject))

pandasSeriesObject = pandasDataFrameObject['temp']
print(type(pandasSeriesObject))
print(pandasSeriesObject)

##Convert the dataFrame to a Json (Dictionary) format
dict_data = pandasDataFrameObject.to_dict()
print(dict_data)

##Convert the Series to List format
temp_list_data = pandasSeriesObject.to_list()
print(temp_list_data)
avg_from_list = sum(temp_list_data) / len(temp_list_data)
print(f"Average temperature from list: {round(avg_from_list)}")

avg_from_pandas_library = pandasSeriesObject.mean()
print(f"Average temperature from pandas library: {round(avg_from_pandas_library)}")

max_value = pandasSeriesObject.max()
print(f"Max temperature from pandas library: {max_value}")

print(pandasDataFrameObject[pandasDataFrameObject.day == "Sunday"])
print(pandasDataFrameObject[pandasDataFrameObject.temp == max_value])
