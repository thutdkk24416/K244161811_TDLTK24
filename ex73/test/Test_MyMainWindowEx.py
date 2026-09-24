import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from chapter5.ex73.ui.MyMainWindowEx import MyMainWindowEx

app = QApplication(sys.argv)
myui = MyMainWindowEx()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()