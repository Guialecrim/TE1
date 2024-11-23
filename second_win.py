from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from inst import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        #pass  
    def set_appear(self):
        self.setWindowTitle(txt_title) #adiciona um nome a janela
        self.resize(win_width, win_height) #redimensiona a janela
        self.move(win_x,win_y) #faz a janela aparecer em um ponto específico 
        #pass
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        # add widgets to self.l_line ------ self.l_line.addWidget(self.btn1)
        # add widgets to self.r_line ------ self.r_line.addWidget(self.timer)
        self.qtimer = QLabel('00:00:00')
        self.r_line.addWidget(self.qtimer, alignment = Qt.AlignRight)
        
        self.qlog_in = QLabel(txt_name)
        self.l_line.addWidget(self.qlog_in, alignment = Qt.AlignLeft)
    
        self.qline_name = QLineEdit('Widget text')
        self.l_line.addWidget(self.qline_name, alignment = Qt.AlignLeft)
        
        self.qlinetext = QLineEdit('Dados')
        self.l_line.addWidget(self.qlinetext, alignment = Qt.AlignLeft)
        
        self.btn_test1 = QPushButton('Start final test')
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        
        
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
        
    def timer_test(self):
        global time
        
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer1Event(self):
        global time
        
        time = time.addSecs(-1)
        self.qtimer.setText(time.toString('hh:mm:ss'))
        self.qtimer.setFont(QFont('Times', 36, QFont.Bold))# define a font
        self.qtimer.setStyleSheet('color:rgb(0, 0, 0)')#define a cor
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
        
        
    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)
        

        
