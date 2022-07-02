from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_error(object):

    def setShadowEffect(self, widget):

        # Set Shadow Effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 0))

        widget.setGraphicsEffect(shadow)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_main_window = QFrame(Dialog)
        self.frame_main_window.setStyleSheet("")
        self.frame_main_window.setFrameShape(QFrame.StyledPanel)
        self.frame_main_window.setFrameShadow(QFrame.Raised)
        self.frame_main_window.setObjectName("frame_main_window")
        self.gridLayout = QGridLayout(self.frame_main_window)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_icon = QLabel(self.frame_main_window)
        self.label_icon.setMinimumSize(QSize(100, 140))
        self.label_icon.setMaximumSize(QSize(100, 140))
        self.label_icon.setObjectName("label_icon")
        self.label_icon.setWordWrap(True)
        self.gridLayout.addWidget(
            self.label_icon, 0, 0, 2, 1, Qt.AlignHCenter | Qt.AlignVCenter)
        self.frame_content = QFrame(self.frame_main_window)
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout = QVBoxLayout(self.frame_content)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_okay = QPushButton(self.frame_content)
        self.btn_okay.setObjectName("btn_okay")
        self.btn_okay.setMinimumSize(QSize(100, 20))
        self.verticalLayout.addWidget(self.btn_okay)
        self.gridLayout.addWidget(
            self.frame_content, 1, 1, 1, 1, Qt.AlignRight | Qt.AlignBottom)
        self.label_error_text = QLabel(self.frame_main_window)
        self.label_error_text.setMinimumSize(QSize(0, 100))
        self.label_error_text.setMaximumSize(QSize(16777215, 100))
        self.label_error_text.setObjectName("label_error_text")
        self.gridLayout.addWidget(
            self.label_error_text, 0, 1, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_main_window)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_error_text.setText(_translate(
            "Dialog", "<html><head/><body><p align=\"left\">The Teachers Entries are Emty so, <br>fill it</p></body></html>"))
        self.btn_okay.setText(_translate("Dialog", "Ok"))
