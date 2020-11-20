from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from administrative_module.cognito import CognitoUser
from ui_module.register import CerebroRegister
import os


class CerebroLogin(QMainWindow):

    def __init__(self):
        super(CerebroLogin, self).__init__()
        self.user_pool_id = os.getenv("USER_POOL_ID")
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(844, 647)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.username_field = QtWidgets.QLineEdit(self.centralwidget)
        self.username_field.setGeometry(QtCore.QRect(340, 280, 201, 21))
        self.username_field.setText("")
        self.username_field.setObjectName("username_field")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(260, 280, 71, 16))
        self.username_label.setObjectName("username_label")
        self.password_field = QtWidgets.QLineEdit(self.centralwidget)
        self.password_field.setGeometry(QtCore.QRect(340, 320, 201, 21))
        self.password_field.setText("")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(260, 320, 71, 16))
        self.password_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.password_label.setObjectName("password_label")
        self.signin_button = QtWidgets.QPushButton(self.centralwidget)
        self.signin_button.setGeometry(QtCore.QRect(380, 370, 113, 32))
        self.signin_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signin_button.setObjectName("signin_button")
        self.register_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(380, 410, 113, 32))
        self.register_button.clicked.connect(self.register)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.register_button.setFont(font)
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_button.setObjectName("register_button")
        self.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 844, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuCerebro = QtWidgets.QMenu(self.menuBar)
        self.menuCerebro.setObjectName("menuCerebro")
        self.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuCerebro.menuAction())
        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.signin_button.setText(_translate("MainWindow", "Sign in"))
        self.signin_button.clicked.connect(self.sign_in)
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.menuCerebro.setTitle(_translate("MainWindow", "Cerebro"))

    def sign_in(self):
        username = self.username_field.text()
        password = self.password_field.text()
        cognito = CognitoUser(user_pool_id=self.user_pool_id, client_id=self.client_id, client_secret=self.client_secret,username=username)
        is_authenticated = cognito.authenticate_user(password)
        print(is_authenticated)

    def register(self):
        window = CerebroRegister(self)
        window.closed.connect(self.show)
        window.show()
        self.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CerebroLogin()
    ui.show()
    sys.exit(app.exec_())
