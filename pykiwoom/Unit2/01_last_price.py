from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()

price = kiwoom.GetMasterLastPrice("005930")

print(price, type(price))
