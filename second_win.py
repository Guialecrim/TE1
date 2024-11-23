from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
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
        line_name = QLineEdit('Widget text')
        self.qlinetext = QLineEdit('Dados')
        self.l_line.addWidget(self.qlinetext, alignment = Qt.AlignLeft)
        
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
        
    def connects(self):
        pass
        
# app = QApplication([])
# mw = TestWin()
# app.exec()