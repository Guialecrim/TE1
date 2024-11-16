# write here a code for the main app and the first screen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from second_win import *
from inst import *
'''
txt_title = 'Health'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
'''

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # define a aparencia da janela
        self.initUI() # criar e configurar elementos graficos
        self.connects() # estabelece conexões entre os elementos
        self.show() # iniciar
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def initUI(self):
        self.qlinetext = QLineEdit('Dados')##### RETIRAR TESTE-----------------------------------------------------------------
        self.hello_text = QLabel(txt_hello)#criar etiqueta
        self.instruction = QLabel(txt_instruction)#criar etiqueta
        self.button = QPushButton(txt_next)#criar botao
        self.layout = QVBoxLayout()#criar layout
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)#add a self widget.hello_text on self.layout
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)#add the self.instruction widget to self.layout
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)#add a self widget.button on self.layout
        self.layout.addWidget(self.qlinetext, alignment = Qt.AlignCenter)###### RETIRAR TESTE----------------------------------------
        self.setLayout(self.layout) # faz o layout aparecer
        
    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()
        

app = QApplication([])
mw = MainWin()
app.exec()