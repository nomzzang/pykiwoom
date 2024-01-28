from pykiwoom.kiwoom import *
import datetime
import time

kiwoom = Kiwoom(login=True)

kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')

codes = kospi + kosdaq

now = datetime.datetime.now()
today = now.strftime("%Y%m%d")
print(today)

for i, code in enumerate(codes):
    print(i, len(codes))

    df = kiwoom.block_request("opt10081",
                              종목코드=code,
                              기준일자=today,
                              수정주가구분=1,
                              output="주식일봉차트조회",
                              next=0)
    

    code_name = kiwoom.GetMasterCodeName(code)
    out_name = f"{code_name}.xlsx"

    df.to_excel(out_name)
    time.sleep(3.6)



