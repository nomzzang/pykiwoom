from pykiwoom.kiwoom import *

kiwoom = Kiwoom(login=True)

kospi = kiwoom.GetCodeListByMarket('0') # kospi
kosdaq = kiwoom.GetCodeListByMarket('10') #kosdaq

codes = kospi + kosdaq

print(codes)
print(len(codes))
