from kiwoom import *
import time

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

# 조건값 로드
kiwoom.GetConditionLoad()
# 읽기
condition = kiwoom.GetConditionNameList()

kiwoom.SendCondition("0101", "2봉하락후 시세전환", "022", 0)
print(kiwoom.condition_codes)


# #첫 번째 조회
# kiwoom.SetInputValue("종목코드", "005930")
# kiwoom.SetInputValue("기준일자", "20200504")
# kiwoom.SetInputValue("수정주가구분", 1)
# kiwoom.CommRqData("opt10081", "opt10081", 0, "0101")

# # 데이터가 남아있다면 연속 조회
# while kiwoom.remained:
#     kiwoom.SetInputValue("종목코드", "005930")
#     kiwoom.SetInputValue("기준일자", "20200504")
#     kiwoom.SetInputValue("수정주가구분", 1)
#     kiwoom.CommRqData("opt10081", "opt10081", 2, "0101")
#     time.sleep(3.6)


# TR (opt10001)
# kiwoom.SetInputValue("종목코드", "005930")
# kiwoom.CommRqData("opt10001", "opt10001", 0, "0101") # 화면 번호 "0000"은 제외
# print(kiwoom.tr_data)

#테마코드에 속해있는 종목의 코드를 불러오는 코드 ex)['010060', '004000', '009830', '052420']
# data = kiwoom.GetThemeGroupCode('100')
# print(data)


# 테마코드 가져오는 코드
# data = kiwoom.GetThemeGroupList(1)
# themes = list(data.keys())

# for name in themes:
#     if '태양광' in name:
#         print(name, data[name])

