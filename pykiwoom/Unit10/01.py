import pandas as pd


df = pd.read_excel("경방.xlsx")
df2 = df[['현재가', '일자']].copy()

# 컬럼 이름 변경
df2.rename(columns={"현재가": "경방"}, inplace=True)              # 현재가 컬럼을 경방으로 변경
df2 = df2.set_index("일자")                                       # 인데스를 일자로 변경 
df2 = df2[::-1]                                                  # 인덱스를 오름차순으로 변경
print(df2)