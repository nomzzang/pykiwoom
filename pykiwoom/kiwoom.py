import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from pandas import DataFrame
import datetime

class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveTrData.connect(self._handler_tr)
        self.ocx.OnReceiveChejanData.connect(self._handler_chejan)
        self.ocx.OnReceiveMsg.connect(self._handler_msg)

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

    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, index, item)
        return data.strip()
    
    def GetRepeatCnt(self, trcode, rqname):
        ret = self.ocx.dynamicCall("GetRepeatCnt(QString, QStirng)", trcode, rqname)
        return ret

    def _handler_tr(self, screen, rqname, trcode, record, next):
        if next == '2':
            self.remained = True
        else:
            self.remained = False
        
        self.tr_data = {}

        #TR 데이터 가져가기 
        if rqname == "opt10081":
            self._opt10081(rqname, trcode)

            try:
                self.tr_loop.exit()
            except:
                pass

        per = self.GetCommData(trcode, rqname, 0, "PER")
        pbr = self.GetCommData(trcode, rqname, 0, "PBR")
        self.tr_data["PER"] = per
        self.tr_data["PBR"] = pbr 

        self.tr_loop.exit()

    def _opt10081(self, rqname, trcode):
        data = []
        columns = ["시가", "고가", "저가", "종가", "거래량"]
        index = []
        rows = self.GetRepeatCnt(trcode, rqname)

        for i in range(rows):
            date = self.GetCommData(trcode, rqname, i, "일자")
            open = self.GetCommData(trcode, rqname, i, "시가")
            high = self.GetCommData(trcode, rqname, i, "고가")
            low = self.GetCommData(trcode, rqname, i, "저가")
            close = self.GetCommData(trcode, rqname, i, "현재가")
            volume = self.GetCommData(trcode, rqname, i, "거래량")

            dt = datetime.datetime.strptime(date, "%Y%m%d")
            index.append(dt)
            data.append((open, high, low, close, volume))
        
        self.tr_data = DataFrame(data=data, index=index, columns=columns)

    def SendOrder(self, rqname, screen, accno, order_type, code, quantity, price, hoga, order_no):
        self.oxc.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                             [rqname, screen, accno, order_type, code, quantity, price, hoga, order_no])

        #이벤트 루프가 필요한 경우에만 사용
        #시장가 주문의 경우 이벤트 루프가 필요없음
        self.order_loop = QEventLoop()
        self.order_loop.exec()

    def _handler_chejan(self, gubun, item_cnt, fid_list):
        print("OnReceiveChejanData", gubun, item_cnt, fid_list)
    
    def _handler_msg(self, screen, rqname, trcode, msg):
        print("OnReceiveMsg: ", screen, rqname, trcode, msg)


app = QApplication(sys.argv)
