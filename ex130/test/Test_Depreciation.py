from PyQt6.QtWidgets import QApplication, QMainWindow

from practice.ex130.ui.DepreciationMainWindowEx import DepreciationMainWindowEx

app = QApplication([])
mainWindow = QMainWindow()
myWindow = DepreciationMainWindowEx()
myWindow.setupUi(mainWindow)
myWindow.show()
app.exec()