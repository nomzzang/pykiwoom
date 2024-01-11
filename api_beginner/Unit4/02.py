import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #로그인
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.dynamicCall("CommConnect()")
        self.ocx.OnEventConnect.connect(self.handel_login)

        #로그인 정보출력
        self.button = QPushButton("로그인 정보", self)
        self.button.move(10,10)
        self.button.clicked.connect(self.handel_button_clicked)

    def handel_login(self, err_code):
        if err_code == 0:
            self.statusBar().showMessage("로그인 성공")
        else:
            self.statusBar().showMessage("로그인 실패")        

    def handel_button_clicked(self):
        #GetLoginInfo('ACCOUNT_CNT' - 전체 계좌 개수를 반환한다., 'USER_ID' - 사용자 ID를 반환한다)
        account_nums = self.ocx.dynamicCall("GetLoginInfo(QStirng)", "USER_ID")
        print(account_nums)    

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
