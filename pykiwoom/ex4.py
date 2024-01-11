from kiwoom import *
from pandas import DataFrame

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인")

kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
codes = kospi + kosdaq

data = []
for code in codes:
    name = kiwoom.GetMasterCodeName(code)
    data.append((code, name))

df = DataFrame(data=data, columns=['code', '종목명'])
df = df.set_index('code')
df.to_excel("code.xlsx")
