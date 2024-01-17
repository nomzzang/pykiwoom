from pandas import DataFrame
import datetime

#DataFrame = Excel Sheet
#raw -> 2차원
data = [[100,200,300,400],
        [200,400,600,800]]

#문자열을 날짜타입으로..
date = ["2020-05-15", "2020-04-14"]
index = [datetime.datetime.strptime(i, "%Y-%m-%d")for i in date]

columns = ['open', 'high', 'low', 'close']
df = DataFrame(data=data, columns=columns, index=index)
print(df)

# date = ["2020-05-15", "2020-05-14"]
# columns = ['open', 'high', 'low', 'close']
# df = DataFrame(data=data, columns=columns, index=data)
# print(df)
