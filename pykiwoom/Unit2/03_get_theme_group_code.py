from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()

group = kiwoom.GetThemeGroupList(type=0)  #'141' : xxx
print(group['141'])

tickers = kiwoom.GetThemeGroupCode('141')
print(tickers)


for code in tickers:
    name = kiwoom.GetMasterCodeName(code)
    print(code, name)