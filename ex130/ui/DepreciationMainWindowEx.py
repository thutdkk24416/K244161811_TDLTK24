from PyQt6.QtWidgets import QMessageBox
from practice.ex130.ui.DepreciationMainWindow import Ui_MainWindow
from libs.module import (
    calculate_original_price,
    calculate_annual_depreciation,
    calculate_monthly_depreciation,
    calculate_detailed_depreciation
)


class DepreciationMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.SetUpSignlAndSlot()

    def SetUpSignlAndSlot(self):
        self.btn_calc_basic.clicked.connect(self.process_calculate_basic)
        self.btn_calc_details.clicked.connect(self.process_calculate_details)

    def _get_input_values(self):
        try:
            purchase = float(self.lineEdit_purchase.text() or 0)
            transport = float(self.lineEdit_transport.text() or 0)
            install = float(self.lineEdit_install.text() or 0)
            years = float(self.lineEdit_years.text() or 0)
            return purchase, transport, install, years
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập số hợp lệ!")
            return None

    def process_calculate_basic(self):
        inputs = self._get_input_values()
        if not inputs: return
        purchase, transport, install, years = inputs

        original_price = calculate_original_price(purchase, transport, install)
        annual_dep = calculate_annual_depreciation(original_price, years)
        monthly_dep = calculate_monthly_depreciation(annual_dep)

        self.lineEdit_original_price.setText(str(int(original_price)))
        self.lineEdit_annual_dep.setText(str(int(annual_dep)))
        self.lineEdit_monthly_dep.setText(str(int(monthly_dep)))

    def process_calculate_details(self):
        inputs = self._get_input_values()
        if not inputs: return

        purchase, transport, install, years = inputs
        if years <= 0:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Số năm sử dụng phải lớn hơn 0")
            return

        original_price = calculate_original_price(purchase, transport, install)
        annual_dep = calculate_annual_depreciation(original_price, years)

        details = calculate_detailed_depreciation(original_price, annual_dep, years)

        self.listWidget_details.clear()
        for item in details:
            line_text = f"Năm {item['year']}, Sau khấu hao còn=>{int(item['remaining'])}"
            self.listWidget_details.addItem(line_text)

    def show(self):
        self.MainWindow.show()