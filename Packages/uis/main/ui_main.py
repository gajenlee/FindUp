from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Main(object):

    def setShadowEffect(self, widget, blur=30, color=QColor(0, 0, 0, 80)):

        # Set Shadow Effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(blur)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(color)

        widget.setGraphicsEffect(shadow)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1122, 571)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TopBar = QFrame(self.centralwidget)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setMaximumSize(QSize(16777215, 50))
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
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        font11 = QFont()
        font11.setFamily(u"./src/font/segoeui.ttf")
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
        font1.setFamily(u"./src/font/segoeui.ttf")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_inter.setFont(font1)

        self.horizontalLayout_7.addWidget(self.btn_inter)

        self.btn_lower = QPushButton(self.frame_add)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setMinimumSize(QSize(100, 0))
        self.btn_lower.setMaximumSize(QSize(250, 30))
        self.btn_lower.setFont(font1)

        self.horizontalLayout_7.addWidget(self.btn_lower)

        self.horizontalLayout_6.addWidget(self.frame_add)

        self.frame_backup = QFrame(self.frame_return_bar)
        self.frame_backup.setObjectName(u"frame_backup")
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

        self.verticalLayout_12.addWidget(self.btn_superuser)

        self.horizontalLayout_6.addWidget(self.frame_backup, 0, Qt.AlignRight)

        self.horizontalLayout_3.addWidget(self.frame_return_bar)

        self.horizontalLayout.addWidget(self.title_bar)

        self.verticalLayout.addWidget(self.TopBar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
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
        self.frame_page.setFrameShape(QFrame.StyledPanel)
        self.frame_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_add_students = QWidget()
        self.page_add_students.setObjectName("page_add_students")
        self.verticalLayout_43 = QVBoxLayout(self.page_add_students)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.frame_2 = QFrame(self.page_add_students)
        self.setShadowEffect(self.frame_2)
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
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_primary.setFont(font)
        self.btn_primary.setObjectName("btn_primary")
        self.horizontalLayout_25.addWidget(self.btn_primary)
        self.btn_ordinary = QPushButton(self.frame_2)
        self.btn_ordinary.setMinimumSize(QSize(0, 45))
        self.btn_ordinary.setMaximumSize(QSize(16777215, 45))
        self.btn_ordinary.setFont(font)
        self.btn_ordinary.setObjectName("btn_ordinary")
        self.horizontalLayout_25.addWidget(self.btn_ordinary)
        self.btn_advanced = QPushButton(self.frame_2)
        self.btn_advanced.setMinimumSize(QSize(0, 45))
        self.btn_advanced.setMaximumSize(QSize(16777215, 45))
        self.btn_advanced.setFont(font)
        self.btn_advanced.setObjectName("btn_advanced")
        self.horizontalLayout_25.addWidget(self.btn_advanced)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_25)
        self.verticalLayout_43.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_add_students)

        self.page_inter_add = QWidget()
        self.page_inter_add.setObjectName("page_inter_add")
        self.verticalLayout_43_inter = QVBoxLayout(self.page_inter_add)
        self.verticalLayout_43_inter.setObjectName("verticalLayout_43_inter")
        self.fakces_inter_3 = QFrame(self.page_inter_add)
        self.fakces_inter_3.setMinimumSize(QSize(0, 100))
        self.fakces_inter_3.setMaximumSize(QSize(16777215, 100))
        self.fakces_inter_3.setFrameShape(QFrame.StyledPanel)
        self.fakces_inter_3.setFrameShadow(QFrame.Raised)
        self.fakces_inter_3.setObjectName("fakces_inter_3")
        self.verticalLayout_43_inter.addWidget(self.fakces_inter_3)
        self.frame_add_btns_inters = QFrame(self.page_inter_add)
        self.frame_add_btns_inters.setFrameShape(QFrame.StyledPanel)
        self.frame_add_btns_inters.setFrameShadow(QFrame.Raised)
        self.frame_add_btns_inters.setObjectName("frame_add_btns_inters")
        self.horizontalLayout_26_inter = QHBoxLayout(
            self.frame_add_btns_inters)
        self.horizontalLayout_26_inter.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26_inter.setSpacing(0)
        self.horizontalLayout_26_inter.setObjectName(
            "horizontalLayout_26_inter")
        self.fakces_inter = QFrame(self.frame_add_btns_inters)
        self.fakces_inter.setMinimumSize(QSize(100, 0))
        self.fakces_inter.setMaximumSize(QSize(20, 16777215))
        self.fakces_inter.setFrameShape(QFrame.StyledPanel)
        self.fakces_inter.setFrameShadow(QFrame.Raised)
        self.fakces_inter.setObjectName("fakces_inter")
        self.horizontalLayout_26_inter.addWidget(self.fakces_inter)
        self.horizontalLayout_25_inter = QHBoxLayout()
        self.horizontalLayout_25_inter.setSpacing(15)
        self.horizontalLayout_25_inter.setObjectName(
            "horizontalLayout_25_inter")
        self.btn_teahers = QPushButton(self.frame_add_btns_inters)
        self.btn_teahers.setMinimumSize(QSize(0, 45))
        self.btn_teahers.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_teahers.setFont(font)
        self.btn_teahers.setObjectName("btn_teahers")
        self.horizontalLayout_25_inter.addWidget(self.btn_teahers)
        self.btn_none_teaher = QPushButton(self.frame_add_btns_inters)
        self.btn_none_teaher.setMinimumSize(QSize(0, 45))
        self.btn_none_teaher.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_none_teaher.setFont(font)
        self.btn_none_teaher.setObjectName("btn_none_teaher")
        self.horizontalLayout_25_inter.addWidget(self.btn_none_teaher)
        self.horizontalLayout_26_inter.addLayout(
            self.horizontalLayout_25_inter)
        self.fakces_inter_2 = QFrame(self.frame_add_btns_inters)
        self.fakces_inter_2.setMinimumSize(QSize(20, 0))
        self.fakces_inter_2.setMaximumSize(QSize(100, 16777215))
        self.fakces_inter_2.setFrameShape(QFrame.StyledPanel)
        self.fakces_inter_2.setFrameShadow(QFrame.Raised)
        self.fakces_inter_2.setObjectName("fakces_inter_2")
        self.horizontalLayout_26_inter.addWidget(self.fakces_inter_2)
        self.verticalLayout_43_inter.addWidget(self.frame_add_btns_inters)
        self.frame_informtion_inter = QFrame(self.page_inter_add)
        self.frame_informtion_inter.setMinimumSize(QSize(0, 100))
        self.frame_informtion_inter.setMaximumSize(QSize(16777215, 100))
        self.frame_informtion_inter.setFrameShape(QFrame.StyledPanel)
        self.frame_informtion_inter.setFrameShadow(QFrame.Raised)
        self.frame_informtion_inter.setObjectName("frame_informtion_inter")
        self.verticalLayout_44_inter = QVBoxLayout(self.frame_informtion_inter)
        self.verticalLayout_44_inter.setObjectName("verticalLayout_44_inter")
        self.verticalLayout_43_inter.addWidget(self.frame_informtion_inter)
        self.stackedWidget.addWidget(self.page_inter_add)

        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_48 = QVBoxLayout(self.page)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_main_content_for_primary = QFrame(self.page)
        self.setShadowEffect(self.frame_main_content_for_primary)
        self.frame_main_content_for_primary.setFrameShape(QFrame.StyledPanel)
        self.frame_main_content_for_primary.setFrameShadow(QFrame.Raised)
        self.frame_main_content_for_primary.setObjectName(
            "frame_main_content_for_primary")
        self.verticalLayout_47 = QVBoxLayout(
            self.frame_main_content_for_primary)
        self.verticalLayout_47.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_47.setObjectName("verticalLayout_47")

        self.frame_user_image_upload_primary = QFrame(
            self.frame_main_content_for_primary)

        self.gridLayout_primary = QGridLayout(
            self.frame_user_image_upload_primary)
        self.gridLayout_primary.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_primary.setSpacing(10)
        self.gridLayout_primary.setObjectName("gridLayout_lower")
        self.label_icon_primary = QLabel(self.frame_user_image_upload_primary)
        self.label_icon_primary.setMinimumSize(QSize(200, 200))
        self.label_icon_primary.setMaximumSize(QSize(200, 200))
        self.label_icon_primary.setObjectName("label_icon_primary")
        self.setShadowEffect(self.label_icon_primary)
        self.gridLayout_primary.addWidget(self.label_icon_primary, 0, 0, 1, 1)
        self.btn_upload_image_primary = QPushButton(
            self.frame_user_image_upload_primary)
        self.btn_upload_image_primary.setMinimumSize(QSize(0, 25))
        self.btn_upload_image_primary.setMaximumSize(QSize(300, 25))
        self.btn_upload_image_primary.setObjectName("btn_upload_image_primary")
        self.gridLayout_primary.addWidget(
            self.btn_upload_image_primary, 1, 0, 1, 1)

        self.verticalLayout_47.addWidget(self.frame_user_image_upload_primary)

        self.scrollArea_primary_add = QScrollArea(
            self.frame_main_content_for_primary)
        self.scrollArea_primary_add.setWidgetResizable(True)
        self.scrollArea_primary_add.setObjectName("scrollArea_primary_add")
        self.scrollAreaWidgetContents_primary = QWidget()
        self.scrollAreaWidgetContents_primary.setGeometry(
            QRect(0, 0, 839, 491))
        self.scrollAreaWidgetContents_primary.setObjectName(
            "scrollAreaWidgetContents_primary")
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_primary)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_gender_primary = QGroupBox(
            self.scrollAreaWidgetContents_primary)
        self.groupBox_gender_primary.setTitle("")
        self.groupBox_gender_primary.setObjectName("groupBox_gender_primary")
        self.verticalLayout_57 = QVBoxLayout(self.groupBox_gender_primary)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.label_info_gender_primary = QLabel(self.groupBox_gender_primary)
        self.label_info_gender_primary.setMinimumSize(QSize(0, 30))
        self.label_info_gender_primary.setObjectName(
            "label_info_gender_primary")
        self.verticalLayout_57.addWidget(self.label_info_gender_primary)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setContentsMargins(50, 0, 50, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.radioButton_male_primary_2 = QRadioButton(
            self.groupBox_gender_primary)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_male_primary_2.setFont(font)
        self.radioButton_male_primary_2.setObjectName(
            "radioButton_male_primary_2")
        self.horizontalLayout_36.addWidget(
            self.radioButton_male_primary_2, 0, Qt.AlignHCenter)
        self.radioButton_female_primary_2 = QRadioButton(
            self.groupBox_gender_primary)
        self.radioButton_female_primary_2.setFont(font)
        self.radioButton_female_primary_2.setObjectName(
            "radioButton_female_primary_2")
        self.horizontalLayout_36.addWidget(
            self.radioButton_female_primary_2, 0, Qt.AlignHCenter)
        self.radioButton_other_primary_2 = QRadioButton(
            self.groupBox_gender_primary)
        self.radioButton_other_primary_2.setFont(font)
        self.radioButton_other_primary_2.setObjectName(
            "radioButton_other_primary_2")
        self.horizontalLayout_36.addWidget(
            self.radioButton_other_primary_2, 0, Qt.AlignHCenter)
        self.verticalLayout_57.addLayout(self.horizontalLayout_36)
        self.gridLayout_6.addWidget(self.groupBox_gender_primary, 12, 0, 1, 2)
        self.lineEdit_father_name_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_father_name_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_father_name_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_father_name_primary.setObjectName(
            "lineEdit_father_name_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_father_name_primary, 2, 0, 1, 1)
        self.lineEdit_religion_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_religion_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_religion_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_religion_primary.setFont(font)
        self.lineEdit_religion_primary.setObjectName(
            "lineEdit_religion_primary")
        self.gridLayout_6.addWidget(self.lineEdit_religion_primary, 4, 0, 1, 1)
        self.lineEdit_admission_no_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_admission_no_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_admission_no_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_admission_no_primary.setFont(font)
        self.lineEdit_admission_no_primary.setObjectName(
            "lineEdit_admission_no_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_admission_no_primary, 4, 1, 1, 1)
        self.lineEdit_name_initial_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_name_initial_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_initial_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_name_initial_primary.setFont(font)
        self.lineEdit_name_initial_primary.setObjectName(
            "lineEdit_name_initial_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_name_initial_primary, 0, 1, 1, 1)
        self.dateEdit_date_of_birth_primary = QDateEdit(
            self.scrollAreaWidgetContents_primary)
        self.dateEdit_date_of_birth_primary.setMinimumSize(QSize(0, 30))
        self.dateEdit_date_of_birth_primary.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_date_of_birth_primary.setFont(font)
        self.dateEdit_date_of_birth_primary.setObjectName(
            "dateEdit_date_of_birth_primary")
        self.gridLayout_6.addWidget(
            self.dateEdit_date_of_birth_primary, 9, 0, 1, 1)
        self.lineEdit_name_full_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_name_full_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_full_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_name_full_primary.setFont(font)
        self.lineEdit_name_full_primary.setObjectName(
            "lineEdit_name_full_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_name_full_primary, 0, 0, 1, 1)
        self.lineEdit_no_siblings_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_no_siblings_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_no_siblings_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_no_siblings_primary.setFont(font)
        self.lineEdit_no_siblings_primary.setObjectName(
            "lineEdit_no_siblings_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_no_siblings_primary, 3, 0, 1, 1)
        self.lineEdit_mather_name_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_mather_name_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather_name_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_mather_name_primary.setObjectName(
            "lineEdit_mather_name_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_mather_name_primary, 2, 1, 1, 1)
        self.comboBox_stream_primary = QComboBox(
            self.scrollAreaWidgetContents_primary)
        self.comboBox_stream_primary.setMinimumSize(QSize(0, 30))
        self.comboBox_stream_primary.setMaximumSize(QSize(16777215, 30))
        self.comboBox_stream_primary.setFont(font)
        self.comboBox_stream_primary.setObjectName("comboBox_stream_primary")
        self.comboBox_stream_primary.addItem("")
        self.comboBox_stream_primary.addItem("")
        self.comboBox_stream_primary.addItem("")
        self.comboBox_stream_primary.addItem("")
        self.comboBox_stream_primary.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_stream_primary, 3, 1, 1, 1)
        self.dateEdit_date_admission_primary = QDateEdit(
            self.scrollAreaWidgetContents_primary)
        self.dateEdit_date_admission_primary.setMinimumSize(QSize(0, 30))
        self.dateEdit_date_admission_primary.setMaximumSize(
            QSize(16777215, 30))
        self.dateEdit_date_admission_primary.setObjectName(
            "dateEdit_date_admission_primary")
        self.gridLayout_6.addWidget(
            self.dateEdit_date_admission_primary, 9, 1, 1, 1)
        self.textEdit_address_home = QTextEdit(
            self.scrollAreaWidgetContents_primary)
        self.textEdit_address_home.setMinimumSize(QSize(0, 100))
        self.textEdit_address_home.setMaximumSize(QSize(16777215, 100))
        self.textEdit_address_home.setObjectName("textEdit_address_home")
        self.gridLayout_6.addWidget(self.textEdit_address_home, 1, 0, 1, 1)
        self.textEdit_address_office = QTextEdit(
            self.scrollAreaWidgetContents_primary)
        self.textEdit_address_office.setMinimumSize(QSize(0, 100))
        self.textEdit_address_office.setMaximumSize(QSize(16777215, 100))
        self.textEdit_address_office.setObjectName("textEdit_address_office")
        self.gridLayout_6.addWidget(self.textEdit_address_office, 1, 1, 1, 1)
        self.lineEdit_father_job_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_father_job_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_father_job_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_father_job_primary.setObjectName(
            "lineEdit_father_job_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_father_job_primary, 6, 0, 1, 1)
        self.lineEdit_mather_job_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_mather_job_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather_job_primary.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_mather_job_primary.setObjectName(
            "lineEdit_mather_job_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_mather_job_primary, 6, 1, 1, 1)
        self.label_inforem_date_of_birth_primary = QLabel(
            self.scrollAreaWidgetContents_primary)
        self.label_inforem_date_of_birth_primary.setMinimumSize(QSize(0, 30))
        self.label_inforem_date_of_birth_primary.setMaximumSize(
            QSize(16777215, 30))
        self.label_inforem_date_of_birth_primary.setObjectName(
            "label_inforem_date_of_birth_primary")
        self.gridLayout_6.addWidget(
            self.label_inforem_date_of_birth_primary, 8, 0, 1, 1)
        self.label_inforem_admission_primary = QLabel(
            self.scrollAreaWidgetContents_primary)
        self.label_inforem_admission_primary.setObjectName(
            "label_inforem_admission_primary")
        self.gridLayout_6.addWidget(
            self.label_inforem_admission_primary, 8, 1, 1, 1)
        self.lineEdit_parent_contact_primary = QLineEdit(
            self.scrollAreaWidgetContents_primary)
        self.lineEdit_parent_contact_primary.setMinimumSize(QSize(0, 30))
        self.lineEdit_parent_contact_primary.setMaximumSize(
            QSize(16777215, 30))
        self.lineEdit_parent_contact_primary.setObjectName(
            "lineEdit_parent_contact_primary")
        self.gridLayout_6.addWidget(
            self.lineEdit_parent_contact_primary, 7, 0, 1, 2)
        self.scrollArea_primary_add.setWidget(
            self.scrollAreaWidgetContents_primary)
        self.verticalLayout_47.addWidget(self.scrollArea_primary_add)

        self.frame_coments_ad_2 = QFrame(self.frame_main_content_for_primary)
        self.frame_coments_ad_2.setFrameShape(QFrame.StyledPanel)
        self.frame_coments_ad_2.setFrameShadow(QFrame.Raised)
        self.frame_coments_ad_2.setObjectName("frame_coments_ad_2")
        self.gridLayout_3 = QGridLayout(self.frame_coments_ad_2)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_show_roll_primary = QLabel(self.frame_coments_ad_2)
        self.label_show_roll_primary.setMinimumSize(QSize(0, 30))
        self.label_show_roll_primary.setMaximumSize(QSize(16777215, 30))
        self.label_show_roll_primary.setObjectName("label_show_roll_primary")
        self.gridLayout_3.addWidget(self.label_show_roll_primary, 10, 0, 1, 2)
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.btn_addLower_primary = QPushButton(self.frame_coments_ad_2)
        self.btn_addLower_primary.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addLower_primary.setFont(font)
        self.btn_addLower_primary.setObjectName("btn_addLower_primary")
        self.horizontalLayout_30.addWidget(self.btn_addLower_primary)
        self.btn_go_home_primary = QPushButton(self.frame_coments_ad_2)
        self.btn_go_home_primary.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_go_home_primary.setFont(font)
        self.btn_go_home_primary.setObjectName("btn_go_home_primary")
        self.horizontalLayout_30.addWidget(self.btn_go_home_primary)
        self.gridLayout_3.addLayout(self.horizontalLayout_30, 11, 0, 1, 2)
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
        self.setShadowEffect(self.frame_main_content_for_advance)
        self.frame_main_content_for_advance.setFrameShape(QFrame.StyledPanel)
        self.frame_main_content_for_advance.setFrameShadow(QFrame.Raised)
        self.frame_main_content_for_advance.setObjectName(
            "frame_main_content_for_advance")
        self.verticalLayout_46 = QVBoxLayout(
            self.frame_main_content_for_advance)
        self.verticalLayout_46.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_46.setObjectName("verticalLayout_46")

        self.frame_user_image_upload_advanced = QFrame(
            self.frame_main_content_for_advance)

        self.gridLayout_advanced = QGridLayout(
            self.frame_user_image_upload_advanced)
        self.gridLayout_advanced.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_advanced.setSpacing(10)
        self.gridLayout_advanced.setObjectName("gridLayout_lower")
        self.label_icon_ = QLabel(self.frame_user_image_upload_advanced)
        self.label_icon_.setMinimumSize(QSize(200, 200))
        self.label_icon_.setMaximumSize(QSize(200, 200))
        self.label_icon_.setObjectName("label_icon_")
        self.setShadowEffect(self.label_icon_)
        self.gridLayout_advanced.addWidget(self.label_icon_, 0, 0, 1, 1)
        self.btn_upload_image_advanced = QPushButton(
            self.frame_user_image_upload_advanced)
        self.btn_upload_image_advanced.setMinimumSize(QSize(0, 25))
        self.btn_upload_image_advanced.setMaximumSize(QSize(300, 25))
        self.btn_upload_image_advanced.setObjectName(
            "btn_upload_image_advanced")
        self.gridLayout_advanced.addWidget(
            self.btn_upload_image_advanced, 1, 0, 1, 1)

        self.verticalLayout_46.addWidget(self.frame_user_image_upload_advanced)

        self.frame_advanced_content = QFrame(
            self.frame_main_content_for_advance)
        self.frame_advanced_content.setMinimumSize(QSize(0, 250))
        self.frame_advanced_content.setFrameShape(QFrame.StyledPanel)
        self.frame_advanced_content.setFrameShadow(QFrame.Raised)
        self.frame_advanced_content.setObjectName("frame_advanced_content")
        self.verticalLayout_52 = QVBoxLayout(self.frame_advanced_content)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.scrollArea_advanced_add = QScrollArea(self.frame_advanced_content)
        self.scrollArea_advanced_add.setWidgetResizable(True)
        self.scrollArea_advanced_add.setObjectName("scrollArea_advanced_add")
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -130, 819, 387))
        self.scrollAreaWidgetContents_5.setObjectName(
            "scrollAreaWidgetContents_5")
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_address_office_ad = QTextEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_address_office_ad.setMinimumSize(QSize(0, 100))
        self.lineEdit_address_office_ad.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_address_office_ad.setFont(font)
        self.lineEdit_address_office_ad.setObjectName(
            "lineEdit_address_office_ad")
        self.gridLayout_5.addWidget(
            self.lineEdit_address_office_ad, 2, 2, 1, 1)
        self.lineEdit_home_address_ad = QTextEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_home_address_ad.setMinimumSize(QSize(0, 100))
        self.lineEdit_home_address_ad.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_home_address_ad.setFont(font)
        self.lineEdit_home_address_ad.setObjectName("lineEdit_home_address_ad")
        self.gridLayout_5.addWidget(self.lineEdit_home_address_ad, 2, 1, 1, 1)
        self.lineEdit_mather_name_ad = QLineEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_mather_name_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather_name_ad.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_mather_name_ad.setObjectName("lineEdit_mather_name_ad")
        self.gridLayout_5.addWidget(self.lineEdit_mather_name_ad, 3, 2, 1, 1)
        self.lineEdit_mather_job_ad = QLineEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_mather_job_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather_job_ad.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_mather_job_ad.setObjectName("lineEdit_mather_job_ad")
        self.gridLayout_5.addWidget(self.lineEdit_mather_job_ad, 4, 1, 1, 1)
        self.lineEdit_siblings_ad = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_siblings_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_siblings_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_siblings_ad.setFont(font)
        self.lineEdit_siblings_ad.setObjectName("lineEdit_siblings_ad")
        self.gridLayout_5.addWidget(self.lineEdit_siblings_ad, 6, 1, 1, 1)
        self.lineEdit_religion_ad = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_religion_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_religion_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_religion_ad.setFont(font)
        self.lineEdit_religion_ad.setObjectName("lineEdit_religion_ad")
        self.gridLayout_5.addWidget(self.lineEdit_religion_ad, 8, 1, 1, 1)
        self.lineEdit_parent_contact_no_ad = QLineEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_parent_contact_no_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_parent_contact_no_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_parent_contact_no_ad.setFont(font)
        self.lineEdit_parent_contact_no_ad.setObjectName(
            "lineEdit_parent_contact_no_ad")
        self.gridLayout_5.addWidget(
            self.lineEdit_parent_contact_no_ad, 8, 2, 1, 1)
        self.label_inforem_date_of_birth_ad = QLabel(
            self.scrollAreaWidgetContents_5)
        self.label_inforem_date_of_birth_ad.setMinimumSize(QSize(0, 30))
        self.label_inforem_date_of_birth_ad.setMaximumSize(QSize(16777215, 30))
        self.label_inforem_date_of_birth_ad.setObjectName(
            "label_inforem_date_of_birth_ad")
        self.gridLayout_5.addWidget(
            self.label_inforem_date_of_birth_ad, 9, 1, 1, 1)
        self.label_date_admission_ad = QLabel(self.scrollAreaWidgetContents_5)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.label_date_admission_ad.setFont(font)
        self.label_date_admission_ad.setObjectName("label_date_admission_ad")
        self.gridLayout_5.addWidget(self.label_date_admission_ad, 9, 2, 1, 1)
        self.dateEdit_date_of_birth_ad = QDateEdit(
            self.scrollAreaWidgetContents_5)
        self.dateEdit_date_of_birth_ad.setMinimumSize(QSize(0, 30))
        self.dateEdit_date_of_birth_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.dateEdit_date_of_birth_ad.setFont(font)
        self.dateEdit_date_of_birth_ad.setObjectName(
            "dateEdit_date_of_birth_ad")
        self.gridLayout_5.addWidget(
            self.dateEdit_date_of_birth_ad, 10, 1, 1, 1)
        self.lineEdit_father_job_ad = QLineEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_father_job_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_father_job_ad.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_father_job_ad.setObjectName("lineEdit_father_job_ad")
        self.gridLayout_5.addWidget(self.lineEdit_father_job_ad, 5, 1, 1, 1)
        self.dateEdit_date_of_admission_ad = QDateEdit(
            self.scrollAreaWidgetContents_5)
        self.dateEdit_date_of_admission_ad.setMinimumSize(QSize(0, 30))
        self.dateEdit_date_of_admission_ad.setMaximumSize(QSize(16777215, 30))
        self.dateEdit_date_of_admission_ad.setObjectName(
            "dateEdit_date_of_admission_ad")
        self.gridLayout_5.addWidget(
            self.dateEdit_date_of_admission_ad, 10, 2, 1, 1)
        self.lineEdit_name_initial_ad = QLineEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_name_initial_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_initial_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_name_initial_ad.setFont(font)
        self.lineEdit_name_initial_ad.setObjectName("lineEdit_name_initial_ad")
        self.gridLayout_5.addWidget(self.lineEdit_name_initial_ad, 1, 2, 1, 1)
        self.lineEdit_name_full_ad = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_name_full_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_full_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_name_full_ad.setFont(font)
        self.lineEdit_name_full_ad.setObjectName("lineEdit_name_full_ad")
        self.gridLayout_5.addWidget(self.lineEdit_name_full_ad, 1, 1, 1, 1)
        self.lineEdit_father_name_ad = QLineEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_father_name_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_father_name_ad.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_father_name_ad.setObjectName("lineEdit_father_name_ad")
        self.gridLayout_5.addWidget(self.lineEdit_father_name_ad, 3, 1, 1, 1)
        self.comboBox_stream = QComboBox(self.scrollAreaWidgetContents_5)
        self.comboBox_stream.setMinimumSize(QSize(0, 30))
        self.comboBox_stream.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.comboBox_stream.setFont(font)
        self.comboBox_stream.setObjectName("comboBox_stream")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.comboBox_stream.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_stream, 4, 2, 1, 1)
        self.lineEdit_admission_no_ad = QLineEdit(
            self.scrollAreaWidgetContents_5)
        self.lineEdit_admission_no_ad.setMinimumSize(QSize(0, 30))
        self.lineEdit_admission_no_ad.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_admission_no_ad.setFont(font)
        self.lineEdit_admission_no_ad.setObjectName("lineEdit_admission_no_ad")
        self.gridLayout_5.addWidget(self.lineEdit_admission_no_ad, 6, 2, 1, 1)
        self.groupBox_gender_advanced = QGroupBox(
            self.scrollAreaWidgetContents_5)
        self.groupBox_gender_advanced.setTitle("")
        self.groupBox_gender_advanced.setObjectName("groupBox_gender_advanced")
        self.verticalLayout_56 = QVBoxLayout(self.groupBox_gender_advanced)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.label_gender_ad = QLabel(self.groupBox_gender_advanced)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.label_gender_ad.setFont(font)
        self.label_gender_ad.setObjectName("label_gender_ad")
        self.verticalLayout_56.addWidget(self.label_gender_ad)
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setContentsMargins(50, 0, 50, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.radioButton_male_ad = QRadioButton(
            self.groupBox_gender_advanced)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_male_ad.setFont(font)
        self.radioButton_male_ad.setObjectName("radioButton_male_ad")
        self.horizontalLayout_35.addWidget(self.radioButton_male_ad)
        self.radioButton_female_ad = QRadioButton(
            self.groupBox_gender_advanced)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_female_ad.setFont(font)
        self.radioButton_female_ad.setObjectName("radioButton_female_ad")
        self.horizontalLayout_35.addWidget(self.radioButton_female_ad)
        self.radioButton_other_ad = QRadioButton(
            self.groupBox_gender_advanced)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_other_ad.setFont(font)
        self.radioButton_other_ad.setObjectName("radioButton_other_ad")
        self.horizontalLayout_35.addWidget(self.radioButton_other_ad)
        self.verticalLayout_56.addLayout(self.horizontalLayout_35)
        self.gridLayout_5.addWidget(self.groupBox_gender_advanced, 11, 1, 1, 2)

        self.comboBox_level_ad = QComboBox(self.scrollAreaWidgetContents_5)
        self.comboBox_level_ad.setMinimumSize(QSize(0, 30))
        self.comboBox_level_ad.setMaximumSize(QSize(16777215, 30))
        self.comboBox_level_ad.setObjectName("comboBox_level_ad")
        self.comboBox_level_ad.addItem("")
        self.comboBox_level_ad.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_level_ad, 5, 2, 1, 1)
        self.scrollArea_advanced_add.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_52.addWidget(self.scrollArea_advanced_add)
        self.verticalLayout_46.addWidget(self.frame_advanced_content)

        self.frame_coments_ad = QFrame(self.frame_main_content_for_advance)
        self.frame_coments_ad.setFrameShape(QFrame.StyledPanel)
        self.frame_coments_ad.setFrameShadow(QFrame.Raised)
        self.frame_coments_ad.setObjectName("frame_coments_ad")
        self.gridLayout_2 = QGridLayout(self.frame_coments_ad)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_show_roll_ad = QLabel(self.frame_coments_ad)
        self.label_show_roll_ad.setMinimumSize(QSize(0, 30))
        self.label_show_roll_ad.setMaximumSize(QSize(16777215, 30))
        self.label_show_roll_ad.setObjectName("label_show_roll_ad")
        self.gridLayout_2.addWidget(self.label_show_roll_ad, 10, 0, 1, 2)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.btn_addLower_adv = QPushButton(self.frame_coments_ad)
        self.btn_addLower_adv.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addLower_adv.setFont(font)
        self.btn_addLower_adv.setObjectName("btn_addLower_adv")
        self.horizontalLayout_28.addWidget(self.btn_addLower_adv)
        self.btn_go_home_ad = QPushButton(self.frame_coments_ad)
        self.btn_go_home_ad.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_go_home_ad.setFont(font)
        self.btn_go_home_ad.setObjectName("btn_go_home_ad")
        self.horizontalLayout_28.addWidget(self.btn_go_home_ad)
        self.gridLayout_2.addLayout(self.horizontalLayout_28, 11, 0, 1, 2)
        self.verticalLayout_46.addWidget(self.frame_coments_ad)
        self.verticalLayout_45.addWidget(self.frame_main_content_for_advance)
        self.stackedWidget.addWidget(self.page_add_advan)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout_6 = QVBoxLayout(self.Home)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_main_home_bar = QFrame(self.Home)
        self.frame_main_home_bar.setObjectName(u"frame_main_home_bar")
        self.frame_main_home_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_home_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_main_home_bar)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.scrollArea = QScrollArea(self.frame_main_home_bar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.page_content_Input = QWidget()
        self.page_content_Input.setObjectName(u"page_content_Input")
        self.page_content_Input.setGeometry(QRect(0, 0, 753, 1636))
        self.verticalLayout_13 = QVBoxLayout(self.page_content_Input)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.widget_inter_1 = QFrame(self.page_content_Input)
        self.widget_inter_1.setObjectName(u"widget_inter_1")
        self.widget_inter_1.setMinimumSize(QSize(0, 500))
        self.setShadowEffect(self.widget_inter_1)
        self.verticalLayout_19 = QVBoxLayout(self.widget_inter_1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.label_info_Inter_face = QLabel(self.widget_inter_1)
        self.label_info_Inter_face.setObjectName(u"label_info_Inter_face")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_Inter_face.setMinimumSize(150, 150)
        self.label_info_Inter_face.setMaximumSize(150, 150)
        self.label_info_Inter_face.setFont(font2)
        self.setShadowEffect(self.label_info_Inter_face)

        self.verticalLayout_19.addWidget(
            self.label_info_Inter_face, 0, Qt.AlignCenter)

        self.label_info_Inter_1 = QLabel(self.widget_inter_1)
        self.label_info_Inter_1.setObjectName(u"label_info_Inter_1")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_Inter_1.setFont(font2)
        self.verticalLayout_19.addWidget(self.label_info_Inter_1)

        self.frame_inter_delet_bar_1 = QFrame(self.widget_inter_1)
        self.frame_inter_delet_bar_1.setObjectName(u"frame_inter_delet_bar_1")
        self.frame_inter_delet_bar_1.setMaximumSize(QSize(16777215, 40))
        self.setShadowEffect(self.frame_inter_delet_bar_1)
        self.frame_inter_delet_bar_1.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_delet_bar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_inter_delet_bar_1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_info_user_inter_1 = QLabel(self.frame_inter_delet_bar_1)
        self.label_info_user_inter_1.setObjectName(u"label_info_user_inter_1")
        font3 = QFont()
        font3.setFamily(u"./src/font/segoeui.ttf")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_info_user_inter_1.setFont(font3)
        self.label_info_user_inter_1.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_12.addWidget(self.label_info_user_inter_1)

        self.btn_delete_inter_1 = QPushButton(self.frame_inter_delet_bar_1)
        self.btn_delete_inter_1.setObjectName(u"btn_delete_inter_1")
        self.btn_delete_inter_1.setMinimumSize(QSize(100, 25))
        self.btn_delete_inter_1.setMaximumSize(QSize(100, 40))
        font4 = QFont()
        font4.setFamily(u"./src/font/segoeui.ttf")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_delete_inter_1.setFont(font4)

        self.horizontalLayout_12.addWidget(self.btn_delete_inter_1)

        self.verticalLayout_19.addWidget(self.frame_inter_delet_bar_1)

        self.verticalLayout_13.addWidget(self.widget_inter_1)

        self.widget_lower_1 = QWidget(self.page_content_Input)
        self.widget_lower_1.setObjectName(u"widget_lower_1")
        self.widget_lower_1.setMinimumSize(QSize(0, 500))
        self.setShadowEffect(self.widget_lower_1)
        self.verticalLayout_21 = QVBoxLayout(self.widget_lower_1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")

        self.label_info_lower_face = QLabel(self.widget_lower_1)
        self.label_info_lower_face.setObjectName(u"label_info_lower_face")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_lower_face.setMinimumSize(150, 150)
        self.label_info_lower_face.setMaximumSize(150, 150)
        self.label_info_lower_face.setFont(font2)
        self.setShadowEffect(self.label_info_lower_face)

        self.verticalLayout_21.addWidget(
            self.label_info_lower_face, 0, Qt.AlignCenter)

        self.label_info_lower_1 = QLabel(self.widget_lower_1)
        self.label_info_lower_1.setObjectName(u"label_info_lower_1")
        self.label_info_lower_1.setFont(font2)

        self.verticalLayout_21.addWidget(self.label_info_lower_1)

        self.frame_inter_delet_bar_3 = QFrame(self.widget_lower_1)
        self.frame_inter_delet_bar_3.setObjectName(u"frame_inter_delet_bar_3")
        self.frame_inter_delet_bar_3.setMaximumSize(QSize(16777215, 40))
        self.setShadowEffect(self.frame_inter_delet_bar_3)
        self.frame_inter_delet_bar_3.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_delet_bar_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_inter_delet_bar_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_info_user_lower_1 = QLabel(self.frame_inter_delet_bar_3)
        self.label_info_user_lower_1.setObjectName(u"label_info_user_lower_1")
        self.label_info_user_lower_1.setFont(font3)
        self.label_info_user_lower_1.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_14.addWidget(self.label_info_user_lower_1)

        self.btn_delete_lower_1 = QPushButton(self.frame_inter_delet_bar_3)
        self.btn_delete_lower_1.setObjectName(u"btn_delete_lower_1")
        self.btn_delete_lower_1.setMinimumSize(QSize(100, 25))
        self.btn_delete_lower_1.setMaximumSize(QSize(100, 40))
        self.btn_delete_lower_1.setFont(font4)

        self.horizontalLayout_14.addWidget(self.btn_delete_lower_1)

        self.verticalLayout_21.addWidget(self.frame_inter_delet_bar_3)

        self.verticalLayout_13.addWidget(self.widget_lower_1)

        self.widget_lower_pri = QWidget(self.page_content_Input)
        self.widget_lower_pri.setObjectName(u"widget_lower_pri")
        self.widget_lower_pri.setMinimumSize(QSize(0, 500))
        self.setShadowEffect(self.widget_lower_pri)
        self.verticalLayout_pri = QVBoxLayout(self.widget_lower_pri)
        self.verticalLayout_pri.setObjectName(u"verticalLayout_pri")

        self.label_info_pri_face = QLabel(self.widget_lower_1)
        self.label_info_pri_face.setObjectName(u"label_info_pri_face")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_pri_face.setMinimumSize(150, 150)
        self.label_info_pri_face.setMaximumSize(150, 150)
        self.label_info_pri_face.setFont(font2)
        self.setShadowEffect(self.label_info_pri_face)

        self.verticalLayout_pri.addWidget(
            self.label_info_pri_face, 0, Qt.AlignCenter)

        self.label_info_lower_pri = QLabel(self.widget_lower_pri)
        self.label_info_lower_pri.setObjectName(u"label_info_lower_pri")
        self.label_info_lower_pri.setFont(font2)

        self.verticalLayout_pri.addWidget(self.label_info_lower_pri)

        self.frame_inter_delet_bar_pri = QFrame(self.widget_lower_pri)
        self.frame_inter_delet_bar_pri.setObjectName(
            u"frame_inter_delet_bar_pri")
        self.frame_inter_delet_bar_pri.setMaximumSize(QSize(16777215, 40))
        self.setShadowEffect(self.frame_inter_delet_bar_pri)
        self.frame_inter_delet_bar_pri.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_delet_bar_pri.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_pri = QHBoxLayout(self.frame_inter_delet_bar_pri)
        self.horizontalLayout_pri.setObjectName(u"horizontalLayout_pri")
        self.label_info_user_lower_pri = QLabel(self.frame_inter_delet_bar_pri)
        self.label_info_user_lower_pri.setObjectName(
            u"label_info_user_lower_pri")
        self.label_info_user_lower_pri.setFont(font3)
        self.label_info_user_lower_pri.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_pri.addWidget(self.label_info_user_lower_pri)

        self.btn_delete_lower_pri = QPushButton(self.frame_inter_delet_bar_pri)
        self.btn_delete_lower_pri.setObjectName(u"btn_delete_lower_pri")
        self.btn_delete_lower_pri.setMinimumSize(QSize(100, 25))
        self.btn_delete_lower_pri.setMaximumSize(QSize(100, 40))
        self.btn_delete_lower_pri.setFont(font4)

        self.horizontalLayout_pri.addWidget(self.btn_delete_lower_pri)

        self.verticalLayout_pri.addWidget(self.frame_inter_delet_bar_pri)

        self.verticalLayout_13.addWidget(self.widget_lower_pri)

        self.widget_lower_advan = QWidget(self.page_content_Input)
        self.widget_lower_advan.setObjectName(u"widget_lower_advan")
        self.widget_lower_advan.setMinimumSize(QSize(0, 500))
        self.setShadowEffect(self.widget_lower_advan)
        self.verticalLayout_advan = QVBoxLayout(self.widget_lower_advan)
        self.verticalLayout_advan.setObjectName(u"verticalLayout_advan")

        self.label_info_advan_face = QLabel(self.widget_lower_1)
        self.label_info_advan_face.setObjectName(u"label_info_advan_face")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_advan_face.setMinimumSize(150, 150)
        self.label_info_advan_face.setMaximumSize(150, 150)
        self.label_info_advan_face.setFont(font2)
        self.setShadowEffect(self.label_info_advan_face)

        self.verticalLayout_advan.addWidget(
            self.label_info_advan_face, 0, Qt.AlignCenter)

        self.label_info_lower_advan = QLabel(self.widget_lower_advan)
        self.label_info_lower_advan.setObjectName(u"label_info_lower_advan")
        self.label_info_lower_advan.setFont(font2)

        self.verticalLayout_advan.addWidget(self.label_info_lower_advan)

        self.frame_inter_delet_bar_advan = QFrame(self.widget_lower_advan)
        self.frame_inter_delet_bar_advan.setObjectName(
            u"frame_inter_delet_bar_advan")
        self.frame_inter_delet_bar_advan.setMaximumSize(QSize(16777215, 40))
        self.setShadowEffect(self.frame_inter_delet_bar_advan)
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
        self.label_info_user_lower_advan.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_advan.addWidget(self.label_info_user_lower_advan)

        self.btn_delete_lower_advan = QPushButton(
            self.frame_inter_delet_bar_advan)
        self.btn_delete_lower_advan.setObjectName(u"btn_delete_lower_advan")
        self.btn_delete_lower_advan.setMinimumSize(QSize(100, 25))
        self.btn_delete_lower_advan.setMaximumSize(QSize(100, 40))
        self.btn_delete_lower_advan.setFont(font4)

        self.horizontalLayout_advan.addWidget(self.btn_delete_lower_advan)

        self.verticalLayout_advan.addWidget(self.frame_inter_delet_bar_advan)

        self.verticalLayout_13.addWidget(self.widget_lower_advan)

        self.scrollArea.setWidget(self.page_content_Input)

        self.verticalLayout_31.addWidget(self.scrollArea)

        self.verticalLayout_6.addWidget(self.frame_main_home_bar)

        self.stackedWidget.addWidget(self.Home)
        self.page_left = QWidget()
        self.page_left.setObjectName(u"page_left")
        self.verticalLayout_7 = QVBoxLayout(self.page_left)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_main_left_bar = QFrame(self.page_left)
        self.frame_main_left_bar.setObjectName(u"frame_main_left_bar")
        self.frame_main_left_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_left_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_main_left_bar)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.scrollArea_2 = QScrollArea(self.frame_main_left_bar)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 753, 1636))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_inter_left_1 = QWidget(self.scrollAreaWidgetContents)
        self.widget_inter_left_1.setObjectName(u"widget_inter_left_1")
        self.widget_inter_left_1.setMinimumSize(QSize(0, 500))
        self.setShadowEffect(self.widget_inter_left_1)
        self.verticalLayout_15 = QVBoxLayout(self.widget_inter_left_1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")

        self.label_info_inter_left_face = QLabel(self.widget_inter_left_1)
        self.label_info_inter_left_face.setObjectName(
            u"label_info_inter_left_face")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_inter_left_face.setMinimumSize(150, 150)
        self.label_info_inter_left_face.setMaximumSize(150, 150)
        self.label_info_inter_left_face.setFont(font2)
        self.setShadowEffect(self.label_info_inter_left_face)

        self.verticalLayout_15.addWidget(
            self.label_info_inter_left_face, 0, Qt.AlignCenter)

        self.info_inter_left_1 = QLabel(self.widget_inter_left_1)
        self.info_inter_left_1.setObjectName(u"info_inter_left_1")
        self.info_inter_left_1.setFont(font2)
        self.info_inter_left_1.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.info_inter_left_1)

        self.frame_inter_left_btns_bar_1 = QFrame(self.widget_inter_left_1)
        self.frame_inter_left_btns_bar_1.setObjectName(
            u"frame_inter_left_btns_bar_1")
        self.frame_inter_left_btns_bar_1.setMinimumSize(QSize(0, 0))
        self.frame_inter_left_btns_bar_1.setMaximumSize(QSize(16777215, 40))
        self.setShadowEffect(self.frame_inter_left_btns_bar_1)
        self.frame_inter_left_btns_bar_1.setFrameShape(QFrame.StyledPanel)
        self.frame_inter_left_btns_bar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_inter_left_btns_bar_1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_info_user_left_inter_1 = QLabel(
            self.frame_inter_left_btns_bar_1)
        self.label_info_user_left_inter_1.setObjectName(
            u"label_info_user_left_inter_1")
        font5 = QFont()
        font5.setFamily(u"./src/font/segoeui.ttf")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_info_user_left_inter_1.setFont(font5)
        self.label_info_user_left_inter_1.setAlignment(Qt.AlignLeft)

        self.horizontalLayout_8.addWidget(self.label_info_user_left_inter_1)

        self.btn_delete_inter_left_1 = QPushButton(
            self.frame_inter_left_btns_bar_1)
        self.btn_delete_inter_left_1.setObjectName(u"btn_delete_inter_left_1")
        self.btn_delete_inter_left_1.setMinimumSize(QSize(0, 25))
        self.btn_delete_inter_left_1.setMaximumSize(QSize(100, 40))
        self.btn_delete_inter_left_1.setFont(font4)

        self.horizontalLayout_8.addWidget(self.btn_delete_inter_left_1)

        self.verticalLayout_15.addWidget(self.frame_inter_left_btns_bar_1)

        self.verticalLayout_14.addWidget(self.widget_inter_left_1)

        self.widget_lower_left_1 = QWidget(self.scrollAreaWidgetContents)
        self.widget_lower_left_1.setObjectName(u"widget_lower_left_1")
        self.widget_lower_left_1.setMinimumSize(QSize(0, 500))
        self.setShadowEffect(self.widget_lower_left_1)
        self.verticalLayout_18 = QVBoxLayout(self.widget_lower_left_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.label_info_lower_left_face = QLabel(self.widget_lower_left_1)
        self.label_info_lower_left_face.setObjectName(
            u"label_info_lower_left_face")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_lower_left_face.setMinimumSize(150, 150)
        self.label_info_lower_left_face.setMaximumSize(150, 150)
        self.label_info_lower_left_face.setFont(font2)
        self.setShadowEffect(self.label_info_lower_left_face)

        self.verticalLayout_18.addWidget(
            self.label_info_lower_left_face, 0, Qt.AlignCenter)

        self.info_lower_1 = QLabel(self.widget_lower_left_1)
        self.info_lower_1.setObjectName(u"info_lower_1")
        self.info_lower_1.setFont(font2)
        self.info_lower_1.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.info_lower_1)

        self.frame_lower_left_btns_bar_1 = QFrame(self.widget_lower_left_1)
        self.frame_lower_left_btns_bar_1.setObjectName(
            u"frame_lower_left_btns_bar_1")
        self.frame_lower_left_btns_bar_1.setMaximumSize(QSize(16777215, 40))
        self.setShadowEffect(self.frame_lower_left_btns_bar_1)
        self.frame_lower_left_btns_bar_1.setFrameShape(QFrame.StyledPanel)
        self.frame_lower_left_btns_bar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(
            self.frame_lower_left_btns_bar_1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_info_user_left_lower_1 = QLabel(
            self.frame_lower_left_btns_bar_1)
        self.label_info_user_left_lower_1.setObjectName(
            u"label_info_user_left_lower_1")
        self.label_info_user_left_lower_1.setAlignment(Qt.AlignLeft)
        self.label_info_user_left_lower_1.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_info_user_left_lower_1)

        self.btn_delete_lower_left_1 = QPushButton(
            self.frame_lower_left_btns_bar_1)
        self.btn_delete_lower_left_1.setObjectName(u"btn_delete_lower_left_1")
        self.btn_delete_lower_left_1.setMinimumSize(QSize(0, 25))
        self.btn_delete_lower_left_1.setMaximumSize(QSize(100, 25))
        self.btn_delete_lower_left_1.setFont(font4)

        self.horizontalLayout_10.addWidget(self.btn_delete_lower_left_1)

        self.verticalLayout_18.addWidget(self.frame_lower_left_btns_bar_1)

        self.verticalLayout_14.addWidget(self.widget_lower_left_1)

        self.widget_lower_left_pri = QWidget(self.scrollAreaWidgetContents)
        self.widget_lower_left_pri.setObjectName(u"widget_lower_left_pri")
        self.widget_lower_left_pri.setMinimumSize(QSize(0, 500))
        self.setShadowEffect(self.widget_lower_left_pri)
        self.verticalLayout_pri = QVBoxLayout(self.widget_lower_left_pri)
        self.verticalLayout_pri.setObjectName(u"verticalLayout_pri")

        self.label_info_pri_left_face = QLabel(self.widget_lower_left_pri)
        self.label_info_pri_left_face.setObjectName(
            u"label_info_pri_left_face")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_pri_left_face.setMinimumSize(150, 150)
        self.label_info_pri_left_face.setMaximumSize(150, 150)
        self.label_info_pri_left_face.setFont(font2)
        self.setShadowEffect(self.label_info_pri_left_face)

        self.verticalLayout_pri.addWidget(
            self.label_info_pri_left_face, 0, Qt.AlignCenter)

        self.info_lower_left_pri = QLabel(self.widget_lower_left_pri)
        self.info_lower_left_pri.setObjectName(u"info_lower_pri")
        self.info_lower_left_pri.setFont(font2)

        self.info_lower_left_pri.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_pri.addWidget(self.info_lower_left_pri)

        self.frame_lower_btns_bar_pri = QFrame(self.widget_lower_left_pri)
        self.frame_lower_btns_bar_pri.setObjectName(
            u"frame_lower_btns_bar_pri")
        self.frame_lower_btns_bar_pri.setMaximumSize(QSize(16777215, 40))
        self.setShadowEffect(self.frame_lower_btns_bar_pri)
        self.frame_lower_btns_bar_pri.setFrameShape(QFrame.StyledPanel)
        self.frame_lower_btns_bar_pri.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_pri = QHBoxLayout(self.frame_lower_btns_bar_pri)
        self.horizontalLayout_pri.setObjectName(u"horizontalLayout_pri")
        self.label_info_user_left_lower_pri = QLabel(
            self.frame_lower_btns_bar_pri)
        self.label_info_user_left_lower_pri.setObjectName(
            u"label_info_user_left_lower_pri")
        self.label_info_user_left_lower_pri.setAlignment(Qt.AlignLeft)
        self.label_info_user_left_lower_pri.setFont(font5)

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

        self.horizontalLayout_pri.addWidget(self.btn_delete_lower_left_pri)

        self.verticalLayout_pri.addWidget(self.frame_lower_btns_bar_pri)

        self.verticalLayout_14.addWidget(self.widget_lower_left_pri)

        self.widget_lower_left_advan = QWidget(self.scrollAreaWidgetContents)
        self.widget_lower_left_advan.setObjectName(u"widget_lower_left_advan")
        self.widget_lower_left_advan.setMinimumSize(QSize(0, 500))
        self.setShadowEffect(self.widget_lower_left_advan)
        self.verticalLayout_advan = QVBoxLayout(self.widget_lower_left_advan)
        self.verticalLayout_advan.setObjectName(u"verticalLayout_advan")

        self.label_info_advan_left_face = QLabel(self.widget_lower_left_advan)
        self.label_info_advan_left_face.setObjectName(
            u"label_info_advan_left_face")
        font2 = QFont()
        font2.setFamily(u"./src/font/segoeui.ttf")
        font2.setPointSize(10)
        self.label_info_advan_left_face.setMinimumSize(150, 150)
        self.label_info_advan_left_face.setMaximumSize(150, 150)
        self.label_info_advan_left_face.setFont(font2)
        self.setShadowEffect(self.label_info_advan_left_face)

        self.verticalLayout_advan.addWidget(
            self.label_info_advan_left_face, 0, Qt.AlignCenter)

        self.info_lower_left_advan = QLabel(self.widget_lower_left_advan)
        self.info_lower_left_advan.setObjectName(u"info_lower_advan")
        self.info_lower_left_advan.setFont(font2)
        self.info_lower_left_advan.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_advan.addWidget(self.info_lower_left_advan)

        self.frame_lower_btns_bar_advan = QFrame(self.widget_lower_left_advan)
        self.frame_lower_btns_bar_advan.setObjectName(
            u"frame_lower_btns_bar_advan")
        self.frame_lower_btns_bar_advan.setMaximumSize(QSize(16777215, 40))
        self.setShadowEffect(self.frame_lower_btns_bar_advan)
        self.frame_lower_btns_bar_advan.setFrameShape(QFrame.StyledPanel)
        self.frame_lower_btns_bar_advan.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_advan = QHBoxLayout(
            self.frame_lower_btns_bar_advan)
        self.horizontalLayout_advan.setObjectName(u"horizontalLayout_advan")
        self.label_info_user_left_lower_advan = QLabel(
            self.frame_lower_btns_bar_advan)
        self.label_info_user_left_lower_advan.setObjectName(
            u"label_info_user_left_lower_advan")
        self.label_info_user_left_lower_advan.setAlignment(Qt.AlignLeft)
        self.label_info_user_left_lower_advan.setFont(font5)

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

        self.horizontalLayout_advan.addWidget(self.btn_delete_lower_left_advan)

        self.verticalLayout_advan.addWidget(self.frame_lower_btns_bar_advan)

        self.verticalLayout_14.addWidget(self.widget_lower_left_advan)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_30.addWidget(self.scrollArea_2)

        self.verticalLayout_7.addWidget(self.frame_main_left_bar)

        self.stackedWidget.addWidget(self.page_left)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.verticalLayout_8 = QVBoxLayout(self.page_search)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_main_search_bar = QFrame(self.page_search)
        self.frame_main_search_bar.setObjectName(u"frame_main_search_bar")
        self.frame_main_search_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_search_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_main_search_bar)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 16, -1, -1)
        self.frame_searching_main = QFrame(self.frame_main_search_bar)
        self.frame_searching_main.setObjectName(u"frame_searching_main")
        self.frame_searching_main.setMinimumSize(QSize(0, 0))
        self.frame_searching_main.setMaximumSize(QSize(16777215, 200))
        self.setShadowEffect(self.frame_searching_main)
        self.frame_searching_main.setFrameShape(QFrame.StyledPanel)
        self.frame_searching_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_searching_main)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_title_search = QFrame(self.frame_searching_main)
        self.frame_title_search.setObjectName(u"frame_title_search")
        self.frame_title_search.setFrameShape(QFrame.StyledPanel)
        self.frame_title_search.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_title_search)

        self.frame_search_bar_itmes = QFrame(self.frame_searching_main)
        self.frame_search_bar_itmes.setObjectName(u"frame_search_bar_itmes")
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
        font8.setFamily(u"./src/font/segoeui.ttf")
        font8.setPointSize(10)
        self.lineEdit_nameSearch.setFont(font8)

        self.gridLayout.addWidget(self.lineEdit_nameSearch, 0, 0, 1, 1)

        self.btn_nameSearch = QPushButton(self.frame_search_bar_itmes)
        self.btn_nameSearch.setObjectName(u"btn_nameSearch")
        self.btn_nameSearch.setMinimumSize(QSize(100, 25))
        self.btn_nameSearch.setMaximumSize(QSize(16777215, 25))

        self.btn_nameSearch.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_nameSearch, 0, 1, 1, 1)

        self.lineEdit_rollSearch = QLineEdit(self.frame_search_bar_itmes)
        self.lineEdit_rollSearch.setClearButtonEnabled(True)
        self.lineEdit_rollSearch.setObjectName(u"lineEdit_rollSearch")
        self.lineEdit_rollSearch.setMinimumSize(QSize(200, 30))
        self.lineEdit_rollSearch.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_rollSearch.setFont(font2)
        self.gridLayout.addWidget(self.lineEdit_rollSearch, 1, 0, 1, 1)

        self.btn_rollSearch = QPushButton(self.frame_search_bar_itmes)
        self.btn_rollSearch.setObjectName(u"btn_rollSearch")
        self.btn_rollSearch.setMinimumSize(QSize(100, 25))
        self.btn_rollSearch.setMaximumSize(QSize(16777215, 25))

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
        self.verticalLayout_11 = QVBoxLayout(self.page_setting)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_main_setting_bar = QFrame(self.page_setting)
        self.frame_main_setting_bar.setObjectName(u"frame_main_setting_bar")
        self.frame_main_setting_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_setting_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_main_setting_bar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame = QFrame(self.frame_main_setting_bar)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_28 = QVBoxLayout(self.frame)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label = QLabel(self.frame)
        self.label.setMinimumSize(QSize(200, 200))
        self.label.setMaximumSize(QSize(200, 200))
        self.setShadowEffect(self.label)
        self.label.setObjectName("label")
        self.verticalLayout_28.addWidget(self.label, 0, Qt.AlignHCenter)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea_3 = QScrollArea(self.frame_3)
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
        self.setShadowEffect(self.frame_user_name_changer)
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
        self.label_username_title.setObjectName("label_username_title")
        self.horizontalLayout_5.addWidget(self.label_username_title)
        self.btn_hidden_username_bar = QPushButton(
            self.frame_name_changer_title_bar)
        self.btn_hidden_username_bar.setMinimumSize(QSize(30, 30))
        self.btn_hidden_username_bar.setMaximumSize(QSize(30, 30))
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
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        self.lineEdit_username_change_input.setFont(font)
        self.lineEdit_username_change_input.setObjectName(
            "lineEdit_username_change_input")
        self.horizontalLayout_18.addWidget(self.lineEdit_username_change_input)
        self.btn_save_username = QPushButton(
            self.frame_name_changer_content_page)
        self.btn_save_username.setMinimumSize(QSize(100, 30))
        self.btn_save_username.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_username.setFont(font)
        self.btn_save_username.setObjectName("btn_save_username")

        self.frame_more_options = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_more_options.setMinimumSize(QSize(0, 50))
        self.setShadowEffect(self.frame_more_options)
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
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_24.addWidget(self.label_title)
        self.btn_hidden_options = QPushButton(self.frame_title_of_more_options)
        self.btn_hidden_options.setMinimumSize(QSize(30, 30))
        self.btn_hidden_options.setMaximumSize(QSize(30, 30))
        self.btn_hidden_options.setText("")
        self.btn_hidden_options.setObjectName("btn_hidden_options")
        self.horizontalLayout_24.addWidget(self.btn_hidden_options)
        self.verticalLayout_41.addWidget(self.frame_title_of_more_options)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
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
        self.label_reload_info.setObjectName("label_reload_info")
        self.verticalLayout_42.addWidget(self.label_reload_info)
        self.btn_reload = QPushButton(self.frame_more_options_contect_bar)
        self.btn_reload.setMinimumSize(QSize(0, 30))
        self.btn_reload.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reload.setFont(font)
        self.btn_reload.setObjectName("btn_reload")
        self.verticalLayout_42.addWidget(self.btn_reload)
        self.label_reset_info = QLabel(self.frame_more_options_contect_bar)
        self.label_reset_info.setObjectName("label_reset_info")
        self.verticalLayout_42.addWidget(self.label_reset_info)
        self.btn_reset = QPushButton(self.frame_more_options_contect_bar)
        self.btn_reset.setMinimumSize(QSize(0, 30))
        self.btn_reset.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
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
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.verticalLayout_42.addWidget(self.btn_logout)

        self.frame_setTheme = QFrame(self.frame_more_options)
        self.frame_setTheme.setFrameShape(QFrame.StyledPanel)
        self.frame_setTheme.setFrameShadow(QFrame.Raised)
        self.frame_setTheme.setObjectName("frame_setTheme")
        self.verticalLayout_58 = QVBoxLayout(self.frame_setTheme)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.label_theme_set_info = QLabel(self.frame_setTheme)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(15)
        self.label_theme_set_info.setFont(font)
        self.label_theme_set_info.setObjectName("label_theme_set_info")
        self.verticalLayout_58.addWidget(self.label_theme_set_info)
        self.comboBox_theme_items = QComboBox(self.frame_setTheme)
        self.comboBox_theme_items.setObjectName("comboBox_theme_items")
        self.comboBox_theme_items.setMinimumSize(QSize(30, 30))
        self.comboBox_theme_items.addItem("")
        self.comboBox_theme_items.addItem("")
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(12)
        self.comboBox_theme_items.setFont(font)
        self.verticalLayout_58.addWidget(self.comboBox_theme_items)
        self.btn_setTheme = QPushButton(self.frame_setTheme)
        self.btn_setTheme.setObjectName("btn_setTheme")
        self.btn_setTheme.setMinimumSize(QSize(30, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        font.setBold(True)
        self.btn_setTheme.setFont(font)
        self.verticalLayout_58.addWidget(self.btn_setTheme)
        self.horizontalLayout_27.addWidget(self.frame_setTheme)
        self.horizontalLayout_27.addWidget(self.frame_more_options_contect_bar)
        self.verticalLayout_41.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_18.addWidget(self.btn_save_username)
        self.verticalLayout_37.addLayout(self.horizontalLayout_18)
        self.verticalLayout_33.addWidget(self.frame_name_changer_content_page)
        self.verticalLayout_32.addWidget(self.frame_user_name_changer)
        self.frame_email_changer = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_email_changer.setMinimumSize(QSize(0, 45))
        self.frame_email_changer.setMaximumSize(QSize(16777215, 45))
        self.setShadowEffect(self.frame_email_changer)
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
        self.label_change_email_title.setObjectName("label_change_email_title")
        self.horizontalLayout_19.addWidget(self.label_change_email_title)
        self.btn_hidden_email_bar = QPushButton(
            self.frame_email_changer_title_bar)
        self.btn_hidden_email_bar.setMinimumSize(QSize(30, 30))
        self.btn_hidden_email_bar.setMaximumSize(QSize(22, 30))
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
        self.label_current_email.setObjectName("label_current_email")
        self.verticalLayout_38.addWidget(self.label_current_email)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lineEdit_change_email_input = QLineEdit(
            self.frame_email_changer_content_bar)
        self.lineEdit_change_email_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_change_email_input.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        self.lineEdit_change_email_input.setFont(font)
        self.lineEdit_change_email_input.setObjectName(
            "lineEdit_change_email_input")
        self.horizontalLayout_20.addWidget(self.lineEdit_change_email_input)
        self.btn_save_change_email = QPushButton(
            self.frame_email_changer_content_bar)
        self.btn_save_change_email.setMinimumSize(QSize(100, 30))
        self.btn_save_change_email.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_change_email.setFont(font)
        self.btn_save_change_email.setObjectName("btn_save_change_email")
        self.horizontalLayout_20.addWidget(self.btn_save_change_email)
        self.verticalLayout_38.addLayout(self.horizontalLayout_20)
        self.verticalLayout_34.addWidget(self.frame_email_changer_content_bar)
        self.verticalLayout_32.addWidget(self.frame_email_changer)
        self.frame_contect_number_changer = QFrame(
            self.scrollAreaWidgetContents_3)
        self.frame_contect_number_changer.setMinimumSize(QSize(0, 45))
        self.frame_contect_number_changer.setMaximumSize(QSize(16777215, 45))
        self.setShadowEffect(self.frame_contect_number_changer)
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
        self.label_change_contact_number_title.setObjectName(
            "label_change_contact_number_title")
        self.horizontalLayout_21.addWidget(
            self.label_change_contact_number_title)
        self.btn_hidden_contact_number_bar = QPushButton(
            self.frame_contect_number_changer_title_bar)
        self.btn_hidden_contact_number_bar.setMinimumSize(QSize(30, 30))
        self.btn_hidden_contact_number_bar.setMaximumSize(QSize(30, 30))
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
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        self.lineEdit_contact_number_input.setFont(font)
        self.lineEdit_contact_number_input.setObjectName(
            "lineEdit_contact_number_input")
        self.horizontalLayout_22.addWidget(self.lineEdit_contact_number_input)
        self.btn_save_contact_number = QPushButton(
            self.frame_contect_number_changer_content_bar)
        self.btn_save_contact_number.setMinimumSize(QSize(100, 30))
        self.btn_save_contact_number.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_contact_number.setFont(font)
        self.btn_save_contact_number.setObjectName("btn_save_contact_number")
        self.horizontalLayout_22.addWidget(self.btn_save_contact_number)
        self.verticalLayout_39.addLayout(self.horizontalLayout_22)
        self.verticalLayout_35.addWidget(
            self.frame_contect_number_changer_content_bar)
        self.verticalLayout_32.addWidget(self.frame_contect_number_changer)
        self.frame_password_changer = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_password_changer.setMinimumSize(QSize(0, 45))
        self.frame_password_changer.setMaximumSize(QSize(16777215, 45))
        self.setShadowEffect(self.frame_password_changer)
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
        self.label_change_password_title.setObjectName(
            "label_change_password_title")
        self.horizontalLayout_23.addWidget(self.label_change_password_title)
        self.btn_hidden_passowd_changer_bar = QPushButton(
            self.frame_password_changer_title_bar)
        self.btn_hidden_passowd_changer_bar.setMinimumSize(QSize(30, 30))
        self.btn_hidden_passowd_changer_bar.setMaximumSize(QSize(30, 30))
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
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_passord_input.setFont(font)
        self.lineEdit_passord_input.setObjectName("lineEdit_passord_input")
        self.verticalLayout_40.addWidget(self.lineEdit_passord_input)
        self.lineEdit_repassword_input = QLineEdit(
            self.frame_password_changer_content_bar)
        self.lineEdit_repassword_input.setMinimumSize(QSize(0, 30))
        self.lineEdit_repassword_input.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_repassword_input.setEchoMode(QLineEdit.Password)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        self.lineEdit_repassword_input.setFont(font)
        self.lineEdit_repassword_input.setObjectName(
            "lineEdit_repassword_input")
        self.verticalLayout_40.addWidget(self.lineEdit_repassword_input)
        self.btn_save_password = QPushButton(
            self.frame_password_changer_content_bar)
        self.btn_save_password.setMinimumSize(QSize(0, 30))
        self.btn_save_password.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_password.setFont(font)

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

        font11 = QFont()
        font11.setFamily(u"./src/font/segoeui.ttf")
        font11.setPointSize(11)
        font11.setBold(False)
        font11.setWeight(50)

        font10 = QFont()
        font10.setFamily(u"./src/font/segoeui.ttf")
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setWeight(50)

        self.page_add_inter_none = QWidget()
        self.page_add_inter_none.setObjectName("page_add_inter_none")
        self.verticalLayout_54 = QVBoxLayout(self.page_add_inter_none)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.frame_main_inter_info_inter_teache_none = QFrame(
            self.page_add_inter_none)
        self.frame_main_inter_info_inter_teache_none.setMinimumSize(
            QSize(0, 0))
        self.frame_main_inter_info_inter_teache_none.setFrameShape(
            QFrame.StyledPanel)
        self.frame_main_inter_info_inter_teache_none.setFrameShadow(
            QFrame.Raised)
        self.frame_main_inter_info_inter_teache_none.setObjectName(
            "frame_main_inter_info_inter_teache_none")
        self.verticalLayout_53 = QVBoxLayout(
            self.frame_main_inter_info_inter_teache_none)
        self.verticalLayout_53.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.frame_content_inter_teacher_none = QFrame(
            self.frame_main_inter_info_inter_teache_none)
        self.frame_content_inter_teacher_none.setMinimumSize(QSize(0, 0))
        self.frame_content_inter_teacher_none.setFrameShape(QFrame.StyledPanel)
        self.frame_content_inter_teacher_none.setFrameShadow(QFrame.Raised)
        self.frame_content_inter_teacher_none.setObjectName(
            "frame_content_inter_teacher_none")
        self.gridLayout_10 = QGridLayout(self.frame_content_inter_teacher_none)
        self.gridLayout_10.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_show_roll_number_none = QLabel(
            self.frame_content_inter_teacher_none)
        self.label_show_roll_number_none.setMinimumSize(QSize(0, 30))
        self.label_show_roll_number_none.setMaximumSize(QSize(16777215, 30))
        self.label_show_roll_number_none.setObjectName(
            "label_show_roll_number_none")
        self.gridLayout_10.addWidget(
            self.label_show_roll_number_none, 1, 0, 1, 2)
        self.horizontalLayout_inter_none = QHBoxLayout()
        self.horizontalLayout_inter_none.setObjectName(
            "horizontalLayout_inter_none")
        self.btn_addInter_teacher_none = QPushButton(
            self.frame_content_inter_teacher_none)
        self.btn_addInter_teacher_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addInter_teacher_none.setFont(font)
        self.btn_addInter_teacher_none.setObjectName(
            "btn_addInter_teacher_none")
        self.horizontalLayout_inter_none.addWidget(
            self.btn_addInter_teacher_none)
        self.btn_go_inter_teacher_none = QPushButton(
            self.frame_content_inter_teacher_none)
        self.btn_go_inter_teacher_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_go_inter_teacher_none.setFont(font)
        self.btn_go_inter_teacher_none.setObjectName(
            "btn_go_inter_teacher_none")
        self.horizontalLayout_inter_none.addWidget(
            self.btn_go_inter_teacher_none)
        self.gridLayout_10.addLayout(
            self.horizontalLayout_inter_none, 2, 0, 1, 2)
        self.scrollArea_add_info_none = QScrollArea(
            self.frame_content_inter_teacher_none)
        self.scrollArea_add_info_none.setWidgetResizable(True)
        self.scrollArea_add_info_none.setObjectName("scrollArea_add_info_none")
        self.scrollAreaWidgetInfo_none = QWidget()
        self.scrollAreaWidgetInfo_none.setGeometry(QRect(0, 0, 835, 1000))
        self.scrollAreaWidgetInfo_none.setMinimumSize(QSize(0, 1000))
        self.scrollAreaWidgetInfo_none.setObjectName(
            "scrollAreaWidgetInfo_none")
        self.verticalLayout_55 = QVBoxLayout(self.scrollAreaWidgetInfo_none)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.frame_user_image_upload_inter_teacher_none = QFrame(
            self.scrollAreaWidgetInfo_none)
        self.frame_user_image_upload_inter_teacher_none.setMaximumSize(
            QSize(16777215, 300))
        self.frame_user_image_upload_inter_teacher_none.setFrameShape(
            QFrame.StyledPanel)
        self.frame_user_image_upload_inter_teacher_none.setFrameShadow(
            QFrame.Raised)
        self.frame_user_image_upload_inter_teacher_none.setObjectName(
            "frame_user_image_upload_inter_teacher_none")
        self.gridLayout_9 = QGridLayout(
            self.frame_user_image_upload_inter_teacher_none)
        self.gridLayout_9.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_9.setSpacing(10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_icon_none = QLabel(
            self.frame_user_image_upload_inter_teacher_none)
        self.label_icon_none.setMinimumSize(QSize(200, 200))
        self.label_icon_none.setMaximumSize(QSize(200, 200))
        self.label_icon_none.setObjectName("label_icon_none")
        self.setShadowEffect(self.label_icon_none)
        self.gridLayout_9.addWidget(self.label_icon_none, 0, 0, 1, 1)
        self.btn_upload_image_inter_teacher_none = QPushButton(
            self.frame_user_image_upload_inter_teacher_none)
        self.btn_upload_image_inter_teacher_none.setMinimumSize(QSize(0, 25))
        self.btn_upload_image_inter_teacher_none.setMaximumSize(QSize(300, 25))
        self.btn_upload_image_inter_teacher_none.setObjectName(
            "btn_upload_image_inter_teacher_none")
        self.gridLayout_9.addWidget(
            self.btn_upload_image_inter_teacher_none, 1, 0, 1, 1)
        self.verticalLayout_55.addWidget(
            self.frame_user_image_upload_inter_teacher_none)
        self.groupBox_lineedit_info_none = QGroupBox(
            self.scrollAreaWidgetInfo_none)
        self.groupBox_lineedit_info_none.setTitle("")
        self.groupBox_lineedit_info_none.setObjectName(
            "groupBox_lineedit_info_none")
        self.gridLayout_13 = QGridLayout(self.groupBox_lineedit_info_none)
        self.gridLayout_13.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_13.setSpacing(10)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lineEdit_email_id_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit_email_id_none.setMinimumSize(QSize(0, 30))
        self.lineEdit_email_id_none.setObjectName("lineEdit_email_id_none")
        self.gridLayout_13.addWidget(self.lineEdit_email_id_none, 2, 0, 1, 1)
        self.lineEdit_educational_qualif_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit_educational_qualif_none.setMinimumSize(QSize(0, 30))
        self.lineEdit_educational_qualif_none.setObjectName(
            "lineEdit_educational_qualif_none")
        self.gridLayout_13.addWidget(
            self.lineEdit_educational_qualif_none, 5, 0, 1, 1)
        self.lineEdit_personal_contact_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit_personal_contact_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_personal_contact_none.setFont(font)
        self.lineEdit_personal_contact_none.setObjectName(
            "lineEdit_personal_contact_none")
        self.gridLayout_13.addWidget(
            self.lineEdit_personal_contact_none, 1, 1, 1, 1)
        self.lineEdit_professional_qualif_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit_professional_qualif_none.setMinimumSize(QSize(0, 30))
        self.lineEdit_professional_qualif_none.setObjectName(
            "lineEdit_professional_qualif_none")
        self.gridLayout_13.addWidget(
            self.lineEdit_professional_qualif_none, 6, 0, 1, 1)
        self.lineEdit_full_name_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit_full_name_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_full_name_none.setFont(font)
        self.lineEdit_full_name_none.setToolTipDuration(4)
        self.lineEdit_full_name_none.setObjectName("lineEdit_full_name_none")
        self.gridLayout_13.addWidget(self.lineEdit_full_name_none, 0, 0, 1, 1)
        self.lineEdit__name_initial_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit__name_initial_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit__name_initial_none.setFont(font)
        self.lineEdit__name_initial_none.setObjectName(
            "lineEdit__name_initial_none")
        self.gridLayout_13.addWidget(
            self.lineEdit__name_initial_none, 0, 1, 1, 1)
        self.lineEdit_WOP_no_none = QLineEdit(self.groupBox_lineedit_info_none)
        self.lineEdit_WOP_no_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_WOP_no_none.setFont(font)
        self.lineEdit_WOP_no_none.setObjectName("lineEdit_WOP_no_none")
        self.gridLayout_13.addWidget(self.lineEdit_WOP_no_none, 2, 1, 1, 1)
        self.lineEdit_spouse_name_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit_spouse_name_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_spouse_name_none.setFont(font)
        self.lineEdit_spouse_name_none.setObjectName(
            "lineEdit_spouse_name_none")
        self.gridLayout_13.addWidget(
            self.lineEdit_spouse_name_none, 3, 1, 1, 1)
        self.lineEdit_agrakara_no_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit_agrakara_no_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_agrakara_no_none.setFont(font)
        self.lineEdit_agrakara_no_none.setObjectName(
            "lineEdit_agrakara_no_none")
        self.gridLayout_13.addWidget(
            self.lineEdit_agrakara_no_none, 3, 0, 1, 1)
        self.lineEdit_inc_no_none = QLineEdit(self.groupBox_lineedit_info_none)
        self.lineEdit_inc_no_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_inc_no_none.setFont(font)
        self.lineEdit_inc_no_none.setObjectName("lineEdit_inc_no_none")
        self.gridLayout_13.addWidget(self.lineEdit_inc_no_none, 1, 0, 1, 1)
        self.lineEdit_nature_of_appoin_none = QLineEdit(
            self.groupBox_lineedit_info_none)
        self.lineEdit_nature_of_appoin_none.setMinimumSize(QSize(0, 30))
        self.lineEdit_nature_of_appoin_none.setMaximumSize(
            QSize(16777215, 16777215))
        self.lineEdit_nature_of_appoin_none.setSizeIncrement(QSize(0, 0))
        self.lineEdit_nature_of_appoin_none.setObjectName(
            "lineEdit_nature_of_appoin_none")
        self.gridLayout_13.addWidget(
            self.lineEdit_nature_of_appoin_none, 6, 1, 1, 1)
        self.lineEdit_salary_none = QLineEdit(self.groupBox_lineedit_info_none)
        self.lineEdit_salary_none.setMinimumSize(QSize(0, 30))
        self.lineEdit_salary_none.setObjectName("lineEdit_salary_none")
        self.gridLayout_13.addWidget(self.lineEdit_salary_none, 5, 1, 1, 1)
        self.verticalLayout_55.addWidget(self.groupBox_lineedit_info_none)
        self.groupBox_increment_date_none = QGroupBox(
            self.scrollAreaWidgetInfo_none)
        self.groupBox_increment_date_none.setMinimumSize(QSize(0, 70))
        self.groupBox_increment_date_none.setObjectName(
            "groupBox_increment_date_none")
        self.horizontalLayout_25 = QHBoxLayout(
            self.groupBox_increment_date_none)
        self.horizontalLayout_25.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.dateEdit_increment_date_none = QDateEdit(
            self.groupBox_increment_date_none)
        self.dateEdit_increment_date_none.setMinimumSize(QSize(0, 30))
        self.dateEdit_increment_date_none.setObjectName(
            "dateEdit_increment_date_none")
        self.horizontalLayout_25.addWidget(self.dateEdit_increment_date_none)
        self.verticalLayout_55.addWidget(self.groupBox_increment_date_none)
        self.horizontalLayout_34_none = QHBoxLayout()
        self.horizontalLayout_34_none.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_34_none.setSpacing(10)
        self.horizontalLayout_34_none.setObjectName("horizontalLayout_34_none")
        self.label_DOB_text_none = QLabel(self.scrollAreaWidgetInfo_none)
        self.label_DOB_text_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.label_DOB_text_none.setFont(font)
        self.label_DOB_text_none.setObjectName("label_DOB_text_none")
        self.horizontalLayout_34_none.addWidget(
            self.label_DOB_text_none, 0, Qt.AlignHCenter)
        self.label_appointment_data_text_none = QLabel(
            self.scrollAreaWidgetInfo_none)
        self.label_appointment_data_text_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.label_appointment_data_text_none.setFont(font)
        self.label_appointment_data_text_none.setObjectName(
            "label_appointment_data_text_none")
        self.horizontalLayout_34_none.addWidget(
            self.label_appointment_data_text_none, 0, Qt.AlignHCenter)
        self.verticalLayout_55.addLayout(self.horizontalLayout_34_none)
        self.horizontalLayout_33_none = QHBoxLayout()
        self.horizontalLayout_33_none.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33_none.setSpacing(10)
        self.horizontalLayout_33_none.setObjectName("horizontalLayout_33_none")
        self.dateEdit_DOB_none = QDateEdit(self.scrollAreaWidgetInfo_none)
        self.dateEdit_DOB_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.dateEdit_DOB_none.setFont(font)
        self.dateEdit_DOB_none.setObjectName("dateEdit_DOB_none")
        self.horizontalLayout_33_none.addWidget(self.dateEdit_DOB_none)
        self.dateEdit_first_appointment_date_none = QDateEdit(
            self.scrollAreaWidgetInfo_none)
        self.dateEdit_first_appointment_date_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.dateEdit_first_appointment_date_none.setFont(font)
        self.dateEdit_first_appointment_date_none.setObjectName(
            "dateEdit_first_appointment_date_none")
        self.horizontalLayout_33_none.addWidget(
            self.dateEdit_first_appointment_date_none)
        self.verticalLayout_55.addLayout(self.horizontalLayout_33_none)
        self.groupBox_address_none = QGroupBox(self.scrollAreaWidgetInfo_none)
        self.groupBox_address_none.setMaximumSize(QSize(16777215, 100))
        self.groupBox_address_none.setTitle("")
        self.groupBox_address_none.setObjectName("groupBox_address_none")
        self.gridLayout_14 = QGridLayout(self.groupBox_address_none)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.textEdit_working_address_none = QTextEdit(
            self.groupBox_address_none)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.textEdit_working_address_none.setFont(font)
        self.textEdit_working_address_none.setObjectName(
            "textEdit_working_address_none")
        self.gridLayout_14.addWidget(
            self.textEdit_working_address_none, 0, 0, 1, 1)
        self.textEdit_emergency_none = QTextEdit(self.groupBox_address_none)
        font = QFont()
        font.setPointSize(10)
        self.textEdit_emergency_none.setFont(font)
        self.textEdit_emergency_none.setObjectName("textEdit_emergency_none")
        self.gridLayout_14.addWidget(self.textEdit_emergency_none, 0, 1, 1, 1)
        self.verticalLayout_55.addWidget(self.groupBox_address_none)
        self.horizontalLayout_37_none = QHBoxLayout()
        self.horizontalLayout_37_none.setObjectName("horizontalLayout_37_none")
        self.label_date_app_to_school_text_none = QLabel(
            self.scrollAreaWidgetInfo_none)
        self.label_date_app_to_school_text_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.label_date_app_to_school_text_none.setFont(font)
        self.label_date_app_to_school_text_none.setObjectName(
            "label_date_app_to_school_text_none")
        self.horizontalLayout_37_none.addWidget(
            self.label_date_app_to_school_text_none, 0, Qt.AlignHCenter)
        self.verticalLayout_55.addLayout(self.horizontalLayout_37_none)
        self.horizontalLayout_38_none = QHBoxLayout()
        self.horizontalLayout_38_none.setObjectName("horizontalLayout_38_none")
        self.dateEdit_appointment_date_none = QDateEdit(
            self.scrollAreaWidgetInfo_none)
        self.dateEdit_appointment_date_none.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.dateEdit_appointment_date_none.setFont(font)
        self.dateEdit_appointment_date_none.setObjectName(
            "dateEdit_appointment_date_none")
        self.horizontalLayout_38_none.addWidget(
            self.dateEdit_appointment_date_none)
        self.verticalLayout_55.addLayout(self.horizontalLayout_38_none)
        self.horizontalLayout_40_none = QHBoxLayout()
        self.horizontalLayout_40_none.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40_none.setSpacing(6)
        self.horizontalLayout_40_none.setObjectName("horizontalLayout_40_none")
        self.groupBox_civil_none = QGroupBox(self.scrollAreaWidgetInfo_none)
        self.groupBox_civil_none.setObjectName("groupBox_civil_none")
        self.groupBox_civil_none.setMinimumSize(QSize(0, 70))
        self.gridLayout_15 = QGridLayout(self.groupBox_civil_none)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_15.setContentsMargins(10, 10, 10, 10)
        self.radioButton_married_none = QRadioButton(self.groupBox_civil_none)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_married_none.setFont(font)
        self.radioButton_married_none.setObjectName("radioButton_married_none")
        self.gridLayout_15.addWidget(
            self.radioButton_married_none, 0, 0, 1, 1, Qt.AlignCenter)
        self.radioButton_unmarried_none = QRadioButton(
            self.groupBox_civil_none)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_unmarried_none.setFont(font)
        self.radioButton_unmarried_none.setObjectName(
            "radioButton_unmarried_none")
        self.gridLayout_15.addWidget(
            self.radioButton_unmarried_none, 0, 1, 1, 1, Qt.AlignCenter)
        self.horizontalLayout_40_none.addWidget(self.groupBox_civil_none)
        self.groupBox_gender_none = QGroupBox(self.scrollAreaWidgetInfo_none)
        self.groupBox_gender_none.setObjectName("groupBox_gender_none")
        self.groupBox_gender_none.setMinimumSize(QSize(0, 70))
        self.gridLayout_16 = QGridLayout(self.groupBox_gender_none)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_16.setContentsMargins(10, 10, 10, 10)
        self.radioButton_other_none = QRadioButton(self.groupBox_gender_none)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_other_none.setFont(font)
        self.radioButton_other_none.setObjectName("radioButton_other_none")
        self.gridLayout_16.addWidget(
            self.radioButton_other_none, 0, 2, 1, 1, Qt.AlignCenter)
        self.radioButton_female_none = QRadioButton(self.groupBox_gender_none)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_female_none.setFont(font)
        self.radioButton_female_none.setObjectName("radioButton_female_none")
        self.gridLayout_16.addWidget(
            self.radioButton_female_none, 0, 1, 1, 1, Qt.AlignCenter)
        self.radioButton_male_none = QRadioButton(self.groupBox_gender_none)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_male_none.setFont(font)
        self.radioButton_male_none.setObjectName("radioButton_male_none")
        self.gridLayout_16.addWidget(
            self.radioButton_male_none, 0, 0, 1, 1, Qt.AlignCenter)
        self.horizontalLayout_40_none.addWidget(self.groupBox_gender_none)
        self.verticalLayout_55.addLayout(self.horizontalLayout_40_none)
        self.scrollArea_add_info_none.setWidget(self.scrollAreaWidgetInfo_none)
        self.gridLayout_10.addWidget(self.scrollArea_add_info_none, 0, 0, 1, 1)
        self.verticalLayout_53.addWidget(self.frame_content_inter_teacher_none)
        self.verticalLayout_54.addWidget(
            self.frame_main_inter_info_inter_teache_none)
        self.stackedWidget.addWidget(self.page_add_inter_none)

        self.page_add_inter = QWidget()
        self.page_add_inter.setObjectName("page_add_inter")
        self.verticalLayout_54 = QVBoxLayout(self.page_add_inter)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.frame_main_inter_info_inter_teacher = QFrame(self.page_add_inter)
        self.frame_main_inter_info_inter_teacher.setMinimumSize(QSize(0, 0))
        self.frame_main_inter_info_inter_teacher.setFrameShape(
            QFrame.StyledPanel)
        self.frame_main_inter_info_inter_teacher.setFrameShadow(QFrame.Raised)
        self.frame_main_inter_info_inter_teacher.setObjectName(
            "frame_main_inter_info_inter_teacher")
        self.verticalLayout_53 = QVBoxLayout(
            self.frame_main_inter_info_inter_teacher)
        self.verticalLayout_53.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.frame_content_inter_teacher = QFrame(
            self.frame_main_inter_info_inter_teacher)
        self.frame_content_inter_teacher.setMinimumSize(QSize(0, 0))
        self.frame_content_inter_teacher.setFrameShape(QFrame.StyledPanel)
        self.frame_content_inter_teacher.setFrameShadow(QFrame.Raised)
        self.frame_content_inter_teacher.setObjectName(
            "frame_content_inter_teacher")
        self.gridLayout_10 = QGridLayout(self.frame_content_inter_teacher)
        self.gridLayout_10.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_show_roll_number = QLabel(self.frame_content_inter_teacher)
        self.label_show_roll_number.setMinimumSize(QSize(0, 30))
        self.label_show_roll_number.setMaximumSize(QSize(16777215, 30))
        self.label_show_roll_number.setObjectName("label_show_roll_number")
        self.gridLayout_10.addWidget(self.label_show_roll_number, 1, 0, 1, 2)
        self.horizontalLayout_inter_2 = QHBoxLayout()
        self.horizontalLayout_inter_2.setObjectName("horizontalLayout_inter_2")
        self.btn_addInter_teacher = QPushButton(
            self.frame_content_inter_teacher)
        self.btn_addInter_teacher.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addInter_teacher.setFont(font)
        self.btn_addInter_teacher.setObjectName("btn_addInter_teacher")
        self.horizontalLayout_inter_2.addWidget(self.btn_addInter_teacher)
        self.btn_go_inter_teacher = QPushButton(
            self.frame_content_inter_teacher)
        self.btn_go_inter_teacher.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_go_inter_teacher.setFont(font)
        self.btn_go_inter_teacher.setObjectName("btn_go_inter_teacher")
        self.horizontalLayout_inter_2.addWidget(self.btn_go_inter_teacher)
        self.gridLayout_10.addLayout(self.horizontalLayout_inter_2, 2, 0, 1, 2)
        self.scrollArea_add_info = QScrollArea(
            self.frame_content_inter_teacher)
        self.scrollArea_add_info.setWidgetResizable(True)
        self.scrollArea_add_info.setObjectName("scrollArea_add_info")
        self.scrollAreaWidgetInfo = QWidget()
        self.scrollAreaWidgetInfo.setGeometry(QRect(0, -467, 835, 1000))
        self.scrollAreaWidgetInfo.setMinimumSize(QSize(0, 1000))
        self.scrollAreaWidgetInfo.setObjectName("scrollAreaWidgetInfo")
        self.verticalLayout_55 = QVBoxLayout(self.scrollAreaWidgetInfo)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.frame_user_image_upload_inter_teacher = QFrame(
            self.scrollAreaWidgetInfo)
        self.frame_user_image_upload_inter_teacher.setMaximumSize(
            QSize(16777215, 300))
        self.frame_user_image_upload_inter_teacher.setFrameShape(
            QFrame.StyledPanel)
        self.frame_user_image_upload_inter_teacher.setFrameShadow(
            QFrame.Raised)
        self.frame_user_image_upload_inter_teacher.setObjectName(
            "frame_user_image_upload_inter_teacher")
        self.gridLayout_9 = QGridLayout(
            self.frame_user_image_upload_inter_teacher)
        self.gridLayout_9.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_9.setSpacing(10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_icon_inter_teacher = QLabel(
            self.frame_user_image_upload_inter_teacher)
        self.setShadowEffect(self.label_icon_inter_teacher)
        self.label_icon_inter_teacher.setMinimumSize(QSize(200, 200))
        self.label_icon_inter_teacher.setMaximumSize(QSize(200, 200))
        self.label_icon_inter_teacher.setObjectName("label_icon_inter_teacher")
        self.gridLayout_9.addWidget(self.label_icon_inter_teacher, 0, 0, 1, 1)
        self.btn_upload_image_inter_teacher = QPushButton(
            self.frame_user_image_upload_inter_teacher)
        self.btn_upload_image_inter_teacher.setMinimumSize(QSize(0, 25))
        self.btn_upload_image_inter_teacher.setMaximumSize(QSize(300, 25))
        self.btn_upload_image_inter_teacher.setObjectName(
            "btn_upload_image_inter_teacher")
        self.gridLayout_9.addWidget(
            self.btn_upload_image_inter_teacher, 1, 0, 1, 1)
        self.verticalLayout_55.addWidget(
            self.frame_user_image_upload_inter_teacher)
        self.groupBox_lineedit_info = QGroupBox(self.scrollAreaWidgetInfo)
        self.groupBox_lineedit_info.setTitle("")
        self.groupBox_lineedit_info.setObjectName("groupBox_lineedit_info")
        self.gridLayout_13 = QGridLayout(self.groupBox_lineedit_info)
        self.gridLayout_13.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_13.setSpacing(10)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lineEdit_email_id = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_email_id.setMinimumSize(QSize(0, 30))
        self.lineEdit_email_id.setObjectName("lineEdit_email_id")
        self.gridLayout_13.addWidget(self.lineEdit_email_id, 2, 0, 1, 1)
        self.lineEdit_educational_qualif = QLineEdit(
            self.groupBox_lineedit_info)
        self.lineEdit_educational_qualif.setMinimumSize(QSize(0, 30))
        self.lineEdit_educational_qualif.setObjectName(
            "lineEdit_educational_qualif")
        self.gridLayout_13.addWidget(
            self.lineEdit_educational_qualif, 6, 0, 1, 1)
        self.lineEdit_professional_qualif = QLineEdit(
            self.groupBox_lineedit_info)
        self.lineEdit_professional_qualif.setMinimumSize(QSize(0, 30))
        self.lineEdit_professional_qualif.setObjectName(
            "lineEdit_professional_qualif")
        self.gridLayout_13.addWidget(
            self.lineEdit_professional_qualif, 6, 1, 1, 1)
        self.lineEdit_personal_contact = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_personal_contact.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_personal_contact.setFont(font)
        self.lineEdit_personal_contact.setObjectName(
            "lineEdit_personal_contact")
        self.gridLayout_13.addWidget(
            self.lineEdit_personal_contact, 1, 1, 1, 1)
        self.lineEdit_appoint_subject = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_appoint_subject.setMinimumSize(QSize(0, 30))
        self.lineEdit_appoint_subject.setObjectName("lineEdit_appoint_subject")
        self.gridLayout_13.addWidget(self.lineEdit_appoint_subject, 5, 1, 1, 1)
        self.lineEdit_full_name = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_full_name.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_full_name.setFont(font)
        self.lineEdit_full_name.setToolTipDuration(4)
        self.lineEdit_full_name.setObjectName("lineEdit_full_name")
        self.gridLayout_13.addWidget(self.lineEdit_full_name, 0, 0, 1, 1)
        self.lineEdit__name_initial = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit__name_initial.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit__name_initial.setFont(font)
        self.lineEdit__name_initial.setObjectName("lineEdit__name_initial")
        self.gridLayout_13.addWidget(self.lineEdit__name_initial, 0, 1, 1, 1)
        self.lineEdit_spouse_name = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_spouse_name.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_spouse_name.setFont(font)
        self.lineEdit_spouse_name.setObjectName("lineEdit_spouse_name")
        self.gridLayout_13.addWidget(self.lineEdit_spouse_name, 3, 1, 1, 1)
        self.lineEdit_WOP_no = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_WOP_no.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_WOP_no.setFont(font)
        self.lineEdit_WOP_no.setObjectName("lineEdit_WOP_no")
        self.gridLayout_13.addWidget(self.lineEdit_WOP_no, 2, 1, 1, 1)
        self.lineEdit_agrakara_no = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_agrakara_no.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_agrakara_no.setFont(font)
        self.lineEdit_agrakara_no.setObjectName("lineEdit_agrakara_no")
        self.gridLayout_13.addWidget(self.lineEdit_agrakara_no, 3, 0, 1, 1)
        self.lineEdit_inc_no = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_inc_no.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_inc_no.setFont(font)
        self.lineEdit_inc_no.setObjectName("lineEdit_inc_no")
        self.gridLayout_13.addWidget(self.lineEdit_inc_no, 1, 0, 1, 1)
        self.lineEdit_teaching_regist_no = QLineEdit(
            self.groupBox_lineedit_info)
        self.lineEdit_teaching_regist_no.setMinimumSize(QSize(0, 30))
        self.lineEdit_teaching_regist_no.setObjectName(
            "lineEdit_teaching_regist_no")
        self.gridLayout_13.addWidget(
            self.lineEdit_teaching_regist_no, 5, 0, 1, 1)
        self.lineEdit_nature_of_appoin = QLineEdit(self.groupBox_lineedit_info)
        self.lineEdit_nature_of_appoin.setMinimumSize(QSize(0, 30))
        self.lineEdit_nature_of_appoin.setMaximumSize(
            QSize(16777215, 16777215))
        self.lineEdit_nature_of_appoin.setSizeIncrement(QSize(0, 0))
        self.lineEdit_nature_of_appoin.setObjectName(
            "lineEdit_nature_of_appoin")
        self.gridLayout_13.addWidget(
            self.lineEdit_nature_of_appoin, 7, 0, 1, 2)
        self.verticalLayout_55.addWidget(self.groupBox_lineedit_info)
        self.groupBox_increment_date = QGroupBox(self.scrollAreaWidgetInfo)
        self.groupBox_increment_date.setObjectName("groupBox_increment_date")
        self.groupBox_increment_date.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_25 = QHBoxLayout(self.groupBox_increment_date)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.dateEdit_increment_date = QDateEdit(self.groupBox_increment_date)
        self.dateEdit_increment_date.setMinimumSize(QSize(0, 30))
        self.dateEdit_increment_date.setObjectName("dateEdit_increment_date")
        self.horizontalLayout_25.addWidget(self.dateEdit_increment_date)
        self.verticalLayout_55.addWidget(self.groupBox_increment_date)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_34.setSpacing(10)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_DOB_text = QLabel(self.scrollAreaWidgetInfo)
        self.label_DOB_text.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.label_DOB_text.setFont(font)
        self.label_DOB_text.setObjectName("label_DOB_text")
        self.horizontalLayout_34.addWidget(
            self.label_DOB_text, 0, Qt.AlignHCenter)
        self.label_appointment_data_text = QLabel(self.scrollAreaWidgetInfo)
        self.label_appointment_data_text.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.label_appointment_data_text.setFont(font)
        self.label_appointment_data_text.setObjectName(
            "label_appointment_data_text")
        self.horizontalLayout_34.addWidget(
            self.label_appointment_data_text, 0, Qt.AlignHCenter)
        self.verticalLayout_55.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setSpacing(10)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.dateEdit_DOB = QDateEdit(self.scrollAreaWidgetInfo)
        self.dateEdit_DOB.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.dateEdit_DOB.setFont(font)
        self.dateEdit_DOB.setObjectName("dateEdit_DOB")
        self.horizontalLayout_33.addWidget(self.dateEdit_DOB)
        self.dateEdit_first_appointment_date = QDateEdit(
            self.scrollAreaWidgetInfo)
        self.dateEdit_first_appointment_date.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.dateEdit_first_appointment_date.setFont(font)
        self.dateEdit_first_appointment_date.setObjectName(
            "dateEdit_first_appointment_date")
        self.horizontalLayout_33.addWidget(
            self.dateEdit_first_appointment_date)
        self.verticalLayout_55.addLayout(self.horizontalLayout_33)
        self.groupBox_address = QGroupBox(self.scrollAreaWidgetInfo)
        self.groupBox_address.setMaximumSize(QSize(16777215, 100))
        self.groupBox_address.setMinimumSize(QSize(0, 70))
        self.groupBox_address.setTitle("")
        self.groupBox_address.setObjectName("groupBox_address")
        self.gridLayout_14 = QGridLayout(self.groupBox_address)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.textEdit_working_address = QTextEdit(self.groupBox_address)
        self.textEdit_working_address.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.textEdit_working_address.setFont(font)
        self.textEdit_working_address.setObjectName("textEdit_working_address")
        self.gridLayout_14.addWidget(
            self.textEdit_working_address, 0, 0, 1, 1)
        self.textEdit_emergency = QTextEdit(self.groupBox_address)
        self.textEdit_emergency.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setPointSize(10)
        self.textEdit_emergency.setFont(font)
        self.textEdit_emergency.setObjectName("textEdit_emergency")
        self.gridLayout_14.addWidget(
            self.textEdit_emergency, 0, 1, 1, 1)
        self.verticalLayout_55.addWidget(self.groupBox_address)
        self.groupBox_present_grade_and_date = QGroupBox(
            self.scrollAreaWidgetInfo)
        self.groupBox_present_grade_and_date.setMinimumSize(QSize(0, 70))
        self.groupBox_present_grade_and_date.setObjectName(
            "groupBox_present_grade_and_date")
        self.gridLayout_7 = QGridLayout(self.groupBox_present_grade_and_date)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.lineEdit_present_grade = QLineEdit(
            self.groupBox_present_grade_and_date)
        self.lineEdit_present_grade.setMinimumSize(QSize(0, 30))
        self.lineEdit_present_grade.setObjectName("lineEdit_present_grade")
        self.gridLayout_7.addWidget(
            self.lineEdit_present_grade, 0, 0, 1, 1)
        self.dateEdit_present_date = QDateEdit(
            self.groupBox_present_grade_and_date)
        self.dateEdit_present_date.setMinimumSize(QSize(200, 30))
        self.dateEdit_present_date.setObjectName("dateEdit_present_date")
        self.gridLayout_7.addWidget(
            self.dateEdit_present_date, 0, 1, 1, 1)
        self.verticalLayout_55.addWidget(self.groupBox_present_grade_and_date)
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_date_app_to_school_text = QLabel(self.scrollAreaWidgetInfo)
        self.label_date_app_to_school_text.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.label_date_app_to_school_text.setFont(font)
        self.label_date_app_to_school_text.setObjectName(
            "label_date_app_to_school_text")
        self.horizontalLayout_37.addWidget(
            self.label_date_app_to_school_text, 0, Qt.AlignHCenter)
        self.verticalLayout_55.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.dateEdit_appointment_date = QDateEdit(self.scrollAreaWidgetInfo)
        self.dateEdit_appointment_date.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.dateEdit_appointment_date.setFont(font)
        self.dateEdit_appointment_date.setObjectName(
            "dateEdit_appointment_date")
        self.horizontalLayout_38.addWidget(self.dateEdit_appointment_date)
        self.verticalLayout_55.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setSpacing(6)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.groupBox_civil = QGroupBox(self.scrollAreaWidgetInfo)
        self.groupBox_civil.setObjectName("groupBox_civil")
        self.groupBox_civil.setMinimumSize(QSize(0, 70))
        self.gridLayout_15 = QGridLayout(self.groupBox_civil)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_15.setContentsMargins(10, 10, 10, 10)
        self.radioButton_married = QRadioButton(self.groupBox_civil)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_married.setFont(font)
        self.radioButton_married.setObjectName("radioButton_married")
        self.gridLayout_15.addWidget(
            self.radioButton_married, 0, 0, 1, 1, Qt.AlignCenter)
        self.radioButton_unmarried = QRadioButton(self.groupBox_civil)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_unmarried.setFont(font)
        self.radioButton_unmarried.setObjectName("radioButton_unmarried")
        self.gridLayout_15.addWidget(
            self.radioButton_unmarried, 0, 1, 1, 1, Qt.AlignCenter)
        self.horizontalLayout_40.addWidget(self.groupBox_civil)
        self.groupBox_gender = QGroupBox(self.scrollAreaWidgetInfo)
        self.groupBox_gender.setObjectName("groupBox_gender")
        self.groupBox_gender.setMinimumSize(QSize(0, 70))
        self.gridLayout_16 = QGridLayout(self.groupBox_gender)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_16.setContentsMargins(10, 10, 10, 10)
        self.radioButton_other = QRadioButton(self.groupBox_gender)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_other.setFont(font)
        self.radioButton_other.setObjectName("radioButton_other")
        self.gridLayout_16.addWidget(
            self.radioButton_other, 0, 2, 1, 1, Qt.AlignCenter)
        self.radioButton_female = QRadioButton(self.groupBox_gender)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_female.setFont(font)
        self.radioButton_female.setObjectName("radioButton_female")
        self.gridLayout_16.addWidget(
            self.radioButton_female, 0, 1, 1, 1, Qt.AlignCenter)
        self.radioButton_male = QRadioButton(self.groupBox_gender)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_male.setFont(font)
        self.radioButton_male.setObjectName("radioButton_male")
        self.gridLayout_16.addWidget(
            self.radioButton_male, 0, 0, 1, 1, Qt.AlignCenter)
        self.horizontalLayout_40.addWidget(self.groupBox_gender)
        self.verticalLayout_55.addLayout(self.horizontalLayout_40)
        self.scrollArea_add_info.setWidget(self.scrollAreaWidgetInfo)
        self.gridLayout_10.addWidget(self.scrollArea_add_info, 0, 0, 1, 1)
        self.verticalLayout_53.addWidget(self.frame_content_inter_teacher)
        self.verticalLayout_54.addWidget(
            self.frame_main_inter_info_inter_teacher)
        self.stackedWidget.addWidget(self.page_add_inter)

        self.analytics = QWidget()

        self.horizontallLayout = QHBoxLayout(self.analytics)
        self.horizontallLayout.setObjectName(u"horizontallLayout")
        self.frame_content = QFrame(self.analytics)
        self.frame_content.setObjectName(u"frame_content")

        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.hotizontalLayout_2 = QHBoxLayout(self.frame_content)
        self.hotizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea_content = QScrollArea(self.frame_content)
        self.scrollArea_content.setObjectName(u"scrollArea_content")
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
        self.verticalLayout_content_layout.addWidget(self.label_inter_head)

        self.frame_inter = QFrame(self.scrollAreaWidgetContents_layout)
        self.frame_inter.setObjectName(u"frame_inter")
        self.frame_inter.setMinimumSize(QSize(0, 450))
        self.frame_inter.setMaximumSize(QSize(16777215, 450))
        self.setShadowEffect(self.frame_inter)
        self.frame_inter.setFrameShape(QFrame.StyledPanel)
        self.frame_inter.setFrameShadow(QFrame.Raised)

        self.inter_frame_layout = QHBoxLayout(self.frame_inter)
        self.inter_frame_layout.setContentsMargins(9, 9, 9, 9)
        self.inter_frame_layout.setSpacing(3)

        self.frame_inter.setLayout(self.inter_frame_layout)

        self.verticalLayout_content_layout.addWidget(self.frame_inter)

        self.label_lower_head = QLabel(self.scrollAreaWidgetContents_layout)
        self.label_lower_head.setObjectName(u"label_lower_head")
        self.verticalLayout_content_layout.addWidget(self.label_lower_head)

        self.frame_lower = QFrame(self.scrollAreaWidgetContents_layout)
        self.frame_lower.setObjectName(u"frame_lower")
        self.frame_lower.setMinimumSize(QSize(0, 500))
        self.frame_lower.setMaximumSize(QSize(16777215, 500))
        self.setShadowEffect(self.frame_lower)
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
        self.setShadowEffect(self.frame_lower_prim)
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
        self.setShadowEffect(self.frame_lower_advan)
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
        self.setShadowEffect(self.frame_main_lower_info)
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

        self.frame_user_image_upload_lower = QFrame(self.frame_logo_icon_lower)

        self.gridLayout_lower = QGridLayout(self.frame_user_image_upload_lower)
        self.gridLayout_lower.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_lower.setSpacing(10)
        self.gridLayout_lower.setObjectName("gridLayout_lower")
        self.label_icon_lower = QLabel(self.frame_user_image_upload_lower)
        self.label_icon_lower.setObjectName(u"label_icon_lower")
        self.label_icon_lower.setMinimumSize(QSize(200, 200))
        self.label_icon_lower.setMaximumSize(QSize(200, 200))
        self.setShadowEffect(self.label_icon_lower)
        self.gridLayout_lower.addWidget(self.label_icon_lower, 0, 0, 1, 1)
        self.btn_upload_image_lower = QPushButton(
            self.frame_user_image_upload_lower)
        self.btn_upload_image_lower.setMinimumSize(QSize(0, 25))
        self.btn_upload_image_lower.setMaximumSize(QSize(300, 25))
        self.btn_upload_image_lower.setObjectName("btn_upload_image_lower")
        self.gridLayout_lower.addWidget(
            self.btn_upload_image_lower, 1, 0, 1, 1)

        self.horizontalLayout_24.addWidget(self.frame_user_image_upload_lower)

        self.verticalLayout_46.addWidget(self.frame_logo_icon_lower)

        self.frame_content_lower = QFrame(self.frame_main_lower_info)
        self.frame_content_lower.setObjectName(u"frame_content_lower")
        self.frame_content_lower.setFrameShape(QFrame.StyledPanel)
        self.frame_content_lower.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_content_lower)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")

        self.scrollArea_lower_add = QScrollArea(
            self.frame_content_lower)
        self.scrollArea_lower_add.setWidgetResizable(True)
        self.scrollArea_lower_add.setObjectName("scrollArea_lower_add")
        self.scrollAreaWidgetContents_lower = QWidget()
        self.scrollAreaWidgetContents_lower.setGeometry(
            QRect(0, 0, 839, 491))
        self.scrollAreaWidgetContents_lower.setObjectName(
            "scrollAreaWidgetContents_lower")
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_lower)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_gender_lower = QGroupBox(
            self.scrollAreaWidgetContents_lower)
        self.groupBox_gender_lower.setTitle("")
        self.groupBox_gender_lower.setObjectName("groupBox_gender_lower")
        self.verticalLayout_57 = QVBoxLayout(self.groupBox_gender_lower)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.label_info_gender_lower = QLabel(self.groupBox_gender_lower)
        self.label_info_gender_lower.setMinimumSize(QSize(0, 30))
        self.label_info_gender_lower.setObjectName(
            "label_info_gender_lower")
        self.verticalLayout_57.addWidget(self.label_info_gender_lower)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setContentsMargins(50, 0, 50, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.radioButton_male_lower_2 = QRadioButton(
            self.groupBox_gender_lower)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_male_lower_2.setFont(font)
        self.radioButton_male_lower_2.setObjectName(
            "radioButton_male_lower_2")
        self.horizontalLayout_36.addWidget(
            self.radioButton_male_lower_2, 0, Qt.AlignHCenter)
        self.radioButton_female_lower_2 = QRadioButton(
            self.groupBox_gender_lower)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_female_lower_2.setFont(font)
        self.radioButton_female_lower_2.setObjectName(
            "radioButton_female_lower_2")
        self.horizontalLayout_36.addWidget(
            self.radioButton_female_lower_2, 0, Qt.AlignHCenter)
        self.radioButton_other_lower_2 = QRadioButton(
            self.groupBox_gender_lower)
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.radioButton_other_lower_2.setFont(font)
        self.radioButton_other_lower_2.setObjectName(
            "radioButton_other_lower_2")
        self.horizontalLayout_36.addWidget(
            self.radioButton_other_lower_2, 0, Qt.AlignHCenter)
        self.verticalLayout_57.addLayout(self.horizontalLayout_36)
        self.gridLayout_6.addWidget(self.groupBox_gender_lower, 12, 0, 1, 2)
        self.lineEdit_father_name_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_father_name_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_father_name_lower.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_father_name_lower.setObjectName(
            "lineEdit_father_name_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_father_name_lower, 2, 0, 1, 1)
        self.lineEdit_religion_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_religion_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_religion_lower.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_religion_lower.setFont(font)
        self.lineEdit_religion_lower.setObjectName(
            "lineEdit_religion_lower")
        self.gridLayout_6.addWidget(self.lineEdit_religion_lower, 4, 0, 1, 1)
        self.lineEdit_admission_no_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_admission_no_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_admission_no_lower.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_admission_no_lower.setFont(font)
        self.lineEdit_admission_no_lower.setObjectName(
            "lineEdit_admission_no_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_admission_no_lower, 4, 1, 1, 1)
        self.lineEdit_name_initial_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_name_initial_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_initial_lower.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_name_initial_lower.setFont(font)
        self.lineEdit_name_initial_lower.setObjectName(
            "lineEdit_name_initial_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_name_initial_lower, 0, 1, 1, 1)
        self.dateEdit_date_of_birth_lower = QDateEdit(
            self.scrollAreaWidgetContents_lower)
        self.dateEdit_date_of_birth_lower.setMinimumSize(QSize(0, 30))
        self.dateEdit_date_of_birth_lower.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.dateEdit_date_of_birth_lower.setFont(font)
        self.dateEdit_date_of_birth_lower.setObjectName(
            "dateEdit_date_of_birth_lower")
        self.gridLayout_6.addWidget(
            self.dateEdit_date_of_birth_lower, 9, 0, 1, 1)
        self.lineEdit_name_full_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_name_full_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_name_full_lower.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_name_full_lower.setFont(font)
        self.lineEdit_name_full_lower.setObjectName(
            "lineEdit_name_full_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_name_full_lower, 0, 0, 1, 1)
        self.lineEdit_no_siblings_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_no_siblings_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_no_siblings_lower.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.lineEdit_no_siblings_lower.setFont(font)
        self.lineEdit_no_siblings_lower.setObjectName(
            "lineEdit_no_siblings_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_no_siblings_lower, 3, 0, 1, 1)
        self.lineEdit_mather_name_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_mather_name_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather_name_lower.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_mather_name_lower.setObjectName(
            "lineEdit_mather_name_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_mather_name_lower, 2, 1, 1, 1)
        self.comboBox_stream_lower = QComboBox(
            self.scrollAreaWidgetContents_lower)
        self.comboBox_stream_lower.setMinimumSize(QSize(0, 30))
        self.comboBox_stream_lower.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"./src/font/segoeui.ttf")
        font.setPointSize(10)
        self.comboBox_stream_lower.setFont(font)
        self.comboBox_stream_lower.setObjectName("comboBox_stream_lower")
        self.comboBox_stream_lower.addItem("")
        self.comboBox_stream_lower.addItem("")
        self.comboBox_stream_lower.addItem("")
        self.comboBox_stream_lower.addItem("")
        self.comboBox_stream_lower.addItem("")
        self.comboBox_stream_lower.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_stream_lower, 3, 1, 1, 1)
        self.dateEdit_date_admission_lower = QDateEdit(
            self.scrollAreaWidgetContents_lower)
        self.dateEdit_date_admission_lower.setMinimumSize(QSize(0, 30))
        self.dateEdit_date_admission_lower.setMaximumSize(
            QSize(16777215, 30))
        self.dateEdit_date_admission_lower.setObjectName(
            "dateEdit_date_admission_lower")
        self.gridLayout_6.addWidget(
            self.dateEdit_date_admission_lower, 9, 1, 1, 1)
        self.textEdit_address_home_lower = QTextEdit(
            self.scrollAreaWidgetContents_lower)
        self.textEdit_address_home_lower.setMinimumSize(QSize(0, 100))
        self.textEdit_address_home_lower.setMaximumSize(QSize(16777215, 100))
        self.textEdit_address_home_lower.setObjectName(
            "textEdit_address_home_lower")
        self.gridLayout_6.addWidget(
            self.textEdit_address_home_lower, 1, 0, 1, 1)
        self.textEdit_address_office_lower = QTextEdit(
            self.scrollAreaWidgetContents_lower)
        self.textEdit_address_office_lower.setMinimumSize(QSize(0, 100))
        self.textEdit_address_office_lower.setMaximumSize(QSize(16777215, 100))
        self.textEdit_address_office_lower.setObjectName(
            "textEdit_address_office_lower")
        self.gridLayout_6.addWidget(
            self.textEdit_address_office_lower, 1, 1, 1, 1)
        self.lineEdit_father_job_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_father_job_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_father_job_lower.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_father_job_lower.setObjectName(
            "lineEdit_father_job_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_father_job_lower, 6, 0, 1, 1)
        self.lineEdit_mather_job_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_mather_job_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_mather_job_lower.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_mather_job_lower.setObjectName(
            "lineEdit_mather_job_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_mather_job_lower, 6, 1, 1, 1)
        self.label_inforem_date_of_birth_lower = QLabel(
            self.scrollAreaWidgetContents_lower)
        self.label_inforem_date_of_birth_lower.setMinimumSize(QSize(0, 30))
        self.label_inforem_date_of_birth_lower.setMaximumSize(
            QSize(16777215, 30))
        self.label_inforem_date_of_birth_lower.setObjectName(
            "label_inforem_date_of_birth_lower")
        self.gridLayout_6.addWidget(
            self.label_inforem_date_of_birth_lower, 8, 0, 1, 1)
        self.label_inforem_admission_lower = QLabel(
            self.scrollAreaWidgetContents_lower)
        self.label_inforem_admission_lower.setObjectName(
            "label_inforem_admission_lower")
        self.gridLayout_6.addWidget(
            self.label_inforem_admission_lower, 8, 1, 1, 1)
        self.lineEdit_parent_contact_lower = QLineEdit(
            self.scrollAreaWidgetContents_lower)
        self.lineEdit_parent_contact_lower.setMinimumSize(QSize(0, 30))
        self.lineEdit_parent_contact_lower.setMaximumSize(
            QSize(16777215, 30))
        self.lineEdit_parent_contact_lower.setObjectName(
            "lineEdit_parent_contact_lower")
        self.gridLayout_6.addWidget(
            self.lineEdit_parent_contact_lower, 7, 0, 1, 2)
        self.scrollArea_lower_add.setWidget(
            self.scrollAreaWidgetContents_lower)
        self.verticalLayout_47.addWidget(self.scrollArea_lower_add)

        self.label_show_roll_number_lower = QLabel(self.frame_content_lower)
        self.label_show_roll_number_lower.setObjectName(
            u"label_show_roll_number_lower")
        self.label_show_roll_number_lower.setMinimumSize(QSize(0, 35))

        self.verticalLayout_47.addWidget(self.label_show_roll_number_lower)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_addlower = QPushButton(self.frame_content_lower)
        self.btn_addlower.setObjectName(u"btn_addlower")
        self.btn_addlower.setMinimumSize(QSize(0, 30))
        self.btn_addlower.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_29.addWidget(self.btn_addlower)

        self.btn_go_home_lower = QPushButton(self.frame_content_lower)
        self.btn_go_home_lower.setObjectName(u"btn_go_home_lower")
        self.btn_go_home_lower.setMinimumSize(QSize(0, 30))
        self.btn_go_home_lower.setMaximumSize(QSize(16777215, 30))

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
        self.label_advanced_level_12.setObjectName("label_advanced_level_12")
        self.verticalLayout_49.addWidget(self.label_advanced_level_12)
        self.frame_advanced_level_12 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_advanced_level_12.setMinimumSize(QSize(0, 500))
        self.frame_advanced_level_12.setMaximumSize(QSize(16777215, 500))
        self.setShadowEffect(self.frame_advanced_level_12)
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
        self.label_advanced_level_13.setObjectName("label_advanced_level_13")
        self.verticalLayout_49.addWidget(self.label_advanced_level_13)
        self.frame_advanced_level_13 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_advanced_level_13.setMinimumSize(QSize(0, 500))
        self.frame_advanced_level_13.setMaximumSize(QSize(16777215, 500))
        self.setShadowEffect(self.frame_advanced_level_13)
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
        self.setShadowEffect(self.frame_user_icon_for_super)
        self.frame_user_icon_for_super.setFrameShape(QFrame.StyledPanel)
        self.frame_user_icon_for_super.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_user_icon_for_super)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_super_icon = QLabel(self.frame_user_icon_for_super)
        self.label_super_icon.setObjectName(u"label_super_icon")

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

        self.verticalLayout_42.addWidget(
            self.label_infor_super, 0, Qt.AlignTop)

        self.btn_edit_setting = QPushButton(self.frame_inforezion_super)
        self.btn_edit_setting.setFont(font11)
        self.btn_edit_setting.setObjectName(u"btn_edit_setting")
        self.btn_edit_setting.setMaximumSize(QSize(16777215, 45))
        self.btn_edit_setting.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_42.addWidget(self.btn_edit_setting)
        self.verticalLayout_40.addWidget(self.frame_inforezion_super)
        self.verticalLayout_32.addWidget(self.frame_more_options)
        self.frame_adout = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_adout.setMinimumSize(QSize(0, 50))
        self.frame_adout.setMaximumSize(QSize(16777215, 50))
        self.frame_adout.setFrameShape(QFrame.StyledPanel)
        self.frame_adout.setFrameShadow(QFrame.Raised)
        self.frame_adout.setObjectName("frame_adout")
        self.verticalLayout_51 = QVBoxLayout(self.frame_adout)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_info_adout = QLabel(self.frame_adout)
        font = QFont()
        font.setFamily("./src/font/segoeui.ttf")
        self.label_info_adout.setFont(font)
        self.label_info_adout.setObjectName("label_info_adout")
        self.horizontalLayout_31.addWidget(self.label_info_adout)
        self.btn_hidden_adout = QPushButton(self.frame_adout)
        self.btn_hidden_adout.setMinimumSize(QSize(30, 30))
        self.btn_hidden_adout.setMaximumSize(QSize(30, 30))
        self.btn_hidden_adout.setText("")
        self.btn_hidden_adout.setObjectName("btn_hidden_adout")
        self.horizontalLayout_31.addWidget(self.btn_hidden_adout)
        self.verticalLayout_51.addLayout(self.horizontalLayout_31)
        self.frame_content_adout = QFrame(self.frame_adout)
        self.frame_content_adout.setMinimumSize(QSize(0, 0))
        self.frame_content_adout.setMaximumSize(QSize(16777215, 0))
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
        self.label_more_info_adout.setObjectName("label_more_info_adout")
        self.label_more_info_adout.setFont(font11)
        self.horizontalLayout_32.addWidget(self.label_more_info_adout)
        self.verticalLayout_51.addWidget(self.frame_content_adout)
        self.verticalLayout_32.addWidget(self.frame_adout)
        self.horizontalLayout_2.addWidget(self.frame_super_user)
        self.verticalLayout.addWidget(self.Content)

        self.StatusBar = QFrame(self.centralwidget)
        self.StatusBar.setMinimumSize(QSize(0, 25))
        self.StatusBar.setFrameShape(QFrame.StyledPanel)
        self.StatusBar.setFrameShadow(QFrame.Raised)
        self.StatusBar.setObjectName("StatusBar")
        self.setShadowEffect(self.StatusBar, 15, QColor(0, 0, 0, 0))
        self.horizontalLayout_29 = QHBoxLayout(self.StatusBar)
        self.horizontalLayout_29.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_status_text = QLabel(self.StatusBar)
        self.label_status_text.setMinimumSize(QSize(250, 15))
        font = QFont()
        font.setPointSize(8)
        self.label_status_text.setFont(font)
        self.label_status_text.setObjectName("label_status_text")
        self.horizontalLayout_29.addWidget(self.label_status_text)
        self.analytics_status = QLabel(self.StatusBar)
        self.analytics_status.setMinimumSize(QSize(250, 15))
        self.analytics_status.setFont(font)
        self.analytics_status.setObjectName("analytics_status")
        self.horizontalLayout_29.addWidget(self.analytics_status)

        self.searching_status = QLabel(self.StatusBar)
        self.searching_status.setMinimumSize(QSize(250, 15))
        self.searching_status.setFont(font)
        self.searching_status.setObjectName("searching_status")
        self.horizontalLayout_29.addWidget(self.searching_status)

        self.other_status = QLabel(self.StatusBar)
        self.other_status.setMinimumSize(QSize(250, 15))
        self.other_status.setFont(font)
        self.other_status.setObjectName("other_status")
        self.horizontalLayout_29.addWidget(self.other_status)

        self.status_prograss = QProgressBar(self.StatusBar)
        self.status_prograss.setMaximumSize(QSize(16777215, 10))
        self.status_prograss.setTextVisible(False)
        self.status_prograss.setObjectName("status_prograss")
        self.horizontalLayout_29.addWidget(self.status_prograss)
        self.verticalLayout.addWidget(self.StatusBar)

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
        self.btn_delete_inter_1.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))

        self.label_info_lower_1.setText("")
        self.btn_delete_lower_1.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.btn_delete_lower_pri.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None)
        )
        self.label_info_lower_pri.setText("")
        self.btn_delete_lower_advan.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None)
        )
        self.label_info_lower_advan.setText("")
        self.info_inter_left_1.setText("")
        self.btn_delete_inter_left_1.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.info_lower_1.setText("")
        self.btn_delete_lower_left_1.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.info_lower_left_pri.setText("")
        self.btn_delete_lower_left_pri.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.info_lower_left_advan.setText("")
        self.btn_delete_lower_left_advan.setText(
            QCoreApplication.translate("MainWindow", u" Delete", None))
        self.lineEdit_nameSearch.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Search Name", None))
        self.btn_nameSearch.setText(
            QCoreApplication.translate("MainWindow", u" Search", None))
        self.lineEdit_rollSearch.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Search Roll ID", None))
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
            "MainWindow", u"Students Analytics", None))
        self.label_super_icon.setText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.btn_edit_setting.setText(QCoreApplication.translate(
            "MainWindow", u"Edit Setting", None))

        self.frame_main_inter_info_inter_teacher.setToolTip(
            QCoreApplication.translate("MainWindow", u"Add Teachers Data", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.btn_upload_image_inter_teacher.setText(QCoreApplication.translate(
            "MainWindow", u"Upload Image", None))
#endif // QT_CONFIG(tooltip)
        self.label_show_roll_number.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Roll ID </span></p></body></html>", None))
        self.btn_addInter_teacher.setText(QCoreApplication.translate(
            "MainWindow", u" Add Teachers", None))
        self.btn_go_inter_teacher.setText(QCoreApplication.translate(
            "MainWindow", u"Go Home", None))
        self.frame_main_lower_info.setToolTip(
            QCoreApplication.translate("MainWindow", u"Add Students Data", None))
# if QT_CONFIG(tooltip)

        self.btn_upload_image_lower.setText(QCoreApplication.translate(
            "MainWindow", u"Upload Image", None))
        self.label_show_roll_number_lower.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Roll ID </span></p></body></html>", None))
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
        self.label_theme_set_info.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p align=\"center\">Change Window Theme</p></body></html>"))
        self.comboBox_theme_items.setItemText(
            0, QCoreApplication.translate("MainWindow", "Light Theme ( default )"))
        self.comboBox_theme_items.setItemText(
            1, QCoreApplication.translate("MainWindow", "Dark Theme"))
        self.btn_setTheme.setText(
            QCoreApplication.translate("MainWindow", "Set Theme"))

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

        self.lineEdit_address_office_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address ( Office )"))
        self.lineEdit_home_address_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address ( Home )"))
        self.lineEdit_mather_name_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Mather Name"))
        self.lineEdit_mather_job_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Mather\'s Nature Of Job"))
        self.lineEdit_siblings_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Number Of Siblings"))
        self.lineEdit_religion_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Religion"))
        self.lineEdit_parent_contact_no_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Parent/Guardian Contact Number"))
        self.label_inforem_date_of_birth_ad.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span>Date Of Birth</span></p></body></html>"))
        self.label_date_admission_ad.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span>Date Of Admission</span></p></body></html>"))
        self.lineEdit_father_job_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Father\'s Nature Of Job"))
        self.lineEdit_name_initial_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name With Initial"))
        self.lineEdit_name_full_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name In Full"))
        self.lineEdit_father_name_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Father Name"))
        self.lineEdit_admission_no_ad.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Admission Number"))
        self.label_gender_ad.setText(
            QCoreApplication.translate("MainWindow", "<html><head/><body><p><span>Gender</span></p></body></html>"))

        self.radioButton_male_ad.setText(
            QCoreApplication.translate("MainWindow", "Male"))
        self.radioButton_female_ad.setText(
            QCoreApplication.translate("MainWindow", "Female"))
        self.radioButton_other_ad.setText(
            QCoreApplication.translate("MainWindow", "Other"))

        self.btn_upload_image_advanced.setText(QCoreApplication.translate(
            "MainWindow", u"Upload Image", None))
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
        self.comboBox_level_ad.setItemText(
            0, QCoreApplication.translate("MainWindow", "Level - 12"))
        self.comboBox_level_ad.setItemText(
            1, QCoreApplication.translate("MainWindow", "Level - 13"))
        self.label_show_roll_ad.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Roll ID </span></p></body></html>"))
        self.btn_addLower_adv.setText(
            QCoreApplication.translate("MainWindow", "Add Students"))
        self.btn_go_home_ad.setText(
            QCoreApplication.translate("MainWindow", "Go Home"))

        self.label_info_gender_primary.setText(
            QCoreApplication.translate("MainWindow", "Gender"))
        self.radioButton_male_primary_2.setText(
            QCoreApplication.translate("MainWindow", "Male"))
        self.radioButton_female_primary_2.setText(
            QCoreApplication.translate("MainWindow", "Female"))
        self.radioButton_other_primary_2.setText(
            QCoreApplication.translate("MainWindow", "Other"))
        self.lineEdit_father_name_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Father Name"))
        self.lineEdit_religion_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Religion"))
        self.lineEdit_admission_no_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Admission Number"))
        self.lineEdit_name_initial_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name With Initial"))
        self.dateEdit_date_of_birth_primary.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.lineEdit_name_full_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name In Full"))
        self.lineEdit_no_siblings_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Number Of Siblings"))
        self.lineEdit_mather_name_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Mather Name"))
        self.comboBox_stream_primary.setItemText(
            0, QCoreApplication.translate("MainWindow", "Level - 01"))
        self.comboBox_stream_primary.setItemText(
            1, QCoreApplication.translate("MainWindow", "Level - 02"))
        self.comboBox_stream_primary.setItemText(
            2, QCoreApplication.translate("MainWindow", "Level - 03 "))
        self.comboBox_stream_primary.setItemText(
            3, QCoreApplication.translate("MainWindow", "Level - 04"))
        self.comboBox_stream_primary.setItemText(
            4, QCoreApplication.translate("MainWindow", "Level - 05"))
        self.dateEdit_date_admission_primary.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.textEdit_address_home.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address ( Home )"))
        self.textEdit_address_office.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address ( Office )"))
        self.lineEdit_father_job_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Father\'s Nature Of Job"))
        self.lineEdit_mather_job_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Mather\'s Nature Of Job"))
        self.label_inforem_date_of_birth_primary.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Date Of Birth</span></p></body></html>"))
        self.label_inforem_admission_primary.setText(
            QCoreApplication.translate("MainWindow", "Date Of Admission"))
        self.lineEdit_parent_contact_primary.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Parent / Guardian Contact Number"))

        self.label_info_gender_lower.setText(
            QCoreApplication.translate("MainWindow", "Gender"))
        self.radioButton_male_lower_2.setText(
            QCoreApplication.translate("MainWindow", "Male"))
        self.radioButton_female_lower_2.setText(
            QCoreApplication.translate("MainWindow", "Female"))
        self.radioButton_other_lower_2.setText(
            QCoreApplication.translate("MainWindow", "Other"))
        self.lineEdit_father_name_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Father Name"))
        self.lineEdit_religion_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Religion"))
        self.lineEdit_admission_no_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Admission Number"))
        self.lineEdit_name_initial_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name With Initial"))
        self.dateEdit_date_of_birth_lower.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.lineEdit_name_full_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name In Full"))
        self.lineEdit_no_siblings_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Number Of Siblings"))
        self.lineEdit_mather_name_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Mather Name"))
        self.comboBox_stream_lower.setItemText(
            0, QCoreApplication.translate("MainWindow", "Level - 06"))
        self.comboBox_stream_lower.setItemText(
            1, QCoreApplication.translate("MainWindow", "Level - 07"))
        self.comboBox_stream_lower.setItemText(
            2, QCoreApplication.translate("MainWindow", "Level - 08 "))
        self.comboBox_stream_lower.setItemText(
            3, QCoreApplication.translate("MainWindow", "Level - 09"))
        self.comboBox_stream_lower.setItemText(
            4, QCoreApplication.translate("MainWindow", "Level - 10"))
        self.comboBox_stream_lower.setItemText(
            5, QCoreApplication.translate("MainWindow", "Level - 11"))
        self.dateEdit_date_admission_lower.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.textEdit_address_home_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address ( Home )"))
        self.textEdit_address_office_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address ( Office )"))
        self.lineEdit_father_job_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Father\'s Nature Of Job"))
        self.lineEdit_mather_job_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Mather\'s Nature Of Job"))
        self.label_inforem_date_of_birth_lower.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span>Date Of Birth</span></p></body></html>"))
        self.label_inforem_admission_lower.setText(
            QCoreApplication.translate("MainWindow", "Date Of Admission"))
        self.lineEdit_parent_contact_lower.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Parent / Guardian Contact Number"))

        self.label_show_roll_primary.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Roll ID </span></p></body></html>"))
        self.btn_addLower_primary.setText(
            QCoreApplication.translate("MainWindow", "Add Students"))
        self.btn_go_home_primary.setText(
            QCoreApplication.translate("MainWindow", "Go Home"))
        self.btn_upload_image_primary.setText(QCoreApplication.translate(
            "MainWindow", u"Upload Image", None))
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

        self.lineEdit_full_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name in Full"))
        self.lineEdit__name_initial.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name With Initial"))
        self.lineEdit_WOP_no.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "W&OP No."))
        self.lineEdit_personal_contact.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Personal Contact No."))
        self.lineEdit_spouse_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Spouse Name"))
        self.lineEdit_agrakara_no.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Agrakara No. "))
        self.lineEdit_inc_no.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", "National Identify Card No ( NIC No )"))
        self.label_DOB_text.setText(
            QCoreApplication.translate("MainWindow", "Date Of Birth"))
        self.label_appointment_data_text.setText(
            QCoreApplication.translate("MainWindow", "First Appointment Date"))
        self.dateEdit_DOB.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.dateEdit_first_appointment_date.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.label_date_app_to_school_text.setText(QCoreApplication.translate(
            "MainWindow", "Date of Appointment To This School"))
        self.lineEdit_appoint_subject.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Appointed Subject"))
        self.btn_upload_image_inter_teacher.setText(
            QCoreApplication.translate("MainWindow", "Upload Image"))
        self.lineEdit_email_id.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "E-Mail ID"))
        self.lineEdit_educational_qualif.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Educational Qualification"))
        self.lineEdit_professional_qualif.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Professional Qualification"))
        self.lineEdit_teaching_regist_no.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Teaching Registration No"))
        self.lineEdit_nature_of_appoin.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Nature Of Appointment"))
        self.groupBox_increment_date.setTitle(
            QCoreApplication.translate("MainWindow", "Increment Date"))
        self.textEdit_working_address.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address"))
        self.textEdit_emergency.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", "Contact No And Address for Emergency"))
        self.groupBox_present_grade_and_date.setTitle(
            QCoreApplication.translate("MainWindow", "Present Grade And The Date"))
        self.lineEdit_present_grade.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Present Grade"))
        self.dateEdit_present_date.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.dateEdit_appointment_date.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.groupBox_civil.setTitle(
            QCoreApplication.translate("MainWindow", "Civil Status"))
        self.radioButton_married.setText(
            QCoreApplication.translate("MainWindow", "Married"))
        self.radioButton_unmarried.setText(
            QCoreApplication.translate("MainWindow", "Unmarried"))
        self.groupBox_gender.setTitle(
            QCoreApplication.translate("MainWindow", "Gender"))
        self.radioButton_female.setText(
            QCoreApplication.translate("MainWindow", "Female"))
        self.radioButton_other.setText(
            QCoreApplication.translate("MainWindow", "Other"))
        self.radioButton_male.setText(
            QCoreApplication.translate("MainWindow", "Male"))
        self.btn_none_teaher.setText(
            QCoreApplication.translate("MainWindow", "None-Teahers"))
        self.btn_teahers.setText(
            QCoreApplication.translate("MainWindow", "Teahers"))
        self.btn_none_teaher.setToolTip(
            QCoreApplication.translate("MainWindow", "Add None Teahers"))
        self.btn_teahers.setToolTip(
            QCoreApplication.translate("MainWindow", "Add Teahers"))
        self.label_show_roll_number_none.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Roll ID </span></p></body></html>"))
        self.btn_addInter_teacher_none.setText(
            QCoreApplication.translate("MainWindow", "Add Teaher"))
        self.btn_go_inter_teacher_none.setText(
            QCoreApplication.translate("MainWindow", "Go Home"))
        self.btn_upload_image_inter_teacher_none.setText(
            QCoreApplication.translate("MainWindow", "Upload Image"))
        self.lineEdit_email_id_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "E-Mail ID"))
        self.lineEdit_educational_qualif_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Educational Qualification"))
        self.lineEdit_personal_contact_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Personal Contact No."))
        self.lineEdit_professional_qualif_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Professional Qualification"))
        self.lineEdit_full_name_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name in Full"))
        self.lineEdit__name_initial_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name With Initial"))
        self.lineEdit_WOP_no_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "W&OP No."))
        self.lineEdit_spouse_name_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Name Of Spouse "))
        self.lineEdit_agrakara_no_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Agrakara Policy No. "))
        self.lineEdit_inc_no_none.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", "National Identify Card No ( NIC No )"))
        self.lineEdit_nature_of_appoin_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Nature Of Appointment"))
        self.lineEdit_salary_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Salary No"))
        self.groupBox_increment_date_none.setTitle(
            QCoreApplication.translate("MainWindow", "Increment Date"))
        self.label_DOB_text_none.setText(
            QCoreApplication.translate("MainWindow", "Date Of Birth"))
        self.label_appointment_data_text_none.setText(
            QCoreApplication.translate("MainWindow", "First Appointment Date"))
        self.dateEdit_DOB_none.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.dateEdit_first_appointment_date_none.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.textEdit_working_address_none.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Address"))
        self.textEdit_emergency_none.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", "Contact No And Address for Emergency"))
        self.label_date_app_to_school_text_none.setText(
            QCoreApplication.translate("MainWindow", "Date of Appointment To This School"))
        self.dateEdit_appointment_date_none.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "d/M/yyyy"))
        self.groupBox_civil_none.setTitle(
            QCoreApplication.translate("MainWindow", "Civil Status"))
        self.radioButton_married_none.setText(
            QCoreApplication.translate("MainWindow", "Married"))
        self.radioButton_unmarried_none.setText(
            QCoreApplication.translate("MainWindow", "Unmarried"))
        self.groupBox_gender_none.setTitle(
            QCoreApplication.translate("MainWindow", "Gender"))
        self.radioButton_other_none.setText(
            QCoreApplication.translate("MainWindow", "Other"))
        self.radioButton_female_none.setText(
            QCoreApplication.translate("MainWindow", "Female"))
        self.radioButton_male_none.setText(
            QCoreApplication.translate("MainWindow", "Male"))
    # retranslateUi
