from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 620)
        Dialog.setStyleSheet("background-color: rgb(255, 231, 248)")

        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 460, 600))

        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.stackedWidget.addWidget(self.page_login)

        self.Email = QtWidgets.QLineEdit(self.page_login)
        self.Email.setGeometry(QtCore.QRect(97, 190, 231, 31))
        self.Email.setStyleSheet("font: italic 13pt \"Annai MN\";\n"
                                 "color: rgb(255, 39, 205);\n"
                                 "")
        self.Email.setPlaceholderText("E-mail")
        self.Email.setObjectName("Email")

        self.password = QtWidgets.QLineEdit(self.page_login)
        self.password.setGeometry(QtCore.QRect(97, 250, 231, 31))
        self.password.setStyleSheet("font: italic 13pt \"Annai MN\";\n"
                                    "color: rgb(255, 39, 205);\n"
                                    "")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setObjectName("password")

        self.Dha = QtWidgets.QLabel(self.page_login)
        self.Dha.setGeometry(QtCore.QRect(140, 330, 141, 16))
        self.Dha.setStyleSheet("color: rgb(0, 0, 0)")
        self.Dha.setObjectName("Dha")

        self.create = QtWidgets.QLabel(self.page_login)
        self.create.setGeometry(QtCore.QRect(260, 350, 121, 16))
        self.create.setStyleSheet("color: rgb(0, 0, 0)")
        self.create.setObjectName("create")

        self.reset = QtWidgets.QLabel(self.page_login)
        self.reset.setGeometry(QtCore.QRect(260, 400, 121, 16))
        self.reset.setObjectName("reset")



        self.LoginButton = QtWidgets.QPushButton(self.page_login)
        self.LoginButton.setGeometry(QtCore.QRect(170, 370, 80, 26))
        self.LoginButton.setStyleSheet("color: rgb(255, 39, 205); \n"
                                       "font: 700 italic 19pt \"Arial\";")
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(self.check_login)

        self.label = QtWidgets.QLabel(self.page_login)
        self.label.setGeometry(QtCore.QRect(140, 60, 151, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Desktop/IMG_0088.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.page_login)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 121, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("photos/IMG_0088.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.page_success = QtWidgets.QWidget()
        self.page_success.setObjectName("page_success")
        self.stackedWidget.addWidget(self.page_success)

        self.successLabel = QtWidgets.QLabel(self.page_success)
        self.successLabel.setGeometry(QtCore.QRect(160, 220, 361, 61))
        self.successLabel.setStyleSheet("color: rgb(0, 170, 0);\n"
                                        "font: 700 italic 19pt \"Arial\";")
        self.successLabel.setObjectName("successLabel")


        self.successPhoto = QtWidgets.QLabel(self.page_success)
        self.successPhoto.setGeometry(QtCore.QRect(190, 120, 100, 100))
        self.successPhoto.setPixmap(QtGui.QPixmap("photos/pig.png"))
        self.successPhoto.setScaledContents(True)
        self.successPhoto.setObjectName("successPhoto")

        self.errorLabel = QtWidgets.QLabel(self.page_login)
        self.errorLabel.setGeometry(QtCore.QRect(100, 290, 300, 31))
        self.errorLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorLabel.setObjectName("errorLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LoginButton.setText(_translate("Dialog", "Log in"))
        self.Email.setPlaceholderText(_translate("Dialog", "E-mail"))
        self.password.setPlaceholderText(_translate("Dialog", "Password"))

        self.successLabel.setText(_translate("Dialog", "Login Successful!"))

    def check_login(self):
        if self.Email.text() == "niagergidze@gmail.com" and self.password.text() == "password":
            self.successLabel.setText("Login Successful!")
            self.stackedWidget.setCurrentIndex(1)
            self.errorLabel.clear()
        else:
            self.Email.setStyleSheet("font: italic 13pt \"Annai MN\";\n"
                                     "color: rgb(255, 39, 205);\n"
                                     "background-color: pink;")
            self.password.setStyleSheet("font: italic 13pt \"Annai MN\";\n"
                                        "color: rgb(255, 39, 205);\n"
                                        "background-color: pink;")
            self.errorLabel.setText("Invalid email or password.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())