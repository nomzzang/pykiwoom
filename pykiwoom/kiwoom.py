import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        self.login_loop = QEventLoop()
        self.login_loop.exec()

    def _handler_login(self, err):
        self.login_loop.exit()

    def GetLogInfo(self, tag):
        data = self.ocx.dynamicCall("GetLoginInfo(QString)", tag)
        return data
    
    def GetCodeListByMarket(self, market):
        data = self.ocx.dynamicCall("GetCodeListByMarket(QSting)", market)
        codes = data.split(";")
        return codes
    
    #코드 -> 종목이름
    def GetMasterCodeName(self, code):
        data = self.ocx.dynamicCall("GetMasterCodeName(QString)",code)
        return data

    #상장 주식수
    def GetMasterListedStockCnt(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockCnt(QString)", code)
        return data

    #상장일
    def GetMasterListedStockDate(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockDate(QString)", code)
        return data
    
    #전일가
    def GetMasterLastPrice(self, code):
        data = self.ocx.dynamicCall("GetMasterLastPrice(QString)", code)
        return int(data)
    
    #감리구분 
    def GetMasterConstruction(self, code):
        data = self.ocx.dynamicCall("GetMasterConstruction(QString)", code)
        return data
    
    #종목 상태   ex) 증거금20%|담보대출|신용가능 필요하면 spilt 사용
    def GetMasterStockState(self, code):
        data = self.ocx.dynamicCall("GetMasterStockState(QString)", code)
        return str(data)
    
    #테마코드와 테마명 (0:코드순 , 1:테마순), #딕셔러리
    def GetThemeGroupList(self, type):
        data = self.ocx.dynamicCall("GetThemeGroupList(int)",type)  #dict
        tokens = data.split(';') 
        
        data_dic = {}
        for theme in tokens:
            code, name =theme.split('|')
            if type == 0:
                data_dic[code] = name
            else:
                data_dic[name] = code
        
        return data_dic
    
    #테마코드에 소속된 종목코드 반환값 : 종목코드 리스트  ex) A000066;A005930;A002345
    def GetThemeGroupCode(self, theme_code):
        data = self.ocx.dynamicCall("GetThemeGroupCode(QString)", theme_code)
        tokens = data.split(';')  
        
        result = []
        for code in tokens:
            result.append(code[1:])

        return result

    def SetInputValue(self, item, value):
        self.ocx.dynamicCall("SetInputValue(QStirng, QString)", item, value)

    def CommRqData(self, rqname, trcode, next, screen):
        self.ocx.dynamicCall("CommRqData(QString, QString, int, QString)", rqname, trcode, next, screen)
        self.tr_loop = QEventLoop()
        self.tr_loop.exec()

        

    
app = QApplication(sys.argv)
