from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1122, 571)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopBar = QFrame(self.centralwidget)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setMaximumSize(QSize(16777215, 50))
        self.TopBar.setStyleSheet(u"background-color: rgb(20, 20, 20);")
        self.TopBar.setFrameShape(QFrame.NoFrame)
        self.TopBar.setFrameShadow(QFrame.Raised)
        self.TopBar.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.TopBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.TopBar)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setMinimumSize(QSize(70, 40))
        self.frame_top.setMaximumSize(QSize(70, 40))
        self.frame_top.setStyleSheet(u"background-color: none;")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(12)
        font11.setBold(True)

        self.btn_Toggle = QPushButton(self.frame_top)
        self.btn_Toggle.setObjectName(u"btn_Toggle")
        self.btn_Toggle.setMinimumSize(QSize(70, 40))
        self.btn_Toggle.setFont(font11)
        self.verticalLayout_2.addWidget(self.btn_Toggle)

        self.horizontalLayout.addWidget(self.frame_top)

        self.title_bar = QFrame(self.TopBar)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_return_bar = QFrame(self.title_bar)
        self.frame_return_bar.setObjectName(u"frame_return_bar")
        self.frame_return_bar.setMinimumSize(QSize(0, 50))
        self.frame_return_bar.setMaximumSize(QSize(16777215, 16777215))
        self.frame_return_bar.setStyleSheet(u"background-color: rgb(40, 43, 53);\n"
                                            "border: none;\n"
                                            "border-top-right-radius: 5px;\n"
                                            "border-top-left-radius: 5px;\n"
                                            "border-bottom-right-radius: 0px;\n"
                                            "border-bottom-left-radius: 0px;")
        self.frame_return_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_return_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_return_bar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_add = QFrame(self.frame_return_bar)
        self.frame_add.setObjectName(u"frame_add")
        self.frame_add.setMinimumSize(QSize(250, 0))
        self.frame_add.setMaximumSize(QSize(300, 16777215))
        self.frame_add.setFrameShape(QFrame.StyledPanel)
        self.frame_add.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_add)
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 10, 10, 10)
        self.btn_inter = QPushButton(self.frame_add)
        self.btn_inter.setObjectName(u"btn_inter")
        self.btn_inter.setMinimumSize(QSize(100, 0))
        self.btn_inter.setMaximumSize(QSize(250, 30))
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_inter.setFont(font1)
        self.btn_inter.setStyleSheet(u"QPushButton{\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "	background-color: none;\n"
                                     "	border: 0px solid;\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "	background-color: rgb(85, 170, 255);\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "	background-color: rgba(85, 170, 255, 100);\n"
                                     "}")

        self.horizontalLayout_7.addWidget(self.btn_inter)

        self.btn_lower = QPushButton(self.frame_add)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setMinimumSize(QSize(100, 0))
        self.btn_lower.setMaximumSize(QSize(250, 30))
        self.btn_lower.setFont(font1)
        self.btn_lower.setStyleSheet(u"QPushButton{\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "	background-color: none;\n"
                                     "	border: 0px solid;\n"
                                     "	border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "	background-color: rgb(85, 170, 255);\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "	background-color: rgba(85, 170, 255, 100);\n"
                                     "}")

        self.horizontalLayout_7.addWidget(self.btn_lower)

        self.horizontalLayout_6.addWidget(self.frame_add)

        self.frame_backup = QFrame(self.frame_return_bar)
        self.frame_backup.setObjectName(u"frame_backup")
        self.frame_backup.setStyleSheet(u"QPushButton{\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "	background-color: none;\n"
                                        "	border: 0px solid;\n"
                                        "	border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "	background-color: rgba(85, 170, 255, 100);\n"
                                        "}")
        self.frame_backup.setFrameShape(QFrame.StyledPanel)
        self.frame_backup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QHBoxLayout(self.frame_backup)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_backup = QPushButton(self.frame_backup)
        self.btn_backup.setObjectName(u"btn_backup")
        self.btn_backup.setMinimumSize(QSize(100, 30))
        self.btn_backup.setMaximumSize(QSize(100, 30))
        self.btn_backup.setFont(font1)

        self.verticalLayout_12.addWidget(self.btn_backup)

        self.btn_superuser = QPushButton(self.frame_backup)
        self.btn_superuser.setObjectName(u"btn_superuser")
        self.btn_superuser.setMinimumSize(QSize(30, 30))
        self.btn_superuser.setMaximumSize(QSize(30, 30))
        self.btn_superuser.setStyleSheet("""
            QPushButton{
                color: rgb(255, 255, 255);
                background-color: rgb(56, 61, 75);
                border: 0px solid;
                border-radius: 15px;
            }
            QPushButton:hover{
                background-color: rgb(85, 170, 255);
            }
            QPushButton:pressed{
                background-color: rgba(85, 170, 255, 100);
            }
        """)

        self.verticalLayout_12.addWidget(self.btn_superuser)

        self.horizontalLayout_6.addWidget(self.frame_backup, 0, Qt.AlignRight)

        self.horizontalLayout_3.addWidget(self.frame_return_bar)

        self.horizontalLayout.addWidget(self.title_bar)

        self.verticalLayout.addWidget(self.TopBar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"QFrame{\n"
                                   "	border: none;\n"
                                   "}\n"
                                   "")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"QPushButton{\n"
                                           "	color: rgb(255, 255, 255);\n"
                                           "	background-color: none;\n"
                                           "	border: 0px solid;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "	background-color: rgb(85, 170, 255);\n"
                                           "}\n"
                                           "QFrame{background-color: rgb(20, 20, 20);}")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.frame_top_menus.setStyleSheet("background-color: none;")
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.btn_page_home = QPushButton(self.frame_top_menus)
        self.btn_page_home.setObjectName(u"btn_page_home")
        self.btn_page_home.setFont(font11)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.btn_page_home.sizePolicy().hasHeightForWidth())
        self.btn_page_home.setSizePolicy(sizePolicy2)
        self.btn_page_home.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.btn_page_home)

        self.btn_page_left = QPushButton(self.frame_top_menus)
        self.btn_page_left.setFont(font11)
        sizePolicy2.setHeightForWidth(
            self.btn_page_left.sizePolicy().hasHeightForWidth())
        self.btn_page_left.setSizePolicy(sizePolicy2)
        self.btn_page_left.setObjectName(u"btn_page_left")
        self.btn_page_left.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.btn_page_left)

        self.btn_page_search = QPushButton(self.frame_top_menus)
        sizePolicy2.setHeightForWidth(
            self.btn_page_search.sizePolicy().hasHeightForWidth())
        self.btn_page_search.setSizePolicy(sizePolicy2)
        self.btn_page_search.setObjectName(u"btn_page_search")
        self.btn_page_search.setMinimumSize(QSize(0, 40))
        self.btn_page_search.setFont(font11)

        self.verticalLayout_4.addWidget(self.btn_page_search)

        self.btn_page_analytics = QPushButton(self.frame_top_menus)
        sizePolicy2.setHeightForWidth(
            self.btn_page_analytics.sizePolicy().hasHeightForWidth())
        self.btn_page_analytics.setSizePolicy(sizePolicy2)
        self.btn_page_analytics.setObjectName(u"btn_page_search")
        self.btn_page_analytics.setMinimumSize(QSize(0, 40))
        self.btn_page_analytics.setFont(font11)

        self.verticalLayout_4.addWidget(self.btn_page_analytics)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.frame_bottom_menus = QFrame(self.frame_left_menu)
        self.frame_bottom_menus.setObjectName(u"frame_bottom_menus")
        self.frame_bottom_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_bottom_menus)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_setting = QPushButton(self.frame_bottom_menus)
        sizePolicy2.setHeightForWidth(
            self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy2)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(40, 40))
        self.btn_setting.setMaximumSize(QSize(16777215, 16777215))
        self.btn_setting.setFont(font11)

        self.verticalLayout_9.addWidget(self.btn_setting)

        self.verticalLayout_3.addWidget(
            self.frame_bottom_menus, 0, Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_page = QFrame(self.Content)
        self.frame_page.setObjectName(u"frame_page")
        self.frame_page.setStyleSheet(u"background-color: rgb(50, 53, 66);")
        self.frame_page.setFrameShape(QFrame.StyledPanel)
        self.frame_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_add_students = QWidget()
        self.page_add_students.setObjectName("page_add_students")
        self.verticalLayout_43 = QVBoxLayout(self.page_add_students)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.frame_2 = QFrame(self.page_add_students)
        self.frame_2.setStyleSheet("""QFrame{
            background-color:rgb(26, 27, 34);
            border-radius: 10px;
        }""")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 400))
        self.frame_2.setMinimumSize(QSize(0, 400))
        self.horizontalLayout_26 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_26.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(15)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.btn_primary = QPushButton(self.frame_2)
        self.btn_primary.setMinimumSize(QSize(0, 45))
        self.btn_primary.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_primary.setFont(font)
        self.btn_primary.setStyleSheet("QPushButton{\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: none;\n"
                                       "    border: 2px solid rgb(85, 170, 255) ;\n"
                                       "    border-radius: 10px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    background-color: rgb(85, 170, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: rgba(85, 170, 255, 100);\n"
                                       "}\n"
                                       "")
        self.btn_primary.setObjectName("btn_primary")
        self.horizontalLayout_25.addWidget(self.btn_primary)
        self.btn_ordinary = QPushButton(self.frame_2)
        self.btn_ordinary.setMinimumSize(QSize(0, 45))
        self.btn_ordinary.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ordinary.setFont(font)
        self.btn_ordinary.setStyleSheet("QPushButton{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: none;\n"
                                        "    border: 2px solid rgb(85, 170, 255) ;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgba(85, 170, 255, 100);\n"
                                        "}")
        self.btn_ordinary.setObjectName("btn_ordinary")
        self.horizontalLayout_25.addWidget(self.btn_ordinary)
        self.btn_advanced = QPushButton(self.frame_2)
        self.btn_advanced.setMinimumSize(QSize(0, 45))
        self.btn_advanced.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_advanced.setFont(font)
        self.btn_advanced.setStyleSheet("QPushButton{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: none;\n"
                                        "    border: 2px solid rgb(85, 170, 255) ;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgba(85, 170, 255, 100);\n"
                                        "}")
        self.btn_advanced.setObjectName("btn_advanced")
        self.horizontalLayout_25.addWidget(self.btn_advanced)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_25)
        self.verticalLayout_43.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_add_students)

        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_48 = QVBoxLayout(self.page)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_main_content_for_primary = QFrame(self.page)
        self.frame_main_content_for_primary.setStyleSheet("QFrame {\n"
                                                          "    \n"
                                                          "    background-color: rgb(26, 27, 34);\n"
                                                          "    border-radius: 10px;\n"
                                                          "    border: 0px solid;\n"
                                                          "}")
        self.frame_main_content_for_primary.setFrameShape(QFrame.StyledPanel)
        self.frame_main_content_for_primary.setFrameShadow(QFrame.Raised)
        self.frame_main_content_for_primary.setObjectName(
            "frame_main_content_for_primary")
        self.verticalLayout_47 = QVBoxLayout(
            self.frame_main_content_for_primary)
        self.verticalLayout_47.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.label_icon_primary = QLabel(self.frame_main_content_for_primary)
        self.label_icon_primary.setMinimumSize(QSize(200, 200))
        self.label_icon_primary.setMaximumSize(QSize(200, 200))
        self.label_icon_primary.setStyleSheet("QLabel{\n"
                                              "    border: 8px solid rgb(37, 38, 48);\n"
                                              "    background-color: rgb(50, 52, 65);\n"
                                              "    border-radius: 100px;\n"
                                              "color: white;\n"
                                              "}")
        self.label_icon_primary.setObjectName("label_icon_primary")
        self.verticalLayout_47.addWidget(
            self.label_icon_primary, 0, Qt.AlignHCenter)
        self.frame_coments_ad_2 = QFrame(self.frame_main_content_for_primary)
        self.frame_coments_ad_2.setStyleSheet("background-color: none;")
        self.frame_coments_ad_2.setFrameShape(QFrame.StyledPanel)
        self.frame_coments_ad_2.setFrameShadow(QFrame.Raised)
        self.frame_coments_ad_2.setObjectName("frame_coments_ad_2")
        self.gridLayout_3 = QGridLayout(self.frame_coments_ad_2)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_show_roll_primary = QLabel(self.frame_coments_ad_2)
        self.label_show_roll_primary.setMinimumSize(QSize(0, 30))
        self.label_show_roll_primary.setMaximumSize(QSize(16777215, 30))
        self.label_show_roll_primary.setStyleSheet("color: white;\n"
                                                   "padding-left: 10px;\n"
                                                   "border-top: 2px solid white;\n"
                                                   "border-bottom: 2px solid white;\n"
                                                   "border-radius: 0px;")
        self.label_show_roll_primary.setObjectName("label_show_roll_primary")
        self.gridLayout_3.addWidget(self.label_show_roll_primary, 10, 0, 1, 2)
        self.dateEdit_date_of_birth_primary = QDateEdit(
            self.frame_coments_ad_2)
        self.dateEdit_date_of_birth_primary.setMinimumSize(QSize(0, 30))
        self.dateEdit_date_of_birth_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.dateEdit_date_of_birth_primary.setFont(font)
        self.dateEdit_date_of_birth_primary.setStyleSheet("QDateEdit{\n"
                                                          "     color:white;\n"
                                                          "     background-color: #1D222E;\n"
                                                          "    padding-left: 10px;\n"
                                                          "    border: none;\n"
                                                          "    border-radius: 10px;\n"
                                                          "}\n"
                                                          "QDateEdit::down-button{\n"
                                                          "       image: url(packges/app/items/icons/main-icons/chevron-down.svg);\n"
                                                          "       margin-right: 6px;\n"
                                                          "}\n"
                                                          " QDateEdit::up-button{\n"
                                                          "        image: url(packges/app/items/icons/main-icons/chevron-up.svg);\n"
                                                          "        margin-right: 6px;\n"
                                                          "}\n"
                                                          "QDateEdit::up-button:pressed{background-color: rgb(26, 114, 255);\n"
                                                          "        border-radius: 5px;}\n"
                                                          "QDateEdit::down-button:pressed{background-color: rgb(26, 114, 255);\n"
                                                          "        border-radius: 5px;}")
        self.dateEdit_date_of_birth_primary.setObjectName(
            "dateEdit_date_of_birth_primary")
        self.gridLayout_3.addWidget(
            self.dateEdit_date_of_birth_primary, 8, 0, 1, 2)
        self.lineEdit_contect_primary = QLineEdit(self.frame_coments_ad_2)
        self.lineEdit_contect_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_contect_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_contect_primary.setFont(font)
        self.lineEdit_contect_primary.setStyleSheet("QLineEdit{\n"
                                                    "                                                 border: 0px solid;\n"
                                                    "                                                 color: rgb(240, 240, 240);\n"
                                                    "                                                 border-radius: 10px;\n"
                                                    "                                                 background-color: #1D222E;\n"
                                                    "                                                 padding-left: 10px;\n"
                                                    "                                                 padding-right: 10px;\n"
                                                    "                                                 selection-background-color: #30313F;\n"
                                                    "                                                 selection-color: #5F6063;\n"
                                                    "                                                 }\n"
                                                    "                                                 QLineEdit:hover{\n"
                                                    "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                    "                                                 }\n"
                                                    "                                                 \n"
                                                    "                                                 QLineEdit:focus{\n"
                                                    "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                    "                                                 }")
        self.lineEdit_contect_primary.setObjectName("lineEdit_contect_primary")
        self.gridLayout_3.addWidget(self.lineEdit_contect_primary, 4, 0, 1, 1)
        self.lineEdit_address_primary = QLineEdit(self.frame_coments_ad_2)
        self.lineEdit_address_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_address_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_address_primary.setFont(font)
        self.lineEdit_address_primary.setStyleSheet("QLineEdit{\n"
                                                    "                                                 border: 0px solid;\n"
                                                    "                                                 color: rgb(240, 240, 240);\n"
                                                    "                                                 border-radius: 10px;\n"
                                                    "                                                 background-color: #1D222E;\n"
                                                    "                                                 padding-left: 10px;\n"
                                                    "                                                 padding-right: 10px;\n"
                                                    "                                                 selection-background-color: #30313F;\n"
                                                    "                                                 selection-color: #5F6063;\n"
                                                    "                                                 }\n"
                                                    "                                                 QLineEdit:hover{\n"
                                                    "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                    "                                                 }\n"
                                                    "                                                 \n"
                                                    "                                                 QLineEdit:focus{\n"
                                                    "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                    "                                                 }")
        self.lineEdit_address_primary.setObjectName("lineEdit_address_primary")
        self.gridLayout_3.addWidget(self.lineEdit_address_primary, 1, 1, 1, 1)
        self.lineEdit_name_primary = QLineEdit(self.frame_coments_ad_2)
        self.lineEdit_name_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_name_primary.setFont(font)
        self.lineEdit_name_primary.setStyleSheet("QLineEdit{\n"
                                                 "                                                 border: 0px solid;\n"
                                                 "                                                 color: rgb(240, 240, 240);\n"
                                                 "                                                 border-radius: 10px;\n"
                                                 "                                                 background-color: #1D222E;\n"
                                                 "                                                 padding-left: 10px;\n"
                                                 "                                                 padding-right: 10px;\n"
                                                 "                                                 selection-background-color: #30313F;\n"
                                                 "                                                 selection-color: #5F6063;\n"
                                                 "                                                 }\n"
                                                 "                                                 QLineEdit:hover{\n"
                                                 "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                 "                                                 }\n"
                                                 "                                                 \n"
                                                 "                                                 QLineEdit:focus{\n"
                                                 "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                 "                                                 }")
        self.lineEdit_name_primary.setObjectName("lineEdit_name_primary")
        self.gridLayout_3.addWidget(self.lineEdit_name_primary, 1, 0, 1, 1)
        self.label_inforem_date_of_birth_ad_2 = QLabel(self.frame_coments_ad_2)
        self.label_inforem_date_of_birth_ad_2.setMinimumSize(QSize(0, 30))
        self.label_inforem_date_of_birth_ad_2.setMaximumSize(
            QSize(16777215, 30))
        self.label_inforem_date_of_birth_ad_2.setStyleSheet("color: white;\n"
                                                            "padding-left: 20px;")
        self.label_inforem_date_of_birth_ad_2.setObjectName(
            "label_inforem_date_of_birth_ad_2")
        self.gridLayout_3.addWidget(
            self.label_inforem_date_of_birth_ad_2, 6, 0, 1, 2)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setContentsMargins(50, 0, 50, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.radioButton_male_primary = QRadioButton(self.frame_coments_ad_2)
        font = QFont()
        font.setPointSize(10)
        self.radioButton_male_primary.setFont(font)
        self.radioButton_male_primary.setStyleSheet("QRadioButton {\n"
                                                    "      color: #fff;\n"
                                                    "      background-color: rgb(26, 27, 34);\n"
                                                    "}\n"
                                                    "QRadioButton::indicator {\n"
                                                    "                                                  border: 3px solid rgb(52, 59, 72);\n"
                                                    "                                                  width: 15px;\n"
                                                    "                                                  height: 15px;\n"
                                                    "                                                  border-radius: 10px;\n"
                                                    "                                                  background: rgb(44, 49, 60);\n"
                                                    "                                                  color: #fff;\n"
                                                    "                                                 }\n"
                                                    "                                                  QRadioButton::indicator:hover {\n"
                                                    "                                                  border: 3px solid rgb(61, 152, 212);\n"
                                                    "                                                  }\n"
                                                    "                                                  QRadioButton::indicator:checked {\n"
                                                    "                                                  background: 3px solid  rgb(82, 197, 130);\n"
                                                    "                                                  border: 3px solid  rgb(82, 197, 130);\n"
                                                    "                                                  }")
        self.radioButton_male_primary.setObjectName("radioButton_male_primary")
        self.horizontalLayout_29.addWidget(
            self.radioButton_male_primary, 0, Qt.AlignHCenter)
        self.radioButton_female_primary = QRadioButton(self.frame_coments_ad_2)
        font = QFont()
        font.setPointSize(10)
        self.radioButton_female_primary.setFont(font)
        self.radioButton_female_primary.setStyleSheet("QRadioButton {\n"
                                                      "      color: #fff;\n"
                                                      "      background-color: rgb(26, 27, 34);\n"
                                                      "}\n"
                                                      "QRadioButton::indicator {\n"
                                                      "                                                  border: 3px solid rgb(52, 59, 72);\n"
                                                      "                                                  width: 15px;\n"
                                                      "                                                  height: 15px;\n"
                                                      "                                                  border-radius: 10px;\n"
                                                      "                                                  background: rgb(44, 49, 60);\n"
                                                      "                                                  color: #fff;\n"
                                                      "                                                 }\n"
                                                      "                                                  QRadioButton::indicator:hover {\n"
                                                      "                                                  border: 3px solid rgb(61, 152, 212);\n"
                                                      "                                                  }\n"
                                                      "                                                  QRadioButton::indicator:checked {\n"
                                                      "                                                  background: 3px solid  rgb(82, 197, 130);\n"
                                                      "                                                  border: 3px solid  rgb(82, 197, 130);\n"
                                                      "                                                  }")
        self.radioButton_female_primary.setObjectName(
            "radioButton_female_primary")
        self.horizontalLayout_29.addWidget(
            self.radioButton_female_primary, 0, Qt.AlignHCenter)
        self.radioButton_other_primary = QRadioButton(self.frame_coments_ad_2)
        font = QFont()
        font.setPointSize(10)
        self.radioButton_other_primary.setFont(font)
        self.radioButton_other_primary.setStyleSheet("QRadioButton {\n"
                                                     "      color: #fff;\n"
                                                     "      background-color: rgb(26, 27, 34);\n"
                                                     "}\n"
                                                     "QRadioButton::indicator {\n"
                                                     "                                                  border: 3px solid rgb(52, 59, 72);\n"
                                                     "                                                  width: 15px;\n"
                                                     "                                                  height: 15px;\n"
                                                     "                                                  border-radius: 10px;\n"
                                                     "                                                  background: rgb(44, 49, 60);\n"
                                                     "                                                  color: #fff;\n"
                                                     "                                                 }\n"
                                                     "                                                  QRadioButton::indicator:hover {\n"
                                                     "                                                  border: 3px solid rgb(61, 152, 212);\n"
                                                     "                                                  }\n"
                                                     "                                                  QRadioButton::indicator:checked {\n"
                                                     "                                                  background: 3px solid  rgb(82, 197, 130);\n"
                                                     "                                                  border: 3px solid  rgb(82, 197, 130);\n"
                                                     "                                                  }")
        self.radioButton_other_primary.setObjectName(
            "radioButton_other_primary")
        self.horizontalLayout_29.addWidget(
            self.radioButton_other_primary, 0, Qt.AlignHCenter)
        self.gridLayout_3.addLayout(self.horizontalLayout_29, 9, 0, 1, 2)
        self.lineEdit_father_primary = QLineEdit(self.frame_coments_ad_2)
        self.lineEdit_father_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_father_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_father_primary.setFont(font)
        self.lineEdit_father_primary.setStyleSheet("QLineEdit{\n"
                                                   "                                                 border: 0px solid;\n"
                                                   "                                                 color: rgb(240, 240, 240);\n"
                                                   "                                                 border-radius: 10px;\n"
                                                   "                                                 background-color: #1D222E;\n"
                                                   "                                                 padding-left: 10px;\n"
                                                   "                                                 padding-right: 10px;\n"
                                                   "                                                 selection-background-color: #30313F;\n"
                                                   "                                                 selection-color: #5F6063;\n"
                                                   "                                                 }\n"
                                                   "                                                 QLineEdit:hover{\n"
                                                   "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                   "                                                 }\n"
                                                   "                                                 \n"
                                                   "                                                 QLineEdit:focus{\n"
                                                   "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                   "                                                 }")
        self.lineEdit_father_primary.setObjectName("lineEdit_father_primary")
        self.gridLayout_3.addWidget(self.lineEdit_father_primary, 2, 0, 1, 1)
        self.lineEdit_mather_primary = QLineEdit(self.frame_coments_ad_2)
        self.lineEdit_mather_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_mather_primary.setFont(font)
        self.lineEdit_mather_primary.setStyleSheet("QLineEdit{\n"
                                                   "                                                 border: 0px solid;\n"
                                                   "                                                 color: rgb(240, 240, 240);\n"
                                                   "                                                 border-radius: 10px;\n"
                                                   "                                                 background-color: #1D222E;\n"
                                                   "                                                 padding-left: 10px;\n"
                                                   "                                                 padding-right: 10px;\n"
                                                   "                                                 selection-background-color: #30313F;\n"
                                                   "                                                 selection-color: #5F6063;\n"
                                                   "                                                 }\n"
                                                   "                                                 QLineEdit:hover{\n"
                                                   "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                   "                                                 }\n"
                                                   "                                                 \n"
                                                   "                                                 QLineEdit:focus{\n"
                                                   "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                   "                                                 }")
        self.lineEdit_mather_primary.setObjectName("lineEdit_mather_primary")
        self.gridLayout_3.addWidget(self.lineEdit_mather_primary, 2, 1, 1, 1)
        self.lineEdit_registration_primary = QLineEdit(self.frame_coments_ad_2)
        self.lineEdit_registration_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_registration_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_registration_primary.setFont(font)
        self.lineEdit_registration_primary.setStyleSheet("QLineEdit{\n"
                                                         "                                                 border: 0px solid;\n"
                                                         "                                                 color: rgb(240, 240, 240);\n"
                                                         "                                                 border-radius: 10px;\n"
                                                         "                                                 background-color: #1D222E;\n"
                                                         "                                                 padding-left: 10px;\n"
                                                         "                                                 padding-right: 10px;\n"
                                                         "                                                 selection-background-color: #30313F;\n"
                                                         "                                                 selection-color: #5F6063;\n"
                                                         "                                                 }\n"
                                                         "                                                 QLineEdit:hover{\n"
                                                         "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                         "                                                 }\n"
                                                         "                                                 \n"
                                                         "                                                 QLineEdit:focus{\n"
                                                         "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                         "                                                 }")
        self.lineEdit_registration_primary.setObjectName(
            "lineEdit_registration_primary")
        self.gridLayout_3.addWidget(
            self.lineEdit_registration_primary, 5, 1, 1, 1)
        self.lineEdit_religion_primary = QLineEdit(self.frame_coments_ad_2)
        self.lineEdit_religion_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_religion_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_religion_primary.setFont(font)
        self.lineEdit_religion_primary.setStyleSheet("QLineEdit{\n"
                                                     "                                                 border: 0px solid;\n"
                                                     "                                                 color: rgb(240, 240, 240);\n"
                                                     "                                                 border-radius: 10px;\n"
                                                     "                                                 background-color: #1D222E;\n"
                                                     "                                                 padding-left: 10px;\n"
                                                     "                                                 padding-right: 10px;\n"
                                                     "                                                 selection-background-color: #30313F;\n"
                                                     "                                                 selection-color: #5F6063;\n"
                                                     "                                                 }\n"
                                                     "                                                 QLineEdit:hover{\n"
                                                     "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                     "                                                 }\n"
                                                     "                                                 \n"
                                                     "                                                 QLineEdit:focus{\n"
                                                     "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                     "                                                 }")
        self.lineEdit_religion_primary.setObjectName(
            "lineEdit_religion_primary")
        self.gridLayout_3.addWidget(self.lineEdit_religion_primary, 5, 0, 1, 1)
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.btn_addLower_primary = QPushButton(self.frame_coments_ad_2)
        self.btn_addLower_primary.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addLower_primary.setFont(font)
        self.btn_addLower_primary.setStyleSheet("QPushButton{\n"
                                                "  color: rgb(255, 255, 255);\n"
                                                "                                        background-color: rgb(26, 114, 255);\n"
                                                "                                        border: 0px solid;\n"
                                                "                                        border-radius: 5px;\n"
                                                "                                        }\n"
                                                "                                        QPushButton:hover{\n"
                                                "                                        background-color: rgb(21, 134, 255);\n"
                                                "                                        }\n"
                                                "                                       QPushButton:pressed{\n"
                                                "                                        background-color: rgba(26, 114, 255, 100);\n"
                                                "                                        }")
        self.btn_addLower_primary.setObjectName("btn_addLower_primary")
        self.horizontalLayout_30.addWidget(self.btn_addLower_primary)
        self.btn_go_home_primary = QPushButton(self.frame_coments_ad_2)
        self.btn_go_home_primary.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_go_home_primary.setFont(font)
        self.btn_go_home_primary.setStyleSheet("QPushButton{\n"
                                               "  color: rgb(255, 255, 255);\n"
                                               "                                        background-color: rgb(44, 46, 58);\n"
                                               "                                        border: 0px solid;\n"
                                               "                                        border-radius: 5px;\n"
                                               "                                        }\n"
                                               "                                        QPushButton:hover{\n"
                                               "                                        background-color: rgb(21, 134, 255);\n"
                                               "                                        }\n"
                                               "                                       QPushButton:pressed{\n"
                                               "                                        background-color: rgba(26, 114, 255, 100);\n"
                                               "                                        }")
        self.btn_go_home_primary.setObjectName("btn_go_home_primary")
        self.horizontalLayout_30.addWidget(self.btn_go_home_primary)
        self.gridLayout_3.addLayout(self.horizontalLayout_30, 11, 0, 1, 2)
        self.comboBox_stream_primary = QComboBox(self.frame_coments_ad_2)
        self.comboBox_stream_primary.setMinimumSize(QSize(0, 30))
        self.comboBox_stream_primary.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.comboBox_stream_primary.setFont(font)
        self.comboBox_stream_primary.setStyleSheet("QComboBox{\n"
                                                   "    background-color: #1D222E;\n"
                                                   "    border-radius: 10px;\n"
                                                   "    border: 2px solid  #1D222E;\n"
                                                   "    padding: 5px;\n"
                                                   "    padding-left: 10px;\n"
                                                   "    color: white;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QComboBox:hover{\n"
                                                   "    border: 2px solid rgb(49, 50, 63);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QComboBox::drop-down {\n"
                                                   "    subcontrol-origin: padding;\n"
                                                   "    subcontrol-position: top right;\n"
                                                   "    width: 25px;\n"
                                                   "    border-left-width: 3px;\n"
                                                   "    border-left-color: rgba(39, 44, 54, 150);\n"
                                                   "    border-left-style: solid;\n"
                                                   "    border-top-right-radius: 3px;\n"
                                                   "    border-bottom-right-radius: 3px;\n"
                                                   "    background-image: url(./packges/app/items/icons/16x16/cil-arrow-bottom.png);\n"
                                                   "    background-position: center;\n"
                                                   "    background-repeat: no-reperat;\n"
                                                   "}\n"
                                                   "QComboBox QAbstractItemView {\n"
                                                   "    color: rgb(85, 170, 255);\n"
                                                   "    background-color: #1D222E;\n"
                                                   "    padding: 10px;\n"
                                                   "    selection-background-color: rgb(39, 44, 54);\n"
                                                   "}")
        self.comboBox_stream_primary.setObjectName("comboBox_stream_primary")
        self.comboBox_stream_primary.addItem("")
        self.comboBox_stream_primary.addItem("")
        self.comboBox_stream_primary.addItem("")
        self.comboBox_stream_primary.addItem("")
        self.comboBox_stream_primary.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_stream_primary, 4, 1, 1, 1)
        self.lineEdit_email_primary = QLineEdit(self.frame_coments_ad_2)
        self.lineEdit_email_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_email_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_email_primary.setStyleSheet("QLineEdit{\n"
                                                  "                                                 border: 0px solid;\n"
                                                  "                                                 color: rgb(240, 240, 240);\n"
                                                  "                                                 border-radius: 10px;\n"
                                                  "                                                 background-color: #1D222E;\n"
                                                  "                                                 padding-left: 10px;\n"
                                                  "                                                 padding-right: 10px;\n"
                                                  "                                                 selection-background-color: #30313F;\n"
                                                  "                                                 selection-color: #5F6063;\n"
                                                  "                                                 }\n"
                                                  "                                                 QLineEdit:hover{\n"
                                                  "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                  "                                                 }\n"
                                                  "                                                 \n"
                                                  "                                                 QLineEdit:focus{\n"
                                                  "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                  "                                                 }")
        self.lineEdit_email_primary.setObjectName("lineEdit_email_primary")
        self.gridLayout_3.addWidget(self.lineEdit_email_primary, 3, 0, 1, 2)
        self.verticalLayout_47.addWidget(self.frame_coments_ad_2)
        self.verticalLayout_48.addWidget(self.frame_main_content_for_primary)
        self.stackedWidget.addWidget(self.page)

        self.page_add_advan = QWidget()
        self.page_add_advan.setObjectName("page_add_advan")
        self.verticalLayout_45 = QVBoxLayout(self.page_add_advan)
        self.verticalLayout_45.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.frame_main_content_for_advance = QFrame(self.page_add_advan)
        self.frame_main_content_for_advance.setStyleSheet("QFrame {\n"
                                                          "    \n"
                                                          "    background-color: rgb(26, 27, 34);\n"
                                                          "    border-radius: 10px;\n"
                                                          "    border: 0px solid;\n"
                                                          "}")
        self.frame_main_content_for_advance.setFrameShape(QFrame.StyledPanel)
        self.frame_main_content_for_advance.setFrameShadow(QFrame.Raised)
        self.frame_main_content_for_advance.setObjectName(
            "frame_main_content_for_advance")
        self.verticalLayout_46 = QVBoxLayout(
            self.frame_main_content_for_advance)
        self.verticalLayout_46.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_icon_ = QLabel(self.frame_main_content_for_advance)
        self.label_icon_.setMinimumSize(QSize(200, 200))
        self.label_icon_.setMaximumSize(QSize(200, 200))
        self.label_icon_.setStyleSheet("QLabel{\n"
                                       "    border: 8px solid rgb(37, 38, 48);\n"
                                       "    background-color: rgb(50, 52, 65);\n"
                                       "    border-radius: 100px;\n"
                                       "color: white;\n"
                                       "}")
        self.label_icon_.setObjectName("label_icon_")
        self.verticalLayout_46.addWidget(self.label_icon_, 0, Qt.AlignHCenter)
        self.frame_coments_ad = QFrame(self.frame_main_content_for_advance)
        self.frame_coments_ad.setStyleSheet("background-color: none;")
        self.frame_coments_ad.setFrameShape(QFrame.StyledPanel)
        self.frame_coments_ad.setFrameShadow(QFrame.Raised)
        self.frame_coments_ad.setObjectName("frame_coments_ad")
        self.gridLayout_2 = QGridLayout(self.frame_coments_ad)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_inforem_date_of_birth_ad = QLabel(self.frame_coments_ad)
        self.label_inforem_date_of_birth_ad.setMinimumSize(QSize(0, 30))
        self.label_inforem_date_of_birth_ad.setMaximumSize(QSize(16777215, 30))
        self.label_inforem_date_of_birth_ad.setStyleSheet("color: white;\n"
                                                          "padding-left: 20px;")
        self.label_inforem_date_of_birth_ad.setObjectName(
            "label_inforem_date_of_birth_ad")
        self.gridLayout_2.addWidget(
            self.label_inforem_date_of_birth_ad, 6, 0, 1, 2)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setContentsMargins(50, 0, 50, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.radioButton_male_ad = QRadioButton(self.frame_coments_ad)
        font = QFont()
        font.setPointSize(10)
        self.radioButton_male_ad.setFont(font)
        self.radioButton_male_ad.setStyleSheet("QRadioButton {\n"
                                               "      color: #fff;\n"
                                               "      background-color: rgb(26, 27, 34);\n"
                                               "}\n"
                                               "QRadioButton::indicator {\n"
                                               "                                                  border: 3px solid rgb(52, 59, 72);\n"
                                               "                                                  width: 15px;\n"
                                               "                                                  height: 15px;\n"
                                               "                                                  border-radius: 10px;\n"
                                               "                                                  background: rgb(44, 49, 60);\n"
                                               "                                                  color: #fff;\n"
                                               "                                                 }\n"
                                               "                                                  QRadioButton::indicator:hover {\n"
                                               "                                                  border: 3px solid rgb(61, 152, 212);\n"
                                               "                                                  }\n"
                                               "                                                  QRadioButton::indicator:checked {\n"
                                               "                                                  background: 3px solid  rgb(82, 197, 130);\n"
                                               "                                                  border: 3px solid  rgb(82, 197, 130);\n"
                                               "                                                  }")
        self.radioButton_male_ad.setObjectName("radioButton_male_ad")
        self.horizontalLayout_27.addWidget(
            self.radioButton_male_ad, 0, Qt.AlignHCenter)
        self.radioButton_female_ad = QRadioButton(self.frame_coments_ad)
        font = QFont()
        font.setPointSize(10)
        self.radioButton_female_ad.setFont(font)
        self.radioButton_female_ad.setStyleSheet("QRadioButton {\n"
                                                 "      color: #fff;\n"
                                                 "      background-color: rgb(26, 27, 34);\n"
                                                 "}\n"
                                                 "QRadioButton::indicator {\n"
                                                 "                                                  border: 3px solid rgb(52, 59, 72);\n"
                                                 "                                                  width: 15px;\n"
                                                 "                                                  height: 15px;\n"
                                                 "                                                  border-radius: 10px;\n"
                                                 "                                                  background: rgb(44, 49, 60);\n"
                                                 "                                                  color: #fff;\n"
                                                 "                                                 }\n"
                                                 "                                                  QRadioButton::indicator:hover {\n"
                                                 "                                                  border: 3px solid rgb(61, 152, 212);\n"
                                                 "                                                  }\n"
                                                 "                                                  QRadioButton::indicator:checked {\n"
                                                 "                                                  background: 3px solid  rgb(82, 197, 130);\n"
                                                 "                                                  border: 3px solid  rgb(82, 197, 130);\n"
                                                 "                                                  }")
        self.radioButton_female_ad.setObjectName("radioButton_female_ad")
        self.horizontalLayout_27.addWidget(self.radioButton_female_ad, 0,
                                           Qt.AlignHCenter)
        self.radioButton_other_ad = QRadioButton(self.frame_coments_ad)
        font = QFont()
        font.setPointSize(10)
        self.radioButton_other_ad.setFont(font)
        self.radioButton_other_ad.setStyleSheet("QRadioButton {\n"
                                                "      color: #fff;\n"
                                                "      background-color: rgb(26, 27, 34);\n"
                                                "}\n"
                                                "QRadioButton::indicator {\n"
                                                "                                                  border: 3px solid rgb(52, 59, 72);\n"
                                                "                                                  width: 15px;\n"
                                                "                                                  height: 15px;\n"
                                                "                                                  border-radius: 10px;\n"
                                                "                                                  background: rgb(44, 49, 60);\n"
                                                "                                                  color: #fff;\n"
                                                "                                                 }\n"
                                                "                                                  QRadioButton::indicator:hover {\n"
                                                "                                                  border: 3px solid rgb(61, 152, 212);\n"
                                                "                                                  }\n"
                                                "                                                  QRadioButton::indicator:checked {\n"
                                                "                                                  background: 3px solid  rgb(82, 197, 130);\n"
                                                "                                                  border: 3px solid  rgb(82, 197, 130);\n"
                                                "                                                  }")
        self.radioButton_other_ad.setObjectName("radioButton_other_ad")
        self.horizontalLayout_27.addWidget(
            self.radioButton_other_ad, 0, Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.horizontalLayout_27, 9, 0, 1, 2)
        self.lineEdit_father_ad = QLineEdit(self.frame_coments_ad)
        self.lineEdit_father_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_father_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_father_ad.setFont(font)
        self.lineEdit_father_ad.setStyleSheet("QLineEdit{\n"
                                              "                                                 border: 0px solid;\n"
                                              "                                                 color: rgb(240, 240, 240);\n"
                                              "                                                 border-radius: 10px;\n"
                                              "                                                 background-color: #1D222E;\n"
                                              "                                                 padding-left: 10px;\n"
                                              "                                                 padding-right: 10px;\n"
                                              "                                                 selection-background-color: #30313F;\n"
                                              "                                                 selection-color: #5F6063;\n"
                                              "                                                 }\n"
                                              "                                                 QLineEdit:hover{\n"
                                              "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                              "                                                 }\n"
                                              "                                                 \n"
                                              "                                                 QLineEdit:focus{\n"
                                              "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                              "                                                 }")
        self.lineEdit_father_ad.setObjectName("lineEdit_father_ad")
        self.lineEdit_father_ad.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.lineEdit_father_ad, 2, 0, 1, 1)
        self.lineEdit_mather_ad = QLineEdit(self.frame_coments_ad)
        self.lineEdit_mather_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_mather_ad.setFont(font)
        self.lineEdit_mather_ad.setStyleSheet("QLineEdit{\n"
                                              "                                                 border: 0px solid;\n"
                                              "                                                 color: rgb(240, 240, 240);\n"
                                              "                                                 border-radius: 10px;\n"
                                              "                                                 background-color: #1D222E;\n"
                                              "                                                 padding-left: 10px;\n"
                                              "                                                 padding-right: 10px;\n"
                                              "                                                 selection-background-color: #30313F;\n"
                                              "                                                 selection-color: #5F6063;\n"
                                              "                                                 }\n"
                                              "                                                 QLineEdit:hover{\n"
                                              "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                              "                                                 }\n"
                                              "                                                 \n"
                                              "                                                 QLineEdit:focus{\n"
                                              "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                              "                                                 }")
        self.lineEdit_mather_ad.setObjectName("lineEdit_mather_ad")
        self.lineEdit_mather_ad.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.lineEdit_mather_ad, 2, 1, 1, 1)
        self.lineEdit_religion_ad = QLineEdit(self.frame_coments_ad)
        self.lineEdit_religion_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_religion_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_religion_ad.setFont(font)
        self.lineEdit_religion_ad.setStyleSheet("QLineEdit{\n"
                                                "                                                 border: 0px solid;\n"
                                                "                                                 color: rgb(240, 240, 240);\n"
                                                "                                                 border-radius: 10px;\n"
                                                "                                                 background-color: #1D222E;\n"
                                                "                                                 padding-left: 10px;\n"
                                                "                                                 padding-right: 10px;\n"
                                                "                                                 selection-background-color: #30313F;\n"
                                                "                                                 selection-color: #5F6063;\n"
                                                "                                                 }\n"
                                                "                                                 QLineEdit:hover{\n"
                                                "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                "                                                 }\n"
                                                "                                                 \n"
                                                "                                                 QLineEdit:focus{\n"
                                                "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                "                                                 }")
        self.lineEdit_religion_ad.setObjectName("lineEdit_religion_ad")
        self.lineEdit_religion_ad.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.lineEdit_religion_ad, 5, 0, 1, 1)
        self.lineEdit_registration_ad = QLineEdit(self.frame_coments_ad)
        self.lineEdit_registration_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_registration_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_registration_ad.setFont(font)
        self.lineEdit_registration_ad.setStyleSheet("QLineEdit{\n"
                                                    "                                                 border: 0px solid;\n"
                                                    "                                                 color: rgb(240, 240, 240);\n"
                                                    "                                                 border-radius: 10px;\n"
                                                    "                                                 background-color: #1D222E;\n"
                                                    "                                                 padding-left: 10px;\n"
                                                    "                                                 padding-right: 10px;\n"
                                                    "                                                 selection-background-color: #30313F;\n"
                                                    "                                                 selection-color: #5F6063;\n"
                                                    "                                                 }\n"
                                                    "                                                 QLineEdit:hover{\n"
                                                    "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                                    "                                                 }\n"
                                                    "                                                 \n"
                                                    "                                                 QLineEdit:focus{\n"
                                                    "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                                    "                                                 }")
        self.lineEdit_registration_ad.setObjectName("lineEdit_registration_ad")
        self.lineEdit_registration_ad.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.lineEdit_registration_ad, 5, 1, 1, 1)
        self.lineEdit_email_ad = QLineEdit(self.frame_coments_ad)
        self.lineEdit_email_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_email_ad.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_email_ad.setFont(font)
        self.lineEdit_email_ad.setStyleSheet("QLineEdit{\n"
                                             "                                                 border: 0px solid;\n"
                                             "                                                 color: rgb(240, 240, 240);\n"
                                             "                                                 border-radius: 10px;\n"
                                             "                                                 background-color: #1D222E;\n"
                                             "                                                 padding-left: 10px;\n"
                                             "                                                 padding-right: 10px;\n"
                                             "                                                 selection-background-color: #30313F;\n"
                                             "                                                 selection-color: #5F6063;\n"
                                             "                                                 }\n"
                                             "                                                 QLineEdit:hover{\n"
                                             "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                             "                                                 }\n"
                                             "                                                 \n"
                                             "                                                 QLineEdit:focus{\n"
                                             "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                             "                                                 }")
        self.lineEdit_email_ad.setObjectName("lineEdit_email_ad")
        self.lineEdit_email_ad.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.lineEdit_email_ad, 3, 0, 1, 1)
        self.lineEdit_level_ad = QComboBox(self.frame_coments_ad)
        self.lineEdit_level_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_level_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_level_ad.setFont(font)
        self.lineEdit_level_ad.setStyleSheet("QComboBox{\n"
                                             "    background-color: #1D222E;\n"
                                             "    border-radius: 10px;\n"
                                             "    border: 2px solid  #1D222E;\n"
                                             "    padding: 5px;\n"
                                             "    padding-left: 10px;\n"
                                             "    color: white;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:hover{\n"
                                             "    border: 2px solid rgb(49, 50, 63);\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::drop-down {\n"
                                             "    subcontrol-origin: padding;\n"
                                             "    subcontrol-position: top right;\n"
                                             "    width: 25px;\n"
                                             "    border-left-width: 3px;\n"
                                             "    border-left-color: rgba(39, 44, 54, 150);\n"
                                             "    border-left-style: solid;\n"
                                             "    border-top-right-radius: 3px;\n"
                                             "    border-bottom-right-radius: 3px;\n"
                                             "    background-image: url(./packges/app/items/icons/16x16/cil-arrow-bottom.png);\n"
                                             "    background-position: center;\n"
                                             "    background-repeat: no-reperat;\n"
                                             "}\n"
                                             "QComboBox QAbstractItemView {\n"
                                             "    color: rgb(85, 170, 255);\n"
                                             "    background-color: #1D222E;\n"
                                             "    padding: 10px;\n"
                                             "    selection-background-color: rgb(39, 44, 54);\n"
                                             "}")
        self.lineEdit_level_ad.setObjectName("lineEdit_level_ad")
        self.lineEdit_level_ad.addItem("")
        self.lineEdit_level_ad.addItem("")
        self.gridLayout_2.addWidget(self.lineEdit_level_ad, 4, 1, 1, 1)
        self.comboBox_stream = QComboBox(self.frame_coments_ad)
        self.comboBox_stream.setMinimumSize(QSize(0, 30))
        self.comboBox_stream.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.comboBox_stream.setFont(font)
        self.comboBox_stream.setObjectName("comboBox_stream")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.setStyleSheet("QComboBox{\n"
                                           "    background-color: #1D222E;\n"
                                           "    border-radius: 10px;\n"
                                           "    border: 2px solid  #1D222E;\n"
                                           "    padding: 5px;\n"
                                           "    padding-left: 10px;\n"
                                           "    color: white;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox:hover{\n"
                                           "    border: 2px solid rgb(49, 50, 63);\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox::drop-down {\n"
                                           "    subcontrol-origin: padding;\n"
                                           "    subcontrol-position: top right;\n"
                                           "    width: 25px;\n"
                                           "    border-left-width: 3px;\n"
                                           "    border-left-color: rgba(39, 44, 54, 150);\n"
                                           "    border-left-style: solid;\n"
                                           "    border-top-right-radius: 3px;\n"
                                           "    border-bottom-right-radius: 3px;\n"
                                           "    background-image: url(./packges/app/items/icons/16x16/cil-arrow-bottom.png);\n"
                                           "    background-position: center;\n"
                                           "    background-repeat: no-reperat;\n"
                                           "}\n"
                                           "QComboBox QAbstractItemView {\n"
                                           "    color: rgb(85, 170, 255);\n"
                                           "    background-color: #1D222E;\n"
                                           "    padding: 10px;\n"
                                           "    selection-background-color: rgb(39, 44, 54);\n"
                                           "}")
        self.gridLayout_2.addWidget(self.comboBox_stream, 3, 1, 1, 1)
        self.dateEdit_date_of_birth_ad = QDateEdit(self.frame_coments_ad)
        self.dateEdit_date_of_birth_ad.setMinimumSize(QSize(0, 30))
        self.dateEdit_date_of_birth_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.dateEdit_date_of_birth_ad.setFont(font)
        self.dateEdit_date_of_birth_ad.setObjectName(
            "dateEdit_date_of_birth_ad")
        self.gridLayout_2.addWidget(self.dateEdit_date_of_birth_ad, 8, 0, 1, 2)
        self.lineEdit_contect_ad = QLineEdit(self.frame_coments_ad)
        self.lineEdit_contect_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_contect_ad.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_contect_ad.setClearButtonEnabled(True)
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_contect_ad.setFont(font)
        self.lineEdit_contect_ad.setStyleSheet("QLineEdit{\n"
                                               "                                                 border: 0px solid;\n"
                                               "                                                 color: rgb(240, 240, 240);\n"
                                               "                                                 border-radius: 10px;\n"
                                               "                                                 background-color: #1D222E;\n"
                                               "                                                 padding-left: 10px;\n"
                                               "                                                 padding-right: 10px;\n"
                                               "                                                 selection-background-color: #30313F;\n"
                                               "                                                 selection-color: #5F6063;\n"
                                               "                                                 }\n"
                                               "                                                 QLineEdit:hover{\n"
                                               "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                               "                                                 }\n"
                                               "                                                 \n"
                                               "                                                 QLineEdit:focus{\n"
                                               "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                               "                                                 }")
        self.lineEdit_contect_ad.setObjectName("lineEdit_contect_ad")
        self.gridLayout_2.addWidget(self.lineEdit_contect_ad, 4, 0, 1, 1)
        self.lineEdit_name_ad = QLineEdit(self.frame_coments_ad)
        self.lineEdit_name_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_ad.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_name_ad.setClearButtonEnabled(True)
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_name_ad.setFont(font)
        self.lineEdit_name_ad.setStyleSheet("QLineEdit{\n"
                                            "                                                 border: 0px solid;\n"
                                            "                                                 color: rgb(240, 240, 240);\n"
                                            "                                                 border-radius: 10px;\n"
                                            "                                                 background-color: #1D222E;\n"
                                            "                                                 padding-left: 10px;\n"
                                            "                                                 padding-right: 10px;\n"
                                            "                                                 selection-background-color: #30313F;\n"
                                            "                                                 selection-color: #5F6063;\n"
                                            "                                                 }\n"
                                            "                                                 QLineEdit:hover{\n"
                                            "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                            "                                                 }\n"
                                            "                                                 \n"
                                            "                                                 QLineEdit:focus{\n"
                                            "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                            "                                                 }")
        self.lineEdit_name_ad.setObjectName("lineEdit_name_ad")
        self.gridLayout_2.addWidget(self.lineEdit_name_ad, 1, 0, 1, 1)
        self.lineEdit_address_ad = QLineEdit(self.frame_coments_ad)
        self.lineEdit_address_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_address_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_address_ad.setFont(font)
        self.lineEdit_address_ad.setStyleSheet("QLineEdit{\n"
                                               "                                                 border: 0px solid;\n"
                                               "                                                 color: rgb(240, 240, 240);\n"
                                               "                                                 border-radius: 10px;\n"
                                               "                                                 background-color: #1D222E;\n"
                                               "                                                 padding-left: 10px;\n"
                                               "                                                 padding-right: 10px;\n"
                                               "                                                 selection-background-color: #30313F;\n"
                                               "                                                 selection-color: #5F6063;\n"
                                               "                                                 }\n"
                                               "                                                 QLineEdit:hover{\n"
                                               "                                                 border: 2px solid rgb(49, 50, 63);\n"
                                               "                                                 }\n"
                                               "                                                 \n"
                                               "                                                 QLineEdit:focus{\n"
                                               "                                                 border: 2px solid rgb(61, 152, 212);\n"
                                               "                                                 }")
        self.lineEdit_address_ad.setObjectName("lineEdit_address_ad")
        self.lineEdit_address_ad.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.lineEdit_address_ad, 1, 1, 1, 1)
        self.label_show_roll_ad = QLabel(self.frame_coments_ad)
        self.label_show_roll_ad.setMinimumSize(QSize(0, 30))
        self.label_show_roll_ad.setMaximumSize(QSize(16777215, 30))
        self.label_show_roll_ad.setStyleSheet("color: white;\n"
                                              "padding-left: 10px;\n"
                                              "border-top: 2px solid white;\n"
                                              "border-bottom: 2px solid white;\n"
                                              "border-radius: 0px;")
        self.label_show_roll_ad.setObjectName("label_show_roll_ad")
        self.gridLayout_2.addWidget(self.label_show_roll_ad, 10, 0, 1, 2)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.btn_addLower_adv = QPushButton(self.frame_coments_ad)
        self.btn_addLower_adv.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addLower_adv.setFont(font)
        self.btn_addLower_adv.setStyleSheet("QPushButton{\n"
                                            "  color: rgb(255, 255, 255);\n"
                                            "                                        background-color: rgb(26, 114, 255);\n"
                                            "                                        border: 0px solid;\n"
                                            "                                        border-radius: 5px;\n"
                                            "                                        }\n"
                                            "                                        QPushButton:hover{\n"
                                            "                                        background-color: rgb(21, 134, 255);\n"
                                            "                                        }\n"
                                            "                                       QPushButton:pressed{\n"
                                            "                                        background-color: rgba(26, 114, 255, 100);\n"
                                            "                                        }")
        self.btn_addLower_adv.setObjectName("btn_addLower_adv")
        self.horizontalLayout_28.addWidget(self.btn_addLower_adv)
        self.btn_go_home_ad = QPushButton(self.frame_coments_ad)
        self.btn_go_home_ad.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_go_home_ad.setFont(font)
        self.btn_go_home_ad.setStyleSheet("QPushButton{\n"
                                          "  color: rgb(255, 255, 255);\n"
                                          "                                        background-color: rgb(44, 46, 58);\n"
                                          "                                        border: 0px solid;\n"
                                          "                                        border-radius: 5px;\n"
                                          "                                        }\n"
                                          "                                        QPushButton:hover{\n"
                                          "                                        background-color: rgb(21, 134, 255);\n"
                                          "                                        }\n"
                                          "                                       QPushButton:pressed{\n"
                                          "                                        background-color: rgba(26, 114, 255, 100);\n"
                                          "                                        }")
        self.btn_go_home_ad.setObjectName("btn_go_home_ad")
        self.horizontalLayout_28.addWidget(self.btn_go_home_ad)
        self.gridLayout_2.addLayout(self.horizontalLayout_28, 11, 0, 1, 2)
        self.verticalLayout_46.addWidget(self.frame_coments_ad)
        self.verticalLayout_45.addWidget(self.frame_main_content_for_advance)
        self.stackedWidget.addWidget(self.page_add_advan)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.Home)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_main_home_bar = QFrame(self.Home)
        self.frame_main_home_bar.setObjectName(u"frame_main_home_bar")
        self.frame_main_home_bar.setStyleSheet(u"")
        self.frame_main_home_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_home_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_main_home_bar)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.scrollArea = QScrollArea(self.frame_main_home_bar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
                                      " QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "        background: rgb(45, 48, 59);\n"
                                      "        width: 15px;\n"
                                      "        margin: 30px 0 30px 0;\n"
                                      "        border-radius: 7px;\n"
                                      " }\n"
                                      "\n"
                                      "/*  HANDLE BAR VERTICAL */\n"
                                      "QScrollBar::handle:vertical {	\n"
                                      "	background-color: rgb(34, 35, 44);\n"
                                      "	min-height: 15px;\n"
                                      "	border-radius: 7px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:hover{	\n"
                                      "	background-color: rgb(38, 40, 50);\n"
                                      "\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:pressed {	\n"
                                      "	background-color: rgb(31, 32, 40);\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "/* BTN TOP - SCROLLBAR */\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "	border: none;\n"
                                      "	background-color: rgb(45, 48, 59);\n"
                                      "	height: 15px;\n"
                                      "	border-top-left-radius: 7px;\n"
                                      "	border-top-right-radius: 7px;\n"
                                      "	subcontrol-position: top;\n"
                                      "	subcontrol-origin: margin;\n"
                                      "	margin-top: 10px;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:hover {	\n"
                                      "	background-color:   rgb(38, 40, 50);\n"
                                      "\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:pressed {	\n"
                                      "	backgrou"
                                      "nd-color:rgb(31, 32, 40);\n"
                                      "        \n"
                                      "}\n"
                                      "\n"
                                      "/* BTN BOTTOM - SCROLLBAR */\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "	border: none;\n"
                                      "	background-color: rgb(45, 48, 59);\n"
                                      "	height: 15px;\n"
                                      "	border-bottom-left-radius: 7px;\n"
                                      "	border-bottom-right-radius: 7px;\n"
                                      "	subcontrol-position: bottom;\n"
                                      "	subcontrol-origin: margin;\n"
                                      "	margin-bottom: 10px;\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:hover {	\n"
                                      "	background-color:    rgb(38, 40, 50);\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:pressed {	\n"
                                      "	background-color:rgb(31, 32, 40);\n"
                                      "}\n"
                                      "/* RESET ARROW */\n"
                                      "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "	background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "	background: none;\n"
                                      "}\n")
        self.scrollArea.setWidgetResizable(True)
        self.page_content_Input = QWidget()
        self.page_content_Input.setObjectName(u"page_content_Input")
        self.page_content_Input.setGeometry(QRect(0, 0, 753, 1636))
        self.page_content_Input.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.page_content_Input)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_inter_1 = QWidget(self.page_content_Input)
        self.widget_inter_1.setObjectName(u"widget_inter_1")
        self.widget_inter_1.setMinimumSize(QSize(0, 450))
        self.widget_inter_1.setMaximumSize(QSize(16777215, 450))
        self.widget_inter_1.setStyleSheet(u"QWidget{\n"
                                          "	background-color:rgb(26, 27, 34);\n"
                                          "	border-radius: 10px;\n"
                                          "}\n"
                                          "QWidget:hover{\n"
                                          "		border: 2px solid rgb(0, 149, 241);\n"
                                          "}")
        self.verticalLayout_19 = QVBoxLayout(self.widget_inter_1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.label_info_Inter_face = QLabel(self.widget_inter_1)
        self.label_info_Inter_face.setObjectName(u"label_info_Inter_face")
        font2 = QFont()
        font2.setFamily(u"MesloLGL Nerd Font")
        font2.setPointSize(10)
        self.label_info_Inter_face.setFont(font2)
        self.label_info_Inter_face.setStyleSheet(u"background-color: none;\n"
                                                 "border: none;\n"
                                                 "padding-left: 25px;\n"
                                                 "color: white;")

        self.verticalLayout_19.addWidget(self.label_info_Inter_face)

        self.label_info_Inter_1 = QLabel(self.widget_inter_1)
        self.label_info_Inter_1.setObjectName(u"label_info_Inter_1")
        font2 = QFont()
        font2.setFamily(u"MesloLGL Nerd Font")
        font2.setPointSize(10)
        self.label_info_Inter_1.setFont(font2)
        self.label_info_Inter_1.setStyleSheet(u"background-color: none;\n"
                                              "border: none;\n"
                                              "padding-left: 25px;\n"
                                              "color: white;")

        self.verticalLayout_19.addWidget(self.label_info_Inter_1)

        self.frame_inter_delet_bar_1 = QFrame(self.widget_inter_1)
        self.frame_inter_delet_bar_1.setObjectName(u"frame_inter_delet_bar_1")
        self.frame_inter_delet_bar_1.setMaximumSize(QSize(16777215, 40))
        self.frame_inter_delet_bar_1.setStyleSheet(
            u"border: none;\n background-color: rgb(40, 41, 52);")
        self.frame_inter_delet_bar_1.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_delet_bar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_inter_delet_bar_1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_info_user_inter_1 = QLabel(self.frame_inter_delet_bar_1)
        self.label_info_user_inter_1.setObjectName(u"label_info_user_inter_1")
        font3 = QFont()
        font3.setFamily(u"MesloLGM NF")
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_info_user_inter_1.setFont(font3)
        self.label_info_user_inter_1.setStyleSheet(
            u"color: white;\n padding-left: 20px;")
        self.label_info_user_inter_1.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_12.addWidget(self.label_info_user_inter_1)

        self.btn_delete_inter_1 = QPushButton(self.frame_inter_delet_bar_1)
        self.btn_delete_inter_1.setObjectName(u"btn_delete_inter_1")
        self.btn_delete_inter_1.setMinimumSize(QSize(100, 25))
        self.btn_delete_inter_1.setMaximumSize(QSize(100, 40))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_delete_inter_1.setFont(font4)
        self.btn_delete_inter_1.setStyleSheet(u"QPushButton{\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "	background-color: rgb(0, 127, 226);\n"
                                              "	border: 0px solid;\n"
                                              "	border-radius: 5px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "	background-color: rgb(85, 170, 255);\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "	background-color: rgba(85, 170, 255, 100);\n"
                                              "}")

        self.horizontalLayout_12.addWidget(self.btn_delete_inter_1)

        self.verticalLayout_19.addWidget(self.frame_inter_delet_bar_1)

        self.verticalLayout_13.addWidget(self.widget_inter_1)

        self.widget_lower_1 = QWidget(self.page_content_Input)
        self.widget_lower_1.setObjectName(u"widget_lower_1")
        self.widget_lower_1.setMinimumSize(QSize(0, 400))
        self.widget_lower_1.setStyleSheet(u"QWidget{\n"
                                          "	background-color:rgb(26, 27, 34);\n"
                                          "	border-radius: 10px;\n"
                                          "}\n"
                                          "QWidget:hover{\n"
                                          "		border: 2px solid rgb(0, 149, 241);\n"
                                          "}")
        self.verticalLayout_21 = QVBoxLayout(self.widget_lower_1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_info_lower_1 = QLabel(self.widget_lower_1)
        self.label_info_lower_1.setObjectName(u"label_info_lower_1")
        self.label_info_lower_1.setFont(font2)
        self.label_info_lower_1.setStyleSheet(u"background-color: none;\n"
                                              "border: none;\n"
                                              "padding-left: 25px;\n"
                                              "color: white;")

        self.verticalLayout_21.addWidget(self.label_info_lower_1)

        self.frame_inter_delet_bar_3 = QFrame(self.widget_lower_1)
        self.frame_inter_delet_bar_3.setObjectName(u"frame_inter_delet_bar_3")
        self.frame_inter_delet_bar_3.setMaximumSize(QSize(16777215, 40))
        self.frame_inter_delet_bar_3.setStyleSheet(
            u"border: none;\n background-color: rgb(40, 41, 52);")
        self.frame_inter_delet_bar_3.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_delet_bar_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_inter_delet_bar_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_info_user_lower_1 = QLabel(self.frame_inter_delet_bar_3)
        self.label_info_user_lower_1.setObjectName(u"label_info_user_lower_1")
        self.label_info_user_lower_1.setFont(font3)
        self.label_info_user_lower_1.setStyleSheet(
            u"color: white;\n padding-left: 20px;")
        self.label_info_user_lower_1.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_14.addWidget(self.label_info_user_lower_1)

        self.btn_delete_lower_1 = QPushButton(self.frame_inter_delet_bar_3)
        self.btn_delete_lower_1.setObjectName(u"btn_delete_lower_1")
        self.btn_delete_lower_1.setMinimumSize(QSize(100, 25))
        self.btn_delete_lower_1.setMaximumSize(QSize(100, 40))
        self.btn_delete_lower_1.setFont(font4)
        self.btn_delete_lower_1.setStyleSheet(u"QPushButton{\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "	background-color: rgb(0, 127, 226);\n"
                                              "	border: 0px solid;\n"
                                              "	border-radius: 5px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "	background-color: rgb(85, 170, 255);\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "	background-color: rgba(85, 170, 255, 100);\n"
                                              "}")

        self.horizontalLayout_14.addWidget(self.btn_delete_lower_1)

        self.verticalLayout_21.addWidget(self.frame_inter_delet_bar_3)

        self.verticalLayout_13.addWidget(self.widget_lower_1)

        self.widget_lower_pri = QWidget(self.page_content_Input)
        self.widget_lower_pri.setObjectName(u"widget_lower_pri")
        self.widget_lower_pri.setMinimumSize(QSize(0, 400))
        self.widget_lower_pri.setStyleSheet(u"QWidget{\n"
                                            "	background-color:rgb(26, 27, 34);\n"
                                            "	border-radius: 10px;\n"
                                            "}\n"
                                            "QWidget:hover{\n"
                                            "		border: 2px solid rgb(0, 149, 241);\n"
                                            "}")
        self.verticalLayout_pri = QVBoxLayout(self.widget_lower_pri)
        self.verticalLayout_pri.setObjectName(u"verticalLayout_pri")
        self.label_info_lower_pri = QLabel(self.widget_lower_pri)
        self.label_info_lower_pri.setObjectName(u"label_info_lower_pri")
        self.label_info_lower_pri.setFont(font2)
        self.label_info_lower_pri.setStyleSheet(u"background-color: none;\n"
                                                "border: none;\n"
                                                "padding-left: 25px;\n"
                                                "color: white;")

        self.verticalLayout_pri.addWidget(self.label_info_lower_pri)

        self.frame_inter_delet_bar_pri = QFrame(self.widget_lower_pri)
        self.frame_inter_delet_bar_pri.setObjectName(
            u"frame_inter_delet_bar_pri")
        self.frame_inter_delet_bar_pri.setMaximumSize(QSize(16777215, 40))
        self.frame_inter_delet_bar_pri.setStyleSheet(
            u"border: none;\n background-color: rgb(40, 41, 52);")
        self.frame_inter_delet_bar_pri.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_delet_bar_pri.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_pri = QHBoxLayout(self.frame_inter_delet_bar_pri)
        self.horizontalLayout_pri.setObjectName(u"horizontalLayout_pri")
        self.label_info_user_lower_pri = QLabel(self.frame_inter_delet_bar_pri)
        self.label_info_user_lower_pri.setObjectName(
            u"label_info_user_lower_pri")
        self.label_info_user_lower_pri.setFont(font3)
        self.label_info_user_lower_pri.setStyleSheet(
            u"color: white;\n padding-left: 20px;")
        self.label_info_user_lower_pri.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_pri.addWidget(self.label_info_user_lower_pri)

        self.btn_delete_lower_pri = QPushButton(self.frame_inter_delet_bar_pri)
        self.btn_delete_lower_pri.setObjectName(u"btn_delete_lower_pri")
        self.btn_delete_lower_pri.setMinimumSize(QSize(100, 25))
        self.btn_delete_lower_pri.setMaximumSize(QSize(100, 40))
        self.btn_delete_lower_pri.setFont(font4)
        self.btn_delete_lower_pri.setStyleSheet(u"QPushButton{\n"
                                                "	color: rgb(255, 255, 255);\n"
                                                "	background-color: rgb(0, 127, 226);\n"
                                                "	border: 0px solid;\n"
                                                "	border-radius: 5px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "	background-color: rgb(85, 170, 255);\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                "	background-color: rgba(85, 170, 255, 100);\n"
                                                "}")

        self.horizontalLayout_pri.addWidget(self.btn_delete_lower_pri)

        self.verticalLayout_pri.addWidget(self.frame_inter_delet_bar_pri)

        self.verticalLayout_13.addWidget(self.widget_lower_pri)

        self.widget_lower_advan = QWidget(self.page_content_Input)
        self.widget_lower_advan.setObjectName(u"widget_lower_advan")
        self.widget_lower_advan.setMinimumSize(QSize(0, 400))
        self.widget_lower_advan.setStyleSheet(u"QWidget{\n"
                                              "	background-color:rgb(26, 27, 34);\n"
                                              "	border-radius: 10px;\n"
                                              "}\n"
                                              "QWidget:hover{\n"
                                              "		border: 2px solid rgb(0, 149, 241);\n"
                                              "}")
        self.verticalLayout_advan = QVBoxLayout(self.widget_lower_advan)
        self.verticalLayout_advan.setObjectName(u"verticalLayout_advan")
        self.label_info_lower_advan = QLabel(self.widget_lower_advan)
        self.label_info_lower_advan.setObjectName(u"label_info_lower_advan")
        self.label_info_lower_advan.setFont(font2)
        self.label_info_lower_advan.setStyleSheet(u"background-color: none;\n"
                                                  "border: none;\n"
                                                  "padding-left: 25px;\n"
                                                  "color: white;")

        self.verticalLayout_advan.addWidget(self.label_info_lower_advan)

        self.frame_inter_delet_bar_advan = QFrame(self.widget_lower_advan)
        self.frame_inter_delet_bar_advan.setObjectName(
            u"frame_inter_delet_bar_advan")
        self.frame_inter_delet_bar_advan.setMaximumSize(QSize(16777215, 40))
        self.frame_inter_delet_bar_advan.setStyleSheet(
            u"border: none;\n background-color: rgb(40, 41, 52);")
        self.frame_inter_delet_bar_advan.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_delet_bar_advan.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_advan = QHBoxLayout(
            self.frame_inter_delet_bar_advan)
        self.horizontalLayout_advan.setObjectName(u"horizontalLayout_advan")
        self.label_info_user_lower_advan = QLabel(
            self.frame_inter_delet_bar_advan)
        self.label_info_user_lower_advan.setObjectName(
            u"label_info_user_lower_advan")
        self.label_info_user_lower_advan.setFont(font3)
        self.label_info_user_lower_advan.setStyleSheet(
            u"color: white;\n padding-left: 20px;")
        self.label_info_user_lower_advan.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_advan.addWidget(self.label_info_user_lower_advan)

        self.btn_delete_lower_advan = QPushButton(
            self.frame_inter_delet_bar_advan)
        self.btn_delete_lower_advan.setObjectName(u"btn_delete_lower_advan")
        self.btn_delete_lower_advan.setMinimumSize(QSize(100, 25))
        self.btn_delete_lower_advan.setMaximumSize(QSize(100, 40))
        self.btn_delete_lower_advan.setFont(font4)
        self.btn_delete_lower_advan.setStyleSheet(u"QPushButton{\n"
                                                  "	color: rgb(255, 255, 255);\n"
                                                  "	background-color: rgb(0, 127, 226);\n"
                                                  "	border: 0px solid;\n"
                                                  "	border-radius: 5px;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  "	background-color: rgb(85, 170, 255);\n"
                                                  "}\n"
                                                  "QPushButton:pressed{\n"
                                                  "	background-color: rgba(85, 170, 255, 100);\n"
                                                  "}")

        self.horizontalLayout_advan.addWidget(self.btn_delete_lower_advan)

        self.verticalLayout_advan.addWidget(self.frame_inter_delet_bar_advan)

        self.verticalLayout_13.addWidget(self.widget_lower_advan)

        self.scrollArea.setWidget(self.page_content_Input)

        self.verticalLayout_31.addWidget(self.scrollArea)

        self.verticalLayout_6.addWidget(self.frame_main_home_bar)

        self.stackedWidget.addWidget(self.Home)
        self.page_left = QWidget()
        self.page_left.setObjectName(u"page_left")
        self.page_left.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.page_left)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_main_left_bar = QFrame(self.page_left)
        self.frame_main_left_bar.setObjectName(u"frame_main_left_bar")
        self.frame_main_left_bar.setStyleSheet(u"")
        self.frame_main_left_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_left_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_main_left_bar)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.scrollArea_2 = QScrollArea(self.frame_main_left_bar)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
                                        " QScrollBar:vertical {\n"
                                        "	border: none;\n"
                                        "        background: rgb(45, 48, 59);\n"
                                        "        width: 15px;\n"
                                        "        margin: 30px 0 30px 0;\n"
                                        "        border-radius: 7px;\n"
                                        " }\n"
                                        "\n"
                                        "/*  HANDLE BAR VERTICAL */\n"
                                        "QScrollBar::handle:vertical {	\n"
                                        "	background-color: rgb(34, 35, 44);\n"
                                        "	min-height: 15px;\n"
                                        "	border-radius: 7px;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:hover{	\n"
                                        "	background-color: rgb(38, 40, 50);\n"
                                        "\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:pressed {	\n"
                                        "	background-color: rgb(31, 32, 40);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "/* BTN TOP - SCROLLBAR */\n"
                                        "QScrollBar::sub-line:vertical {\n"
                                        "	border: none;\n"
                                        "	background-color: rgb(45, 48, 59);\n"
                                        "	height: 15px;\n"
                                        "	border-top-left-radius: 7px;\n"
                                        "	border-top-right-radius: 7px;\n"
                                        "	subcontrol-position: top;\n"
                                        "	subcontrol-origin: margin;\n"
                                        "	margin-top: 10px;\n"
                                        "}\n"
                                        "QScrollBar::sub-line:vertical:hover {	\n"
                                        "	background-color:   rgb(38, 40, 50);\n"
                                        "\n"
                                        "}\n"
                                        "QScrollBar::sub-line:vertical:pressed {	\n"
                                        "	backgrou"
                                        "nd-color:rgb(31, 32, 40);\n"
                                        "        \n"
                                        "}\n"
                                        "\n"
                                        "/* BTN BOTTOM - SCROLLBAR */\n"
                                        "QScrollBar::add-line:vertical {\n"
                                        "	border: none;\n"
                                        "	background-color: rgb(45, 48, 59);\n"
                                        "	height: 15px;\n"
                                        "	border-bottom-left-radius: 7px;\n"
                                        "	border-bottom-right-radius: 7px;\n"
                                        "	subcontrol-position: bottom;\n"
                                        "	subcontrol-origin: margin;\n"
                                        "	margin-bottom: 10px;\n"
                                        "}\n"
                                        "QScrollBar::add-line:vertical:hover {	\n"
                                        "	background-color:    rgb(38, 40, 50);\n"
                                        "}\n"
                                        "QScrollBar::add-line:vertical:pressed {	\n"
                                        "	background-color:rgb(31, 32, 40);\n"
                                        "}\n"
                                        "/* RESET ARROW */\n"
                                        "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                        "	background: none;\n"
                                        "}\n"
                                        "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                        "	background: none;\n"
                                        "}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 753, 1636))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_inter_left_1 = QWidget(self.scrollAreaWidgetContents)
        self.widget_inter_left_1.setObjectName(u"widget_inter_left_1")
        self.widget_inter_left_1.setMinimumSize(QSize(0, 400))
        self.widget_inter_left_1.setStyleSheet(u"QWidget{\n"
                                               "	background-color:rgb(26, 27, 34);\n"
                                               "	border-radius: 10px;\n"
                                               "}\n"
                                               "QWidget:hover{\n"
                                               "		border: 2px solid rgb(0, 149, 241);\n"
                                               "}")
        self.verticalLayout_15 = QVBoxLayout(self.widget_inter_left_1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.info_inter_left_1 = QLabel(self.widget_inter_left_1)
        self.info_inter_left_1.setObjectName(u"info_inter_left_1")
        self.info_inter_left_1.setFont(font2)
        self.info_inter_left_1.setStyleSheet(u"background-color: none;\n"
                                             "border: none;\n"
                                             "padding-left: 25px;\n"
                                             "color: white;")
        self.info_inter_left_1.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.info_inter_left_1)

        self.frame_inter_left_btns_bar_1 = QFrame(self.widget_inter_left_1)
        self.frame_inter_left_btns_bar_1.setObjectName(
            u"frame_inter_left_btns_bar_1")
        self.frame_inter_left_btns_bar_1.setMinimumSize(QSize(0, 0))
        self.frame_inter_left_btns_bar_1.setMaximumSize(QSize(16777215, 40))
        self.frame_inter_left_btns_bar_1.setStyleSheet(
            u"border:none;\n background-color: rgb(40, 41, 52);")
        self.frame_inter_left_btns_bar_1.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_left_btns_bar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_inter_left_btns_bar_1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_info_user_left_inter_1 = QLabel(
            self.frame_inter_left_btns_bar_1)
        self.label_info_user_left_inter_1.setObjectName(
            u"label_info_user_left_inter_1")
        font5 = QFont()
        font5.setFamily(u"MesloLGLDZ Nerd Font Mono")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_info_user_left_inter_1.setFont(font5)
        self.label_info_user_left_inter_1.setStyleSheet(
            u"color: white;\n padding-left: 20px;")
        self.label_info_user_left_inter_1.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_8.addWidget(self.label_info_user_left_inter_1)

        self.btn_delete_inter_left_1 = QPushButton(
            self.frame_inter_left_btns_bar_1)
        self.btn_delete_inter_left_1.setObjectName(u"btn_delete_inter_left_1")
        self.btn_delete_inter_left_1.setMinimumSize(QSize(0, 25))
        self.btn_delete_inter_left_1.setMaximumSize(QSize(100, 40))
        self.btn_delete_inter_left_1.setFont(font4)
        self.btn_delete_inter_left_1.setStyleSheet(u"QPushButton{\n"
                                                   "	color: rgb(255, 255, 255);\n"
                                                   "	background-color: rgb(0, 127, 226);\n"
                                                   "	border: 0px solid;\n"
                                                   "	border-radius: 5px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "	background-color: rgb(85, 170, 255);\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   "	background-color: rgba(85, 170, 255, 100);\n"
                                                   "}")

        self.horizontalLayout_8.addWidget(self.btn_delete_inter_left_1)

        self.verticalLayout_15.addWidget(self.frame_inter_left_btns_bar_1)

        self.verticalLayout_14.addWidget(self.widget_inter_left_1)

        self.widget_lower_left_1 = QWidget(self.scrollAreaWidgetContents)
        self.widget_lower_left_1.setObjectName(u"widget_lower_left_1")
        self.widget_lower_left_1.setMinimumSize(QSize(0, 400))
        self.widget_lower_left_1.setStyleSheet(u"QWidget{\n"
                                               "	background-color:rgb(26, 27, 34);\n"
                                               "	border-radius: 10px;\n"
                                               "}\n"
                                               "QWidget:hover{\n"
                                               "		border: 2px solid rgb(0, 149, 241);\n"
                                               "}")
        self.verticalLayout_18 = QVBoxLayout(self.widget_lower_left_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.info_lower_1 = QLabel(self.widget_lower_left_1)
        self.info_lower_1.setObjectName(u"info_lower_1")
        self.info_lower_1.setFont(font2)
        self.info_lower_1.setStyleSheet(u"background-color: none;\n"
                                        "border: none;\n"
                                        "padding-left: 25px;\n"
                                        "color: white;")
        self.info_lower_1.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.info_lower_1)

        self.frame_lower_left_btns_bar_1 = QFrame(self.widget_lower_left_1)
        self.frame_lower_left_btns_bar_1.setObjectName(
            u"frame_lower_left_btns_bar_1")
        self.frame_lower_left_btns_bar_1.setMaximumSize(QSize(16777215, 40))
        self.frame_lower_left_btns_bar_1.setStyleSheet(
            u"border: none;\n background-color: rgb(40, 41, 52);")
        self.frame_lower_left_btns_bar_1.setFrameShape(QFrame.StyledPanel)
        self.frame_lower_left_btns_bar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(
            self.frame_lower_left_btns_bar_1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_info_user_left_lower_1 = QLabel(
            self.frame_lower_left_btns_bar_1)
        self.label_info_user_left_lower_1.setObjectName(
            u"label_info_user_left_lower_1")
        self.label_info_user_left_lower_1.setStyleSheet(
            u"color: white;\n padding-left: 20px;")
        self.label_info_user_left_lower_1.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_10.addWidget(self.label_info_user_left_lower_1)

        self.btn_delete_lower_left_1 = QPushButton(
            self.frame_lower_left_btns_bar_1)
        self.btn_delete_lower_left_1.setObjectName(u"btn_delete_lower_left_1")
        self.btn_delete_lower_left_1.setMinimumSize(QSize(0, 25))
        self.btn_delete_lower_left_1.setMaximumSize(QSize(100, 25))
        self.btn_delete_lower_left_1.setFont(font4)
        self.btn_delete_lower_left_1.setStyleSheet(u"QPushButton{\n"
                                                   "	color: rgb(255, 255, 255);\n"
                                                   "	background-color: rgb(0, 127, 226);\n"
                                                   "	border: 0px solid;\n"
                                                   "	border-radius: 5px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "	background-color: rgb(85, 170, 255);\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   "	background-color: rgba(85, 170, 255, 100);\n"
                                                   "}")

        self.horizontalLayout_10.addWidget(self.btn_delete_lower_left_1)

        self.verticalLayout_18.addWidget(self.frame_lower_left_btns_bar_1)

        self.verticalLayout_14.addWidget(self.widget_lower_left_1)

        self.widget_lower_left_pri = QWidget(self.scrollAreaWidgetContents)
        self.widget_lower_left_pri.setObjectName(u"widget_lower_left_pri")
        self.widget_lower_left_pri.setMinimumSize(QSize(0, 400))
        self.widget_lower_left_pri.setStyleSheet(u"QWidget{\n"
                                                 "	background-color:rgb(26, 27, 34);\n"
                                                 "	border-radius: 10px;\n"
                                                 "}\n"
                                                 "QWidget:hover{\n"
                                                 "		border: 2px solid rgb(0, 149, 241);\n"
                                                 "}")
        self.verticalLayout_pri = QVBoxLayout(self.widget_lower_left_pri)
        self.verticalLayout_pri.setObjectName(u"verticalLayout_pri")
        self.info_lower_left_pri = QLabel(self.widget_lower_left_pri)
        self.info_lower_left_pri.setObjectName(u"info_lower_pri")
        self.info_lower_left_pri.setFont(font2)
        self.info_lower_left_pri.setStyleSheet(u"background-color: none;\n"
                                               "border: none;\n"
                                               "padding-left: 25px;\n"
                                               "color: white;")
        self.info_lower_left_pri.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_pri.addWidget(self.info_lower_left_pri)

        self.frame_lower_btns_bar_pri = QFrame(self.widget_lower_left_pri)
        self.frame_lower_btns_bar_pri.setObjectName(
            u"frame_lower_btns_bar_pri")
        self.frame_lower_btns_bar_pri.setMaximumSize(QSize(16777215, 40))
        self.frame_lower_btns_bar_pri.setStyleSheet(
            u"border: none;\n background-color: rgb(40, 41, 52);")
        self.frame_lower_btns_bar_pri.setFrameShape(QFrame.StyledPanel)
        self.frame_lower_btns_bar_pri.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_pri = QHBoxLayout(self.frame_lower_btns_bar_pri)
        self.horizontalLayout_pri.setObjectName(u"horizontalLayout_pri")
        self.label_info_user_left_lower_pri = QLabel(
            self.frame_lower_btns_bar_pri)
        self.label_info_user_left_lower_pri.setObjectName(
            u"label_info_user_left_lower_pri")
        self.label_info_user_left_lower_pri.setStyleSheet(
            u"color: white;\n padding-left: 20px;")
        self.label_info_user_left_lower_pri.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_pri.addWidget(
            self.label_info_user_left_lower_pri)

        self.btn_delete_lower_left_pri = QPushButton(
            self.frame_lower_btns_bar_pri)
        self.btn_delete_lower_left_pri.setObjectName(
            u"btn_delete_lower_left_pri")
        self.btn_delete_lower_left_pri.setMinimumSize(QSize(0, 25))
        self.btn_delete_lower_left_pri.setMaximumSize(QSize(100, 25))
        self.btn_delete_lower_left_pri.setSizeIncrement(QSize(0, 0))
        self.btn_delete_lower_left_pri.setFont(font4)
        self.btn_delete_lower_left_pri.setStyleSheet(u"QPushButton{\n"
                                                     "	color: rgb(255, 255, 255);\n"
                                                     "	background-color: rgb(0, 127, 226);\n"
                                                     "	border: 0px solid;\n"
                                                     "	border-radius: 5px;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     "	background-color: rgb(85, 170, 255);\n"
                                                     "}\n"
                                                     "QPushButton:pressed{\n"
                                                     "	background-color: rgba(85, 170, 255, 100);\n"
                                                     "}")

        self.horizontalLayout_pri.addWidget(self.btn_delete_lower_left_pri)

        self.verticalLayout_pri.addWidget(self.frame_lower_btns_bar_pri)

        self.verticalLayout_14.addWidget(self.widget_lower_left_pri)

        self.widget_lower_left_advan = QWidget(self.scrollAreaWidgetContents)
        self.widget_lower_left_advan.setObjectName(u"widget_lower_left_advan")
        self.widget_lower_left_advan.setMinimumSize(QSize(0, 400))
        self.widget_lower_left_advan.setStyleSheet(u"QWidget{\n"
                                                   "	background-color:rgb(26, 27, 34);\n"
                                                   "	border-radius: 10px;\n"
                                                   "}\n"
                                                   "QWidget:hover{\n"
                                                   "		border: 2px solid rgb(0, 149, 241);\n"
                                                   "}")
        self.verticalLayout_advan = QVBoxLayout(self.widget_lower_left_advan)
        self.verticalLayout_advan.setObjectName(u"verticalLayout_advan")
        self.info_lower_left_advan = QLabel(self.widget_lower_left_advan)
        self.info_lower_left_advan.setObjectName(u"info_lower_advan")
        self.info_lower_left_advan.setFont(font2)
        self.info_lower_left_advan.setStyleSheet(u"background-color: none;\n"
                                                 "border: none;\n"
                                                 "padding-left: 25px;\n"
                                                 "color: white;")
        self.info_lower_left_advan.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_advan.addWidget(self.info_lower_left_advan)

        self.frame_lower_btns_bar_advan = QFrame(self.widget_lower_left_advan)
        self.frame_lower_btns_bar_advan.setObjectName(
            u"frame_lower_btns_bar_advan")
        self.frame_lower_btns_bar_advan.setMaximumSize(QSize(16777215, 40))
        self.frame_lower_btns_bar_advan.setStyleSheet(
            u"border: none;\n background-color: rgb(40, 41, 52);")
        self.frame_lower_btns_bar_advan.setFrameShape(QFrame.StyledPanel)
        self.frame_lower_btns_bar_advan.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_advan = QHBoxLayout(
            self.frame_lower_btns_bar_advan)
        self.horizontalLayout_advan.setObjectName(u"horizontalLayout_advan")
        self.label_info_user_left_lower_advan = QLabel(
            self.frame_lower_btns_bar_advan)
        self.label_info_user_left_lower_advan.setObjectName(
            u"label_info_user_left_lower_advan")
        self.label_info_user_left_lower_advan.setStyleSheet(
            u"color: white;\n padding-left: 20px;")
        self.label_info_user_left_lower_advan.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_advan.addWidget(
            self.label_info_user_left_lower_advan)

        self.btn_delete_lower_left_advan = QPushButton(
            self.frame_lower_btns_bar_advan)
        self.btn_delete_lower_left_advan.setObjectName(
            u"btn_delete_lower_left_advan")
        self.btn_delete_lower_left_advan.setMinimumSize(QSize(0, 25))
        self.btn_delete_lower_left_advan.setMaximumSize(QSize(100, 25))
        self.btn_delete_lower_left_advan.setSizeIncrement(QSize(0, 0))
        self.btn_delete_lower_left_advan.setFont(font4)
        self.btn_delete_lower_left_advan.setStyleSheet(u"QPushButton{\n"
                                                       "	color: rgb(255, 255, 255);\n"
                                                       "	background-color: rgb(0, 127, 226);\n"
                                                       "	border: 0px solid;\n"
                                                       "	border-radius: 5px;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "	background-color: rgb(85, 170, 255);\n"
                                                       "}\n"
                                                       "QPushButton:pressed{\n"
                                                       "	background-color: rgba(85, 170, 255, 100);\n"
                                                       "}")

        self.horizontalLayout_advan.addWidget(self.btn_delete_lower_left_advan)

        self.verticalLayout_advan.addWidget(self.frame_lower_btns_bar_advan)

        self.verticalLayout_14.addWidget(self.widget_lower_left_advan)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_30.addWidget(self.scrollArea_2)

        self.verticalLayout_7.addWidget(self.frame_main_left_bar)

        self.stackedWidget.addWidget(self.page_left)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.page_search.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.page_search)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_main_search_bar = QFrame(self.page_search)
        self.frame_main_search_bar.setObjectName(u"frame_main_search_bar")
        self.frame_main_search_bar.setStyleSheet(u"QFrame{\n"
                                                 "	border-bottom-right-radius: 5px;\n"
                                                 "	border-bottom-left-radius: 5px;\n"
                                                 "}")
        self.frame_main_search_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_search_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_main_search_bar)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 16, -1, -1)
        self.frame_searching_main = QFrame(self.frame_main_search_bar)
        self.frame_searching_main.setObjectName(u"frame_searching_main")
        self.frame_searching_main.setMinimumSize(QSize(0, 0))
        self.frame_searching_main.setMaximumSize(QSize(16777215, 200))
        self.frame_searching_main.setStyleSheet(u"\n"
                                                "background-color:rgb(26, 27, 34);\n"
                                                "border-radius: 10px;\n"
                                                "")
        self.frame_searching_main.setFrameShape(QFrame.StyledPanel)
        self.frame_searching_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_searching_main)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_title_search = QFrame(self.frame_searching_main)
        self.frame_title_search.setObjectName(u"frame_title_search")
        self.frame_title_search.setStyleSheet(u"background-color: none;\n"
                                              "border: none;")
        self.frame_title_search.setFrameShape(QFrame.StyledPanel)
        self.frame_title_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_title_search)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.userInfoForSearch = QLabel(self.frame_title_search)
        self.userInfoForSearch.setObjectName(u"userInfoForSearch")
        font7 = QFont()
        font7.setFamily(u"MesloLGL Nerd Font")
        font7.setPointSize(9)
        self.userInfoForSearch.setFont(font7)
        self.userInfoForSearch.setStyleSheet(u"color: white;")

        self.verticalLayout_24.addWidget(self.userInfoForSearch)

        self.verticalLayout_23.addWidget(self.frame_title_search)

        self.frame_search_bar_itmes = QFrame(self.frame_searching_main)
        self.frame_search_bar_itmes.setObjectName(u"frame_search_bar_itmes")
        self.frame_search_bar_itmes.setStyleSheet(u"background-color: none;\n"
                                                  "border: none;")
        self.frame_search_bar_itmes.setFrameShape(QFrame.StyledPanel)
        self.frame_search_bar_itmes.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_search_bar_itmes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_nameSearch = QLineEdit(self.frame_search_bar_itmes)
        self.lineEdit_nameSearch.setClearButtonEnabled(True)
        self.lineEdit_nameSearch.setObjectName(u"lineEdit_nameSearch")
        self.lineEdit_nameSearch.setMinimumSize(QSize(0, 30))
        self.lineEdit_nameSearch.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setFamily(u"MesloLGL Nerd Font Mono")
        font8.setPointSize(10)
        self.lineEdit_nameSearch.setFont(font8)
        self.lineEdit_nameSearch.setStyleSheet(u"QLineEdit{\n"
                                               "	border: 0px solid;\n"
                                               "	color: rgb(240, 240, 240);\n"
                                               "	border-radius: 10px;\n"
                                               "	background-color: rgb(37, 38, 48);\n"
                                               "	padding-left: 10px;\n"
                                               "	padding-right: 10px;\n"
                                               "   selection-background-color: #30313F;\n"
                                               "   selection-color: #5F6063;\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:hover{\n"
                                               "	border: 2px solid rgb(49, 50, 63);\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "QLineEdit:focus{\n"
                                               "	border: 2px solid rgb(61, 152, 212);\n"
                                               "}")

        self.gridLayout.addWidget(self.lineEdit_nameSearch, 0, 0, 1, 1)

        self.btn_nameSearch = QPushButton(self.frame_search_bar_itmes)
        self.btn_nameSearch.setObjectName(u"btn_nameSearch")
        self.btn_nameSearch.setMinimumSize(QSize(100, 25))
        self.btn_nameSearch.setMaximumSize(QSize(16777215, 25))
        self.btn_nameSearch.setStyleSheet(u"QPushButton{\n"
                                          "	color: rgb(255, 255, 255);\n"
                                          "	background-color: rgb(0, 127, 226);\n"
                                          "	border: 0px solid;\n"
                                          "	border-radius: 5px;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "	background-color: rgb(85, 170, 255);\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "	background-color: rgba(85, 170, 255, 100);\n"
                                          "}")

        self.btn_nameSearch.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_nameSearch, 0, 1, 1, 1)

        self.lineEdit_rollSearch = QLineEdit(self.frame_search_bar_itmes)
        self.lineEdit_rollSearch.setClearButtonEnabled(True)
        self.lineEdit_rollSearch.setObjectName(u"lineEdit_rollSearch")
        self.lineEdit_rollSearch.setMinimumSize(QSize(200, 30))
        self.lineEdit_rollSearch.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_rollSearch.setFont(font2)
        self.lineEdit_rollSearch.setStyleSheet(u"QLineEdit{\n"
                                               "	border: 0px solid;\n"
                                               "	color: rgb(240, 240, 240);\n"
                                               "	border-radius: 10px;\n"
                                               "	background-color: rgb(37, 38, 48);\n"
                                               "	padding-left: 10px;\n"
                                               "	padding-right: 10px;\n"
                                               "   selection-background-color: #30313F;\n"
                                               "   selection-color: #5F6063;\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:hover{\n"
                                               "	border: 2px solid rgb(49, 50, 63);\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "QLineEdit:focus{\n"
                                               "	border: 2px solid rgb(61, 152, 212);\n"
                                               "}")

        self.gridLayout.addWidget(self.lineEdit_rollSearch, 1, 0, 1, 1)

        self.btn_rollSearch = QPushButton(self.frame_search_bar_itmes)
        self.btn_rollSearch.setObjectName(u"btn_rollSearch")
        self.btn_rollSearch.setMinimumSize(QSize(100, 25))
        self.btn_rollSearch.setMaximumSize(QSize(16777215, 25))
        self.btn_rollSearch.setStyleSheet(u"QPushButton{\n"
                                          "	color: rgb(255, 255, 255);\n"
                                          "	background-color: rgb(0, 127, 226);\n"
                                          "	border: 0px solid;\n"
                                          "	border-radius: 5px;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "	background-color: rgb(85, 170, 255);\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "	background-color: rgba(85, 170, 255, 100);\n"
                                          "}")

        self.btn_rollSearch.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_rollSearch, 1, 1, 1, 1)

        self.verticalLayout_23.addWidget(self.frame_search_bar_itmes)

        self.verticalLayout_29.addWidget(self.frame_searching_main)

        self.frame_resalt_bar = QFrame(self.frame_main_search_bar)
        self.frame_resalt_bar.setObjectName(u"frame_resalt_bar")
        self.frame_resalt_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_resalt_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_resalt_bar)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 10, 0, 0)
        self.scrollArea_resalt = QScrollArea(self.frame_resalt_bar)
        self.scrollArea_resalt.setObjectName(u"scrollArea_resalt")
        self.scrollArea_resalt.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
                                             " QScrollBar:vertical {\n"
                                             "	border: none;\n"
                                             "        background: rgb(45, 48, 59);\n"
                                             "        width: 15px;\n"
                                             "        margin: 30px 0 30px 0;\n"
                                             "        border-radius: 7px;\n"
                                             " }\n"
                                             "\n"
                                             "/*  HANDLE BAR VERTICAL */\n"
                                             "QScrollBar::handle:vertical {	\n"
                                             "	background-color: rgb(34, 35, 44);\n"
                                             "	min-height: 15px;\n"
                                             "	border-radius: 7px;\n"
                                             "}\n"
                                             "QScrollBar::handle:vertical:hover{	\n"
                                             "	background-color: rgb(38, 40, 50);\n"
                                             "\n"
                                             "}\n"
                                             "QScrollBar::handle:vertical:pressed {	\n"
                                             "	background-color: rgb(31, 32, 40);\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "/* BTN TOP - SCROLLBAR */\n"
                                             "QScrollBar::sub-line:vertical {\n"
                                             "	border: none;\n"
                                             "	background-color: rgb(45, 48, 59);\n"
                                             "	height: 15px;\n"
                                             "	border-top-left-radius: 7px;\n"
                                             "	border-top-right-radius: 7px;\n"
                                             "	subcontrol-position: top;\n"
                                             "	subcontrol-origin: margin;\n"
                                             "	margin-top: 10px;\n"
                                             "}\n"
                                             "QScrollBar::sub-line:vertical:hover {	\n"
                                             "	background-color:   rgb(38, 40, 50);\n"
                                             "\n"
                                             "}\n"
                                             "QScrollBar::sub-line:vertical:pressed {	\n"
                                             "	backgrou"
                                             "nd-color:rgb(31, 32, 40);\n"
                                             "        \n"
                                             "}\n"
                                             "\n"
                                             "/* BTN BOTTOM - SCROLLBAR */\n"
                                             "QScrollBar::add-line:vertical {\n"
                                             "	border: none;\n"
                                             "	background-color: rgb(45, 48, 59);\n"
                                             "	height: 15px;\n"
                                             "	border-bottom-left-radius: 7px;\n"
                                             "	border-bottom-right-radius: 7px;\n"
                                             "	subcontrol-position: bottom;\n"
                                             "	subcontrol-origin: margin;\n"
                                             "	margin-bottom: 10px;\n"
                                             "}\n"
                                             "QScrollBar::add-line:vertical:hover {	\n"
                                             "	background-color:    rgb(38, 40, 50);\n"
                                             "}\n"
                                             "QScrollBar::add-line:vertical:pressed {	\n"
                                             "	background-color:rgb(31, 32, 40);\n"
                                             "}\n"
                                             "/* RESET ARROW */\n"
                                             "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                             "	background: none;\n"
                                             "}\n"
                                             "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                             "	background: none;\n"
                                             "}")
        self.scrollArea_resalt.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 768, 328))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 5)

        self.scrollArea_resalt.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_25.addWidget(self.scrollArea_resalt)

        self.verticalLayout_29.addWidget(self.frame_resalt_bar)

        self.verticalLayout_8.addWidget(self.frame_main_search_bar)

        self.stackedWidget.addWidget(self.page_search)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.page_setting.setMinimumSize(QSize(702, 424))
        self.page_setting.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.page_setting)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_main_setting_bar = QFrame(self.page_setting)
        self.frame_main_setting_bar.setObjectName(u"frame_main_setting_bar")
        self.frame_main_setting_bar.setStyleSheet(u"")
        self.frame_main_setting_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_setting_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_main_setting_bar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame = QFrame(self.frame_main_setting_bar)
        self.frame.setStyleSheet("QFrame {\n"
                                 "    background-color: rgb(26, 27, 34);\n"
                                 "    border-radius: 10px;\n"
                                 "    border: 0px solid;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_28 = QVBoxLayout(self.frame)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label = QLabel(self.frame)
        self.label.setMinimumSize(QSize(200, 200))
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setStyleSheet("border-radius: 100px;\n"
                                 "background-color: rgb(34, 35, 44);\n"
                                 "border: 10px solid rgb(30, 31, 39);\n"
                                 "color: white;")
        self.label.setObjectName("label")
        self.verticalLayout_28.addWidget(self.label, 0, Qt.AlignHCenter)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
                                   "QScrollBar:vertical {\n"
                                   "    border: none;\n"
                                   "    background: rgb(45, 48, 59);\n"
                                   "    width: 15px;\n"
                                   "    margin: 30px 0 30px 0;\n"
                                   "    border-radius: 7px;\n"
                                   "}\n"
                                   "\n"
                                   "/*  HANDLE BAR VERTICAL */\n"
                                   "QScrollBar::handle:vertical {\n"
                                   "   background-color: rgb(34, 35, 44);\n"
                                   "   min-height: 15px;\n"
                                   "   border-radius: 7px;\n"
                                   "}\n"
                                   "QScrollBar::handle:vertical:hover{\n"
                                   "   background-color: rgb(38, 40, 50);\n"
                                   "}\n"
                                   "QScrollBar::handle:vertical:pressed {\n"
                                   "   background-color: rgb(31, 32, 40);\n"
                                   "}\n"
                                   "\n"
                                   "/* BTN TOP - SCROLLBAR */\n"
                                   "QScrollBar::sub-line:vertical {\n"
                                   "   border: none;\n"
                                   "   background-color: rgb(45, 48, 59);\n"
                                   "   height: 15px;\n"
                                   "   border-top-left-radius: 7px;\n"
                                   "   border-top-right-radius: 7px;\n"
                                   "   subcontrol-position: top;\n"
                                   "   subcontrol-origin: margin;\n"
                                   "   margin-top: 10px;\n"
                                   "}\n"
                                   "\n"
                                   "QScrollBar::sub-line:vertical:hover {\n"
                                   "   background-color:   rgb(38, 40, 50);\n"
                                   "}\n"
                                   "\n"
                                   "QScrollBar::sub-line:vertical:pressed {\n"
                                   "   background-color:rgb(31, 32, 40);\n"
                                   "   }\n"
                                   "\n"
                                   "/* BTN BOTTOM - SCROLLBAR */\n"
                                   "QScrollBar::add-line:vertical {\n"
                                   "   border: none;\n"
                                   "   background-color: rgb(45, 48, 59);\n"
                                   "   height: 15px;\n"
                                   "   border-bottom-left-radius: 7px;\n"
                                   "   border-bottom-right-radius: 7px;\n"
                                   "   subcontrol-position: bottom;\n"
                                   "   subcontrol-origin: margin;\n"
                                   "   margin-bottom: 10px;\n"
                                   "}\n"
                                   "QScrollBar::add-line:vertical:hover {\n"
                                   "    background-color:    rgb(38, 40, 50);\n"
                                   "}\n"
                                   "QScrollBar::add-line:vertical:pressed {\n"
                                   "   background-color:rgb(31, 32, 40);\n"
                                   "}\n"
                                   "/* RESET ARROW */\n"
                                   "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                   "  background: none;\n"
                                   "}\n"
                                   "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                   "  background: none;\n"
                                   "}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea_3 = QScrollArea(self.frame_3)
        self.scrollArea_3.setStyleSheet("background-color: rgb(26, 27, 34);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 717, 836))
        self.scrollAreaWidgetContents_3.setObjectName(
            "scrollAreaWidgetContents_3")
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.frame_user_name_changer = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_user_name_changer.setMinimumSize(QSize(0, 200))
        self.frame_user_name_changer.setMaximumSize(QSize(16777215, 200))
        self.frame_user_name_changer.setStyleSheet("QFrame {\n"
                                                   "    background-color: rgb(34, 35, 44);\n"
                                                   "}")
        self.frame_user_name_changer.setFrameShape(QFrame.StyledPanel)
        self.frame_user_name_changer.setFrameShadow(QFrame.Raised)
        self.frame_user_name_changer.setObjectName("frame_user_name_changer")
        self.verticalLayout_33 = QVBoxLayout(self.frame_user_name_changer)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.frame_name_changer_title_bar = QFrame(
            self.frame_user_name_changer)
        self.frame_name_changer_title_bar.setMinimumSize(QSize(0, 30))
        self.frame_name_changer_title_bar.setMaximumSize(QSize(16777215, 30))
        self.frame_name_changer_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_name_changer_title_bar.setFrameShadow(QFrame.Raised)
        self.frame_name_changer_title_bar.setObjectName(
            "frame_name_changer_title_bar")
        self.horizontalLayout_5 = QHBoxLayout(
            self.frame_name_changer_title_bar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_username_title = QLabel(self.frame_name_changer_title_bar)
        self.label_username_title.setStyleSheet("color: white;\n"
                                                "padding-left: 20px;")
        self.label_username_title.setObjectName("label_username_title")
        self.horizontalLayout_5.addWidget(self.label_username_title)
        self.btn_hidden_username_bar = QPushButton(
            self.frame_name_changer_title_bar)
        self.btn_hidden_username_bar.setMinimumSize(QSize(30, 30))
        self.btn_hidden_username_bar.setMaximumSize(QSize(30, 30))
        self.btn_hidden_username_bar.setStyleSheet("QPushButton {\n"
                                                   "    background-color: none;\n"
                                                   "    color: white;\n"
                                                   "    border: 0px solid;\n"
                                                   "    border-radius: 15px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    background-color: rgb(0, 127, 226);\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   "    background-color: rgba(0, 127, 226, 100);\n"
                                                   "}")
        self.btn_hidden_username_bar.setText("")
        self.btn_hidden_username_bar.setObjectName("btn_hidden_username_bar")
        self.horizontalLayout_5.addWidget(self.btn_hidden_username_bar)
        self.verticalLayout_33.addWidget(self.frame_name_changer_title_bar)
        self.frame_name_changer_content_page = QFrame(
            self.frame_user_name_changer)
        self.frame_name_changer_content_page.setFrameShape(QFrame.StyledPanel)
        self.frame_name_changer_content_page.setFrameShadow(QFrame.Raised)
        self.frame_name_changer_content_page.setMaximumSize(
            QSize(16777215, 150))
        self.frame_name_changer_content_page.setMinimumSize(QSize(0, 150))
        self.frame_name_changer_content_page.setObjectName(
            "frame_name_changer_content_page")
        self.verticalLayout_37 = QVBoxLayout(
            self.frame_name_changer_content_page)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.label_show_current_username = QLabel(
            self.frame_name_changer_content_page)
        self.label_show_current_username.setMinimumSize(QSize(0, 30))
        self.label_show_current_username.setMaximumSize(QSize(16777215, 30))
        self.label_show_current_username.setStyleSheet("color: white;")
        self.label_show_current_username.setObjectName(
            "label_show_current_username")
        self.verticalLayout_37.addWidget(self.label_show_current_username)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lineEdit_username_change_input = QLineEdit(
            self.frame_name_changer_content_page)
        self.lineEdit_username_change_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_username_change_input.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_username_change_input.setFont(font)
        self.lineEdit_username_change_input.setStyleSheet("QLineEdit {\n"
                                                          "    background-color: rgb(43, 44, 56);\n"
                                                          "    color: white;\n"
                                                          "    border: 0px solid;\n"
                                                          "    border-radius: 10px;\n"
                                                          "    padding-left: 20px;\n"
                                                          "}\n"
                                                          "QLineEdit:hover {\n"
                                                          "    border: 2px solid rgb(51, 52, 67);\n"
                                                          "}\n"
                                                          "QLineEdit:pressed {\n"
                                                          "    border: 2px solid rgb(0, 106, 189);\n"
                                                          "}")
        self.lineEdit_username_change_input.setObjectName(
            "lineEdit_username_change_input")
        self.horizontalLayout_18.addWidget(self.lineEdit_username_change_input)
        self.btn_save_username = QPushButton(
            self.frame_name_changer_content_page)
        self.btn_save_username.setMinimumSize(QSize(100, 30))
        self.btn_save_username.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_username.setFont(font)
        self.btn_save_username.setStyleSheet("QPushButton {\n"
                                             "    background-color:  rgb(0, 127, 226);\n"
                                             "    color: white;\n"
                                             "    border: 0px solid;\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: rgb(0, 124, 218);\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "    background-color: rgba(0, 127, 226, 100);\n"
                                             "}")
        self.btn_save_username.setObjectName("btn_save_username")

        self.frame_more_options = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_more_options.setMinimumSize(QSize(0, 50))
        self.frame_more_options.setStyleSheet("QFrame {\n"
                                              "    background-color: rgb(34, 35, 44);\n"
                                              "}")
        self.frame_more_options.setFrameShape(QFrame.StyledPanel)
        self.frame_more_options.setFrameShadow(QFrame.Raised)
        self.frame_more_options.setObjectName("frame_more_options")
        self.verticalLayout_41 = QVBoxLayout(self.frame_more_options)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.frame_title_of_more_options = QFrame(self.frame_more_options)
        self.frame_title_of_more_options.setMinimumSize(QSize(0, 30))
        self.frame_title_of_more_options.setMaximumSize(QSize(16777215, 30))
        self.frame_title_of_more_options.setFrameShape(QFrame.StyledPanel)
        self.frame_title_of_more_options.setFrameShadow(QFrame.Raised)
        self.frame_title_of_more_options.setObjectName(
            "frame_title_of_more_options")
        self.horizontalLayout_24 = QHBoxLayout(
            self.frame_title_of_more_options)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_title = QLabel(self.frame_title_of_more_options)
        self.label_title.setStyleSheet("color: white;\n"
                                       "padding-left: 20px;")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_24.addWidget(self.label_title)
        self.btn_hidden_options = QPushButton(self.frame_title_of_more_options)
        self.btn_hidden_options.setMinimumSize(QSize(30, 30))
        self.btn_hidden_options.setMaximumSize(QSize(30, 30))
        self.btn_hidden_options.setStyleSheet("QPushButton {\n"
                                              "    background-color: none;\n"
                                              "    color: white;\n"
                                              "    border: 0px solid;\n"
                                              "    border-radius: 15px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "    background-color: rgb(0, 127, 226);\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgba(0, 127, 226, 100);\n"
                                              "}")
        self.btn_hidden_options.setText("")
        self.btn_hidden_options.setObjectName("btn_hidden_options")
        self.horizontalLayout_24.addWidget(self.btn_hidden_options)
        self.verticalLayout_41.addWidget(self.frame_title_of_more_options)
        self.frame_more_options_contect_bar = QFrame(self.frame_more_options)
        self.frame_more_options_contect_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_more_options_contect_bar.setFrameShadow(QFrame.Raised)
        self.frame_more_options_contect_bar.setObjectName(
            "frame_more_options_contect_bar")
        self.frame_more_options_contect_bar.setMaximumSize(QSize(16777215, 0))
        self.frame_more_options_contect_bar.setMinimumSize(QSize(0, 0))
        self.verticalLayout_42 = QVBoxLayout(
            self.frame_more_options_contect_bar)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_reload_info = QLabel(self.frame_more_options_contect_bar)
        self.label_reload_info.setStyleSheet("color: white;\n"
                                             "padding-left: 5px;")
        self.label_reload_info.setObjectName("label_reload_info")
        self.verticalLayout_42.addWidget(self.label_reload_info)
        self.btn_reload = QPushButton(self.frame_more_options_contect_bar)
        self.btn_reload.setMinimumSize(QSize(0, 30))
        self.btn_reload.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reload.setFont(font)
        self.btn_reload.setStyleSheet("QPushButton {\n"
                                      "    background-color:  rgb(0, 127, 226);\n"
                                      "    color: white;\n"
                                      "    border: 0px solid;\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(0, 124, 218);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: rgba(0, 127, 226, 100);\n"
                                      "}")
        self.btn_reload.setObjectName("btn_reload")
        self.verticalLayout_42.addWidget(self.btn_reload)
        self.label_reset_info = QLabel(self.frame_more_options_contect_bar)
        self.label_reset_info.setStyleSheet("color: white;\n"
                                            "padding-left: 5px;")
        self.label_reset_info.setObjectName("label_reset_info")
        self.verticalLayout_42.addWidget(self.label_reset_info)
        self.btn_reset = QPushButton(self.frame_more_options_contect_bar)
        self.btn_reset.setMinimumSize(QSize(0, 30))
        self.btn_reset.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setStyleSheet("QPushButton {\n"
                                     "    background-color:  rgb(255, 21, 83);\n"
                                     "    color: white;\n"
                                     "    border: 0px solid;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color: rgb(156, 12, 51);\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color: rgba(156, 12, 51, 100);\n"
                                     "}")
        self.btn_reset.setObjectName("btn_reset")
        self.verticalLayout_42.addWidget(self.btn_reset)
        self.label_6 = QLabel(self.frame_more_options_contect_bar)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_42.addWidget(self.label_6)
        self.btn_logout = QPushButton(self.frame_more_options_contect_bar)
        self.btn_logout.setMinimumSize(QSize(0, 30))
        self.btn_logout.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet("QPushButton {\n"
                                      "    background-color:  rgb(0, 127, 226);\n"
                                      "    color: white;\n"
                                      "    border: 0px solid;\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(0, 124, 218);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: rgba(0, 127, 226, 100);\n"
                                      "}")
        self.btn_logout.setObjectName("btn_logout")
        self.verticalLayout_42.addWidget(self.btn_logout)
        self.verticalLayout_41.addWidget(self.frame_more_options_contect_bar)

        self.horizontalLayout_18.addWidget(self.btn_save_username)
        self.verticalLayout_37.addLayout(self.horizontalLayout_18)
        self.verticalLayout_33.addWidget(self.frame_name_changer_content_page)
        self.verticalLayout_32.addWidget(self.frame_user_name_changer)
        self.frame_email_changer = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_email_changer.setMinimumSize(QSize(0, 45))
        self.frame_email_changer.setMaximumSize(QSize(16777215, 45))
        self.frame_email_changer.setStyleSheet("QFrame {\n"
                                               "    background-color: rgb(34, 35, 44);\n"
                                               "}")
        self.frame_email_changer.setFrameShape(QFrame.StyledPanel)
        self.frame_email_changer.setFrameShadow(QFrame.Raised)
        self.frame_email_changer.setObjectName("frame_email_changer")
        self.verticalLayout_34 = QVBoxLayout(self.frame_email_changer)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_email_changer_title_bar = QFrame(self.frame_email_changer)
        self.frame_email_changer_title_bar.setMinimumSize(QSize(0, 30))
        self.frame_email_changer_title_bar.setMaximumSize(QSize(16777215, 30))
        self.frame_email_changer_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_email_changer_title_bar.setFrameShadow(QFrame.Raised)
        self.frame_email_changer_title_bar.setObjectName(
            "frame_email_changer_title_bar")
        self.horizontalLayout_19 = QHBoxLayout(
            self.frame_email_changer_title_bar)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_change_email_title = QLabel(
            self.frame_email_changer_title_bar)
        self.label_change_email_title.setStyleSheet("color: white;\n"
                                                    "padding-left: 20px;")
        self.label_change_email_title.setObjectName("label_change_email_title")
        self.horizontalLayout_19.addWidget(self.label_change_email_title)
        self.btn_hidden_email_bar = QPushButton(
            self.frame_email_changer_title_bar)
        self.btn_hidden_email_bar.setMinimumSize(QSize(30, 30))
        self.btn_hidden_email_bar.setMaximumSize(QSize(22, 30))
        self.btn_hidden_email_bar.setStyleSheet("QPushButton {\n"
                                                "    background-color: none;\n"
                                                "    color: white;\n"
                                                "    border: 0px solid;\n"
                                                "    border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color: rgb(0, 127, 226);\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                "    background-color: rgba(0, 127, 226, 100);\n"
                                                "}")
        self.btn_hidden_email_bar.setText("")
        self.btn_hidden_email_bar.setObjectName("btn_hidden_email_bar")
        self.horizontalLayout_19.addWidget(self.btn_hidden_email_bar)
        self.verticalLayout_34.addWidget(self.frame_email_changer_title_bar)
        self.frame_email_changer_content_bar = QFrame(self.frame_email_changer)
        self.frame_email_changer_content_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_email_changer_content_bar.setFrameShadow(QFrame.Raised)
        self.frame_email_changer_content_bar.setObjectName(
            "frame_email_changer_content_bar")
        self.frame_email_changer_content_bar.setMaximumSize(QSize(16777215, 0))
        self.frame_email_changer_content_bar.setMinimumSize(QSize(0, 0))
        self.verticalLayout_38 = QVBoxLayout(
            self.frame_email_changer_content_bar)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.label_current_email = QLabel(self.frame_email_changer_content_bar)
        self.label_current_email.setMinimumSize(QSize(0, 30))
        self.label_current_email.setMaximumSize(QSize(16777215, 30))
        self.label_current_email.setStyleSheet("color: white;")
        self.label_current_email.setObjectName("label_current_email")
        self.verticalLayout_38.addWidget(self.label_current_email)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lineEdit_change_email_input = QLineEdit(
            self.frame_email_changer_content_bar)
        self.lineEdit_change_email_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_change_email_input.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_change_email_input.setFont(font)
        self.lineEdit_change_email_input.setStyleSheet("QLineEdit {\n"
                                                       "    background-color: rgb(43, 44, 56);\n"
                                                       "    color: white;\n"
                                                       "    border: 0px solid;\n"
                                                       "    border-radius: 10px;\n"
                                                       "    padding-left: 20px;\n"
                                                       "}\n"
                                                       "QLineEdit:hover {\n"
                                                       "    border: 2px solid rgb(51, 52, 67);\n"
                                                       "}\n"
                                                       "QLineEdit:pressed {\n"
                                                       "    border: 2px solid rgb(0, 106, 189);\n"
                                                       "}")
        self.lineEdit_change_email_input.setObjectName(
            "lineEdit_change_email_input")
        self.horizontalLayout_20.addWidget(self.lineEdit_change_email_input)
        self.btn_save_change_email = QPushButton(
            self.frame_email_changer_content_bar)
        self.btn_save_change_email.setMinimumSize(QSize(100, 30))
        self.btn_save_change_email.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_change_email.setFont(font)
        self.btn_save_change_email.setStyleSheet("QPushButton {\n"
                                                 "    background-color:  rgb(0, 127, 226);\n"
                                                 "    color: white;\n"
                                                 "    border: 0px solid;\n"
                                                 "    border-radius: 5px;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "    background-color: rgb(0, 124, 218);\n"
                                                 "}\n"
                                                 "QPushButton:pressed{\n"
                                                 "    background-color: rgba(0, 127, 226, 100);\n"
                                                 "}")
        self.btn_save_change_email.setObjectName("btn_save_change_email")
        self.horizontalLayout_20.addWidget(self.btn_save_change_email)
        self.verticalLayout_38.addLayout(self.horizontalLayout_20)
        self.verticalLayout_34.addWidget(self.frame_email_changer_content_bar)
        self.verticalLayout_32.addWidget(self.frame_email_changer)
        self.frame_contect_number_changer = QFrame(
            self.scrollAreaWidgetContents_3)
        self.frame_contect_number_changer.setMinimumSize(QSize(0, 45))
        self.frame_contect_number_changer.setMaximumSize(QSize(16777215, 45))
        self.frame_contect_number_changer.setStyleSheet("QFrame {\n"
                                                        "    background-color: rgb(34, 35, 44);\n"
                                                        "}")
        self.frame_contect_number_changer.setFrameShape(QFrame.StyledPanel)
        self.frame_contect_number_changer.setFrameShadow(QFrame.Raised)
        self.frame_contect_number_changer.setObjectName(
            "frame_contect_number_changer")
        self.verticalLayout_35 = QVBoxLayout(self.frame_contect_number_changer)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_contect_number_changer_title_bar = QFrame(
            self.frame_contect_number_changer)
        self.frame_contect_number_changer_title_bar.setMinimumSize(
            QSize(0, 30))
        self.frame_contect_number_changer_title_bar.setMaximumSize(
            QSize(16777215, 30))
        self.frame_contect_number_changer_title_bar.setFrameShape(
            QFrame.StyledPanel)
        self.frame_contect_number_changer_title_bar.setFrameShadow(
            QFrame.Raised)
        self.frame_contect_number_changer_title_bar.setObjectName(
            "frame_contect_number_changer_title_bar")
        self.horizontalLayout_21 = QHBoxLayout(
            self.frame_contect_number_changer_title_bar)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_change_contact_number_title = QLabel(
            self.frame_contect_number_changer_title_bar)
        self.label_change_contact_number_title.setStyleSheet("color: white;\n"
                                                             "padding-left: 20px;")
        self.label_change_contact_number_title.setObjectName(
            "label_change_contact_number_title")
        self.horizontalLayout_21.addWidget(
            self.label_change_contact_number_title)
        self.btn_hidden_contact_number_bar = QPushButton(
            self.frame_contect_number_changer_title_bar)
        self.btn_hidden_contact_number_bar.setMinimumSize(QSize(30, 30))
        self.btn_hidden_contact_number_bar.setMaximumSize(QSize(30, 30))
        self.btn_hidden_contact_number_bar.setStyleSheet("QPushButton {\n"
                                                         "    background-color: none;\n"
                                                         "    color: white;\n"
                                                         "    border: 0px solid;\n"
                                                         "    border-radius: 15px;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    background-color: rgb(0, 127, 226);\n"
                                                         "}\n"
                                                         "QPushButton:pressed{\n"
                                                         "    background-color: rgba(0, 127, 226, 100);\n"
                                                         "}")
        self.btn_hidden_contact_number_bar.setText("")
        self.btn_hidden_contact_number_bar.setObjectName(
            "btn_hidden_contact_number_bar")
        self.horizontalLayout_21.addWidget(self.btn_hidden_contact_number_bar)
        self.verticalLayout_35.addWidget(
            self.frame_contect_number_changer_title_bar)
        self.frame_contect_number_changer_content_bar = QFrame(
            self.frame_contect_number_changer)
        self.frame_contect_number_changer_content_bar.setFrameShape(
            QFrame.StyledPanel)
        self.frame_contect_number_changer_content_bar.setFrameShadow(
            QFrame.Raised)
        self.frame_contect_number_changer_content_bar.setMinimumSize(
            QSize(0, 0))
        self.frame_contect_number_changer_content_bar.setMaximumSize(
            QSize(16777215, 0))
        self.frame_contect_number_changer_content_bar.setObjectName(
            "frame_contect_number_changer_content_bar")
        self.verticalLayout_39 = QVBoxLayout(
            self.frame_contect_number_changer_content_bar)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.label_show_current_contact_number = QLabel(
            self.frame_contect_number_changer_content_bar)
        self.label_show_current_contact_number.setMinimumSize(QSize(0, 30))
        self.label_show_current_contact_number.setMaximumSize(
            QSize(16777215, 30))
        self.label_show_current_contact_number.setStyleSheet("color: white;")
        self.label_show_current_contact_number.setObjectName(
            "label_show_current_contact_number")
        self.verticalLayout_39.addWidget(
            self.label_show_current_contact_number)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lineEdit_contact_number_input = QLineEdit(
            self.frame_contect_number_changer_content_bar)
        self.lineEdit_contact_number_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_contact_number_input.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_contact_number_input.setFont(font)
        self.lineEdit_contact_number_input.setStyleSheet("QLineEdit {\n"
                                                         "    background-color: rgb(43, 44, 56);\n"
                                                         "    color: white;\n"
                                                         "    border: 0px solid;\n"
                                                         "    border-radius: 10px;\n"
                                                         "    padding-left: 20px;\n"
                                                         "}\n"
                                                         "QLineEdit:hover {\n"
                                                         "    border: 2px solid rgb(51, 52, 67);\n"
                                                         "}\n"
                                                         "QLineEdit:pressed {\n"
                                                         "    border: 2px solid rgb(0, 106, 189);\n"
                                                         "}")
        self.lineEdit_contact_number_input.setObjectName(
            "lineEdit_contact_number_input")
        self.horizontalLayout_22.addWidget(self.lineEdit_contact_number_input)
        self.btn_save_contact_number = QPushButton(
            self.frame_contect_number_changer_content_bar)
        self.btn_save_contact_number.setMinimumSize(QSize(100, 30))
        self.btn_save_contact_number.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_contact_number.setFont(font)
        self.btn_save_contact_number.setStyleSheet("QPushButton {\n"
                                                   "    background-color:  rgb(0, 127, 226);\n"
                                                   "    color: white;\n"
                                                   "    border: 0px solid;\n"
                                                   "    border-radius: 5px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    background-color: rgb(0, 124, 218);\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   "    background-color: rgba(0, 127, 226, 100);\n"
                                                   "}")
        self.btn_save_contact_number.setObjectName("btn_save_contact_number")
        self.horizontalLayout_22.addWidget(self.btn_save_contact_number)
        self.verticalLayout_39.addLayout(self.horizontalLayout_22)
        self.verticalLayout_35.addWidget(
            self.frame_contect_number_changer_content_bar)
        self.verticalLayout_32.addWidget(self.frame_contect_number_changer)
        self.frame_password_changer = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_password_changer.setMinimumSize(QSize(0, 45))
        self.frame_password_changer.setMaximumSize(QSize(16777215, 45))
        self.frame_password_changer.setStyleSheet("QFrame {\n"
                                                  "    background-color: rgb(34, 35, 44);\n"
                                                  "}")
        self.frame_password_changer.setFrameShape(QFrame.StyledPanel)
        self.frame_password_changer.setFrameShadow(QFrame.Raised)
        self.frame_password_changer.setObjectName("frame_password_changer")
        self.verticalLayout_36 = QVBoxLayout(self.frame_password_changer)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_password_changer_title_bar = QFrame(
            self.frame_password_changer)
        self.frame_password_changer_title_bar.setMinimumSize(QSize(0, 30))
        self.frame_password_changer_title_bar.setMaximumSize(
            QSize(16777215, 30))
        self.frame_password_changer_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_password_changer_title_bar.setFrameShadow(QFrame.Raised)
        self.frame_password_changer_title_bar.setObjectName(
            "frame_password_changer_title_bar")
        self.horizontalLayout_23 = QHBoxLayout(
            self.frame_password_changer_title_bar)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_change_password_title = QLabel(
            self.frame_password_changer_title_bar)
        self.label_change_password_title.setStyleSheet("color: white;\n"
                                                       "padding-left: 20px;")
        self.label_change_password_title.setObjectName(
            "label_change_password_title")
        self.horizontalLayout_23.addWidget(self.label_change_password_title)
        self.btn_hidden_passowd_changer_bar = QPushButton(
            self.frame_password_changer_title_bar)
        self.btn_hidden_passowd_changer_bar.setMinimumSize(QSize(30, 30))
        self.btn_hidden_passowd_changer_bar.setMaximumSize(QSize(30, 30))
        self.btn_hidden_passowd_changer_bar.setStyleSheet("QPushButton {\n"
                                                          "    background-color: none;\n"
                                                          "    color: white;\n"
                                                          "    border: 0px solid;\n"
                                                          "    border-radius: 15px;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    background-color: rgb(0, 127, 226);\n"
                                                          "}\n"
                                                          "QPushButton:pressed{\n"
                                                          "    background-color: rgba(0, 127, 226, 100);\n"
                                                          "}")
        self.btn_hidden_passowd_changer_bar.setText("")
        self.btn_hidden_passowd_changer_bar.setObjectName(
            "btn_hidden_passowd_changer_bar")
        self.horizontalLayout_23.addWidget(self.btn_hidden_passowd_changer_bar)
        self.verticalLayout_36.addWidget(self.frame_password_changer_title_bar)
        self.frame_password_changer_content_bar = QFrame(
            self.frame_password_changer)
        self.frame_password_changer_content_bar.setFrameShape(
            QFrame.StyledPanel)
        self.frame_password_changer_content_bar.setFrameShadow(QFrame.Raised)
        self.frame_password_changer_content_bar.setObjectName(
            "frame_password_changer_content_bar")
        self.frame_password_changer_content_bar.setMaximumSize(
            QSize(16777215, 0))
        self.frame_password_changer_content_bar.setMinimumSize(QSize(0, 0))
        self.verticalLayout_40 = QVBoxLayout(
            self.frame_password_changer_content_bar)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.lineEdit_passord_input = QLineEdit(
            self.frame_password_changer_content_bar)
        self.lineEdit_passord_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_passord_input.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_passord_input.setEchoMode(QLineEdit.Password)
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_passord_input.setFont(font)
        self.lineEdit_passord_input.setStyleSheet("QLineEdit {\n"
                                                  "    background-color: rgb(43, 44, 56);\n"
                                                  "    color: white;\n"
                                                  "    border: 0px solid;\n"
                                                  "    border-radius: 10px;\n"
                                                  "    padding-left: 20px;\n"
                                                  "}\n"
                                                  "QLineEdit:hover {\n"
                                                  "    border: 2px solid rgb(51, 52, 67);\n"
                                                  "}\n"
                                                  "QLineEdit:pressed {\n"
                                                  "    border: 2px solid rgb(0, 106, 189);\n"
                                                  "}")
        self.lineEdit_passord_input.setObjectName("lineEdit_passord_input")
        self.verticalLayout_40.addWidget(self.lineEdit_passord_input)
        self.lineEdit_repassword_input = QLineEdit(
            self.frame_password_changer_content_bar)
        self.lineEdit_repassword_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_repassword_input.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_repassword_input.setEchoMode(QLineEdit.Password)
        font = QFont()
        font.setPointSize(11)
        self.lineEdit_repassword_input.setFont(font)
        self.lineEdit_repassword_input.setStyleSheet("QLineEdit {\n"
                                                     "    background-color: rgb(43, 44, 56);\n"
                                                     "    color: white;\n"
                                                     "    border: 0px solid;\n"
                                                     "    border-radius: 10px;\n"
                                                     "    padding-left: 20px;\n"
                                                     "}\n"
                                                     "QLineEdit:hover {\n"
                                                     "    border: 2px solid rgb(51, 52, 67);\n"
                                                     "}\n"
                                                     "QLineEdit:pressed {\n"
                                                     "    border: 2px solid rgb(0, 106, 189);\n"
                                                     "}")
        self.lineEdit_repassword_input.setObjectName(
            "lineEdit_repassword_input")
        self.verticalLayout_40.addWidget(self.lineEdit_repassword_input)
        self.btn_save_password = QPushButton(
            self.frame_password_changer_content_bar)
        self.btn_save_password.setMinimumSize(QSize(0, 30))
        self.btn_save_password.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_password.setFont(font)
        self.btn_save_password.setStyleSheet("QPushButton {\n"
                                             "    background-color:  rgb(0, 127, 226);\n"
                                             "    color: white;\n"
                                             "    border: 0px solid;\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: rgb(0, 124, 218);\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "    background-color: rgba(0, 127, 226, 100);\n"
                                             "}")
        self.btn_save_password.setObjectName("btn_save_password")
        self.verticalLayout_40.addWidget(self.btn_save_password)
        self.verticalLayout_36.addWidget(
            self.frame_password_changer_content_bar)
        self.verticalLayout_32.addWidget(self.frame_password_changer)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_4.addWidget(self.scrollArea_3)
        self.verticalLayout_28.addWidget(self.frame_3)
        self.verticalLayout_10.addWidget(self.frame)

        self.verticalLayout_11.addWidget(self.frame_main_setting_bar)

        self.stackedWidget.addWidget(self.page_setting)

        self.page_add_inter = QWidget()
        self.page_add_inter.setObjectName(u"page_add_inter")
        self.verticalLayout_43 = QVBoxLayout(self.page_add_inter)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_main_inter_info = QFrame(self.page_add_inter)
        self.frame_main_inter_info.setObjectName(u"frame_main_inter_info")
        self.frame_main_inter_info.setMaximumSize(QSize(16777215, 600))
        self.frame_main_inter_info.setStyleSheet(u"QFrame {\n"
                                                 "   background-color: rgb(26, 27, 34);\n"
                                                 "   color: #fff;\n"
                                                 "   border-radius: 10px;\n"
                                                 "}")
        self.frame_main_inter_info.setFrameShape(QFrame.StyledPanel)
        self.frame_main_inter_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_main_inter_info)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_logo_icon = QFrame(self.frame_main_inter_info)
        self.frame_logo_icon.setObjectName(u"frame_logo_icon")
        self.frame_logo_icon.setFrameShape(QFrame.StyledPanel)
        self.frame_logo_icon.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_logo_icon)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.frame_user_image_upload = QFrame(self.frame_logo_icon)
        self.frame_user_image_upload.setFrameShape(QFrame.StyledPanel)
        self.frame_user_image_upload.setFrameShadow(QFrame.Raised)
        self.frame_user_image_upload.setObjectName("frame_user_image_upload")
        self.gridLayout_4 = QGridLayout(self.frame_user_image_upload)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_icon_inter = QLabel(self.frame_user_image_upload)
        self.label_icon_inter.setMinimumSize(QSize(200, 200))
        self.label_icon_inter.setMaximumSize(QSize(200, 200))
        self.label_icon_inter.setStyleSheet("QLabel{\n"
                                            "    border: 8px solid rgb(37, 38, 48);\n"
                                            "    background-color: rgb(50, 52, 65);\n"
                                            "    border-radius: 100px;\n"
                                            "color: white;\n"
                                            "}")
        self.label_icon_inter.setObjectName("label_icon_")
        self.gridLayout_4.addWidget(self.label_icon_inter, 0, 0, 1, 1)
        self.btn_upload_image = QPushButton(self.frame_user_image_upload)
        self.btn_upload_image.setMinimumSize(QSize(0, 25))
        self.btn_upload_image.setMaximumSize(QSize(300, 25))
        self.btn_upload_image.setStyleSheet("QPushButton{\n"
                                            "  color: rgb(255, 255, 255);\n"
                                            "                                        background-color: rgb(26, 114, 255);\n"
                                            "                                        border: 0px solid;\n"
                                            "                                        border-radius: 5px;\n"
                                            "                                        }\n"
                                            "                                        QPushButton:hover{\n"
                                            "                                        background-color: rgb(21, 134, 255);\n"
                                            "                                        }\n"
                                            "                                       QPushButton:pressed{\n"
                                            "                                        background-color: rgba(26, 114, 255, 100);\n"
                                            "                                        }")
        self.btn_upload_image.setObjectName("btn_upload_image")
        self.gridLayout_4.addWidget(self.btn_upload_image, 1, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_user_image_upload)

        self.verticalLayout_44.addWidget(self.frame_logo_icon)

        self.frame_content = QFrame(self.frame_main_inter_info)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_content)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_name = QLineEdit(self.frame_content)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMinimumSize(QSize(0, 30))
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(False)
        font11.setWeight(50)
        self.lineEdit_name.setFont(font11)
        self.lineEdit_name.setStyleSheet(u"QLineEdit{\n"
                                         "border: 0px solid;\n"
                                         "color: rgb(240, 240, 240);\n"
                                         "border-radius: 10px;\n"
                                         "background-color: #1D222E;\n"
                                         "padding-left: 10px;\n"
                                         "padding-right: 10px;\n"
                                         "selection-background-color: #30313F;\n"
                                         "selection-color: #5F6063;\n"
                                         "}\n"
                                         "QLineEdit:hover{\n"
                                         "border: 2px solid rgb(49, 50, 63);\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:focus{\n"
                                         "border: 2px solid rgb(61, 152, 212);\n"
                                         "}")
        self.lineEdit_name.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_name)
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setWeight(50)
        self.lineEdit_address = QLineEdit(self.frame_content)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setMinimumSize(QSize(0, 30))
        self.lineEdit_address.setFont(font10)
        self.lineEdit_address.setStyleSheet(u"QLineEdit{\n"
                                            "border: 0px solid;\n"
                                            "color: rgb(240, 240, 240);\n"
                                            "border-radius: 10px;\n"
                                            "background-color: #1D222E;\n"
                                            "padding-left: 10px;\n"
                                            "padding-right: 10px;\n"
                                            "selection-background-color: #30313F;\n"
                                            "selection-color: #5F6063;\n"
                                            "}\n"
                                            "QLineEdit:hover{\n"
                                            "border: 2px solid rgb(49, 50, 63);\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit:focus{\n"
                                            "border: 2px solid rgb(61, 152, 212);\n"
                                            "}")
        self.lineEdit_address.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_address)

        self.verticalLayout_45.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lineEdit_subject = QLineEdit(self.frame_content)
        self.lineEdit_subject.setObjectName(u"lineEdit_subject")
        self.lineEdit_subject.setMinimumSize(QSize(0, 30))
        self.lineEdit_subject.setFont(font10)
        self.lineEdit_subject.setStyleSheet(u"QLineEdit{\n"
                                            "border: 0px solid;\n"
                                            "color: rgb(240, 240, 240);\n"
                                            "border-radius: 10px;\n"
                                            "background-color: #1D222E;\n"
                                            "padding-left: 10px;\n"
                                            "padding-right: 10px;\n"
                                            "selection-background-color: #30313F;\n"
                                            "selection-color: #5F6063;\n"
                                            "}\n"
                                            "QLineEdit:hover{\n"
                                            "border: 2px solid rgb(49, 50, 63);\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit:focus{\n"
                                            "border: 2px solid rgb(61, 152, 212);\n"
                                            "}")
        self.lineEdit_subject.setClearButtonEnabled(True)

        self.horizontalLayout_18.addWidget(self.lineEdit_subject)

        self.lineEdit_email = QLineEdit(self.frame_content)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setMinimumSize(QSize(0, 30))
        self.lineEdit_email.setFont(font10)
        self.lineEdit_email.setStyleSheet(u"QLineEdit{\n"
                                          "border: 0px solid;\n"
                                          "color: rgb(240, 240, 240);\n"
                                          "border-radius: 10px;\n"
                                          "background-color: #1D222E;\n"
                                          "padding-left: 10px;\n"
                                          "padding-right: 10px;\n"
                                          "selection-background-color: #30313F;\n"
                                          "selection-color: #5F6063;\n"
                                          "}\n"
                                          "QLineEdit:hover{\n"
                                          "border: 2px solid rgb(49, 50, 63);\n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit:focus{\n"
                                          "border: 2px solid rgb(61, 152, 212);\n"
                                          "}")
        self.lineEdit_email.setClearButtonEnabled(True)

        self.horizontalLayout_18.addWidget(self.lineEdit_email)

        self.verticalLayout_45.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lineEdit_contect = QLineEdit(self.frame_content)
        self.lineEdit_contect.setObjectName(u"lineEdit_contect")
        self.lineEdit_contect.setMinimumSize(QSize(0, 30))
        self.lineEdit_contect.setFont(font10)
        self.lineEdit_contect.setStyleSheet(u"QLineEdit{\n"
                                            "border: 0px solid;\n"
                                            "color: rgb(240, 240, 240);\n"
                                            "border-radius: 10px;\n"
                                            "background-color: #1D222E;\n"
                                            "padding-left: 10px;\n"
                                            "padding-right: 10px;\n"
                                            "selection-background-color: #30313F;\n"
                                            "selection-color: #5F6063;\n"
                                            "}\n"
                                            "QLineEdit:hover{\n"
                                            "border: 2px solid rgb(49, 50, 63);\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit:focus{\n"
                                            "border: 2px solid rgb(61, 152, 212);\n"
                                            "}")
        self.lineEdit_contect.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.lineEdit_contect)

        self.lineEdit_level = QLineEdit(self.frame_content)
        self.lineEdit_level.setObjectName(u"lineEdit_level")
        self.lineEdit_level.setMinimumSize(QSize(0, 30))
        self.lineEdit_level.setFont(font10)
        self.lineEdit_level.setStyleSheet(u"QLineEdit{\n"
                                          "border: 0px solid;\n"
                                          "color: rgb(240, 240, 240);\n"
                                          "border-radius: 10px;\n"
                                          "background-color: #1D222E;\n"
                                          "padding-left: 10px;\n"
                                          "padding-right: 10px;\n"
                                          "selection-background-color: #30313F;\n"
                                          "selection-color: #5F6063;\n"
                                          "}\n"
                                          "QLineEdit:hover{\n"
                                          "border: 2px solid rgb(49, 50, 63);\n"
                                          "}\n"
                                          "\n"
                                          "QLineEdit:focus{\n"
                                          "border: 2px solid rgb(61, 152, 212);\n"
                                          "}")
        self.lineEdit_level.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.lineEdit_level)

        self.verticalLayout_45.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(50, -1, 50, -1)
        self.radioButton_male = QRadioButton(self.frame_content)
        self.radioButton_male.setObjectName(u"radioButton_male")
        self.radioButton_male.setMaximumSize(QSize(100, 16777215))
        self.radioButton_male.setStyleSheet(u"QRadioButton {\n"
                                            "color: #fff;\n"
                                            "   background-color: rgb(26, 27, 34);\n"
                                            "}\n"
                                            "\n"
                                            "QRadioButton::indicator {\n"
                                            "border: 3px solid rgb(52, 59, 72);\n"
                                            "width: 15px;\n"
                                            "height: 15px;\n"
                                            "border-radius: 10px;\n"
                                            "background: rgb(44, 49, 60);\n"
                                            "color: #fff;\n"
                                            "}\n"
                                            "QRadioButton::indicator:hover {\n"
                                            "border: 3px solid rgb(61, 152, 212);\n"
                                            "}\n"
                                            "QRadioButton::indicator:checked {\n"
                                            "background: 3px solid  rgb(82, 197, 130);\n"
                                            "border: 3px solid  rgb(82, 197, 130);  \n"
                                            "}")

        self.horizontalLayout_20.addWidget(self.radioButton_male)

        self.radioButton_female = QRadioButton(self.frame_content)
        self.radioButton_female.setObjectName(u"radioButton_female")
        self.radioButton_female.setMaximumSize(QSize(100, 16777215))
        self.radioButton_female.setStyleSheet(u"QRadioButton {\n"
                                              "color: #fff;\n"
                                              "background-color: rgb(26, 27, 34);\n"
                                              "}\n"
                                              "\n"
                                              "QRadioButton::indicator {\n"
                                              "border: 3px solid rgb(52, 59, 72);\n"
                                              "width: 15px;\n"
                                              "height: 15px;\n"
                                              "border-radius: 10px;\n"
                                              "background: rgb(44, 49, 60);\n"
                                              "color: #fff;\n"
                                              "}\n"
                                              "QRadioButton::indicator:hover {\n"
                                              "border: 3px solid rgb(61, 152, 212);\n"
                                              "}\n"
                                              "QRadioButton::indicator:checked {\n"
                                              "background: 3px solid  rgb(82, 197, 130);\n"
                                              "border: 3px solid  rgb(82, 197, 130);  \n"
                                              "}")

        self.horizontalLayout_20.addWidget(self.radioButton_female)

        self.radioButton_other = QRadioButton(self.frame_content)
        self.radioButton_other.setObjectName(u"radioButton_other")
        self.radioButton_other.setMaximumSize(QSize(100, 16777215))
        self.radioButton_other.setStyleSheet(u"QRadioButton {\n"
                                             "color: #fff;\n"
                                             "background-color: rgb(26, 27, 34);\n"
                                             "}\n"
                                             "\n"
                                             "QRadioButton::indicator {\n"
                                             "border: 3px solid rgb(52, 59, 72);\n"
                                             "width: 15px;\n"
                                             "height: 15px;\n"
                                             "border-radius: 10px;\n"
                                             "background: rgb(44, 49, 60);\n"
                                             "color: #fff;\n"
                                             "}\n"
                                             "QRadioButton::indicator:hover {\n"
                                             "border: 3px solid rgb(61, 152, 212);\n"
                                             "}\n"
                                             "QRadioButton::indicator:checked {\n"
                                             "background: 3px solid  rgb(82, 197, 130);\n"
                                             "border: 3px solid  rgb(82, 197, 130);  \n"
                                             "}")

        self.horizontalLayout_20.addWidget(self.radioButton_other)

        self.verticalLayout_45.addLayout(self.horizontalLayout_20)

        self.label_emtye = QLabel(self.frame_content)
        self.label_emtye.setObjectName(u"label_emtye")
        self.label_emtye.setStyleSheet(u"")

        self.verticalLayout_45.addWidget(self.label_emtye)

        self.label_show_roll_number = QLabel(self.frame_content)
        self.label_show_roll_number.setObjectName(u"label_show_roll_number")
        self.label_show_roll_number.setMinimumSize(QSize(0, 35))
        self.label_show_roll_number.setStyleSheet(u"color: white;\n"
                                                  "padding-left: 10px;\n"
                                                  "border-top: 2px solid white;\n"
                                                  "border-bottom: 2px solid white;\n"
                                                  "border-radius: 0px;")

        self.verticalLayout_45.addWidget(self.label_show_roll_number)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.btn_addInter = QPushButton(self.frame_content)
        self.btn_addInter.setObjectName(u"btn_addInter")
        self.btn_addInter.setMinimumSize(QSize(0, 30))
        self.btn_addInter.setMaximumSize(QSize(16777215, 30))
        self.btn_addInter.setStyleSheet(u"QPushButton{\n"
                                        "   color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(26, 114, 255);\n"
                                        "border: 0px solid;\n"
                                        "border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(21, 134, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgba(26, 114, 255, 100);\n"
                                        "}")

        self.horizontalLayout_23.addWidget(self.btn_addInter)

        self.btn_go_home = QPushButton(self.frame_content)
        self.btn_go_home.setObjectName(u"btn_go_home")
        self.btn_go_home.setMinimumSize(QSize(0, 30))
        self.btn_go_home.setMaximumSize(QSize(16777215, 30))
        self.btn_go_home.setStyleSheet(u"QPushButton{\n"
                                       "   color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(30, 36, 48);\n"
                                       "border: 0px solid;\n"
                                       "border-radius: 5px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgb(21, 134, 255);\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "background-color: rgba(26, 114, 255, 100);\n"
                                       "}")

        self.horizontalLayout_23.addWidget(self.btn_go_home)

        self.verticalLayout_45.addLayout(self.horizontalLayout_23)

        self.verticalLayout_44.addWidget(self.frame_content)

        self.verticalLayout_43.addWidget(self.frame_main_inter_info)

        self.stackedWidget.addWidget(self.page_add_inter)

        self.analytics = QWidget()

        self.horizontallLayout = QHBoxLayout(self.analytics)
        self.horizontallLayout.setObjectName(u"horizontallLayout")
        self.frame_content = QFrame(self.analytics)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"QFrame {\n"
                                         "	background-color: rgb(50, 53, 66);\n"
                                         "}\n"
                                         "/* VERTICAL SCROLLBAR */\n"
                                         " QScrollBar:vertical {\n"
                                         "	border: none;\n"
                                         "        background: rgb(45, 48, 59);\n"
                                         "        width: 15px;\n"
                                         "        margin: 30px 0 30px 0;\n"
                                         "        border-radius: 7px;\n"
                                         " }\n"
                                         "\n"
                                         "/*  HANDLE BAR VERTICAL */\n"
                                         "QScrollBar::handle:vertical {	\n"
                                         "	background-color: rgb(34, 35, 44);\n"
                                         "	min-height: 15px;\n"
                                         "	border-radius: 7px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:hover{	\n"
                                         "	background-color: rgb(38, 40, 50);\n"
                                         "\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:pressed {	\n"
                                         "	background-color: rgb(31, 32, 40);\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "/* BTN TOP - SCROLLBAR */\n"
                                         "QScrollBar::sub-line:vertical {\n"
                                         "	border: none;\n"
                                         "	background-color: rgb(45, 48, 59);\n"
                                         "	height: 15px;\n"
                                         "	border-top-left-radius: 7px;\n"
                                         "	border-top-right-radius: 7px;\n"
                                         "	subcontrol-position: top;\n"
                                         "	subcontrol-origin: margin;\n"
                                         "	margin-top: 10px;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:hover {	\n"
                                         "	background-color:   rgb(38, 40, 50);\n"
                                         "\n"
                                         "}"
                                         "\n"
                                         "QScrollBar::sub-line:vertical:pressed {	\n"
                                         "	background-color:rgb(31, 32, 40);\n"
                                         "        \n"
                                         "}\n"
                                         "\n"
                                         "/* BTN BOTTOM - SCROLLBAR */\n"
                                         "QScrollBar::add-line:vertical {\n"
                                         "	border: none;\n"
                                         "	background-color: rgb(45, 48, 59);\n"
                                         "	height: 15px;\n"
                                         "	border-bottom-left-radius: 7px;\n"
                                         "	border-bottom-right-radius: 7px;\n"
                                         "	subcontrol-position: bottom;\n"
                                         "	subcontrol-origin: margin;\n"
                                         "	margin-bottom: 10px;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:hover {	\n"
                                         "	background-color:    rgb(38, 40, 50);\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:pressed {	\n"
                                         "	background-color:rgb(31, 32, 40);\n"
                                         "}\n"
                                         "/* RESET ARROW */\n"
                                         "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                         "	background: none;\n"
                                         "}\n"
                                         "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                         "	background: none;\n"
                                         "}")

        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.hotizontalLayout_2 = QHBoxLayout(self.frame_content)
        self.hotizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea_content = QScrollArea(self.frame_content)
        self.scrollArea_content.setObjectName(u"scrollArea_content")
        self.scrollArea_content.setStyleSheet(u"background-color: rgb(50, 53, 66);\n"
                                              "border: none;")
        self.scrollArea_content.setWidgetResizable(True)
        self.scrollAreaWidgetContents_layout = QWidget()
        self.scrollAreaWidgetContents_layout.setObjectName(
            u"scrollAreaWidgetContents_layout")
        self.scrollAreaWidgetContents_layout.setGeometry(QRect(0, 0, 587, 502))
        self.verticalLayout_content_layout = QVBoxLayout(
            self.scrollAreaWidgetContents_layout)
        self.verticalLayout_content_layout.setObjectName(
            u"verticalLayout_content_layout")
        self.label_inter_head = QLabel(self.scrollAreaWidgetContents_layout)
        self.label_inter_head.setObjectName(u"label_inter_head")
        self.label_inter_head.setStyleSheet(u"QLabel {\n"
                                            "	color: white;\n"
                                            "	font: 22pt \"Microsoft Sans Serif\";\n"
                                            "	padding-left: 10px;\n"
                                            "	background-color: qlineargradient(spread:pad, x1:0, y1:0.562, x2:1, y2:0.511, stop:0 rgba(38, 40, 50, 255), stop:1 rgba(50, 53, 66, 255));\n"
                                            "	border-radius: 10px;\n"
                                            "}")
        self.verticalLayout_content_layout.addWidget(self.label_inter_head)

        self.frame_inter = QFrame(self.scrollAreaWidgetContents_layout)
        self.frame_inter.setObjectName(u"frame_inter")
        self.frame_inter.setMinimumSize(QSize(0, 450))
        self.frame_inter.setMaximumSize(QSize(16777215, 450))
        self.frame_inter.setStyleSheet(u"QFrame {\n"
                                       "	background-color: rgb(26, 27, 34);\n"
                                       "	border-radius:10px;\n"
                                       "	border: 0px solid;\n"
                                       "}\n"
                                       "QFrame:hover {\n"
                                       "	border: 2px solid rgb(11, 109, 255);\n"
                                       "}")
        self.frame_inter.setFrameShape(QFrame.StyledPanel)
        self.frame_inter.setFrameShadow(QFrame.Raised)

        self.inter_frame_layout = QHBoxLayout(self.frame_inter)
        self.inter_frame_layout.setContentsMargins(9, 9, 9, 9)
        self.inter_frame_layout.setSpacing(3)

        self.frame_inter.setLayout(self.inter_frame_layout)

        self.verticalLayout_content_layout.addWidget(self.frame_inter)

        self.label_lower_head = QLabel(self.scrollAreaWidgetContents_layout)
        self.label_lower_head.setObjectName(u"label_lower_head")
        self.label_lower_head.setStyleSheet(u"QLabel {\n"
                                            "	color: white;\n"
                                            "	font: 22pt \"Microsoft Sans Serif\";\n"
                                            "	padding-left: 10px;\n"
                                            "	background-color: qlineargradient(spread:pad, x1:0, y1:0.562, x2:1, y2:0.511, stop:0 rgba(38, 40, 50, 255), stop:1 rgba(50, 53, 66, 255));\n"
                                            "	border-radius: 10px;\n"
                                            "}")
        self.verticalLayout_content_layout.addWidget(self.label_lower_head)

        self.frame_lower = QFrame(self.scrollAreaWidgetContents_layout)
        self.frame_lower.setObjectName(u"frame_lower")
        self.frame_lower.setMinimumSize(QSize(0, 500))
        self.frame_lower.setMaximumSize(QSize(16777215, 500))
        self.frame_lower.setStyleSheet(u"QFrame {\n"
                                       "	background-color: rgb(26, 27, 34);\n"
                                       "	border-radius:10px;\n"
                                       "	border: 0px solid;\n"
                                       "}\n"
                                       "QFrame:hover {\n"
                                       "	border: 2px solid rgb(11, 109, 255);\n"
                                       "}")
        self.frame_lower.setFrameShape(QFrame.StyledPanel)
        self.frame_lower.setFrameShadow(QFrame.Raised)

        self.lower_frame_layout = QHBoxLayout(self.frame_lower)
        self.lower_frame_layout.setContentsMargins(9, 9, 9, 9)
        self.lower_frame_layout.setSpacing(3)
        self.frame_lower.setLayout(self.lower_frame_layout)

        self.verticalLayout_content_layout.addWidget(self.frame_lower)

        self.frame_lower_prim = QFrame(self.scrollAreaWidgetContents_layout)
        self.frame_lower_prim.setObjectName("frame_lower_prim")
        self.frame_lower_prim.setMinimumSize(QSize(0, 500))
        self.frame_lower_prim.setMaximumSize(QSize(16777215, 500))
        self.frame_lower_prim.setStyleSheet(u"QFrame {\n"
                                            "	background-color: rgb(26, 27, 34);\n"
                                            "	border-radius:10px;\n"
                                            "	border: 0px solid;\n"
                                            "}\n"
                                            "QFrame:hover {\n"
                                            "	border: 2px solid rgb(11, 109, 255);\n"
                                            "}"
                                            )
        self.frame_lower_prim.setFrameShape(QFrame.StyledPanel)
        self.frame_lower_prim.setFrameShadow(QFrame.Raised)

        self.frame_lower_prim_layout = QHBoxLayout(self.frame_lower_prim)
        self.frame_lower_prim_layout.setContentsMargins(9, 9, 9, 9)
        self.frame_lower_prim_layout.setSpacing(3)

        self.verticalLayout_content_layout.addWidget(self.frame_lower_prim)

        self.frame_lower_advan = QFrame(self.scrollAreaWidgetContents_layout)
        self.frame_lower_advan.setObjectName("frame_lower_advan")
        self.frame_lower_advan.setMinimumSize(QSize(0, 500))
        self.frame_lower_advan.setMaximumSize(QSize(16777215, 500))
        self.frame_lower_advan.setStyleSheet(u"QFrame {\n"
                                             "	background-color: rgb(26, 27, 34);\n"
                                             "	border-radius:10px;\n"
                                             "	border: 0px solid;\n"
                                             "}\n"
                                             "QFrame:hover {\n"
                                             "	border: 2px solid rgb(11, 109, 255);\n"
                                             "}"
                                             )
        self.frame_lower_advan.setFrameShape(QFrame.StyledPanel)
        self.frame_lower_advan.setFrameShadow(QFrame.Raised)

        self.frame_lower_advan_layout = QHBoxLayout(self.frame_lower_advan)
        self.frame_lower_advan_layout.setContentsMargins(9, 9, 9, 9)
        self.frame_lower_advan_layout.setSpacing(3)

        self.verticalLayout_content_layout.addWidget(self.frame_lower_advan)

        self.scrollArea_content.setWidget(self.scrollAreaWidgetContents_layout)

        self.hotizontalLayout_2.addWidget(self.scrollArea_content)

        self.horizontallLayout.addWidget(self.frame_content)
        self.stackedWidget.addWidget(self.analytics)

        self.page_add_lower = QWidget()
        self.page_add_lower.setObjectName(u"page_add_lower")
        self.verticalLayout_48 = QVBoxLayout(self.page_add_lower)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_main_lower_info = QFrame(self.page_add_lower)
        self.frame_main_lower_info.setObjectName(u"frame_main_lower_info")
        self.frame_main_lower_info.setMaximumSize(QSize(16777215, 650))
        self.frame_main_lower_info.setStyleSheet(u"QFrame {\n"
                                                 "       background-color: rgb(26, 27, 34);\n"
                                                 "       color: #fff;\n"
                                                 "       border-radius: 10px;\n"
                                                 "}")
        self.frame_main_lower_info.setFrameShape(QFrame.StyledPanel)
        self.frame_main_lower_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_main_lower_info)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_logo_icon_lower = QFrame(self.frame_main_lower_info)
        self.frame_logo_icon_lower.setObjectName(u"frame_logo_icon_lower")
        self.frame_logo_icon_lower.setFrameShape(QFrame.StyledPanel)
        self.frame_logo_icon_lower.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_logo_icon_lower)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_icon_lower = QLabel(self.frame_logo_icon_lower)
        self.label_icon_lower.setObjectName(u"label_icon_lower")
        self.label_icon_lower.setMinimumSize(QSize(210, 210))
        self.label_icon_lower.setMaximumSize(QSize(210, 210))
        self.label_icon_lower.setStyleSheet(u"QLabel{\n"
                                            "       border: 8px solid rgb(37, 38, 48);\n"
                                            "       background-color: rgb(50, 52, 65);\n"
                                            "       border-radius: 105px;\n"
                                            "}")

        self.horizontalLayout_24.addWidget(self.label_icon_lower)

        self.verticalLayout_46.addWidget(self.frame_logo_icon_lower)

        self.frame_content_lower = QFrame(self.frame_main_lower_info)
        self.frame_content_lower.setObjectName(u"frame_content_lower")
        self.frame_content_lower.setFrameShape(QFrame.StyledPanel)
        self.frame_content_lower.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_content_lower)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lineEdit_name_lower = QLineEdit(self.frame_content_lower)
        self.lineEdit_name_lower.setObjectName(u"lineEdit_name_lower")
        self.lineEdit_name_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_lower.setFont(font11)
        self.lineEdit_name_lower.setStyleSheet(u"QLineEdit{\n"
                                               "border: 0px solid;\n"
                                               "color: rgb(240, 240, 240);\n"
                                               "border-radius: 10px;\n"
                                               "background-color: #1D222E;\n"
                                               "padding-left: 10px;\n"
                                               "padding-right: 10px;\n"
                                               "selection-background-color: #30313F;\n"
                                               "selection-color: #5F6063;\n"
                                               "}\n"
                                               "QLineEdit:hover{\n"
                                               "border: 2px solid rgb(49, 50, 63);\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:focus{\n"
                                               "border: 2px solid rgb(61, 152, 212);\n"
                                               "}")
        self.lineEdit_name_lower.setClearButtonEnabled(True)

        self.horizontalLayout_25.addWidget(self.lineEdit_name_lower)

        self.lineEdit_address_lower = QLineEdit(self.frame_content_lower)
        self.lineEdit_address_lower.setObjectName(u"lineEdit_address_lower")
        self.lineEdit_address_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_address_lower.setFont(font10)
        self.lineEdit_address_lower.setStyleSheet(u"QLineEdit{\n"
                                                  "border: 0px solid;\n"
                                                  "color: rgb(240, 240, 240);\n"
                                                  "border-radius: 10px;\n"
                                                  "background-color: #1D222E;\n"
                                                  "padding-left: 10px;\n"
                                                  "padding-right: 10px;\n"
                                                  "selection-background-color: #30313F;\n"
                                                  "selection-color: #5F6063;\n"
                                                  "}\n"
                                                  "QLineEdit:hover{\n"
                                                  "border: 2px solid rgb(49, 50, 63);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:focus{\n"
                                                  "border: 2px solid rgb(61, 152, 212);\n"
                                                  "}")
        self.lineEdit_address_lower.setClearButtonEnabled(True)

        self.horizontalLayout_25.addWidget(self.lineEdit_address_lower)

        self.verticalLayout_47.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lineEdit_father = QLineEdit(self.frame_content_lower)
        self.lineEdit_father.setObjectName(u"lineEdit_father")
        self.lineEdit_father.setMinimumSize(QSize(0, 30))
        self.lineEdit_father.setFont(font10)
        self.lineEdit_father.setStyleSheet(u"QLineEdit{\n"
                                           "border: 0px solid;\n"
                                           "color: rgb(240, 240, 240);\n"
                                           "border-radius: 10px;\n"
                                           "background-color: #1D222E;\n"
                                           "padding-left: 10px;\n"
                                           "padding-right: 10px;\n"
                                           "selection-background-color: #30313F;\n"
                                           "selection-color: #5F6063;\n"
                                           "}\n"
                                           "QLineEdit:hover{\n"
                                           "border: 2px solid rgb(49, 50, 63);\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:focus{\n"
                                           "border: 2px solid rgb(61, 152, 212);\n"
                                           "}")

        self.horizontalLayout_30.addWidget(self.lineEdit_father)

        self.lineEdit_mather = QLineEdit(self.frame_content_lower)
        self.lineEdit_mather.setObjectName(u"lineEdit_mather")
        self.lineEdit_mather.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather.setFont(font10)
        self.lineEdit_mather.setStyleSheet(u"QLineEdit{\n"
                                           "border: 0px solid;\n"
                                           "color: rgb(240, 240, 240);\n"
                                           "border-radius: 10px;\n"
                                           "background-color: #1D222E;\n"
                                           "padding-left: 10px;\n"
                                           "padding-right: 10px;\n"
                                           "selection-background-color: #30313F;\n"
                                           "selection-color: #5F6063;\n"
                                           "}\n"
                                           "QLineEdit:hover{\n"
                                           "border: 2px solid rgb(49, 50, 63);\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:focus{\n"
                                           "border: 2px solid rgb(61, 152, 212);\n"
                                           "}")

        self.horizontalLayout_30.addWidget(self.lineEdit_mather)

        self.verticalLayout_47.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lineEdit_email_lower = QLineEdit(self.frame_content_lower)
        self.lineEdit_email_lower.setObjectName(u"lineEdit_email_lower")
        self.lineEdit_email_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_email_lower.setFont(font10)
        self.lineEdit_email_lower.setStyleSheet(u"QLineEdit{\n"
                                                "border: 0px solid;\n"
                                                "color: rgb(240, 240, 240);\n"
                                                "border-radius: 10px;\n"
                                                "background-color: #1D222E;\n"
                                                "padding-left: 10px;\n"
                                                "padding-right: 10px;\n"
                                                "selection-background-color: #30313F;\n"
                                                "selection-color: #5F6063;\n"
                                                "}\n"
                                                "QLineEdit:hover{\n"
                                                "border: 2px solid rgb(49, 50, 63);\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit:focus{\n"
                                                "border: 2px solid rgb(61, 152, 212);\n"
                                                "}")
        self.lineEdit_email_lower.setClearButtonEnabled(True)

        self.horizontalLayout_26.addWidget(self.lineEdit_email_lower)

        self.verticalLayout_47.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lineEdit_contect_lower = QLineEdit(self.frame_content_lower)
        self.lineEdit_contect_lower.setObjectName(u"lineEdit_contect_lower")
        self.lineEdit_contect_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_contect_lower.setFont(font10)
        self.lineEdit_contect_lower.setStyleSheet(u"QLineEdit{\n"
                                                  "border: 0px solid;\n"
                                                  "color: rgb(240, 240, 240);\n"
                                                  "border-radius: 10px;\n"
                                                  "background-color: #1D222E;\n"
                                                  "padding-left: 10px;\n"
                                                  "padding-right: 10px;\n"
                                                  "selection-background-color: #30313F;\n"
                                                  "selection-color: #5F6063;\n"
                                                  "}\n"
                                                  "QLineEdit:hover{\n"
                                                  "border: 2px solid rgb(49, 50, 63);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:focus{\n"
                                                  "border: 2px solid rgb(61, 152, 212);\n"
                                                  "}")
        self.lineEdit_contect_lower.setClearButtonEnabled(True)

        self.horizontalLayout_27.addWidget(self.lineEdit_contect_lower)

        self.lineEdit_level_lower = QComboBox(self.frame_content_lower)
        self.lineEdit_level_lower.setObjectName(u"lineEdit_level_lower")
        self.lineEdit_level_lower.setMinimumSize(QSize(495, 30))
        self.lineEdit_level_lower.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_level_lower.setFont(font10)
        self.lineEdit_level_lower.setStyleSheet("QComboBox{\n"
                                                "    background-color: #1D222E;\n"
                                                "    border-radius: 10px;\n"
                                                "    border: 2px solid  #1D222E;\n"
                                                "    padding: 5px;\n"
                                                "    padding-left: 10px;\n"
                                                "    color: white;\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox:hover{\n"
                                                "    border: 2px solid rgb(49, 50, 63);\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox::drop-down {\n"
                                                "    subcontrol-origin: padding;\n"
                                                "    subcontrol-position: top right;\n"
                                                "    width: 25px;\n"
                                                "    border-left-width: 3px;\n"
                                                "    border-left-color: rgba(39, 44, 54, 150);\n"
                                                "    border-left-style: solid;\n"
                                                "    border-top-right-radius: 3px;\n"
                                                "    border-bottom-right-radius: 3px;\n"
                                                "    background-image: url(./packges/app/items/icons/16x16/cil-arrow-bottom.png);\n"
                                                "    background-position: center;\n"
                                                "    background-repeat: no-reperat;\n"
                                                "}\n"
                                                "QComboBox QAbstractItemView {\n"
                                                "    color: rgb(85, 170, 255);\n"
                                                "    background-color: #1D222E;\n"
                                                "    padding: 10px;\n"
                                                "    selection-background-color: rgb(39, 44, 54);\n"
                                                "}")
        self.lineEdit_level_lower.addItem("")
        self.lineEdit_level_lower.addItem("")
        self.lineEdit_level_lower.addItem("")
        self.lineEdit_level_lower.addItem("")
        self.lineEdit_level_lower.addItem("")
        self.lineEdit_level_lower.addItem("")

        self.horizontalLayout_27.addWidget(self.lineEdit_level_lower)

        self.verticalLayout_47.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lineEdit_religion = QLineEdit(self.frame_content_lower)
        self.lineEdit_religion.setObjectName(u"lineEdit_religion")
        self.lineEdit_religion.setMinimumSize(QSize(0, 30))
        self.lineEdit_religion.setFont(font10)
        self.lineEdit_religion.setStyleSheet(u"QLineEdit{\n"
                                             "border: 0px solid;\n"
                                             "color: rgb(240, 240, 240);\n"
                                             "border-radius: 10px;\n"
                                             "background-color: #1D222E;\n"
                                             "padding-left: 10px;\n"
                                             "padding-right: 10px;\n"
                                             "selection-background-color: #30313F;\n"
                                             "selection-color: #5F6063;\n"
                                             "}\n"
                                             "QLineEdit:hover{\n"
                                             "border: 2px solid rgb(49, 50, 63);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus{\n"
                                             "border: 2px solid rgb(61, 152, 212);\n"
                                             "}")

        self.horizontalLayout_31.addWidget(self.lineEdit_religion)

        self.lineEdit_ragis_number = QLineEdit(self.frame_content_lower)
        self.lineEdit_ragis_number.setObjectName(u"lineEdit_ragis_number")
        self.lineEdit_ragis_number.setMinimumSize(QSize(0, 30))
        self.lineEdit_ragis_number.setFont(font10)
        self.lineEdit_ragis_number.setStyleSheet(u"QLineEdit{\n"
                                                 "border: 0px solid;\n"
                                                 "color: rgb(240, 240, 240);\n"
                                                 "border-radius: 10px;\n"
                                                 "background-color: #1D222E;\n"
                                                 "padding-left: 10px;\n"
                                                 "padding-right: 10px;\n"
                                                 "selection-background-color: #30313F;\n"
                                                 "selection-color: #5F6063;\n"
                                                 "}\n"
                                                 "QLineEdit:hover{\n"
                                                 "border: 2px solid rgb(49, 50, 63);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:focus{\n"
                                                 "border: 2px solid rgb(61, 152, 212);\n"
                                                 "}")

        self.horizontalLayout_31.addWidget(self.lineEdit_ragis_number)

        self.verticalLayout_47.addLayout(self.horizontalLayout_31)

        self.label_dateofbirth_info = QLabel(self.frame_content_lower)
        self.label_dateofbirth_info.setObjectName(u"label_dateofbirth_info")
        self.label_dateofbirth_info.setFont(font10)

        self.verticalLayout_47.addWidget(self.label_dateofbirth_info)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.dateEdit_data_of_birth = QDateEdit(self.frame_content_lower)
        self.dateEdit_data_of_birth.setObjectName(u"dateEdit_data_of_birth")
        self.dateEdit_data_of_birth.setMinimumSize(QSize(150, 30))
        self.dateEdit_data_of_birth.setMaximumSize(QSize(16777215, 16777215))
        self.dateEdit_data_of_birth.setFont(font10)
        self.dateEdit_data_of_birth.setStyleSheet(u"QDateEdit{\n"
                                                  "color:white;\n"
                                                  "background-color: #1D222E;\n"
                                                  "padding-left: 10px;\n"
                                                  "border: none;\n"
                                                  "border-radius: 10px;\n"
                                                  "}\n"
                                                  "QDateEdit::down-button{\n"
                                                  "image: url(packges/app/items/icons/main-icons/chevron-down.svg);\n"
                                                  "margin-right: 6px;\n"
                                                  "}\n"
                                                  "QDateEdit::up-button{\n"
                                                  "image: url(packges/app/items/icons/main-icons/chevron-up.svg);\n"
                                                  "margin-right: 6px;\n"
                                                  "}\n"
                                                  "QDateEdit::up-button:pressed{background-color: rgb(26, 114, 255);\n"
                                                  "border-radius: 5px;}\n"
                                                  "QDateEdit::down-button:pressed{background-color: rgb(26, 114, 255);\n"
                                                  "border-radius: 5px;}")

        self.horizontalLayout_32.addWidget(self.dateEdit_data_of_birth)

        self.verticalLayout_47.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(50, -1, 50, -1)
        self.radioButton_male_lower = QRadioButton(self.frame_content_lower)
        self.radioButton_male_lower.setObjectName(u"radioButton_male_lower")
        self.radioButton_male_lower.setMaximumSize(QSize(100, 16777215))
        self.radioButton_male_lower.setStyleSheet(u"QRadioButton {\n"
                                                  "color: #fff;\n"
                                                  "       background-color: rgb(26, 27, 34);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QRadioButton::indicator {\n"
                                                  "border: 3px solid rgb(52, 59, 72);\n"
                                                  "width: 15px;\n"
                                                  "height: 15px;\n"
                                                  "border-radius: 10px;\n"
                                                  "background: rgb(44, 49, 60);\n"
                                                  "color: #fff;\n"
                                                  "}\n"
                                                  "QRadioButton::indicator:hover {\n"
                                                  "border: 3px solid rgb(61, 152, 212);\n"
                                                  "}\n"
                                                  "QRadioButton::indicator:checked {\n"
                                                  "background: 3px solid  rgb(82, 197, 130);\n"
                                                  "border: 3px solid  rgb(82, 197, 130);  \n"
                                                  "}")

        self.horizontalLayout_28.addWidget(self.radioButton_male_lower)

        self.radioButton_female_lower = QRadioButton(self.frame_content_lower)
        self.radioButton_female_lower.setObjectName(
            u"radioButton_female_lower")
        self.radioButton_female_lower.setMaximumSize(QSize(100, 16777215))
        self.radioButton_female_lower.setStyleSheet(u"QRadioButton {\n"
                                                    "color: #fff;\n"
                                                    "background-color: rgb(26, 27, 34);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QRadioButton::indicator {\n"
                                                    "border: 3px solid rgb(52, 59, 72);\n"
                                                    "width: 15px;\n"
                                                    "height: 15px;\n"
                                                    "border-radius: 10px;\n"
                                                    "background: rgb(44, 49, 60);\n"
                                                    "color: #fff;\n"
                                                    "}\n"
                                                    "QRadioButton::indicator:hover {\n"
                                                    "border: 3px solid rgb(61, 152, 212);\n"
                                                    "}\n"
                                                    "QRadioButton::indicator:checked {\n"
                                                    "background: 3px solid  rgb(82, 197, 130);\n"
                                                    "border: 3px solid  rgb(82, 197, 130);  \n"
                                                    "}")

        self.horizontalLayout_28.addWidget(self.radioButton_female_lower)

        self.radioButton_other_lower = QRadioButton(self.frame_content_lower)
        self.radioButton_other_lower.setObjectName(u"radioButton_other_lower")
        self.radioButton_other_lower.setMaximumSize(QSize(100, 16777215))
        self.radioButton_other_lower.setStyleSheet(u"QRadioButton {\n"
                                                   "color: #fff;\n"
                                                   "background-color: rgb(26, 27, 34);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QRadioButton::indicator {\n"
                                                   "border: 3px solid rgb(52, 59, 72);\n"
                                                   "width: 15px;\n"
                                                   "height: 15px;\n"
                                                   "border-radius: 10px;\n"
                                                   "background: rgb(44, 49, 60);\n"
                                                   "color: #fff;\n"
                                                   "}\n"
                                                   "QRadioButton::indicator:hover {\n"
                                                   "border: 3px solid rgb(61, 152, 212);\n"
                                                   "}\n"
                                                   "QRadioButton::indicator:checked {\n"
                                                   "background: 3px solid  rgb(82, 197, 130);\n"
                                                   "border: 3px solid  rgb(82, 197, 130);  \n"
                                                   "}")

        self.horizontalLayout_28.addWidget(self.radioButton_other_lower)

        self.verticalLayout_47.addLayout(self.horizontalLayout_28)

        self.label_show_roll_number_lower = QLabel(self.frame_content_lower)
        self.label_show_roll_number_lower.setObjectName(
            u"label_show_roll_number_lower")
        self.label_show_roll_number_lower.setMinimumSize(QSize(0, 35))
        self.label_show_roll_number_lower.setStyleSheet(u"color: white;\n"
                                                        "padding-left: 10px;\n"
                                                        "border-top: 2px solid white;\n"
                                                        "border-bottom: 2px solid white;\n"
                                                        "border-radius: 0px;")

        self.verticalLayout_47.addWidget(self.label_show_roll_number_lower)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_addlower = QPushButton(self.frame_content_lower)
        self.btn_addlower.setObjectName(u"btn_addlower")
        self.btn_addlower.setMinimumSize(QSize(0, 30))
        self.btn_addlower.setMaximumSize(QSize(16777215, 30))
        self.btn_addlower.setStyleSheet(u"QPushButton{\n"
                                        "       color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(26, 114, 255);\n"
                                        "border: 0px solid;\n"
                                        "border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(21, 134, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgba(26, 114, 255, 100);\n"
                                        "}")

        self.horizontalLayout_29.addWidget(self.btn_addlower)

        self.btn_go_home_lower = QPushButton(self.frame_content_lower)
        self.btn_go_home_lower.setObjectName(u"btn_go_home_lower")
        self.btn_go_home_lower.setMinimumSize(QSize(0, 30))
        self.btn_go_home_lower.setMaximumSize(QSize(16777215, 30))
        self.btn_go_home_lower.setStyleSheet(u"QPushButton{\n"
                                             "       color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(30, 36, 48);\n"
                                             "border: 0px solid;\n"
                                             "border-radius: 5px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color: rgb(21, 134, 255);\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "background-color: rgba(26, 114, 255, 100);\n"
                                             "}")

        self.horizontalLayout_29.addWidget(self.btn_go_home_lower)

        self.verticalLayout_47.addLayout(self.horizontalLayout_29)

        self.verticalLayout_46.addWidget(self.frame_content_lower)

        self.verticalLayout_48.addWidget(self.frame_main_lower_info)

        self.stackedWidget.addWidget(self.page_add_lower)

        self.page_more_advanced = QWidget()
        self.page_more_advanced.setObjectName("page_more_advanced")
        self.verticalLayout_50 = QVBoxLayout(self.page_more_advanced)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.scrollArea_4 = QScrollArea(self.page_more_advanced)
        self.scrollArea_4.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
                                        "QScrollBar:vertical {\n"
                                        "    border: none;\n"
                                        "    background: rgb(45, 48, 59);\n"
                                        "    width: 15px;\n"
                                        "    margin: 30px 0 30px 0;\n"
                                        "    border-radius: 7px;\n"
                                        "}\n"
                                        "\n"
                                        "/*  HANDLE BAR VERTICAL */\n"
                                        "QScrollBar::handle:vertical {\n"
                                        "   background-color: rgb(34, 35, 44);\n"
                                        "   min-height: 15px;\n"
                                        "   border-radius: 7px;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:hover{\n"
                                        "   background-color: rgb(38, 40, 50);\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:pressed {\n"
                                        "   background-color: rgb(31, 32, 40);\n"
                                        "}\n"
                                        "\n"
                                        "/* BTN TOP - SCROLLBAR */\n"
                                        "QScrollBar::sub-line:vertical {\n"
                                        "   border: none;\n"
                                        "   background-color: rgb(45, 48, 59);\n"
                                        "   height: 15px;\n"
                                        "   border-top-left-radius: 7px;\n"
                                        "   border-top-right-radius: 7px;\n"
                                        "   subcontrol-position: top;\n"
                                        "   subcontrol-origin: margin;\n"
                                        "   margin-top: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:vertical:hover {\n"
                                        "   background-color:   rgb(38, 40, 50);\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::sub-line:vertical:pressed {\n"
                                        "   background-color:rgb(31, 32, 40);\n"
                                        "   }\n"
                                        "\n"
                                        "/* BTN BOTTOM - SCROLLBAR */\n"
                                        "QScrollBar::add-line:vertical {\n"
                                        "   border: none;\n"
                                        "   background-color: rgb(45, 48, 59);\n"
                                        "   height: 15px;\n"
                                        "   border-bottom-left-radius: 7px;\n"
                                        "   border-bottom-right-radius: 7px;\n"
                                        "   subcontrol-position: bottom;\n"
                                        "   subcontrol-origin: margin;\n"
                                        "   margin-bottom: 10px;\n"
                                        "}\n"
                                        "QScrollBar::add-line:vertical:hover {\n"
                                        "    background-color:    rgb(38, 40, 50);\n"
                                        "}\n"
                                        "QScrollBar::add-line:vertical:pressed {\n"
                                        "   background-color:rgb(31, 32, 40);\n"
                                        "}\n"
                                        "/* RESET ARROW */\n"
                                        "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                        "  background: none;\n"
                                        "}\n"
                                        "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                        "  background: none;\n"
                                        "}")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, -549, 851, 1136))
        self.scrollAreaWidgetContents_4.setObjectName(
            "scrollAreaWidgetContents_4")
        self.verticalLayout_49 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.label_advanced_level_12 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_advanced_level_12.setMinimumSize(QSize(0, 50))
        self.label_advanced_level_12.setMaximumSize(QSize(16777215, 50))
        self.label_advanced_level_12.setStyleSheet("QLabel {\n"
                                                   "    color: white;\n"
                                                   "    font: 22pt \"Microsoft Sans Serif\";\n"
                                                   "    padding-left: 10px;\n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0.562, x2:1, y2:0.511, stop:0 rgba(38, 40, 50, 255), stop:1 rgba(50, 53, 66, 255));\n"
                                                   "    border-radius: 10px;\n"
                                                   "}")
        self.label_advanced_level_12.setObjectName("label_advanced_level_12")
        self.verticalLayout_49.addWidget(self.label_advanced_level_12)
        self.frame_advanced_level_12 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_advanced_level_12.setMinimumSize(QSize(0, 500))
        self.frame_advanced_level_12.setMaximumSize(QSize(16777215, 500))
        self.frame_advanced_level_12.setStyleSheet("QFrame {\n"
                                                   "    background-color: rgb(26, 27, 34);\n"
                                                   "    border: 0px soild;\n"
                                                   "    border-radius: 10px;\n"
                                                   "}\n"
                                                   "QFrame:hover {\n"
                                                   "    border: 2px solid rgb(11, 109, 255);\n"
                                                   "}")
        self.frame_advanced_level_12.setFrameShape(QFrame.StyledPanel)
        self.frame_advanced_level_12.setFrameShadow(QFrame.Raised)
        self.frame_advanced_level_12.setObjectName("frame_advanced_level_12")
        self.frame_advanced_level_12_layout = QHBoxLayout(
            self.frame_advanced_level_12)
        self.frame_advanced_level_12_layout.setContentsMargins(9, 9, 9, 9)
        self.frame_advanced_level_12_layout.setSpacing(3)
        self.verticalLayout_49.addWidget(self.frame_advanced_level_12)
        self.label_advanced_level_13 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_advanced_level_13.setMinimumSize(QSize(0, 50))
        self.label_advanced_level_13.setMaximumSize(QSize(16777215, 50))
        self.label_advanced_level_13.setStyleSheet("QLabel {\n"
                                                   "    color: white;\n"
                                                   "    font: 22pt \"Microsoft Sans Serif\";\n"
                                                   "    padding-left: 10px;\n"
                                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0.562, x2:1, y2:0.511, stop:0 rgba(38, 40, 50, 255), stop:1 rgba(50, 53, 66, 255));\n"
                                                   "    border-radius: 10px;\n"
                                                   "}")
        self.label_advanced_level_13.setObjectName("label_advanced_level_13")
        self.verticalLayout_49.addWidget(self.label_advanced_level_13)
        self.frame_advanced_level_13 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_advanced_level_13.setMinimumSize(QSize(0, 500))
        self.frame_advanced_level_13.setMaximumSize(QSize(16777215, 500))
        self.frame_advanced_level_13.setStyleSheet("QFrame {\n"
                                                   "    background-color: rgb(26, 27, 34);\n"
                                                   "    border: 0px soild;\n"
                                                   "    border-radius: 10px;\n"
                                                   "}\n"
                                                   "QFrame:hover {\n"
                                                   "    border: 2px solid rgb(11, 109, 255);\n"
                                                   "}")
        self.frame_advanced_level_13.setFrameShape(QFrame.StyledPanel)
        self.frame_advanced_level_13.setFrameShadow(QFrame.Raised)
        self.frame_advanced_level_13.setObjectName("frame_advanced_level_13")
        self.frame_advanced_level_13_layout = QHBoxLayout(
            self.frame_advanced_level_13)
        self.frame_advanced_level_13_layout.setContentsMargins(9, 9, 9, 9)
        self.frame_advanced_level_13_layout.setSpacing(3)
        self.verticalLayout_49.addWidget(self.frame_advanced_level_13)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_50.addWidget(self.scrollArea_4)
        self.stackedWidget.addWidget(self.page_more_advanced)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayout_2.addWidget(self.frame_page)

        self.frame_super_user = QFrame(self.Content)
        self.frame_super_user.setObjectName(u"frame_super_user")
        self.frame_super_user.setMinimumSize(QSize(0, 0))
        self.frame_super_user.setMaximumSize(QSize(0, 16777215))
        self.frame_super_user.setStyleSheet(u"QFrame#frame_super_user{\n"
                                            "   background-color: rgb(26, 27, 34);\n"
                                            "}\n"
                                            "\n"
                                            "QFrame{\n"
                                            "   Background-color: none;\n"
                                            "}")
        self.frame_super_user.setFrameShape(QFrame.StyledPanel)
        self.frame_super_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_super_user)
        self.verticalLayout_40.setSpacing(2)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(5, 5, 5, 5)
        self.frame_user_icon_for_super = QFrame(self.frame_super_user)
        self.frame_user_icon_for_super.setObjectName(
            u"frame_user_icon_for_super")
        self.frame_user_icon_for_super.setMinimumSize(QSize(210, 210))
        self.frame_user_icon_for_super.setMaximumSize(QSize(210, 210))
        self.frame_user_icon_for_super.setStyleSheet(u"")
        self.frame_user_icon_for_super.setFrameShape(QFrame.StyledPanel)
        self.frame_user_icon_for_super.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_user_icon_for_super)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_super_icon = QLabel(self.frame_user_icon_for_super)
        self.label_super_icon.setObjectName(u"label_super_icon")
        self.label_super_icon.setStyleSheet(u"QLabel{\n"
                                            "   background-color: rgb(34, 35, 44);\n"
                                            "   border: 15px solid rgb(30, 31, 39);\n"
                                            "   border-radius: 95px;\n"
                                            "   color: #fff;\n"
                                            "   font: 75 12pt \"Segoe UI\";\n"
                                            "}")

        self.verticalLayout_41.addWidget(self.label_super_icon)

        self.verticalLayout_40.addWidget(self.frame_user_icon_for_super)

        self.frame_inforezion_super = QFrame(self.frame_super_user)
        self.frame_inforezion_super.setObjectName(u"frame_inforezion_super")
        self.frame_inforezion_super.setFrameShape(QFrame.StyledPanel)
        self.frame_inforezion_super.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_inforezion_super)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")

        self.label_infor_super = QLabel(self.frame_inforezion_super)
        self.label_infor_super.setMaximumSize(QSize(16777215, 400))
        self.label_infor_super.setObjectName(u"label_infor_super")
        self.label_infor_super.setStyleSheet("color: white\n;"
                                             "background-color: rgb(34, 35, 44);\n"
                                             "border: 6px solid rgb(30, 31, 39);\n"
                                             "border-radius: 15px;\n"
                                             "margin-top: 10px;\n")

        self.verticalLayout_42.addWidget(
            self.label_infor_super, 0, Qt.AlignTop)

        self.btn_edit_setting = QPushButton(self.frame_inforezion_super)
        self.btn_edit_setting.setFont(font11)
        self.btn_edit_setting.setObjectName(u"btn_edit_setting")
        self.btn_edit_setting.setStyleSheet(u"QPushButton { \n"
                                            "  background-color: #1e1f27;\n"
                                            "  text-align: left;\n"
                                            "  color: #fff;\n"
                                            "  border-radius: 10px;\n"
                                            "  padding-left: 5px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "  background-color: rgb(85, 170, 255);\n"
                                            "}\n"
                                            "QPushButton:pressed { \n"
                                            "  background-color: rgba(90, 175, 255, 100);\n"
                                            "}")
        self.btn_edit_setting.setMaximumSize(QSize(16777215, 45))
        self.btn_edit_setting.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_42.addWidget(self.btn_edit_setting)
        self.verticalLayout_40.addWidget(self.frame_inforezion_super)
        self.verticalLayout_32.addWidget(self.frame_more_options)
        self.frame_adout = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_adout.setMinimumSize(QSize(0, 50))
        self.frame_adout.setMaximumSize(QSize(16777215, 50))
        self.frame_adout.setStyleSheet("QFrame {\n"
                                       "    background-color: rgb(34, 35, 44);\n"
                                       "}")
        self.frame_adout.setFrameShape(QFrame.StyledPanel)
        self.frame_adout.setFrameShadow(QFrame.Raised)
        self.frame_adout.setObjectName("frame_adout")
        self.verticalLayout_51 = QVBoxLayout(self.frame_adout)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_info_adout = QLabel(self.frame_adout)
        font = QFont()
        font.setFamily("Segoe UI")
        self.label_info_adout.setFont(font)
        self.label_info_adout.setStyleSheet("color: white;\n"
                                            "padding-left: 20px;")
        self.label_info_adout.setObjectName("label_info_adout")
        self.horizontalLayout_31.addWidget(self.label_info_adout)
        self.btn_hidden_adout = QPushButton(self.frame_adout)
        self.btn_hidden_adout.setMinimumSize(QSize(30, 30))
        self.btn_hidden_adout.setMaximumSize(QSize(30, 30))
        self.btn_hidden_adout.setStyleSheet("QPushButton {\n"
                                            "    background-color: none;\n"
                                            "    color: white;\n"
                                            "    border: 0px solid;\n"
                                            "    border-radius: 15px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgb(0, 127, 226);\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color: rgba(0, 127, 226, 100);\n"
                                            "}")
        self.btn_hidden_adout.setText("")
        self.btn_hidden_adout.setObjectName("btn_hidden_adout")
        self.horizontalLayout_31.addWidget(self.btn_hidden_adout)
        self.verticalLayout_51.addLayout(self.horizontalLayout_31)
        self.frame_content_adout = QFrame(self.frame_adout)
        self.frame_content_adout.setMinimumSize(QSize(0, 0))
        self.frame_content_adout.setMaximumSize(QSize(16777215, 0))
        self.frame_content_adout.setStyleSheet(
            "background-color: rgb(26, 27, 34);")
        self.frame_content_adout.setFrameShape(QFrame.StyledPanel)
        self.frame_content_adout.setFrameShadow(QFrame.Raised)
        self.frame_content_adout.setObjectName("frame_content_adout")
        self.horizontalLayout_32 = QHBoxLayout(self.frame_content_adout)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_logo_adout = QLabel(self.frame_content_adout)
        self.label_logo_adout.setMinimumSize(QSize(0, 0))
        self.label_logo_adout.setMaximumSize(QSize(16777215, 16777215))
        self.label_logo_adout.setObjectName("label_logo_adout")
        self.horizontalLayout_32.addWidget(self.label_logo_adout)
        self.label_more_info_adout = QLabel(self.frame_content_adout)
        self.label_more_info_adout.setStyleSheet("color: white;\n"
                                                 "padding-left: 20px;")
        self.label_more_info_adout.setObjectName("label_more_info_adout")
        self.horizontalLayout_32.addWidget(self.label_more_info_adout)
        self.verticalLayout_51.addWidget(self.frame_content_adout)
        self.verticalLayout_32.addWidget(self.frame_adout)
        self.horizontalLayout_2.addWidget(self.frame_super_user)
        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        # if QT_CONFIG(tooltip)
        self.btn_Toggle.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Full view", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Toggle.setText("Hide Menu")
# if QT_CONFIG(tooltip)
        self.btn_inter.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Add School Teachers", None))
#endif // QT_CONFIG(tooltip)
        self.btn_inter.setText(QCoreApplication.translate(
            "MainWindow", u"  Add Teachers", None))
# if QT_CONFIG(tooltip)
        self.btn_lower.setToolTip(QCoreApplication.translate(
            "MainWindow", u" Add School Student ", None))
#endif // QT_CONFIG(tooltip)
        self.btn_lower.setText(QCoreApplication.translate(
            "MainWindow", u"  Add Students", None))
# if QT_CONFIG(tooltip)
        self.btn_backup.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Backup data in CSV", None))
#endif // QT_CONFIG(tooltip)
        self.btn_backup.setText(QCoreApplication.translate(
            "MainWindow", u"Backup", None))
# if QT_CONFIG(tooltip)
        self.btn_page_home.setToolTip(
            QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_home.setText("Home")
# if QT_CONFIG(tooltip)
        self.btn_page_left.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Left Status Or Recycle Bin", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_left.setText("Recycle Bin")
# if QT_CONFIG(tooltip)
        self.btn_page_search.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Search & Delete", None))
#endif // QT_CONFIG(tooltip)
        self.btn_page_search.setText("Search")
# if QT_CONFIG(tooltip)
        self.btn_setting.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Control", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setting.setText("Setting")
#endif // QT_CONFIG(tooltip)
        self.btn_page_analytics.setText("Analytics")
        self.btn_page_analytics.setToolTip(
            QCoreApplication.translate("MainWindow", u"Analytics Data", None)
        )

        self.label_info_Inter_1.setText("")
        self.label_info_user_inter_1.setText(QCoreApplication.translate(
            "MainWindow", u"This <b>\"Delete\"</b> is Add in to Recycle Bin ", None))
        self.btn_delete_inter_1.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))

        self.label_info_lower_1.setText("")
        self.label_info_user_lower_1.setText(QCoreApplication.translate(
            "MainWindow", u"This <b>\"Delete\"</b> is Add in to Recycle Bin ", None))
        self.btn_delete_lower_1.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.label_info_user_lower_pri.setText(
            QCoreApplication.translate(
                "MainWindow", u"This <b>\"Delete\"</b>  is Add in to Recycle Bin ", None)
        )
        self.btn_delete_lower_pri.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None)
        )
        self.label_info_lower_pri.setText("")
        self.label_info_user_lower_advan.setText(
            QCoreApplication.translate(
                "MainWindow", u"This <b>\"Delete\"</b>  is Add in to Recycle Bin ", None)
        )
        self.btn_delete_lower_advan.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None)
        )
        self.label_info_lower_advan.setText("")
        self.info_inter_left_1.setText("")
        self.label_info_user_left_inter_1.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>", None))
        self.btn_delete_inter_left_1.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.info_lower_1.setText("")
        self.label_info_user_left_lower_1.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>", None))
        self.btn_delete_lower_left_1.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.info_lower_left_pri.setText("")
        self.label_info_user_left_lower_pri.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>", None))
        self.btn_delete_lower_left_pri.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.info_lower_left_advan.setText("")
        self.label_info_user_left_lower_advan.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>This &quot;Delete&quot; is remove out of data</p></body></html>", None))
        self.btn_delete_lower_left_advan.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.userInfoForSearch.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
                                                                  "<head/>\n"
                                                                  "<body>\n"
                                                                  "<p>You can search any Name and Roll Number everthing available <br>in Active Status and Recycle Bin.</p>\n"
                                                                  "</body>\n"
                                                                  "</html>", None))
        self.lineEdit_nameSearch.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Search Name", None))
        self.btn_nameSearch.setText(
            QCoreApplication.translate("MainWindow", u" Search", None))
        self.lineEdit_rollSearch.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Search Roll Number", None))
        self.btn_rollSearch.setText(
            QCoreApplication.translate("MainWindow", u" Search", None))
# if QT_CONFIG(tooltip)
        self.frame_main_setting_bar.setToolTip(
            QCoreApplication.translate("MainWindow", u"Main Setting", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
#endif // QT_CONFIG(tooltip)
        self.label_username_title.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Change User Name</span></p></body></html>"))
        self.label_show_current_username.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Current User Name : </span></p></body></html>"))
        self.lineEdit_username_change_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Username"))
        self.btn_save_username.setText(
            QCoreApplication.translate("MainWindow", "Save"))
        self.label_change_email_title.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Change E-mail ID</span></p></body></html>"))
        self.label_current_email.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Current E-mail ID :</span></p></body></html>"))
        self.lineEdit_change_email_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "E-Mail"))
        self.btn_save_change_email.setText(
            QCoreApplication.translate("MainWindow", "Save"))
        self.label_change_contact_number_title.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Change Contact Number</span></p></body></html>"))
        self.label_show_current_contact_number.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Current Contact Number : </span></p></body></html>"))
        self.lineEdit_contact_number_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Contact Number"))
        self.btn_save_contact_number.setText(
            QCoreApplication.translate("MainWindow", "Save"))
        self.label_change_password_title.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Change Password</span></p></body></html>"))
        self.lineEdit_passord_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Password"))
        self.lineEdit_repassword_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Repassword"))
        self.btn_save_password.setText(
            QCoreApplication.translate("MainWindow", "Save"))

        self.label_inter_head.setText(QCoreApplication.translate(
            "MainWindow", u"Teachers Analytics", None))
        self.label_lower_head.setText(QCoreApplication.translate(
            "MainWindow", u"Students Analtics", None))
        self.label_super_icon.setText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.btn_edit_setting.setText(QCoreApplication.translate(
            "MainWindow", u"Edit Setting", None))

        self.frame_main_inter_info.setToolTip(
            QCoreApplication.translate("MainWindow", u"Add Teachers Data", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.lineEdit_name.setToolTip(
            QCoreApplication.translate("MainWindow", u"Name", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Name", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_address.setToolTip(
            QCoreApplication.translate("MainWindow", u"Addres", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_address.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Address", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_subject.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Havan't Subject Skip it", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_subject.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Subject", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_email.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Havan't Email Skip it", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_email.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Email", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_contect.setToolTip(
            QCoreApplication.translate("MainWindow", u"Contact Number", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_contect.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Contact Number", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_level.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Havan't Level Skip it", None))
        self.btn_upload_image.setText(QCoreApplication.translate(
            "MainWindow", u"Upload Image", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_level.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Level", None))
        self.radioButton_male.setText(
            QCoreApplication.translate("MainWindow", u"Male", None))
        self.radioButton_female.setText(
            QCoreApplication.translate("MainWindow", u"Female", None))
        self.radioButton_other.setText(
            QCoreApplication.translate("MainWindow", u"Other", None))
        self.label_emtye.setText("")
        self.label_show_roll_number.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Roll Number </span></p></body></html>", None))
        self.btn_addInter.setText(QCoreApplication.translate(
            "MainWindow", u" Add Teachers", None))
        self.btn_go_home.setText(QCoreApplication.translate(
            "MainWindow", u"Go Home", None))
        self.frame_main_lower_info.setToolTip(
            QCoreApplication.translate("MainWindow", u"Add Students Data", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.lineEdit_name_lower.setToolTip(
            QCoreApplication.translate("MainWindow", u"Name", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_name_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Name", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_address_lower.setToolTip(
            QCoreApplication.translate("MainWindow", u"Addres", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_address_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Address", None))
        self.lineEdit_father.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Father Name", None))
        self.lineEdit_mather.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Mather Name", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_email_lower.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Havan't Email Skip it", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_email_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Email", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_contect_lower.setToolTip(
            QCoreApplication.translate("MainWindow", u"Contact Number", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_contect_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Contact Number", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_level_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Level", None))
        self.lineEdit_religion.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Religion", None))
        self.lineEdit_ragis_number.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Registration Number", None))
        self.radioButton_male_lower.setText(
            QCoreApplication.translate("MainWindow", u"Male", None))
        self.radioButton_female_lower.setText(
            QCoreApplication.translate("MainWindow", u"Female", None))
        self.radioButton_other_lower.setText(
            QCoreApplication.translate("MainWindow", u"Other", None))
        self.label_show_roll_number_lower.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Roll Number </span></p></body></html>", None))
        self.btn_addlower.setText(QCoreApplication.translate(
            "MainWindow", u" Add Students", None))
        self.btn_go_home_lower.setText(
            QCoreApplication.translate("MainWindow", u"Go Home", None))
        self.label_title.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">More Options</span></p></body></html>"))
        self.label_reload_info.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">If you wnat to reload Findup, Clikc the button blow here.</span></p></body></html>"))
        self.btn_reload.setText(
            QCoreApplication.translate("MainWindow", "Reload"))
        self.label_reset_info.setText(QCoreApplication.translate(
            "MainWindow", "Reset your Findup to tis factory default settings. This will erase all data and  including data files."))
        self.btn_reset.setText(
            QCoreApplication.translate("MainWindow", "Reset"))
        self.btn_logout.setText(
            QCoreApplication.translate("MainWindow", "Log Out"))
        self.btn_primary.setToolTip(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">In Primary Students Button, You can include <b>1 to 5</b> grade students only.</span></p></body></html>"))
        self.btn_primary.setText(QCoreApplication.translate(
            "MainWindow", "Primary Students"))
        self.btn_ordinary.setToolTip(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">In Ordinary Students Button, You can include <b>6 to 11</b> grade students only.</span></p></body></html>"))
        self.btn_ordinary.setText(QCoreApplication.translate(
            "MainWindow", "Ordinary Students"))
        self.btn_advanced.setToolTip(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">In Advanced Students Button, You can include <b>12 to 13</b> grade any stream students.</span></p></body></html>"))
        self.btn_advanced.setText(QCoreApplication.translate(
            "MainWindow", "Advanced Students"))
        self.label_icon_.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/img/user100.png\"/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ADD STUDENTS</span></p></body></html>"))
        self.label_inforem_date_of_birth_ad.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Date Of Birth</span></p></body></html>"))
        self.radioButton_male_ad.setText(
            QCoreApplication.translate("MainWindow", "Male"))
        self.radioButton_female_ad.setText(
            QCoreApplication.translate("MainWindow", "Female"))
        self.radioButton_other_ad.setText(
            QCoreApplication.translate("MainWindow", "Other"))
        self.lineEdit_father_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Father Name"))
        self.lineEdit_mather_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Mather Name"))
        self.lineEdit_religion_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Religion"))
        self.lineEdit_registration_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Registration Number"))
        self.lineEdit_email_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Email"))
        self.lineEdit_level_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Level"))
        self.lineEdit_level_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Level"))
        self.comboBox_stream.setItemText(
            0, QCoreApplication.translate("MainWindow", "Mathematics"))
        self.comboBox_stream.setItemText(
            1, QCoreApplication.translate("MainWindow", "Science"))
        self.comboBox_stream.setItemText(2, QCoreApplication.translate(
            "MainWindow", "Engineering Technology"))
        self.comboBox_stream.setItemText(
            3, QCoreApplication.translate("MainWindow", "Bio Technology"))
        self.comboBox_stream.setItemText(
            4, QCoreApplication.translate("MainWindow", "Commerce"))
        self.comboBox_stream.setItemText(
            5, QCoreApplication.translate("MainWindow", "Art"))
        self.lineEdit_level_ad.setItemText(
            0, QCoreApplication.translate("MainWindow", "Level - 12"))
        self.lineEdit_level_ad.setItemText(
            1, QCoreApplication.translate("MainWindow", "Level - 13"))
        self.lineEdit_level_lower.setItemText(
            0, QCoreApplication.translate("MainWindow", "Level - 06"))
        self.lineEdit_level_lower.setItemText(
            1, QCoreApplication.translate("MainWindow", "Level - 07"))
        self.lineEdit_level_lower.setItemText(
            2, QCoreApplication.translate("MainWindow", "Level - 08"))
        self.lineEdit_level_lower.setItemText(
            3, QCoreApplication.translate("MainWindow", "Level - 09"))
        self.lineEdit_level_lower.setItemText(
            4, QCoreApplication.translate("MainWindow", "Level - 10"))
        self.lineEdit_level_lower.setItemText(
            5, QCoreApplication.translate("MainWindow", "Level - 11"))
        self.lineEdit_contect_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Contact Number"))
        self.lineEdit_name_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name"))
        self.lineEdit_address_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address"))
        self.label_show_roll_ad.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Roll Number </span></p></body></html>"))
        self.btn_addLower_adv.setText(
            QCoreApplication.translate("MainWindow", "Add Students"))
        self.btn_go_home_ad.setText(
            QCoreApplication.translate("MainWindow", "Go Home"))
        self.comboBox_stream_primary.setItemText(
            0, QCoreApplication.translate("MainWindow", "Level - 01"))
        self.comboBox_stream_primary.setItemText(
            1, QCoreApplication.translate("MainWindow", "Level - 02"))
        self.comboBox_stream_primary.setItemText(
            2, QCoreApplication.translate("MainWindow", "Level - 03"))
        self.comboBox_stream_primary.setItemText(
            3, QCoreApplication.translate("MainWindow", "Level - 04"))
        self.comboBox_stream_primary.setItemText(
            4, QCoreApplication.translate("MainWindow", "Level - 05"))
        self.lineEdit_email_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Email"))
        self.label_icon_primary.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/img/user100.png\"/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ADD STUDENTS</span></p></body></html>"))
        self.label_show_roll_primary.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Roll Number </span></p></body></html>"))
        self.lineEdit_contect_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Contact Number"))
        self.lineEdit_address_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address"))
        self.lineEdit_name_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name"))
        self.label_inforem_date_of_birth_ad_2.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Date Of Birth</span></p></body></html>"))
        self.radioButton_male_primary.setText(
            QCoreApplication.translate("MainWindow", "Male"))
        self.radioButton_female_primary.setText(
            QCoreApplication.translate("MainWindow", "Female"))
        self.radioButton_other_primary.setText(
            QCoreApplication.translate("MainWindow", "Other"))
        self.lineEdit_father_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Father Name"))
        self.lineEdit_mather_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Mather Name"))
        self.lineEdit_registration_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Registration Number"))
        self.lineEdit_religion_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Religion"))
        self.btn_addLower_primary.setText(
            QCoreApplication.translate("MainWindow", "Add Students"))
        self.btn_go_home_primary.setText(
            QCoreApplication.translate("MainWindow", "Go Home"))
        self.label_advanced_level_12.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p>Level - 12 Analytics</p></body></html>"))
        self.label_advanced_level_13.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p>Level - 13 Analytics</p></body></html>"))
        self.label_info_adout.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">About Findup</span></p></body></html>"))
        self.label_more_info_adout.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Version 4.1.0</span></p><p align=\"center\"><span style=\" font-size:9pt;\">Findup is a Store the sudents and teachers data more safely <br/>and backup the data csv file format. You can access the data single click.</span></p><p align=\"center\"><br/><span style=\" font-size:10pt;\">Copyright (C) 2022 The Gajen Lee Network.</span></p></body></html>"))
        self.label_more_info_adout.setToolTip(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p>About Findup</p></body></html>"))
        self.frame_adout.setToolTip(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p>About Findup</p></body></html>"))
    # retranslateUi
