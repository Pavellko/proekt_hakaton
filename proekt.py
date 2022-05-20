from PyQt5 import uic
from PyQt5.QtWidgets import  QProgressBar, QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap

app = QApplication([])
ui = uic.loadUi("interfeis.ui")

ui.setWindowTitle('Моя программа')
ui.setFixedSize(568, 290)

qp = QPixmap('int.jpg')
qp2 = QPixmap('logo1.png')
ui.label.setPixmap(qp)
ui.label_3.setPixmap(qp2)
ui.show()

def inp():
    text = ui.lineEdit.text()
    ui.progressBar.setValue(100)
    ui.label_2.setText("Привет!" + text)

ui.progressBar.setValue(0)

ui.pushButton.clicked.connect(inp)

app.exec_()
