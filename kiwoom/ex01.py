from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")


data = kiwoom.GetThemeGroupCode('100')
print(data)


# 테마코드 가져오는 코드
# data = kiwoom.GetThemeGroupList(1)
# themes = list(data.keys())

# for name in themes:
#     if '태양광' in name:
#         print(name, data[name])

