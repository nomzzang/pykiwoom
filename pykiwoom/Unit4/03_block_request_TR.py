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
time.sleep(3.6)

# 멀티데이터 일경우 연속조회하는 코드
while kiwoom.tr_remained:
    df = kiwoom.block_request("opt10081",
                     종목코드 = "005930",
                     기준일자="20240126",
                     수정주가구분=1,
                     output="주식일봉차트조회",
                     next=2) #멀티데이터 조회
    time.sleep(3.6)
    print(df.head())
    