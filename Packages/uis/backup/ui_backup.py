from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

style = """
QFrame {
    border-radius: 10px;
    background-color: #1A1E28;
}

/* COMBOBOX */
QComboBox{
    background-color: rgb(41, 48, 63);
    border-radius: 5px;
    border: 2px solid rgb(27, 29, 35);
    padding: 5px;
    padding-left: 10px;
}

QComboBox:hover{
    border: 2px solid rgb(49, 50, 63);
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px;
    border-left-width: 3px;
    border-left-color: rgba(39, 44, 54, 150);
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    background-image: url(./packges/app/items/icons/16x16/cil-arrow-bottom.png);
    background-position: center;
    background-repeat: no-reperat;
}
QComboBox QAbstractItemView {
    color: rgb(85, 170, 255);
    background-color: rgb(41, 48, 63);
    padding: 10px;
    selection-background-color: rgb(39, 44, 54);
}
"""


class Ui_Backup(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(427, 192)

        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(10)
        font11.setBold(True)

        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backup_window = QFrame(Dialog)
        self.backup_window.setObjectName(u"backup_window")
        self.backup_window.setMinimumSize(QSize(427, 192))
        self.backup_window.setMaximumSize(QSize(427, 192))
        font = QFont()
        font.setFamily(u"MesloLGL Nerd Font")
        self.backup_window.setFont(font)
        self.backup_window.setStyleSheet(style)
        self.backup_window.setFrameShape(QFrame.StyledPanel)
        self.backup_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.backup_window)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_titile_bar = QFrame(self.backup_window)
        self.frame_titile_bar.setObjectName(u"frame_titile_bar")
        self.frame_titile_bar.setMinimumSize(QSize(0, 30))
        self.frame_titile_bar.setMaximumSize(QSize(427, 30))
        self.frame_titile_bar.setStyleSheet("QFrame {\n"
                                            "   Background-color: rgb(52, 59, 71);\n"
                                            "   border: opx solid;\n"
                                            "   border-radius: 10px;\n"
                                            "}\n")
        self.frame_titile_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_titile_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_titile_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_title = QLabel(self.frame_titile_bar)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(70, 16777215))
        self.label_title.setStyleSheet(u"QLabel{\n"
                                       "	padding-left: 10px;\n"
                                       "	color: white;\n"
                                       "}")
        self.label_title.setFont(font11)

        self.horizontalLayout.addWidget(self.label_title, 0, Qt.AlignLeft)

        self.btn_close = QPushButton(self.frame_titile_bar)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setMaximumSize(QSize(20, 20))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
                                     "	color: white;\n"
                                     "	background-color:  rgb(52, 59, 71);\n"
                                     "	border: 0px solid;\n"
                                     "  border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "	background-color: rgb(255, 0, 0);\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "	background-color:rgba(255, 0, 0, 100);\n"
                                     "}")
        icon = QIcon()
        icon.addFile(u"packges/app/items/icons/24x24/cil-x.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_close, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.frame_titile_bar)

        self.frame_content_window = QFrame(self.backup_window)
        self.frame_content_window.setObjectName(u"frame_content_window")
        self.frame_content_window.setStyleSheet(u"")
        self.frame_content_window.setFrameShape(QFrame.StyledPanel)
        self.frame_content_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content_window)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 15, 30, 15)
        self.label = QLabel(self.frame_content_window)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"color: white;")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_path = QLineEdit(self.frame_content_window)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setMinimumSize(QSize(0, 25))
        self.lineEdit_path.setMaximumSize(QSize(16777215, 25))
        self.lineEdit_path.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_path.setFont(font1)
        self.lineEdit_path.setStyleSheet(u"QLineEdit {\n"
                                         "	color: white;\n"
                                         "	background-color: rgb(41, 48, 63);\n"
                                         "	border: 0px solid;\n"
                                         "	border-radius: 10px;\n"
                                         "	padding-left: 20px;\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(49, 50, 63);\n"
                                         "}\n"
                                         "QLineEdit:focus {\n"
                                         "    border: 2px solid rgb(61, 152, 212);\n"
                                         "}")

        self.horizontalLayout_2.addWidget(self.lineEdit_path)

        self.open_folder = QPushButton(self.frame_content_window)
        self.open_folder.setObjectName(u"open_folder")
        self.open_folder.setMinimumSize(QSize(100, 25))
        self.open_folder.setMaximumSize(QSize(100, 25))
        self.open_folder.setFont(font1)
        self.open_folder.setStyleSheet(u"QPushButton {\n"
                                       "	background-color: rgb(26, 114, 255);\n"
                                       "	border-radius: 5px;\n"
                                       "	color: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "	background-color: rgb(21, 134, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "	background-color: rgba(26, 114, 255, 100);\n"
                                       "}")

        self.horizontalLayout_2.addWidget(self.open_folder)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.comboBox = QComboBox(self.frame_content_window)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))
        self.comboBox.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setFamily(u"MesloLGL Nerd Font")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.comboBox.setFont(font2)
        self.comboBox.setStyleSheet(u"/* Combo box styles  */\n"
                                    "QComboBox{\n"
                                    "	border: 0px solid;\n"
                                    "	border-radius: 10px;\n"
                                    "	color: white;\n"
                                    "	background-color: rgb(41, 48, 63);\n"
                                    "}\n"
                                    "QComboBox::down-arrow {\n"
                                    "    image: url(./packges/app/items/icons/16x16/cil-arrow-bottom.png);\n"
                                    "}\n"
                                    "QComboBox::drop-down{\n"
                                    "	border: none;\n"
                                    "	 padding: 2px;\n"
                                    "	 position: relative;\n"
                                    "    top: 1px;\n"
                                    "	right: 5px;\n"
                                    "	padding-left: 5px;\n"
                                    "}\n"
                                    "QListView{\n"
                                    "	font-weight: bold;\n"
                                    "	selection-background-color: #0092D0;\n"
                                    "	show-decoration-selected: 1;\n"
                                    "	border: 1px solid white;\n"
                                    "	border-radius: 5px;\n"
                                    "	background-color:  rgb(41, 48, 63);\n"
                                    "	color: white;\n"
                                    "	padding-left: 5px;\n"
                                    "}")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.btn_backup = QPushButton(self.frame_content_window)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"MesloLGL Nerd Font")
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_backup.setFont(font3)
        self.btn_backup.setStyleSheet(u"QPushButton {\n"
                                      "	background-color: rgb(26, 114, 255);\n"
                                      "	border-radius: 5px;\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(21, 134, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "	background-color: rgba(26, 114, 255, 100);\n"
                                      "}")

        self.verticalLayout_3.addWidget(self.btn_backup)

        self.verticalLayout_2.addWidget(self.frame_content_window)

        self.verticalLayout.addWidget(self.backup_window)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.label_title.setText(QCoreApplication.translate(
            "Dialog", u"Backup", None))
        self.btn_close.setText("")
        self.label.setText(QCoreApplication.translate(
            "Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Backup Type</span></p></body></html>", None))
        self.open_folder.setText(QCoreApplication.translate(
            "Dialog", u"Open Folder", None))
        self.btn_backup.setText(
            QCoreApplication.translate("Dialog", u"Backup", None))
    # retranslateUi
