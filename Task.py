from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from UI_MainWindow import Ui_MainWindow
import sys

USER = "admin"
PASS = "admin"

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.main_win.setWindowIcon(QIcon("money.png"))
        self.ui.setupUi(self.main_win)

        self.ui.login_btn.clicked.connect(self.login)
        self.ui.logout_btn.clicked.connect(self.log_out)
        self.ui.convert_btn.clicked.connect(self.convert)
        self.ui.reset_btn.clicked.connect(self.reset)

        self.ui.stackedWidget.setCurrentWidget(self.ui.login)
        self.ui.pswd.setEchoMode(QLineEdit.Password)

    def show(self):
        self.main_win.show()

    def login(self):
        if self.ui.user.text() == USER and self.ui.pswd.text() == PASS:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
            self.ui.user.setText("")
            self.ui.pswd.setText("")
            self.ui.wrong.setText("")
        else:
            self.ui.wrong.setText("Wrong Credentials")


    def log_out(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)
        self.reset()

    def convert(self):

        currencies = {"GEL": {"USD": 0.37, "EUR": 0.34},
                      "USD": {"GEL": 2.69, "EUR": 0.9},
                      "EUR": {"GEL": 2.97, "USD": 1.11}}

        from_currency = self.ui.from_box.currentText().split()[0]
        to_currency = self.ui.to_box.currentText().split()[0]

        try:
            amount = float(self.ui.amount_input.text())
        except ValueError:
            self.ui.converted.setText("Invalid input!")
            return

        if amount < 0:
            self.ui.converted.setText("Amount must be positive!")
            return

        if from_currency == to_currency:
            result = amount
        else:
            result = amount * currencies[from_currency][to_currency]

        self.ui.converted.setText(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

    def reset(self):
        self.ui.amount_input.setText("")
        self.ui.from_box.setCurrentIndex(0)
        self.ui.to_box.setCurrentIndex(0)
        self.ui.converted.setText("")

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
