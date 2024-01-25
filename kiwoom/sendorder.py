from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("ok")

accounts = kiwoom.GetLogInfo("ACCNO")
account = accounts.spilt(';')[0]

kiwoom.SendOrder("매수", "0101", account, 1, "005930", 10, 0, "03", "") 