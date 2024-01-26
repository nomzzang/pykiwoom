from pykiwoom.kiwoom import *

kiwoom = Kiwoom(login=True)

accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

kiwoom.SendOrder("시장가매도", "0101", stock_account, 2, "005930", 10, 0, "03", "")
