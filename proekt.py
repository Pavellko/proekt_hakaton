from PyQt5 import uic
from PyQt5.QtWidgets import  QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap 

app = QApplication([])
ui = uic.loadUi("interfeis.ui")

ui.setWindowTitle('Моя программа')
ui.setFixedSize(568, 290)

qp = QPixmap('int.jpg')
ui.label.setPixmap(qp)
ui.show()

app.exec_()
