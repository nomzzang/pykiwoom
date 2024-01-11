from kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

theme_grp = kiwoom.GetThemeGroupList(0)
theme_codes = kiwoom.GetThemeGroupCode('100')

print("테마명:", theme_grp['100'])
for code in theme_codes:
    name = kiwoom.GetMasterCodeName(code)
    print(code, name)