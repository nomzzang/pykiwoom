from kiwoom import *
import time


kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

codes = kiwoom.GetCodeListByMarket('0') + kiwoom.GetCodeListByMarket('10')
print(len(codes))

per_result = []
for code in codes[:50]:

    #TR 
    kiwoom.SetInputValue("종목코드", code)
    kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")

    per = kiwoom.tr_data["PER"]
    pbr = kiwoom.tr_data["PBR"]

    try:
        per = float(per)
    except:
        per = 0


    try:
        pbr = float(pbr)
    except:
        pbr = 0

    #스크리닝
    #per 2.5 ~ 10인 주식을 필터링하고
    if 2.5 <= per <= 10:
        per_result.append((code, per, pbr))

    time.sleep(0.2)


print(per_result)

#PBR 정렬
#그중 pbr이 가장 낮은 30개 주식을 매수한다. 
result = sorted(per_result, key=lambda x:x[2])

for item in result:
    print(item[0], item[1], item[2])