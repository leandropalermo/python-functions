import pandas

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
newDF = df.rename(columns={'Primary Fur Color': 'Fur Color'})
furColorSeries = newDF['Fur Color']
count = furColorSeries.value_counts()
# grayQtt = furColorSeries.value_counts()
# cQtt = furColorSeries.Cinnamon.counts()
# bQtt = furColorSeries.Black.counts()
#
# data = {
#     "Full Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grayQtt, cQtt, bQtt]
# }
print(count)
df = pandas.DataFrame(count)
df.to_csv("squirrel_count.csv")
