import os
import pandas as pd

flist = os.listdir('C:\\Users\\weather\\Desktop\\pykiwoom\\pykiwoom\\Unit10')  #폴더에 있는 파일 리스트
xlsx_list = [x for x in flist if x.endswith(".xlsx")]                          #.xlsx로 끝나는 파일을 xlsx_list에 넣는다. 

close_data = []
for xlsx in xlsx_list:
    code_name = xlsx.split(".")[0]

    df = pd.read_excel(xlsx)
    df2 = df[['현재가', '일자']].copy()
    df2.rename(columns={'현재가': code_name}, inplace=True)    
    df2 = df2.set_index('일자')
    df2 = df2[::-1]


    close_data.append(df2)

df = pd.concat(close_data, axis=1)
df.to_excel("merge.xlsx")
