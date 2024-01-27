from pykiwoom.kiwoom import *
import time

kiwoom = Kiwoom(login=True)

df = kiwoom.block_request("opt10081",
                     종목코드 = "005930",
                     기준일자="20240126",
                     수정주가구분=1,
                     output="주식일봉차트조회",
                     next=0) #싱글데이터 조회

print(df.head())
print(len(df))
