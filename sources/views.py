import sys
from PyQt5.QtWidgets import *
import PyQt5.QtGui

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

        outer_layout = QHBoxLayout()

        #ここから左カラムの作成
        left_container = QFrame()
        left_container.setFrameStyle(1)
        left_container.setFrameShadow(QFrame.Sunken)
        left = QVBoxLayout(left_container)

        #ラベル作成
        lbl11 = QLabel("商品番号",self)
        lbl12 = QLabel("値引き後の値段\r\n（初期価格は空白）", self)

        #入力バー作成
        self.txtbox11 = QLineEdit(self)
        self.txtbox12 = QLineEdit(self)

        #ボタン作成
        add_to_cart_button = QPushButton("カートに追加",self)
        add_to_cart_button.clicked.connect(self.pass_on_click)

        #leftのwidget配置
        left.addWidget(lbl11)
        left.addWidget(self.txtbox11)
        left.addStretch(1)
        left.addWidget(lbl12)
        left.addWidget(self.txtbox12)
        left.addStretch(2)
        left.addWidget(add_to_cart_button)
        left.addStretch(10)

        #middleのカート
        lbl21 = QLabel("カート", self)


        #middleのチェックボックス
        lbl22 = QLabel("配送", self)

        check21 = QCheckBox("配送(￥５００）", self)

        middle_container = QFrame()
        middle_container.setFrameStyle(1)
        middle_container.setFrameShadow(QFrame.Sunken) 
        middle = QVBoxLayout(middle_container)

        #middleのwidget配置
        middle.addWidget(lbl21)
        middle.addWidget(lbl22)
        middle.addStretch(1)
        middle.addWidget(check21)
       
        #ここから右カラムの作成
        right_container = QFrame()
        right_container.setFrameStyle(1)
        right_container.setFrameShadow(QFrame.Sunken)
        right = QGridLayout(right_container)

        #ラベル作成
        lbl1 = QLabel("値段",self)
        lbl2 = QLabel("お預り", self)
        lbl3 = QLabel("おつり", self)
        self.lbl4 = QLabel("",self)

        # 入力バー作成
        self.txtbox1 = QLineEdit(self)
        self.txtbox2 = QLineEdit(self)

        # OKボタン作成
        OKbutton = QPushButton("OK", self)
        OKbutton.clicked.connect(self.calc_on_click)

        #rightのwidget配置
        right.addWidget(lbl1, 0, 0)
        right.addWidget(lbl2, 1, 0)
        right.addWidget(lbl3, 2, 0)
        right.addWidget(self.lbl4, 2, 1)
        right.addWidget(self.txtbox1,0,1)
        right.addWidget(self.txtbox2,1,1)
        right.addWidget(OKbutton,2,2)



        #大枠の配置
        outer_layout.addWidget(left_container)
        outer_layout.addWidget(middle_container)
        outer_layout.addWidget(right_container)

        self.setLayout(outer_layout)


        self.show()

    def calc_on_click(self):
       # self.a = Do_not_touch_me()
        p = int(self.txtbox1.text())
        m = int(self.txtbox2.text())
        change = Calc(p, m)
        self.lbl4.setText(str(change))

        print(p,m,change)

    def pass_on_click(self):
        pass
        
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
