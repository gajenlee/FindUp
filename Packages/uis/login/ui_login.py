from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.background.setStyleSheet("#background {\n"
                                      "    background-color: rgb(26, 27, 34);\n"
                                      "    color:rgb(255, 255, 255);\n"
                                      "    border-radius: 10px;\n"
                                      "}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.frame_widgets = QtWidgets.QFrame(self.background)
        self.frame_widgets.setGeometry(QtCore.QRect(0, 70, 280, 720))
        self.frame_widgets.setMinimumSize(QtCore.QSize(280, 720))
        self.frame_widgets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_widgets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_widgets.setObjectName("frame_widgets")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_widgets)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QFrame(self.frame_widgets)
        self.logo.setMinimumSize(QtCore.QSize(0, 200))
        self.logo.setMaximumSize(QtCore.QSize(16777215, 200))
        self.logo.setStyleSheet("image: url(:/icon/findup.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.logo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_logo = QtWidgets.QLabel(self.logo)
        self.label_logo.setMinimumSize(QtCore.QSize(200, 200))
        self.label_logo.setMaximumSize(QtCore.QSize(160, 160))
        self.label_logo.setStyleSheet("")
        self.label_logo.setObjectName("label_logo")
        self.verticalLayout_3.addWidget(
            self.label_logo, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.logo)
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame_widgets)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_name.setClearButtonEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("#lineEdit_name {\n"
                                         "    border: 0px solid;\n"
                                         "    background-color: rgb(37, 38, 48);\n"
                                         "    border-radius: 10px;\n"
                                         "    padding-left: 10px;\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "#lineEdit_name:hover {border: 3px solid rgb(59, 61, 77);}\n"
                                         "#lineEdit_name:focus {border: 3px solid rgb(39, 53, 84);}\n"
                                         "\n"
                                         "")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_2.addWidget(self.lineEdit_name)
        self.lineEdit_pass = QtWidgets.QLineEdit(self.frame_widgets)
        self.lineEdit_pass.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_pass.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEdit_pass.setClearButtonEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setStyleSheet("#lineEdit_pass {\n"
                                         "    border: 0px solid;\n"
                                         "    background-color: rgb(37, 38, 48);\n"
                                         "    border-radius: 10px;\n"
                                         "    padding-left: 10px;\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "#lineEdit_pass:hover {border: 3px solid rgb(59, 61, 77);}\n"
                                         "#lineEdit_pass:focus {border: 3px solid rgb(39, 53, 84);}")
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.verticalLayout_2.addWidget(self.lineEdit_pass)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.preloader = QtWidgets.QFrame(self.frame_widgets)
        self.preloader.setMinimumSize(QtCore.QSize(0, 300))
        self.preloader.setMaximumSize(QtCore.QSize(280, 300))
        self.preloader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.preloader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.preloader.setObjectName("preloader")
        self.verticalLayout_2.addWidget(
            self.preloader)
        self.verticalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_name.setToolTip(_translate(
            "MainWindow", "Username Or Email ID"))
        self.lineEdit_name.setPlaceholderText(
            _translate("MainWindow", "Username"))
        self.lineEdit_pass.setToolTip(_translate("MainWindow", "Password"))
        self.lineEdit_pass.setPlaceholderText(
            _translate("MainWindow", "Password"))
        MainWindow.setToolTip(_translate(
            "MainWindow", "<p>Do You Want To Close ?,  Press <b>ESE</b> Key On Your Keybord</p><p>Do You Want To Confirm The Document ?,  Press The <b>ENTER</b> Key On Your Keybord</p>"))
