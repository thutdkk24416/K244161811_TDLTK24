from chapter5.ex73.libs.my_module import quadratic
from chapter5.ex73.ui.MyMainWindow import Ui_MainWindow


class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        # taij sao phair can dongf 7
        self.setupSignalAndSlot()


    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.solve_equation)

    def solve_equation(self):
        a = int(self.aLineEdit.text())
        b = int(self.bLineEdit.text())
        c = int(self.cLineEdit.text())
        result = quadratic (a, b, c)
        self.resultLineEdit.setText(str(result))
