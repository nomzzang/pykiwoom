from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()

kiwoom.GetConditionLoad()
conditions = kiwoom.GetConditionNameList()
# print(conditions)
condition_index, condition_name = conditions[0]
codes = kiwoom.SendCondition("0101","만점", "008", 0)

for code in codes:
    name = kiwoom.GetMasterCodeName(code)
    print(code, name)