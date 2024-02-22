import sys
import os
import csv
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import pandas as pd
from datetime import datetime
from PyQt5.QtCore import QTimer, QTime
from pykiwoom.kiwoom import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Kiwoom 실시간 조건식 테스트")

        self.data_to_save = []
        self.seen_codes = set()  # Initialize an empty set to track seen codes

        #Timer setup 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.timer.start(60000)

        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveConditionVer.connect(self._handler_condition_load)
        self.ocx.OnReceiveRealCondition.connect(self._handler_real_condition)
        self.CommConnect()

        btn1 = QPushButton("condition down")
        btn2 = QPushButton("condition list")
        btn3 = QPushButton("condition send")
        save_btn = QPushButton("Save to Excel")

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        self.setCentralWidget(widget)


        # Adding to layout
        layout.addWidget(save_btn)  # Assuming 'layout' is your QVBoxLayout

        # event
        btn1.clicked.connect(self.GetConditionLoad)
        btn2.clicked.connect(self.GetConditionNameList)
        btn3.clicked.connect(self.send_condition)
        save_btn.clicked.connect(self.save_to_csv)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")

    def _handler_login(self, err_code):
        print("handler login", err_code)

    def _handler_condition_load(self, ret, msg):
        print("handler condition load", ret, msg)

    def _handler_real_condition(self, code, type, cond_name, cond_index):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            stock_name = self.GetMasterCodeName(code)  # Convert code to stock name
            print(cond_name, code, stock_name, type, current_time)

            if type == 'I' and code not in self.seen_codes:
                self.data_to_save.append([code, stock_name, current_time])  # Save stock name instead of code
                # self.data_to_save.append([code, stock_name, current_time  ])  # Save stock name instead of code
                self.seen_codes.add(code)
                
    def save_to_csv(self):
        # Format current date as YYYYMMDD
        date_str = datetime.datetime.now().strftime("%Y%m%d")
        path = os.path.join(os.path.dirname(__file__), "result")

        os.makedirs(path, exist_ok=True)
        filename = os.path.join(path, f'Auto_Kyu_{date_str}.csv')

        # Select only 'Time', 'Code', and 'Item Name' columns
        df = pd.DataFrame(self.data_to_save, columns=['코드', '종목명', '조건만족시간'])
        df['코드'] = df['코드'].astype(str).str.zfill(6)
        df.to_csv(filename, index=False, encoding='utf-8-sig', quoting=csv.QUOTE_NONNUMERIC)
        print("save_to_csv")
        
    def GetConditionLoad(self):
        self.ocx.dynamicCall("GetConditionLoad()")

    def GetConditionNameList(self):
        data = self.ocx.dynamicCall("GetConditionNameList()")
        conditions = data.split(";")[:-1]
        for condition in conditions:
            index, name = condition.split('^')
            print(index, name)

    def SendCondition(self, screen, cond_name, cond_index, search):
        ret = self.ocx.dynamicCall("SendCondition(QString, QString, int, int)", screen, cond_name, cond_index, search)
        print(cond_name, cond_index)

    def SendConditionStop(self, screen, cond_name, cond_index):
        ret = self.ocx.dynamicCall("SendConditionStop(QString, QString, int)", screen, cond_name, cond_index)

    def send_condition(self):
        self.SendCondition("100", "Auto_kyu", "047", 1)

    #코드 -> 종목이름
    def GetMasterCodeName(self, code):
        data = self.ocx.dynamicCall("GetMasterCodeName(QString)",code)
        return data
    
    def check_time(self):
        #Check if current time is 09:30
        if QTime.currentTime().toString("HH:mm") == "09:30":
            self.save_to_csv()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
