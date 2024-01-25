from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True) # 로그인 될때 까지 기다린다.
print("블록킹 로그인 완료")

