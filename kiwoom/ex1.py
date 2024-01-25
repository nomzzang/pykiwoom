from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("login")

codes = kiwoom.GetCodeListByMarket('0')
for code in codes:
    name = kiwoom.GetMasterCodeName(code)

    if '삼성' in name:
        print(code, name)
