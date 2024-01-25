from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("login")


samsung = []
codes = kiwoom.GetCodeListByMarket('0')
for code in codes:
    name = kiwoom.GetMasterCodeName(code)

    if '삼성' in name:
        samsung.append(code)


print(samsung)
print(len(samsung))