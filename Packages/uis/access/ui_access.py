from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Access(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(368, 183)
        Dialog.setMinimumSize(QSize(368, 183))
        Dialog.setMaximumSize(QSize(368, 183))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(Dialog)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setMinimumSize(QSize(368, 183))
        self.frame_main.setMaximumSize(QSize(368, 183))
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 9)
        self.frame_title_bar = QFrame(self.frame_main)
        self.frame_title_bar.setObjectName(u"frame_title_bar")
        self.frame_title_bar.setMinimumSize(QSize(0, 35))
        self.frame_title_bar.setMaximumSize(QSize(16777215, 35))
        self.frame_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title_label = QFrame(self.frame_title_bar)
        self.frame_title_label.setObjectName(u"frame_title_label")
        self.frame_title_label.setMaximumSize(QSize(16777215, 16777215))
        self.frame_title_label.setFrameShape(QFrame.StyledPanel)
        self.frame_title_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_title_label)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_title_label)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(75, 17))
        self.label_title.setMaximumSize(QSize(75, 17))
        font = QFont()
        font.setFamily(u"MesloLGL Nerd Font")
        font.setPointSize(10)
        self.label_title.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_title)

        self.horizontalLayout.addWidget(
            self.frame_title_label, 0, Qt.AlignLeft)

        self.frame_title_btns = QFrame(self.frame_title_bar)
        self.frame_title_btns.setObjectName(u"frame_title_btns")
        self.frame_title_btns.setMinimumSize(QSize(100, 0))
        self.frame_title_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_title_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_title_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title_btns)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(60, 0, 0, 0)
        self.btn_close = QPushButton(self.frame_title_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_close)

        self.horizontalLayout.addWidget(self.frame_title_btns)

        self.verticalLayout_2.addWidget(self.frame_title_bar)

        self.frame_work_follw = QFrame(self.frame_main)
        self.frame_work_follw.setObjectName(u"frame_work_follw")
        self.frame_work_follw.setFrameShape(QFrame.StyledPanel)
        self.frame_work_follw.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_work_follw)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, -1, 0)
        self.label_user_info = QLabel(self.frame_work_follw)
        self.label_user_info.setObjectName(u"label_user_info")
        self.label_user_info.setFont(font)
        self.verticalLayout_3.addWidget(self.label_user_info)

        self.lineEdit_current_password = QLineEdit(self.frame_work_follw)
        self.lineEdit_current_password.setObjectName(
            u"lineEdit_current_password")
        self.lineEdit_current_password.setMinimumSize(QSize(0, 30))
        self.lineEdit_current_password.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_current_password.setFont(font1)
        self.lineEdit_current_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.lineEdit_current_password)

        self.btn_verify = QPushButton(self.frame_work_follw)
        self.btn_verify.setObjectName(u"btn_verify")
        self.btn_verify.setMinimumSize(QSize(0, 25))
        self.btn_verify.setMaximumSize(QSize(16777215, 25))
        self.btn_verify.setFont(font1)

        self.verticalLayout_3.addWidget(self.btn_verify)

        self.verticalLayout_2.addWidget(self.frame_work_follw)

        self.verticalLayout.addWidget(self.frame_main)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.label_title.setText(QCoreApplication.translate(
            "Dialog", u"<b>Verify</b>", None))
        self.btn_close.setText("")
        self.label_user_info.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Enter the <b>Current password</b> to <b>verify</b> \n"
                                                                "<br>your changes.</p></body></html>", None))
        self.lineEdit_current_password.setPlaceholderText(
            QCoreApplication.translate("Dialog", u"Current Password", None))
        self.btn_verify.setText(
            QCoreApplication.translate("Dialog", u"Verify", None))
    # retranslateUi
