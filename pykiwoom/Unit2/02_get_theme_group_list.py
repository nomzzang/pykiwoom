from pykiwoom.kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect()


#type == 0 {'100': '테마명'}, type == {'테마명':"100"}

#테마명만 가져올때
# group = kiwoom.GetThemeGroupList(type=0)
# for name in group.values():
#     print(name)

# 테마명 key값으로 가져오기 
group = kiwoom.GetThemeGroupList(type=1)
print(type(group))
pprint.pprint(group)


