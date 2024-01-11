from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인")

codes = kiwoom.GetCodeListByMarket('0') + kiwoom.GetCodeListByMarket('10')

for code in codes:
    state = kiwoom.GetMasterStockState(code)
    tokens = state.split("|")

    target = False
    if '거래정지' in tokens:
        target = True
    elif '관리종목' in tokens:
        target = True 
    elif '감리종목' in tokens:
        target = True
    elif '투자유의종목' in tokens:
        target = True

    if target is True:
        print(code, state)