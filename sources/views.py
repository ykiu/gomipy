import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    '''
    メインウィンドウとして
    実はこれしかウィンドウ無い
    '''

    def __init__(self):
        '''
        メインウィンドウの設定
        '''
        super().__init__()
        self.setWindowTitle('電卓的な練習の模倣')
        self.setGeometry(300, 200, 400, 300)

        outer_layout = QHBoxLayout()
        left_container = QFrame()
        left = QGridLayout(left_container)

        #ラベル作成
        lbl11 = QLabel("商品番号",self)
        lbl12 = QLabel("値引き後の値段\r\n（初期価格は空白）", self)
        
        #ボタン作成
        add_to_cart_button = QPushButton("カートに追加",self)
        add_to_cart_button.clicked.connect(self.on_click)






        right_container = QFrame()
        right = QGridLayout(right_container)

        #OKボタン作成
        OKbutton = QPushButton("O K",self)
        OKbutton.clicked.connect(self.on_click)

        #ラベル作成
        lbl1 = QLabel("値段",self)
        lbl2 = QLabel("お預り", self)
        lbl3 = QLabel("おつり", self)
        self.lbl4 = QLabel("",self)


        right.addWidget(lbl1,0,0)
        right.addWidget(lbl2,1,0)
        right.addWidget(lbl3,2,0)
        right.addWidget(self.lbl4,2,1)

        self.txtbox1 = QLineEdit(self)
        self.txtbox2 = QLineEdit(self)

        right.addWidget(self.txtbox1,0,1)
        right.addWidget(self.txtbox2,1,1)

        right.addWidget(OKbutton,2,2)

        
        outer_layout.addWidget(right_container)

        self.setLayout(outer_layout)


        self.show()

    def on_click(self):
       # self.a = Do_not_touch_me()
        p = int(self.txtbox1.text())
        m = int(self.txtbox2.text())
        change = Calc(p, m)
        self.lbl4.setText(str(change))

        print(p,m,change)

        
def Calc(price, money):
    return money - price


##class Do_not_touch_me(QWidget):
##    #触らないで！と声に出そう
##
##    def __init__(self):
##        super().__init__()
##        self.setWindowTitle('触らないで！')
##        self.setGeometry(300, 200, 100, 150)
##        label = QLabel("触らないで！", self)
##
##        self.show()
        

app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec_())