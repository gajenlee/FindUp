import cv2 as cv
import sys
import pandas as pd
import matplotlib as mtp
import numpy as np
import json
import re
import shortuuid


from threading import Thread
from Packages.connecter.compands.checkers import checkTheContactNum, checkTheEmail, checkTheUserName

from Packages.uis.access.ui_access import *
from Packages.uis.backup.ui_backup import *
from Packages.uis.create.ui_create import *
from Packages.uis.login.ui_login import *
from Packages.uis.main.ui_main import *
from Packages.uis.error.ui_error import *

from Packages.connecter.cryptography.crypto import *
from Packages.connecter.progressBar.circular_progress import *
from Packages.connecter.store.store import *
from Packages.connecter.thread_findup.threadForFindup import *
from Packages.connecter.compands.checkers import *

from src.style import dark
from src.style import light


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from nav_runer import *
from logging_findup import *


class Access_Window(QDialog):

    isIconPlace = False

    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Access()
        self.ui.setupUi(self)

        logger.debug("The Access Window Is Runing... [ Access_Window ]")

        # remove the frame of window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # SET TITLE BAR
        self.ui.frame_title_bar.mouseMoveEvent = self.moveWindow

        # Button connecter
        self.btn_connecter()

        # Defualt theme
        self.defualt_theme()

        # Animation
        self.animation()

        self.show()

    # Light Theme
    def setLightTheme(self):
        self.ui.frame_main.setStyleSheet(light.BACKGROUND_FRAME_MAIN)
        self.ui.frame_title_bar.setStyleSheet(light.TITTE_BAR_BACKGROUND)
        self.ui.label_title.setStyleSheet(light.LABEL_TITLE)
        self.ui.label_user_info.setStyleSheet(light.LABEL_USER_INFO)

        self.ui.btn_close.setStyleSheet(light.BTN_CLOSE)
        self.ui.lineEdit_current_password.setStyleSheet(light.LINE_EDIT_ACCESS)
        self.ui.btn_verify.setStyleSheet(light.BTN_VARIFY)

    def setIconLightTheme(self):
        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        if not self.isIconPlace:
            setIcon_line(self.ui.lineEdit_current_password, light.ICON_LOCK)
        else:
            setIcon_line_(self.ui.lineEdit_current_password, light.ICON_LOCK)

        icon = QIcon()
        icon.addFile(light.ICON_CLOSE)
        self.ui.btn_close.setIcon(icon)

    # Dark Theme
    def setDarkTheme(self):
        self.ui.frame_main.setStyleSheet(dark.BACKGROUND_FRAME_MAIN)
        self.ui.frame_title_bar.setStyleSheet(dark.TITTE_BAR_BACKGROUND)
        self.ui.label_title.setStyleSheet(dark.LABEL_TITLE)
        self.ui.label_user_info.setStyleSheet(dark.LABEL_USER_INFO)

        self.ui.btn_close.setStyleSheet(dark.BTN_CLOSE)
        self.ui.lineEdit_current_password.setStyleSheet(dark.LINE_EDIT_ACCESS)
        self.ui.btn_verify.setStyleSheet(dark.BTN_VARIFY)

    def setIconDarkTheme(self):

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        if not self.isIconPlace:
            setIcon_line(self.ui.lineEdit_current_password, dark.ICON_LOCK)
        else:
            setIcon_line_(self.ui.lineEdit_current_password, dark.ICON_LOCK)

        icon = QIcon()
        icon.addFile(dark.ICON_CLOSE)
        self.ui.btn_close.setIcon(icon)

    def defualt_theme(self):
        logger.debug("The Default Theme Is Runing... [defualt_theme]")
        setting = Setting.load_superuser()
        if setting["Setting"]["Default-theme"] == "light":
            self.setLightTheme()
            self.setIconLightTheme()
        else:
            self.setDarkTheme()
            self.setIconDarkTheme()

    def setShadow(self):
        # Set Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

    def btn_connecter(self):

        # Close Button
        self.ui.btn_close.clicked.connect(lambda: self.close())

    def shacke_window(self):

        logger.debug("The shacke function Actived... [ shacke_window ]")

        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(
            actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(
            actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(
            actual_pos.x(), actual_pos.y()))

    # key Event
    def moveWindow(self, event):

        # IF LEFT CLICK MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        # Mouse Press Event
        self.dragPos = event.globalPos()

    def animation(self):

        self.opacity = QGraphicsOpacityEffect()
        self.animation = QPropertyAnimation(self.opacity, b"opacity")
        self.ui.frame_main.setGraphicsEffect(self.opacity)
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)

        self.no_effect = QGraphicsOpacityEffect()
        self.animation_two = QPropertyAnimation(self.no_effect, b"opacity")
        self.ui.frame_main.setGraphicsEffect(self.opacity)
        self.animation_two.setStartValue(0)
        self.animation_two.setEndValue(1)
        self.animation_two.setDuration(500)

        self.hiding_effect = QGraphicsOpacityEffect()
        self.animation_three = QPropertyAnimation(
            self.hiding_effect, b"opacity")
        self.ui.frame_main.setGraphicsEffect(self.opacity)
        self.animation_three.setStartValue(1)
        self.animation_three.setEndValue(0)
        self.animation_two.setDuration(500)

        self.group = QSequentialAnimationGroup()
        self.group.addAnimation(self.animation)
        self.group.addAnimation(self.animation_two)
        self.group.addAnimation(self.animation_three)

        self.group.start()


class Backup_Window(QDialog):
    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Backup()
        self.ui.setupUi(self)

        # Animation
        self.animation()

        self.show()

    def animation(self):

        self.opacity = QGraphicsOpacityEffect()
        self.animation = QPropertyAnimation(self.opacity, b"opacity")
        self.ui.backup_window.setGraphicsEffect(self.opacity)
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)

        self.no_effect = QGraphicsOpacityEffect()
        self.animation_two = QPropertyAnimation(self.no_effect, b"opacity")
        self.ui.backup_window.setGraphicsEffect(self.opacity)
        self.animation_two.setStartValue(0)
        self.animation_two.setEndValue(1)
        self.animation_two.setDuration(500)

        self.hiding_effect = QGraphicsOpacityEffect()
        self.animation_three = QPropertyAnimation(
            self.hiding_effect, b"opacity")
        self.ui.backup_window.setGraphicsEffect(self.opacity)
        self.animation_three.setStartValue(1)
        self.animation_three.setEndValue(0)
        self.animation_two.setDuration(500)

        self.group = QSequentialAnimationGroup()
        self.group.addAnimation(self.animation)
        self.group.addAnimation(self.animation_two)
        self.group.addAnimation(self.animation_three)

        self.group.start()


class Create_Window(QMainWindow):
    iconReplace = False
    progress_conter = 0

    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Create()
        self.ui.setupUi(self)

        # remove the frame of window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        logger.debug("Createing Inti function is runing... [ Create_Window ]")

        # Set Theme
        self.default_theme()

        # Set shadow
        self.setShadowWindow()

        # Store User Data
        Store.init()
        Setting.init()

        # KEY EVENT FOR LOGIN WINDOW
        self.keyPressEvent = self.clickEvent

        self.show()

    # Dark Theme
    def setThemeDark(self):

        logger.debug("Theme is setting... [ setThemeDark ]")

        # Theme Contents
        self.ui.background.setStyleSheet(dark.BACKGROUND_WIDGET)
        self.ui.lineEdit_name.setStyleSheet(dark.LOGIN_LINE_EDIT)
        self.ui.lineEdit_pass.setStyleSheet(dark.LOGIN_LINE_EDIT)
        self.ui.lineEdit_con_pass.setStyleSheet(dark.LOGIN_LINE_EDIT)
        self.ui.lineEdit_email.setStyleSheet(dark.LOGIN_LINE_EDIT)
        self.ui.lineEdit_contact.setStyleSheet(dark.LOGIN_LINE_EDIT)

        # TEXT CONTENTS
        self.ui.label_logo.setText(dark.LOGO_OF_WINDOW)

    def setIconDark(self):

        logger.debug("Icon is setting... [ setIconDark ]")

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        if not self.iconReplace:
            logger.debug("Icon is palce setting... [ setIconDark ]")

            setIcon_line(self.ui.lineEdit_name, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_pass, dark.ICON_LOCK)
            setIcon_line(self.ui.lineEdit_con_pass, dark.ICON_LOCK)
            setIcon_line(self.ui.lineEdit_contact, dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_email, dark.ICON_AT)
        else:
            logger.debug("Icon is repalce setting... [ setIconDark ]")

            setIcon_line_(self.ui.lineEdit_name, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_pass, dark.ICON_LOCK)
            setIcon_line_(self.ui.lineEdit_con_pass, dark.ICON_LOCK)
            setIcon_line_(self.ui.lineEdit_contact, dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_email, dark.ICON_AT)

    def prograssBarDark(self):

        logger.debug("The Prograss Bar is starting... [prograssBarDark]")

        # Set Progress Bar
        self.progress = CircularProgress()
        self.progress.width = 258
        self.progress.height = 258

        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 30
        self.progress.progress_color = QColor("#316B4F")
        self.progress.text_color = QColor("#b3b1b1")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.label_greeting = self.ui.label_greeting
        self.progress.label_greeting_img = ["#", "./src/img/greeting/en-light.png",
                                            "./src/img/greeting/ta-light.png", "./src/img/greeting/si-light.png"]
        self.progress.show()

    # Light Theme
    def setThemeLight(self):

        logger.debug("Theme is setting... [ setThemeLight ]")

        # Theme Contents
        self.ui.background.setStyleSheet(light.BACKGROUND_WIDGET)
        self.ui.lineEdit_name.setStyleSheet(light.LOGIN_LINE_EDIT)
        self.ui.lineEdit_pass.setStyleSheet(light.LOGIN_LINE_EDIT)
        self.ui.lineEdit_con_pass.setStyleSheet(light.LOGIN_LINE_EDIT)
        self.ui.lineEdit_email.setStyleSheet(light.LOGIN_LINE_EDIT)
        self.ui.lineEdit_contact.setStyleSheet(light.LOGIN_LINE_EDIT)

        # TEXT CONTENTS
        self.ui.label_logo.setText(light.LOGO_OF_WINDOW)

    def setIconLight(self):

        logger.debug("Icon is setting... [ setIconLight ]")

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        if not self.iconReplace:
            logger.debug("Icon is palce setting... [ setIconDark ]")

            setIcon_line(self.ui.lineEdit_name, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_pass, light.ICON_LOCK)
            setIcon_line(self.ui.lineEdit_con_pass, light.ICON_LOCK)
            setIcon_line(self.ui.lineEdit_contact, light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_email, light.ICON_AT)
        else:
            logger.debug("Icon is repalce setting... [ setIconDark ]")

            setIcon_line_(self.ui.lineEdit_name, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_pass, light.ICON_LOCK)
            setIcon_line_(self.ui.lineEdit_con_pass, light.ICON_LOCK)
            setIcon_line_(self.ui.lineEdit_contact, light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_email, light.ICON_AT)

    def prograssBarLight(self):

        logger.debug("The Prograss Bar is starting... [prograssBarLight]")

        # Set Progress Bar
        self.progress = CircularProgress()
        self.progress.width = 258
        self.progress.height = 258

        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 30
        self.progress.progress_color = QColor("#316B4F")
        self.progress.text_color = QColor("#262525")
        self.progress.bg_color = QColor("#999797")
        self.progress.setParent(self.ui.preloader)
        self.progress.label_greeting = self.ui.label_greeting
        self.progress.label_greeting_img = ["#", "./src/img/greeting/en-dark.png",
                                            "./src/img/greeting/ta-dark.png", "./src/img/greeting/si-dark.png"]
        self.progress.show()

    # set Shadow Window
    def setShadowWindow(self):
        # Set Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.background.setGraphicsEffect(self.shadow)

    # defalt theme setter
    def default_theme(self):
        logger.debug("The Default Theme Is Runing... [default_theme]")
        try:

            if SETTING_FILE in os.listdir(PATH_CONFIG_DIR):

                setting = Setting.load_superuser()
                if setting["Setting"]["Default-theme"] == "light":
                    self.setThemeLight()
                    self.setIconLight()
                    self.prograssBarLight()
                else:
                    self.setThemeDark()
                    self.setIconDark()
                    self.prograssBarDark()
            else:
                self.setThemeLight()
                self.setIconLight()
                self.prograssBarLight()

        except FileNotFoundError:
            self.setThemeLight()
            self.setIconLight()
            self.prograssBarLight()

    # Update The Prograss Bar
    def update(self):

        def mainwindow():
            main = Main_Window()
            self.close()

        if self.progress_conter >= 100:
            self.timer.stop()
            thread = Thread_Open()
            thread.opening_window.connect(
                lambda: QTimer.singleShot(1200, lambda: mainwindow()))
            thread.start()
            thread.exec_()

        self.progress.set_value(self.progress_conter)
        self.progress_conter += 2

    def animation_create(self):

        logger.debug("Animation of login is working... [ animation_login ]")
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(
            QRect(0, 30, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(
            QRect(0, -410, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def shacke_window(self):

        logger.debug("The shacke function Actived... [ shacke_window ]")

        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(
            actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(
            actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(
            actual_pos.x(), actual_pos.y()))

    # Click Event
    def clickEvent(self, event):

        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:

            logger.info("The Enter Button Clicked... [ clickEvent ]")

            def prosses():
                self.animation_create()
                self.timer = QTimer()
                self.timer.timeout.connect(self.update)
                self.timer.start(35)

            __getuserinput = self.getInputFromUser()
            if __getuserinput != False:

                if checkThePassword(__getuserinput[1]) and \
                    (checkTheEmail(__getuserinput[2]) == True or checkTheEmail(__getuserinput[2]) == None) and \
                        checkTheContactNum(__getuserinput[-1]) and \
                        checkTheUserName(__getuserinput[0]):

                    if checkTheEmail(__getuserinput[2]) == None:
                        obj = Crypto.encrypt_superuser(
                            __getuserinput[0],
                            __getuserinput[1],
                            __getuserinput[-1]
                        )

                    else:
                        obj = Crypto.encrypt_superuser(
                            __getuserinput[0],
                            __getuserinput[1],
                            __getuserinput[-1],
                            __getuserinput[2]
                        )

                    Thread(target=Setting.store_superuser,
                           args=(obj, )).start()
                    logger.debug("The Data was saveing... [clickEvent]")

                    thread_loading = Thread_Loading()
                    thread_loading.prograss_function.connect(
                        lambda: QTimer.singleShot(1400, lambda: prosses()))
                    thread_loading.start()
                    thread_loading.exec_()

                else:
                    self.shacke_window()
            else:
                self.shacke_window()

        elif event.key() == Qt.Key_Escape or event.key == Qt.Key_Enter:
            self.close()

    # Get Input From User
    def getInputFromUser(self):
        __name = self.ui.lineEdit_name.text()
        __pass = self.ui.lineEdit_pass.text()
        __con_pass = self.ui.lineEdit_con_pass.text()
        __email = self.ui.lineEdit_email.text()
        __contact = self.ui.lineEdit_contact.text()

        if __con_pass == __pass:
            return [__name, __pass, __email, __contact]
        return False


class Login_Window(QMainWindow):

    iconReplace = False
    progress_conter = 0

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # remove the frame of window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        logger.debug("Logging Inti function is runing... [ Login_Window ]")

        # Set Theme
        self.default_theme()

        # Set shadow
        self.setShadowWindow()

        # Store User Data
        Store.init()

        # KEY EVENT FOR LOGIN WINDOW
        self.keyPressEvent = self.clickEvent

        self.show()

    # Dark Theme
    def setThemeDark(self):

        logger.debug("Theme is setting... [ setThemeDark ]")

        # Theme Contents
        self.ui.background.setStyleSheet(dark.BACKGROUND_WIDGET)
        self.ui.lineEdit_name.setStyleSheet(dark.LOGIN_LINE_EDIT)
        self.ui.lineEdit_pass.setStyleSheet(dark.LOGIN_LINE_EDIT)

        # TEXT CONTENTS
        self.ui.label_logo.setText(dark.LOGO_OF_WINDOW)

    def setIconDark(self):

        logger.debug("Icon is setting... [ setIconDark ]")

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        if not self.iconReplace:
            logger.debug("Icon is palce setting... [ setIconDark ]")

            setIcon_line(self.ui.lineEdit_name, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_pass, dark.ICON_LOCK)
        else:
            logger.debug("Icon is repalce setting... [ setIconDark ]")

            setIcon_line_(self.ui.lineEdit_name, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_pass, dark.ICON_LOCK)

    def prograssBarDark(self):

        logger.debug("The Prograss Bar is starting... [prograssBarDark]")

        # Set Progress Bar
        self.progress = CircularProgress()
        self.progress.width = 258
        self.progress.height = 258

        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 30
        self.progress.progress_color = QColor("#316B4F")
        self.progress.text_color = QColor("#E6E6E6")
        self.progress.bg_color = QColor("#222222")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()

    # Light Theme

    def setThemeLight(self):

        logger.debug("Theme is setting... [ setThemeLight ]")

        # Theme Contents
        self.ui.background.setStyleSheet(light.BACKGROUND_WIDGET)
        self.ui.lineEdit_name.setStyleSheet(light.LOGIN_LINE_EDIT)
        self.ui.lineEdit_pass.setStyleSheet(light.LOGIN_LINE_EDIT)

        # TEXT CONTENTS
        self.ui.label_logo.setText(light.LOGO_OF_WINDOW)

    def setIconLight(self):

        logger.debug("Icon is setting... [ setIconLight ]")

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        if not self.iconReplace:
            logger.debug("Icon is palce setting... [ setIconLight ]")

            setIcon_line(self.ui.lineEdit_name, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_pass, light.ICON_LOCK)
        else:
            logger.debug("Icon is repalce setting... [ setIconLight ]")

            setIcon_line_(self.ui.lineEdit_name, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_pass, light.ICON_LOCK)

    def prograssBarLight(self):

        logger.debug("The Prograss Bar is starting... [prograssBarLight]")

        # Set Progress Bar
        self.progress = CircularProgress()
        self.progress.width = 258
        self.progress.height = 258

        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.font_size = 20
        self.progress.add_shadow(True)
        self.progress.progress_width = 30
        self.progress.progress_color = QColor("#316B4F")
        self.progress.text_color = QColor("#262525")
        self.progress.bg_color = QColor("#999797")
        self.progress.setParent(self.ui.preloader)
        self.progress.show()

    # set Shadow Window
    def setShadowWindow(self):
        # Set Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.background.setGraphicsEffect(self.shadow)

    # defalt theme setter
    def default_theme(self):

        logger.debug("The Default Theme Is Runing... [default_theme]")
        setting = Setting.load_superuser()
        if setting["Setting"]["Default-theme"] == "light":
            self.setThemeLight()
            self.setIconLight()
            self.prograssBarLight()
        else:
            self.setThemeDark()
            self.setIconDark()
            self.prograssBarDark()

    # Update The Prograss Bar
    def update(self):

        def mainwindow():
            main = Main_Window()
            self.close()

        if self.progress_conter >= 100:
            self.timer.stop()
            thread = Thread_Open()
            thread.opening_window.connect(
                lambda: QTimer.singleShot(1200, lambda: mainwindow()))
            thread.start()
            thread.exec_()

        self.progress.set_value(self.progress_conter)
        self.progress_conter += 2

    def animation_login(self):

        logger.debug("Animation of login is working... [ animation_login ]")
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(
            QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(
            QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def shacke_window(self):

        logger.debug("The shacke function Actived... [ shacke_window ]")

        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(
            actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(
            actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(
            actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(
            actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(
            actual_pos.x(), actual_pos.y()))

    # Click Event
    def clickEvent(self, event):

        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:

            logger.info("The Enter Button Clicked... [ clicEvent ]")

            def prosses():
                self.animation_login()
                self.timer = QTimer()
                self.timer.timeout.connect(self.update)
                self.timer.start(35)

            user = self.getUserInput()
            if user:

                __data = Setting.load_superuser()
                __user = Crypto.decrypt_superuser_user(
                    [__data[SETTING]["Name"][0], __data[SETTING]["Name"][-1]],
                    [__data[SETTING]["Password"][0],
                        __data[SETTING]["Password"][-1]]
                )

                if __user[0] == user[0] and __user[-1] == user[-1]:

                    thread_loading = Thread_Loading()
                    thread_loading.prograss_function.connect(
                        lambda: QTimer.singleShot(1200, lambda: prosses()))
                    thread_loading.start()
                    thread_loading.exec_()

                else:
                    self.shacke_window()

            else:
                self.shacke_window()

        elif event.key() == Qt.Key_Escape or event.key == Qt.Key_Enter:
            self.close()

    def getUserInput(self):
        __name = self.ui.lineEdit_name.text()
        __pwd = self.ui.lineEdit_pass.text()

        if __name != '' and __pwd != '':
            return [__name, __pwd]

        return False


class Error_Window(QDialog):
    def __init__(self, perent_wnd):
        super().__init__(perent_wnd)
        logger.debug("The Mesage Window is Runing.... [Error_Window]")
        self.resize(405, 162)
        self.ui = Ui_error()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.CustomizeWindowHint |
                            Qt.WindowTitleHint | Qt.Dialog)

        self.default_theme()
        self.connect_button_function()

        # remove the frame of window
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Animation
        self.animation()

        self.show()

    def connect_button_function(self):
        self.ui.btn_okay.clicked.connect(self.close)

    def dark_theme(self):
        self.ui.frame_main_window.setStyleSheet(dark.MAIN_FRAME_STYLE)
        self.ui.label_error_text.setStyleSheet(dark.ERROR_INFORMATION_LABEL)
        self.ui.btn_okay.setStyleSheet(dark.ERROR_OKAY_BUTTON)
        self.ui.label_icon.setStyleSheet(
            "margin-top: 10px; margin-bottom: 10px;")

    def light_theme(self):
        self.ui.frame_main_window.setStyleSheet(light.MAIN_FRAME_STYLE)
        self.ui.label_error_text.setStyleSheet(light.ERROR_INFORMATION_LABEL)
        self.ui.btn_okay.setStyleSheet(light.ERROR_OKAY_BUTTON)
        self.ui.label_icon.setStyleSheet(
            "margin-top: 10px; margin-bottom: 10px;")

    def default_theme(self):
        logger.debug("The Default Theme Is Runing... [ [ERROR] default_theme]")
        setting = Setting.load_superuser()
        if setting["Setting"]["Default-theme"] == "light":
            self.light_theme()
        else:
            self.dark_theme()

    def animation(self):

        self.opacity = QGraphicsOpacityEffect()
        self.animation = QPropertyAnimation(self.opacity, b"opacity")
        self.ui.frame_main_window.setGraphicsEffect(self.opacity)
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)

        self.no_effect = QGraphicsOpacityEffect()
        self.animation_two = QPropertyAnimation(self.no_effect, b"opacity")
        self.ui.frame_main_window.setGraphicsEffect(self.opacity)
        self.animation_two.setStartValue(0)
        self.animation_two.setEndValue(1)
        self.animation_two.setDuration(500)

        self.hiding_effect = QGraphicsOpacityEffect()
        self.animation_three = QPropertyAnimation(
            self.hiding_effect, b"opacity")
        self.ui.frame_main_window.setGraphicsEffect(self.opacity)
        self.animation_three.setStartValue(1)
        self.animation_three.setEndValue(0)
        self.animation_two.setDuration(500)

        self.group = QSequentialAnimationGroup()
        self.group.addAnimation(self.animation)
        self.group.addAnimation(self.animation_two)
        self.group.addAnimation(self.animation_three)

        self.group.start()


class PickImageWindow(QFileDialog):

    title = "Pick Your Image"
    default_path = f"C:\\Users\\{os.getlogin()}\\Pictures\\"
    file_format = "Images (*.png *.jpg *.jpeg);;All File (*)"
    path = ""

    def __init__(self):
        super().__init__()

        global path_userImage
        if path_userImage != str():
            self.default_path = path_userImage

        self.path, _ = self.getOpenFileName(self,
                                            self.title,
                                            self.default_path,
                                            self.file_format,
                                            options=self.Options()
                                            )
        path_value = self.path.split("/")
        path_value.pop()
        path = str()
        for name in path_value:
            path += name + "/"
        path_userImage = path
        self.resize(300, 300)

    def getPath(self):
        return self.path


class Main_Window(QMainWindow):

    # window started theme [If it's True, change the theme light]
    theme_button_pressed = False

    # Gender value and status
    __gender = str()
    __status = str()

    # Last Roll ID
    __lastRollID = str()

    # Level And Streem
    __level = str()
    __streem = str()

    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        logger.debug("init function is runing ... [connect ui of main]")

        # Run Default Theme runer
        self.default_theme()

        # Button activity connecter
        self.btnToFunctionConnecter()

        # Label text coping event installer function
        self.label_text_coping_event_installer()

        # Shortcut
        self.button_shortcutKey_connecter()

        # Set The Label Text
        self.setTheAllLabelText()

        self.show()

    # Set The Label Text
    def setTheAllLabelText(self):
        __data = Setting.load_superuser()

        __userinfo = Crypto.decrypt_superuser(
            __data[SETTING]["Name"],
            __data[SETTING]["Password"],
            __data[SETTING]["Contact"],
            __data[SETTING]["E-mail"]
        )
        self.ui.label_show_current_username.setText(
            f""" <html>
                    <head/>
                    <body>
                        <p>
                            <span style=\" font-size:12pt; font-weight:600;\">
                            Current User Name : {__userinfo[0]}
                            </span>
                        </p>
                    </body>
                </html>
            """
        )
        self.ui.label_current_email.setText(
            f""" <html>
                    <head/>
                    <body>
                        <p>
                            <span style=\" font-size:12pt; font-weight:600;\">
                            Current E-mail ID : {__userinfo[2]}
                            </span>
                        </p>
                    </body>
                </html>
            """
        )
        self.ui.label_show_current_contact_number.setText(
            f""" <html>
                    <head/>
                    <body>
                        <p>
                            <span style=\" font-size:12pt; font-weight:600;\">
                            Current Contact Number : {__userinfo[-1]}
                            </span>
                        </p>
                    </body>
                </html>
            """
        )

    # Button Conntecter
    def btnToFunctionConnecter(self):
        logger.debug(
            "Button function connecter Actived... [ btnToFunctionConnecter ]")

        # THEME BUTTON FOE CHAMGE THEME
        self.ui.btn_setTheme.clicked.connect(self.setTheme)

        # Chnagers
        self.ui.btn_save_username.clicked.connect(
            self.thread_connecter_access_name)
        self.ui.btn_save_password.clicked.connect(
            self.thread_connecter_access_pwd)
        self.ui.btn_save_contact_number.clicked.connect(
            self.thread_connecter_access_cont)
        self.ui.btn_save_change_email.clicked.connect(
            self.thread_connecter_access_email)

        # inuter user
        self.ui.btn_addInter_teacher.clicked.connect(
            self.store_interuser_data
        )
        self.ui.btn_upload_image_inter_teacher.clicked.connect(
            self.pickImageFromComputer_teachers)

        # None-Inter
        self.ui.btn_addInter_teacher_none.clicked.connect(
            self.store_noneinteruser_data)
        self.ui.btn_upload_image_inter_teacher_none.clicked.connect(
            self.pickImageFromComputer_teacher_none)

        # Primary
        self.ui.btn_addLower_primary.clicked.connect(
            self.store_primaryuser_data
        )
        self.ui.btn_upload_image_primary.clicked.connect(
            self.pickImageFromComputer_primary
        )

        # Ordnary
        self.ui.btn_addlower.clicked.connect(
            self.store_ordnaryuser_data
        )
        self.ui.btn_upload_image_lower.clicked.connect(
            self.pickImageFromComputer_ordnary
        )

        # Advanced
        self.ui.btn_addLower_adv.clicked.connect(
            self.store_advanceduser_data
        )
        self.ui.btn_upload_image_advanced.clicked.connect(
            self.pickImageFromComputer_advanced
        )

    def label_text_coping_event_installer(self):
        self.ui.label_show_roll_number.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_number.installEventFilter(self)
        self.ui.label_show_roll_number.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_show_roll_number.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.label_show_roll_number_none.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_number_none.installEventFilter(self)
        self.ui.label_show_roll_number_none.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_show_roll_number_none.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.label_show_roll_primary.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_primary.installEventFilter(self)
        self.ui.label_show_roll_primary.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_show_roll_primary.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.label_show_roll_number_lower.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_number_lower.installEventFilter(self)
        self.ui.label_show_roll_number_lower.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_show_roll_number_lower.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui.label_show_roll_ad.setTextInteractionFlags(
            Qt.TextSelectableByMouse)
        self.ui.label_show_roll_ad.installEventFilter(self)
        self.ui.label_show_roll_ad.setCursor(QCursor(Qt.IBeamCursor))
        self.ui.label_show_roll_ad.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

    def button_shortcutKey_connecter(self):

        self.ui.btn_teahers.setShortcut("Ctrl+t")
        self.ui.btn_none_teaher.setShortcut("Ctrl+n")
        self.ui.btn_primary.setShortcut("Ctrl+p")
        self.ui.btn_advanced.setShortcut("Ctrl+a")
        self.ui.btn_ordinary.setShortcut("Ctrl+o")

        self.ui.btn_inter.setShortcut("Ctrl+Shift+i")
        self.ui.btn_lower.setShortcut("Ctrl+Shift+l")

        self.ui.btn_page_home.setShortcut("Ctrl+Shift+h")
        self.ui.btn_page_left.setShortcut("Ctrl+Shift+r")
        self.ui.btn_page_search.setShortcut("Ctrl+Shift+s")
        self.ui.btn_page_analytics.setShortcut("Ctrl+Shift+a")
        self.ui.btn_edit_setting.setShortcut("Ctrl+Shift+e")

        # Inter user
        if self.ui.stackedWidget.currentWidget() == self.ui.page_add_inter:
            self.ui.btn_addInter_teacher.setShortcut("Return")
            self.ui.btn_go_inter_teacher.setShortcut("Backspace")
            self.ui.btn_upload_image_inter_teacher.setShortcut("Ctrl+u")

        # None Inter user
        elif self.ui.stackedWidget.currentWidget() == self.ui.page_add_inter_none:
            self.ui.btn_addInter_teacher_none.setShortcut("Return")
            self.ui.btn_go_inter_teacher_none.setShortcut("Backspace")
            self.ui.btn_upload_image_inter_teacher_none.setShortcut("Ctrl+u")

        # Primary
        elif self.ui.stackedWidget.currentWidget() == self.ui.page:
            self.ui.btn_addLower_primary.setShortcut("Return")
            self.ui.btn_go_home_primary.setShortcut("Backspace")
            self.ui.btn_upload_image_primary.setShortcut("Ctrl+u")

        # Ordnary
        elif self.ui.stackedWidget.currentWidget() == self.ui.page_add_lower:
            self.ui.btn_addlower.setShortcut("Return")
            self.ui.btn_go_home_lower.setShortcut("Backspace")
            self.ui.btn_upload_image_lower.setShortcut("Ctrl+u")

        # Advanced
        elif self.ui.stackedWidget.currentWidget() == self.ui.page_add_advan:
            self.ui.btn_addLower_adv.setShortcut("Return")
            self.ui.btn_go_home_ad.setShortcut("Backspace")
            self.ui.btn_upload_image_advanced.setShortcut("Ctrl+u")

    # light theme of window

    def connect_functiom_light(self):

        logger.debug("Connect function Actived... [ connect_functiom_light ]")

        # Toggle Burguer Menu
        self.ui.btn_Toggle.clicked.connect(
            lambda: UIFunctions.thread_connecter_light(self, 200, True))

        # Setting Bar Animation
        self.ui.btn_hidden_username_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_light_connecter(self,  self.ui.frame_user_name_changer.height(
        ), self.ui.frame_user_name_changer, self.ui.frame_name_changer_content_page, True, self.ui.btn_hidden_username_bar, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))
        self.ui.btn_hidden_email_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_light_connecter(self,  self.ui.frame_email_changer.height(
        ), self.ui.frame_email_changer, self.ui.frame_email_changer_content_bar, True, self.ui.btn_hidden_email_bar, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))
        self.ui.btn_hidden_contact_number_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_light_connecter(self,  self.ui.frame_contect_number_changer.height(
        ), self.ui.frame_contect_number_changer, self.ui.frame_contect_number_changer_content_bar, True, self.ui.btn_hidden_contact_number_bar, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))
        self.ui.btn_hidden_passowd_changer_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_light_connecter(self,  self.ui.frame_password_changer.height(
        ), self.ui.frame_password_changer, self.ui.frame_password_changer_content_bar, True, self.ui.btn_hidden_passowd_changer_bar, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))

        self.ui.btn_hidden_options.clicked.connect(lambda: UIFunctions.settingHiddenBar_two_light(self,  self.ui.frame_more_options.height(
        ), self.ui.frame_more_options, self.ui.frame_more_options_contect_bar, True, self.ui.btn_hidden_options, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))
        self.ui.btn_hidden_adout.clicked.connect(lambda: UIFunctions.settingHiddenBar_two_light(self, self.ui.frame_adout.height(
        ), self.ui.frame_adout, self.ui.frame_content_adout, True, self.ui.btn_hidden_adout, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))

        # SUPER USER BTN
        self.ui.btn_superuser.clicked.connect(
            lambda: UIFunctions.userSide_toggle_light_connecter(self, 300, True))

        # BUTTONE CONNECTER
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        UIFunctions.current_page_light(self)

        self.ui.btn_page_home.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_page_left.clicked.connect(
            lambda: UIFunctions.left_light(self))
        self.ui.btn_page_search.clicked.connect(
            lambda: UIFunctions.search_light(self))
        self.ui.btn_setting.clicked.connect(
            lambda: UIFunctions.setting_light(self))
        self.ui.btn_page_analytics.clicked.connect(
            lambda: UIFunctions.analytics_light(self))
        self.ui.btn_go_inter_teacher.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_inter_teacher_none.clicked.connect(
            lambda: UIFunctions.home_light(self))

        # Super User Btn
        self.ui.btn_edit_setting.clicked.connect(
            lambda: UIFunctions.setting_light(self))

        # Inter and Lower Btn
        self.ui.btn_inter.clicked.connect(
            lambda: UIFunctions.callInter_window_light(self)
        )
        self.ui.btn_lower.clicked.connect(
            lambda: UIFunctions.callLower_window_light(self)
        )

        # Connect into btn_ordinary
        self.ui.btn_ordinary.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_lower))
        # Connect into btn_advanced
        self.ui.btn_advanced.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_advan))
        # Connect into btn_primary
        self.ui.btn_primary.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page))

        # Conntect into btn_teahers
        self.ui.btn_teahers.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_inter)
        )
        # Conntect into btn_none_teaher
        self.ui.btn_none_teaher.clicked.connect(
            lambda: UIFunctions.call_input_menu(
                self, self.ui.page_add_inter_none)
        )

        # Go Home Button
        self.ui.btn_go_inter_teacher.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_inter_teacher_none.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_home_primary.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_home_ad.clicked.connect(
            lambda: UIFunctions.home_light(self))

    def setTheme_for_window_light(self):

        logger.debug("Light Theme Actived... [ setTheme_for_window_light ]")

        self.ui.scrollArea_2.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_resalt.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_3.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_content.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_4.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_add_info.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_advanced_add.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_primary_add.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_lower_add.setStyleSheet(light.SCROLLAREA)

        self.ui.scrollArea_add_info_none.setStyleSheet(light.SCROLLAREA)

        self.ui.comboBox_stream_primary.setStyleSheet(light.COMBO_BOX)

        self.setStyleSheet(light.MAIN_WINDOW_BACKGROUND)
        self.ui.btn_Toggle.setStyleSheet(light.TOGGLE_BTN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN)
        self.ui.TopBar.setStyleSheet(light.TOP_BAR_BACKGROUND)
        self.ui.frame_top.setStyleSheet(light.TOP_FRAME_BACKGROUND)
        self.ui.frame_return_bar.setStyleSheet(light.FRAME_RETURN_BAR)
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN)
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN)
        self.ui.frame_backup.setStyleSheet(light.FRAME_BACKUP)
        self.ui.btn_superuser.setStyleSheet(light.SUPERUSER_BTN)
        self.ui.frame_left_menu.setStyleSheet(light.FRAME_LEFT_MENU)
        self.ui.page_add_students.setStyleSheet(light.PAGE_ADD_STUDENTS)
        self.ui.frame_top_menus.setStyleSheet(light.FRAME_TOP_MENU)
        self.ui.frame_page.setStyleSheet(light.FRAME_PAGE)
        self.ui.frame_2.setStyleSheet(light.FRAME_2)
        self.ui.btn_primary.setStyleSheet(light.PRIMARY_BTN)
        self.ui.btn_ordinary.setStyleSheet(light.ORDNARY_BTN)
        self.ui.btn_advanced.setStyleSheet(light.ADVANCED_BTN)
        self.ui.btn_teahers.setStyleSheet(light.ADVANCED_BTN)
        self.ui.btn_none_teaher.setStyleSheet(light.ADVANCED_BTN)
        self.ui.frame_add_btns_inters.setStyleSheet(light.FRAME_2)

        # INTER USER COMPENTS
        self.ui.lineEdit_full_name.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit__name_initial.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_inc_no.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_personal_contact.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_WOP_no.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_agrakara_no.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_spouse_name.setStyleSheet(light.LINE_EDIT)

        self.ui.lineEdit_nature_of_appoin.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_present_grade.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_appoint_subject.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_personal_contact.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_professional_qualif.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_educational_qualif.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_email_id.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_teaching_regist_no.setStyleSheet(light.LINE_EDIT)

        self.ui.textEdit_emergency.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_working_address.setStyleSheet(light.TEXT_EDIT)

        self.ui.dateEdit_present_date.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_increment_date.setStyleSheet(light.DATE_EDIT)

        self.ui.dateEdit_DOB.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_first_appointment_date.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_appointment_date.setStyleSheet(light.DATE_EDIT)

        self.ui.radioButton_married.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_unmarried.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_male.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other.setStyleSheet(light.RASIO_BUTTON)

        self.ui.scrollAreaWidgetInfo.setStyleSheet(
            light.INTER_ADD_TEACHER_BACKGROUND)

        self.ui.label_date_app_to_school_text.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_appointment_data_text.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_DOB_text.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_info_Inter_face.setStyleSheet(
            light.LABEL_INFO_INTER_FACE)
        self.ui.label_info_user_inter_1.setStyleSheet(
            light.LABEL_INFO_INTER_USER_1)
        self.ui.label_info_Inter_1.setStyleSheet(light.LABEL_INFO_INTER_1)
        self.ui.info_inter_left_1.setStyleSheet(light.LABEL_INFO_INTER_1)
        self.ui.label_info_user_left_inter_1.setStyleSheet(
            light.LABEL_INFO_INTER_USER_1)
        self.ui.label_icon_inter_teacher.setStyleSheet(light.LABEL_ICON_INTER)
        self.ui.label_show_roll_number.setStyleSheet(
            light.LABEL_SHOW_ROLL_INTER)
        self.ui.label_inter_head.setStyleSheet(
            light.ANALYTICS_LABEL_INTER_HEAD)

        self.ui.groupBox_civil.setStyleSheet(light.GROUP)
        self.ui.groupBox_gender.setStyleSheet(light.GROUP)
        self.ui.groupBox_increment_date.setStyleSheet(light.GROUP)
        self.ui.groupBox_present_grade_and_date.setStyleSheet(light.GROUP)
        self.ui.groupBox_gender_primary.setStyleSheet(light.GROUP)
        self.ui.groupBox_gender_advanced.setStyleSheet(light.GROUP)
        self.ui.groupBox_gender_lower.setStyleSheet(light.GROUP)

        self.ui.widget_inter_1.setStyleSheet(light.WIDGET_INTER_1)
        self.ui.widget_inter_left_1.setStyleSheet(light.WIDGET_INTER_1)

        self.ui.label_info_Inter_face.setStyleSheet(light.LABEL_ACTIVE_LEFT)
        self.ui.label_info_inter_left_face.setStyleSheet(
            light.LABEL_ACTIVE_LEFT)

        self.ui.frame_inter_delet_bar_1.setStyleSheet(
            light.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_inter_left_btns_bar_1.setStyleSheet(
            light.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_main_inter_info_inter_teacher.setStyleSheet(
            light.FRMAE_MAIN_INTER_INFO)
        self.ui.frame_inter.setStyleSheet(light.ANALYTICS_FRAME_INTER)

        self.ui.btn_delete_inter_1.setStyleSheet(light.DELETE_INTER_BTN_1)
        self.ui.btn_delete_inter_left_1.setStyleSheet(light.DELETE_INTER_BTN_1)
        self.ui.btn_upload_image_inter_teacher.setStyleSheet(
            light.UPLOAD_IMAGE_BTN)
        self.ui.btn_addInter_teacher.setStyleSheet(light.ADDINTER_BTN)
        self.ui.btn_go_inter_teacher.setStyleSheet(light.GOHOME_INTER_BTN)
        self.ui.btn_edit_interuser.setStyleSheet(light.DELETE_INTER_BTN_1)
        self.ui.btn_edit_interuser_left.setStyleSheet(light.DELETE_INTER_BTN_1)

        self.ui.page_add_inter.setStyleSheet(light.PAGE_ADD_INTER)
        self.ui.page_inter_add.setStyleSheet(light.PAGE_ADD_INTER)

        # NONE TEACHER USER COMPENTS
        self.ui.lineEdit_nature_of_appoin_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_personal_contact_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_professional_qualif_none.setStyleSheet(
            light.LINE_EDIT)
        self.ui.lineEdit_educational_qualif_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_email_id_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_full_name_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit__name_initial_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_inc_no_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_personal_contact_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_WOP_no_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_agrakara_no_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_spouse_name_none.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_salary_none.setStyleSheet(light.LINE_EDIT)

        self.ui.dateEdit_increment_date_none.setStyleSheet(light.DATE_EDIT)

        self.ui.textEdit_emergency_none.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_working_address_none.setStyleSheet(light.TEXT_EDIT)

        self.ui.dateEdit_DOB_none.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_first_appointment_date_none.setStyleSheet(
            light.DATE_EDIT)
        self.ui.dateEdit_appointment_date_none.setStyleSheet(light.DATE_EDIT)

        self.ui.radioButton_married_none.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_unmarried_none.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_male_none.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female_none.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other_none.setStyleSheet(light.RASIO_BUTTON)

        self.ui.scrollAreaWidgetInfo.setStyleSheet(
            light.INTER_ADD_TEACHER_BACKGROUND)

        self.ui.label_date_app_to_school_text_none.setStyleSheet(
            light.LABEL_COLOR)
        self.ui.label_appointment_data_text_none.setStyleSheet(
            light.LABEL_COLOR)
        self.ui.label_DOB_text_none.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_icon_none.setStyleSheet(light.LABEL_ICON_INTER)
        self.ui.label_show_roll_number_none.setStyleSheet(
            light.LABEL_SHOW_ROLL_INTER)

        self.ui.label_info_user_noneinter.setStyleSheet(
            light.LABEL_INFO_INTER_USER_1)
        self.ui.label_info_noneinter.setStyleSheet(
            light.LABEL_INFO_INTER_1)
        self.ui.label_info_NoneInter_face.setStyleSheet(
            light.LABEL_ACTIVE_LEFT)

        self.ui.btn_delete_noneinter.setStyleSheet(light.DELETE_INTER_BTN_1)
        self.ui.btn_edit_noneinteruser.setStyleSheet(light.DELETE_INTER_BTN_1)

        self.ui.label_info_user_noneinter_left.setStyleSheet(
            light.LABEL_INFO_INTER_USER_1)
        self.ui.label_info_noneinter_left.setStyleSheet(
            light.LABEL_INFO_INTER_1)
        self.ui.label_info_NoneInter_face_left.setStyleSheet(
            light.LABEL_ACTIVE_LEFT)

        self.ui.btn_delete_noneinter_left.setStyleSheet(
            light.DELETE_INTER_BTN_1)
        self.ui.btn_edit_noneinteruser_left.setStyleSheet(
            light.DELETE_INTER_BTN_1)
        self.ui.page_add_inter_none.setStyleSheet(light.PAGE_ADD_INTER)

        self.ui.frame_main_inter_info_inter_teache_none.setStyleSheet(
            light.FRMAE_MAIN_INTER_INFO)

        self.ui.frame_noneinter_delet_bar.setStyleSheet(
            light.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_noneinter_delet_bar_left.setStyleSheet(
            light.FRAME_INTER_DELETE_BAR_1)

        self.ui.groupBox_civil_none.setStyleSheet(light.GROUP)
        self.ui.groupBox_gender_none.setStyleSheet(light.GROUP)
        self.ui.groupBox_increment_date_none.setStyleSheet(light.GROUP)

        self.ui.btn_upload_image_inter_teacher_none.setStyleSheet(
            light.UPLOAD_IMAGE_BTN)
        self.ui.btn_addInter_teacher_none.setStyleSheet(light.ADDINTER_BTN)
        self.ui.btn_go_inter_teacher_none.setStyleSheet(light.GOHOME_INTER_BTN)
        self.ui.widget_noneinter.setStyleSheet(light.WIDGET_INTER_1)
        self.ui.widget_noneinter_left.setStyleSheet(light.WIDGET_INTER_1)

        # PRIMARY LOWER USER COMPENTS
        self.ui.dateEdit_date_of_birth_primary.setStyleSheet(light.DATE_EDIT)
        self.ui.lineEdit_religion_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_name_full_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_name_initial_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_name_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_name_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_job_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_job_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.textEdit_address_home.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_address_office.setStyleSheet(light.TEXT_EDIT)
        self.ui.lineEdit_admission_no_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_parent_contact_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.dateEdit_date_admission_primary.setStyleSheet(light.DATE_EDIT)
        self.ui.lineEdit_no_siblings_primary.setStyleSheet(light.LINE_EDIT)

        self.ui.radioButton_male_primary_2.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female_primary_2.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other_primary_2.setStyleSheet(light.RASIO_BUTTON)

        self.ui.label_inforem_admission_primary.setStyleSheet(
            light.GLOBAL_LABEL)
        self.ui.label_info_gender_primary.setStyleSheet(light.GLOBAL_LABEL)
        self.ui.label_inforem_date_of_birth_primary.setStyleSheet(
            light.GLOBAL_LABEL)
        self.ui.label_info_user_lower_pri.setStyleSheet(
            light.LABEL_INFO_PRIMARY_USER_1)
        self.ui.label_info_lower_pri.setStyleSheet(light.LABEL_INFO_PRIMARY_1)
        self.ui.label_icon_primary.setStyleSheet(light.LABEL_ICON_PRIMARY)
        self.ui.label_show_roll_primary.setStyleSheet(
            light.LABEL_SHOW_ROLL_PRIMARY)
        self.ui.info_lower_left_pri.setStyleSheet(light.LABEL_INFO_PRIMARY_1)
        self.ui.label_info_user_left_lower_pri.setStyleSheet(
            light.LABEL_INFO_PRIMARY_USER_1)

        self.ui.btn_addLower_primary.setStyleSheet(light.ADDLOWER_PRIMARY_BTN)
        self.ui.btn_go_home_primary.setStyleSheet(light.GOHOME_PRIMARY_BTN)
        self.ui.btn_delete_lower_pri.setStyleSheet(light.DELETE_PRIMARY_BTN_1)

        self.ui.frame_inter_delet_bar_pri.setStyleSheet(
            light.FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.frame_main_content_for_primary.setStyleSheet(
            light.FRAME_MAIN_CONTENT_FOR_PRIMARY)
        self.ui.frame_coments_ad_2.setStyleSheet(
            light.FRAME_CONTENT_ADVANCED_2)
        self.ui.frame_lower_btns_bar_pri.setStyleSheet(
            light.FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.frame_lower_prim.setStyleSheet(light.ANALYTICS_FRAME_PRIM)

        self.ui.page.setStyleSheet(light.PAGE_ADD_PRIMARY)

        self.ui.widget_lower_pri.setStyleSheet(light.WIDGET_PRIMARY_1)
        self.ui.widget_lower_left_pri.setStyleSheet(light.WIDGET_PRIMARY_1)

        self.ui.label_info_pri_face.setStyleSheet(light.LABEL_ACTIVE_LEFT)
        self.ui.label_info_pri_left_face.setStyleSheet(light.LABEL_ACTIVE_LEFT)

        self.ui.btn_delete_lower_left_pri.setStyleSheet(
            light.DELETE_PRIMARY_BTN_1)
        self.ui.btn_upload_image_primary.setStyleSheet(light.UPLOAD_IMAGE_BTN)
        self.ui.btn_edit_lower.setStyleSheet(light.DELETE_PRIMARY_BTN_1)
        self.ui.btn_edit_lower_left.setStyleSheet(light.DELETE_PRIMARY_BTN_1)

        # ORDNARY LOWER USER COMPENTS
        self.ui.lineEdit_name_full_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_name_initial_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_name_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_name_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_job_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_job_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_no_siblings_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_religion_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.textEdit_address_home_lower.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_address_office_lower.setStyleSheet(light.TEXT_EDIT)
        self.ui.comboBox_stream_lower.setStyleSheet(light.COMBO_BOX)
        self.ui.lineEdit_parent_contact_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_admission_no_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.dateEdit_date_admission_lower.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_date_of_birth_lower.setStyleSheet(light.DATE_EDIT)

        self.ui.radioButton_male_lower_2.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female_lower_2.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other_lower_2.setStyleSheet(light.RASIO_BUTTON)

        self.ui.frame_inter_delet_bar_3.setStyleSheet(
            light.FRAME_LOWER_DELETE_BAR_1)
        self.ui.frame_lower_left_btns_bar_1.setStyleSheet(
            light.FRAME_LOWER_DELETE_BAR_1)
        self.ui.frame_lower.setStyleSheet(light.ANALYTICS_FRAME_LOWER)
        self.ui.frame_main_lower_info.setStyleSheet(
            light.FRAME_MAIN_LOWER_INFO)

        self.ui.label_inforem_admission_lower.setStyleSheet(light.GLOBAL_LABEL)
        self.ui.label_info_gender_lower.setStyleSheet(light.GLOBAL_LABEL)
        self.ui.label_inforem_date_of_birth_lower.setStyleSheet(
            light.GLOBAL_LABEL)
        self.ui.label_info_lower_1.setStyleSheet(light.LABEL_INFO_LOWER_1)
        self.ui.label_info_user_lower_1.setStyleSheet(
            light.LABEL_INFO_LOWER_USER_1)
        self.ui.info_lower_1.setStyleSheet(light.LABEL_INFO_LOWER_1)
        self.ui.label_info_user_left_lower_1.setStyleSheet(
            light.LABEL_INFO_LOWER_USER_1)
        self.ui.label_lower_head.setStyleSheet(
            light.ANALYTICS_LABEL_LOWER_HEAD)
        self.ui.label_icon_lower.setStyleSheet(light.LABEL_ICON_LOWER)
        self.ui.label_show_roll_number_lower.setStyleSheet(
            light.LABEL_SHOW_ROLL_LOWER)

        self.ui.widget_lower_1.setStyleSheet(light.WIDGET_LOWER_1)
        self.ui.widget_lower_left_1.setStyleSheet(light.WIDGET_LOWER_1)

        self.ui.label_info_lower_face.setStyleSheet(light.LABEL_ACTIVE_LEFT)
        self.ui.label_info_lower_left_face.setStyleSheet(
            light.LABEL_ACTIVE_LEFT)

        self.ui.btn_delete_lower_1.setStyleSheet(light.DELETE_LOWER_BTN_1)
        self.ui.btn_delete_lower_left_1.setStyleSheet(light.DELETE_LOWER_BTN_1)
        self.ui.btn_upload_image_lower.setStyleSheet(light.UPLOAD_IMAGE_BTN)
        self.ui.btn_addlower.setStyleSheet(light.ADDLOWER_LOWER_BTN)
        self.ui.btn_go_home_lower.setStyleSheet(light.GOHOME_LOWER_BTN)
        self.ui.btn_edit_pri.setStyleSheet(light.DELETE_LOWER_BTN_1)
        self.ui.btn_edit_pri_left.setStyleSheet(light.DELETE_LOWER_BTN_1)

        self.ui.page_add_lower.setStyleSheet(light.PAGE_ADD_LOWER)

        # ADVANCED LOWER USER COMPENTS
        self.ui.lineEdit_name_initial_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_name_full_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_religion_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_address_office_ad.setStyleSheet(light.TEXT_EDIT)
        self.ui.lineEdit_home_address_ad.setStyleSheet(light.TEXT_EDIT)
        self.ui.lineEdit_admission_no_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_name_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_name_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_job_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_job_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_parent_contact_no_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_siblings_ad.setStyleSheet(light.LINE_EDIT)

        self.ui.comboBox_level_ad.setStyleSheet(light.COMBO_BOX)
        self.ui.comboBox_stream.setStyleSheet(light.COMBO_BOX)

        self.ui.dateEdit_date_of_admission_ad.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_date_of_birth_ad.setStyleSheet(light.DATE_EDIT)

        self.ui.radioButton_male_ad.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female_ad.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other_ad.setStyleSheet(light.RASIO_BUTTON)

        self.ui.label_inforem_date_of_birth_ad.setStyleSheet(
            light.GLOBAL_LABEL)
        self.ui.label_icon_.setStyleSheet(light.LABEL_ICON_)
        self.ui.label_show_roll_ad.setStyleSheet(
            light.LABEL_SHOW_ROLL_ADVANCED)
        self.ui.label_info_lower_advan.setStyleSheet(
            light.LABEL_INFO_ADVANCED_1)
        self.ui.label_info_user_lower_advan.setStyleSheet(
            light.LABEL_INFO_ADVANCED_USER_1)
        self.ui.info_lower_left_advan.setStyleSheet(
            light.LABEL_INFO_ADVANCED_1)
        self.ui.label_info_user_left_lower_advan.setStyleSheet(
            light.LABEL_INFO_ADVANCED_USER_1)
        self.ui.label_advanced_level_13.setStyleSheet(
            light.LABEL_ADVANCED_LEVEL_13)
        self.ui.label_advanced_level_12.setStyleSheet(
            light.LABEL_ADVANCED_LEVEL_12)
        self.ui.label_gender_ad.setStyleSheet(light.GLOBAL_LABEL)
        self.ui.label_date_admission_ad.setStyleSheet(light.GLOBAL_LABEL)

        self.ui.page_add_advan.setStyleSheet(light.PAGE_ADD_ADVAN)

        self.ui.frame_coments_ad.setStyleSheet(light.FRAME_CONTENT_ADVANCED)
        self.ui.frame_main_content_for_advance.setStyleSheet(
            light.FRAME_MAIN_CONTENT_FOR_ADVANCED)
        self.ui.frame_inter_delet_bar_advan.setStyleSheet(
            light.FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.frame_lower_btns_bar_advan.setStyleSheet(
            light.FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.frame_lower_advan.setStyleSheet(light.ANALYTICS_FRAME_ADVAN)
        self.ui.frame_advanced_level_12.setStyleSheet(
            light.FRAME_ADVANCED_LEVEL_12)
        self.ui.frame_advanced_level_13.setStyleSheet(
            light.FRAME_ADVANCED_LEVEL_13)

        self.ui.btn_addLower_adv.setStyleSheet(light.ADDLOWER_ADVANCED_BTN)
        self.ui.btn_go_home_ad.setStyleSheet(light.GOHOME_ADVANCED_BTN)
        self.ui.btn_delete_lower_advan.setStyleSheet(
            light.DELETE_ADVANCED_BTN_1)
        self.ui.btn_delete_lower_left_advan.setStyleSheet(
            light.DELETE_ADVANCED_BTN_1)
        self.ui.btn_upload_image_advanced.setStyleSheet(light.UPLOAD_IMAGE_BTN)
        self.ui.btn_edit_advan.setStyleSheet(light.DELETE_ADVANCED_BTN_1)
        self.ui.btn_edit_advan_left.setStyleSheet(light.DELETE_ADVANCED_BTN_1)

        self.ui.widget_lower_advan.setStyleSheet(light.WIDGET_ADVANCED_1)
        self.ui.widget_lower_left_advan.setStyleSheet(light.WIDGET_ADVANCED_1)

        self.ui.label_info_advan_face.setStyleSheet(light.LABEL_ACTIVE_LEFT)
        self.ui.label_info_advan_left_face.setStyleSheet(
            light.LABEL_ACTIVE_LEFT)

        # SUPER USER COMPENTS
        self.ui.lineEdit_username_change_input.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_change_email_input.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_contact_number_input.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_passord_input.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_repassword_input.setStyleSheet(light.LINE_EDIT)

        self.ui.frame_user_name_changer.setStyleSheet(
            light.SETTING_NAME_CHANGER)
        self.ui.frame_more_options.setStyleSheet(light.SETTING_FRAME_MORE_OP)
        self.ui.frame_email_changer.setStyleSheet(
            light.SETTING_FRAME_EMAIL_CHANGER)
        self.ui.frame_contect_number_changer.setStyleSheet(
            light.SETTING_FRAME_CONTECT_NUM_CHANGER)
        self.ui.frame_password_changer.setStyleSheet(
            light.SETTING_FRAME_PASSWORD_CHANGER)
        self.ui.frame_super_user.setStyleSheet(light.FRAME_SUPERUSER)

        self.ui.label_username_title.setStyleSheet(
            light.SETTING_USER_NAME_TITLE)
        self.ui.label_show_current_username.setStyleSheet(
            light.SETTING_LABEL_SHOW_CURRENT_USERNAME)
        self.ui.label_title.setStyleSheet(light.SETTING_LABEL_TITLE)
        self.ui.label_reload_info.setStyleSheet(light.SETTING_LABEL_RELOAD)
        self.ui.label_reset_info.setStyleSheet(light.SETTING_LABEL_INFO_RESET)
        self.ui.label_change_email_title.setStyleSheet(
            light.SETTING_LABEL_CHANGE_EMAIL_TITLE)
        self.ui.label_current_email.setStyleSheet(
            light.SETTING_LABEL_CURRENT_EMAIL)
        self.ui.label_change_contact_number_title.setStyleSheet(
            light.SETTING_LABEL_CHANGE_CONTECT_NUM_TITLE)
        self.ui.label_show_current_contact_number.setStyleSheet(
            light.SETTING_SHOW_CURRENT_CONTECT_NUM)
        self.ui.label_change_password_title.setStyleSheet(
            light.SETTING_LABEL_CHANGE_PASSWORD_TITLE)
        self.ui.label_super_icon.setStyleSheet(light.LABEL_SUPERUSER_ICON)
        self.ui.label_infor_super.setStyleSheet(light.LABEL_INFO_SUPERUSER)

        self.ui.btn_hidden_username_bar.setStyleSheet(
            light.SETTING_USERNAME_HIDDEN_BTN)
        self.ui.btn_save_username.setStyleSheet(
            light.SETTING_SAVE_USERNAME_BTN)
        self.ui.btn_hidden_options.setStyleSheet(light.SETTING_HIDDEN_BTN_OP)
        self.ui.btn_reload.setStyleSheet(light.SETTING_RELOAD_BTN)
        self.ui.btn_reset.setStyleSheet(light.SETTING_RESET_BTN)
        self.ui.btn_logout.setStyleSheet(light.SETTING_LOGOUT_BTN)
        self.ui.btn_hidden_email_bar.setStyleSheet(
            light.SETTING_HIDDEN_EMAIL_BTN)
        self.ui.btn_save_change_email.setStyleSheet(
            light.SETTING_SAVE_EMAIL_BTN)
        self.ui.btn_hidden_contact_number_bar.setStyleSheet(
            light.SETTING_HIDDEN_BTN_CONTECT)
        self.ui.btn_save_contact_number.setStyleSheet(
            light.SETTING_SAVE_CONTECT_NUM_BTN)
        self.ui.btn_hidden_passowd_changer_bar.setStyleSheet(
            light.SETTING_PASSWORD_CHANGER_BTN)
        self.ui.btn_save_password.setStyleSheet(
            light.SETTING_SAVE_PASSWORD_BTN)

        # SOFTWARE COMPENTS
        self.ui.lineEdit_rollSearch.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_nameSearch.setStyleSheet(light.LINE_EDIT)

        self.ui.btn_nameSearch.setStyleSheet(light.SEARCH_BAR_BTN)
        self.ui.btn_rollSearch.setStyleSheet(light.SEARCH_BAR_BTN)
        self.ui.btn_edit_setting.setStyleSheet(light.EDIT_SETTING_BTN)
        self.ui.btn_hidden_adout.setStyleSheet(light.HIDDEN_ABOUT_BTN)

        self.ui.frame_main_home_bar.setStyleSheet(light.FRAME_MAIN_HOME_BAR)
        self.ui.frame_main_left_bar.setStyleSheet(light.FRAME_MAIN_LEFT_BAR)
        self.ui.frame_main_search_bar.setStyleSheet(
            light.FRAME_MAIN_SEARCH_BAR)
        self.ui.frame_searching_main.setStyleSheet(light.FRAME_SEARCHING_MAIN)
        self.ui.frame_title_search.setStyleSheet(light.FRAME_TITLE_SEARCH)
        self.ui.frame_search_bar_itmes.setStyleSheet(
            light.FRAME_SEARCH_BAR_ITEMS)
        self.ui.frame_main_setting_bar.setStyleSheet(light.SETTING_BACKGROUND)
        self.ui.frame.setStyleSheet(light.SETTING_FRAME)
        self.ui.frame_content.setStyleSheet(light.ANALYTICS_FRAME_CONTENT)
        self.ui.frame_adout.setStyleSheet(light.FRAME_ABOUT)
        self.ui.frame_content_adout.setStyleSheet(light.FRAME_CONTENT_ABOUT)

        self.ui.label_more_info_adout.setStyleSheet(light.LABEL_MORE_ABOUT)
        self.ui.label.setStyleSheet(light.SETTING_LABEL)
        self.ui.label_info_adout.setStyleSheet(light.LABEL_INFO_ABOUT)

        self.ui.page_content_Input.setStyleSheet(light.PAGE_CONTECT)

        self.ui.scrollAreaWidgetContents.setStyleSheet(light.SCROLLAREA_WIDGET)
        self.ui.analytics.setStyleSheet(light.ANALYTICS)

        self.ui.frame_setTheme.setStyleSheet(light.SETTING_FRAME_SETTHEME)
        self.ui.label_theme_set_info.setStyleSheet(light.SETTING_LABEL_THEME)
        self.ui.btn_setTheme.setStyleSheet(light.THEME_BTN)
        self.ui.comboBox_theme_items.setStyleSheet(light.COMBO_BOX)

        self.ui.scrollAreaWidgetContents_2.setStyleSheet(
            light.SETTING_FRAME_SETTHEME)

        self.ui.status_prograss.setStyleSheet(light.PROGRESS_BAR)
        self.ui.label_status_text.setStyleSheet(light.STATUS_BAR_LABEL)
        self.ui.StatusBar.setStyleSheet(light.STATUS_BAR_BACKGROUND)

        self.ui.label_status_text.setStyleSheet(light.STATUS_BAR_LABEL)
        self.ui.analytics_status.setStyleSheet(light.STATUS_BAR_LABEL)
        self.ui.searching_status.setStyleSheet(light.STATUS_BAR_LABEL)
        self.ui.other_status.setStyleSheet(light.STATUS_BAR_LABEL)

    def setIcon_for_window_light(self):

        logger.debug(
            "Set Icon Function Actived... [ setIcon_for_window_light ]")

        # SET ICON FUNCTION
        def setIcon(widget, path,):
            icon = QIcon()
            icon.addFile(path)
            widget.setIcon(icon)

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        self.setWindowTitle("Findup")
        icon = QIcon()
        icon.addFile(light.MAIN_WINDOW_TITLE_ICON)
        self.setWindowIcon(icon)

        self.ui.label_icon_inter_teacher.setText(light.LABEL_ICON_INTER_TEXT)
        self.ui.label_icon_lower.setText(light.LABEL_ICON_LOWER_TEXT)
        self.ui.label.setText(light.LABEL_EDIT_TEXT)
        self.ui.label_icon_none.setText(light.LABEL_ICON_INTER_TEXT)

        self.ui.label_icon_.setText(light.LABEL_ICON_LOWER_TEXT)

        self.ui.label_inforem_date_of_birth_ad.setText(
            light.LABEL_DOB_TEXT)
        self.ui.label_icon_primary.setText(light.LABEL_ICON_LOWER_TEXT)
        self.ui.label_inforem_date_of_birth_primary.setText(
            light.LABEL_DOB_TEXT)

        # SUPER USER ICON
        setIcon(self.ui.btn_superuser, light.ICON_USER)
        setIcon(self.ui.btn_edit_setting, light.ICON_GO)

        # USER ADD ICONS
        setIcon(self.ui.btn_addInter_teacher, light.ICON_ADD_USER)
        setIcon(self.ui.btn_addInter_teacher_none, light.ICON_ADD_USER)
        setIcon(self.ui.btn_addlower, light.ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_adv, light.ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_primary, light.ICON_ADD_USER)

        setIcon(self.ui.btn_go_inter_teacher, light.ICON_GO)
        setIcon(self.ui.btn_go_inter_teacher_none, light.ICON_GO)
        setIcon(self.ui.btn_go_home_lower, light.ICON_GO)
        setIcon(self.ui.btn_go_home_primary, light.ICON_GO)
        setIcon(self.ui.btn_go_home_ad, light.ICON_GO)

        # SETTING BAR HIDDEN ICON BARS
        setIcon(self.ui.btn_hidden_username_bar, light.BTN_OPENED_ICON)
        setIcon(self.ui.btn_hidden_email_bar, light.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_contact_number_bar,
                light.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_passowd_changer_bar,
                light.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_options, light.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_adout, light.BTN_HIDDEN_ICON)

        # SEARCH BAR ICON
        setIcon(self.ui.btn_nameSearch, light.ICON_SEARCH)
        setIcon(self.ui.btn_rollSearch, light.ICON_SEARCH)

        if not self.theme_button_pressed:

            logger.debug(
                "Light icon placer Actived... [ setIcon_for_window_light ]")

            # ADD INTER USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_full_name, light.ICON_USER)
            setIcon_line(self.ui.lineEdit__name_initial, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_personal_contact, light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_spouse_name, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_agrakara_no, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_WOP_no, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_inc_no, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_email_id, light.ICON_AT)
            setIcon_line(self.ui.lineEdit_educational_qualif,
                         light.ICON_QUALIF)
            setIcon_line(self.ui.lineEdit_professional_qualif,
                         light.ICON_QUALIF)
            setIcon_line(self.ui.lineEdit_teaching_regist_no,
                         light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_appoint_subject, light.ICON_SUBJECT)

            # ADD INTER NONE USER ICON
            setIcon_line(self.ui.lineEdit_full_name_none, light.ICON_USER)
            setIcon_line(self.ui.lineEdit__name_initial_none, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_personal_contact_none,
                         light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_spouse_name_none, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_agrakara_no_none, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_WOP_no_none, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_inc_no_none, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_email_id_none, light.ICON_AT)
            setIcon_line(self.ui.lineEdit_educational_qualif_none,
                         light.ICON_QUALIF)
            setIcon_line(self.ui.lineEdit_professional_qualif_none,
                         light.ICON_QUALIF)
            setIcon_line(self.ui.lineEdit_salary_none, light.ICON_RIG_NUM)

            # ADD LOWER PRIMARY USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_name_full_primary, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_primary,
                         light.ICON_USER)
            setIcon_line(self.ui.lineEdit_parent_contact_primary,
                         light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_no_siblings_primary,
                         light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_primary,
                         light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_name_primary,
                         light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_admission_no_primary,
                         light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_religion_primary, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_mather_job_primary, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_father_job_primary, light.ICON_JOB)

            # ADD LOWER ORDNARY USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_name_full_lower, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_lower, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_parent_contact_lower,
                         light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_no_siblings_lower, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_lower, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_name_lower, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_job_lower, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_mather_job_lower, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_admission_no_lower,
                         light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_religion_lower, light.ICON_RIL)

            # ADD LOWER ADVANCED USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_admission_no_ad, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_mather_name_ad, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_ad, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_job_ad, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_father_job_ad, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_parent_contact_no_ad,
                         light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_siblings_ad, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_name_full_ad, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_ad, light.ICON_USER)

        else:

            logger.debug(
                "Light icon replacer Actived... [ setIcon_for_window_light ]")
            # ADD INTER USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_full_name, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit__name_initial, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_personal_contact, light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_spouse_name, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_agrakara_no, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_WOP_no, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_inc_no, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_email_id, light.ICON_AT)
            setIcon_line_(self.ui.lineEdit_educational_qualif,
                          light.ICON_QUALIF)
            setIcon_line_(self.ui.lineEdit_professional_qualif,
                          light.ICON_QUALIF)
            setIcon_line_(self.ui.lineEdit_teaching_regist_no,
                          light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_appoint_subject, light.ICON_SUBJECT)

            # ADD INTER NONE USER ICON
            setIcon_line_(self.ui.lineEdit_full_name_none, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit__name_initial_none, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_personal_contact_none,
                          light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_spouse_name_none, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_agrakara_no_none,
                          light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_WOP_no_none, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_inc_no_none, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_email_id_none, light.ICON_AT)
            setIcon_line_(self.ui.lineEdit_educational_qualif_none,
                          light.ICON_QUALIF)
            setIcon_line_(self.ui.lineEdit_professional_qualif_none,
                          light.ICON_QUALIF)
            setIcon_line_(self.ui.lineEdit_salary_none, light.ICON_RIG_NUM)

            # ADD LOWER PRIMARY USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_name_full_primary, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_primary,
                          light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_parent_contact_primary,
                          light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_no_siblings_primary,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_primary,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_name_primary,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_admission_no_primary,
                          light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_religion_primary,
                          light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_mather_job_primary, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_father_job_primary, light.ICON_JOB)

            # ADD LOWER ORDNARY USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_name_full_lower, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_lower, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_parent_contact_lower,
                          light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_no_siblings_lower,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_lower,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_name_lower,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_job_lower, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_mather_job_lower, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_admission_no_lower,
                          light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_religion_lower, light.ICON_RIL)

            # ADD LOWER ADVANCED USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_admission_no_ad, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_mather_name_ad, light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_ad, light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_job_ad, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_father_job_ad, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_parent_contact_no_ad,
                          light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_siblings_ad, light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_name_full_ad, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_ad, light.ICON_USER)

        # SUPERUSER ICON AND NAME
        self.setTheSuperUserSideBarText_light()

        # DELETE BTN ICONS
        setIcon(self.ui.btn_delete_inter_1, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_1, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_pri, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_advan, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_noneinter, light.ICON_DELETE)

        setIcon(self.ui.btn_delete_inter_left_1, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_1, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_advan, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_pri, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_noneinter_left, light.ICON_DELETE)

        setIcon(self.ui.btn_edit_interuser_left, light.ICON_ADD_USER)
        setIcon(self.ui.btn_edit_noneinteruser_left, light.ICON_ADD_USER)
        setIcon(self.ui.btn_edit_lower_left, light.ICON_ADD_USER)
        setIcon(self.ui.btn_edit_advan_left, light.ICON_ADD_USER)
        setIcon(self.ui.btn_edit_pri_left, light.ICON_ADD_USER)

        setIcon(self.ui.btn_edit_interuser, light.ICON_EDIT)
        setIcon(self.ui.btn_edit_noneinteruser, light.ICON_EDIT)
        setIcon(self.ui.btn_edit_lower, light.ICON_EDIT)
        setIcon(self.ui.btn_edit_advan, light.ICON_EDIT)
        setIcon(self.ui.btn_edit_pri, light.ICON_EDIT)

        # ABOUT LABEL ICON
        self.ui.label_logo_adout.setText(light.ICON_LABEL_TEXT)

        # ACTIVE AND LEFT LABEL TEXT
        self.ui.label_info_user_inter_1.setText(
            light.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_1.setText(
            light.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_pri.setText(
            light.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_advan.setText(
            light.ACTIVE_LABEL_INFO_TEXT)

        self.ui.label_info_user_left_inter_1.setText(
            light.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_1.setText(
            light.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_pri.setText(
            light.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_advan.setText(
            light.LAFT_LABEL_INFO_TEXT)

    # Super User Side Bar Text
    def setTheSuperUserSideBarText_light(self):

        __data = Setting.load_superuser()
        __getuser = Crypto.decrypt_superuser(
            __data[SETTING]["Name"],
            __data[SETTING]["Password"],
            __data[SETTING]["Contact"],
            __data[SETTING]["E-mail"]
        )
        __user = [__getuser[0], __getuser[2], __getuser[-1]]
        light.setSuperUserIconName(__getuser[0], self.ui.label_super_icon)
        light.setSuperUserFinform(__user, self.ui.label_infor_super)

    # this dark theme of window
    def connect_functiom_dark(self):
        logger.debug("Connect Function Actived... [ connect_functiom_dark ]")

        # Toggle Burguer Menu
        self.ui.btn_Toggle.clicked.connect(
            lambda: UIFunctions.thread_connecter_dark(self, 200, True))

        # Setting Bar Animation
        self.ui.btn_hidden_username_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_dark_connecter(self,  self.ui.frame_user_name_changer.height(
        ), self.ui.frame_user_name_changer, self.ui.frame_name_changer_content_page, True, self.ui.btn_hidden_username_bar, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))
        self.ui.btn_hidden_email_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_dark_connecter(self,  self.ui.frame_email_changer.height(
        ), self.ui.frame_email_changer, self.ui.frame_email_changer_content_bar, True, self.ui.btn_hidden_email_bar, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))
        self.ui.btn_hidden_contact_number_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_dark_connecter(self,  self.ui.frame_contect_number_changer.height(
        ), self.ui.frame_contect_number_changer, self.ui.frame_contect_number_changer_content_bar, True, self.ui.btn_hidden_contact_number_bar, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))
        self.ui.btn_hidden_passowd_changer_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_dark_connecter(self,  self.ui.frame_password_changer.height(
        ), self.ui.frame_password_changer, self.ui.frame_password_changer_content_bar, True, self.ui.btn_hidden_passowd_changer_bar, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))

        self.ui.btn_hidden_options.clicked.connect(lambda: UIFunctions.settingHiddenBar_two_dark(self,  self.ui.frame_more_options.height(
        ), self.ui.frame_more_options, self.ui.frame_more_options_contect_bar, True, self.ui.btn_hidden_options, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))
        self.ui.btn_hidden_adout.clicked.connect(lambda: UIFunctions.settingHiddenBar_two_dark(self, self.ui.frame_adout.height(
        ), self.ui.frame_adout, self.ui.frame_content_adout, True, self.ui.btn_hidden_adout, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))

        # SUPER USER BTN
        self.ui.btn_superuser.clicked.connect(
            lambda: UIFunctions.userSide_toggle_dark_connecter(self, 300, True))

        # BUTTONE CONNECTER
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        UIFunctions.current_page_dark(self)

        self.ui.btn_page_home.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_page_left.clicked.connect(
            lambda: UIFunctions.left_dark(self))
        self.ui.btn_page_search.clicked.connect(
            lambda: UIFunctions.search_dark(self))
        self.ui.btn_setting.clicked.connect(
            lambda: UIFunctions.setting_dark(self))
        self.ui.btn_page_analytics.clicked.connect(
            lambda: UIFunctions.analytics_dark(self))
        self.ui.btn_go_inter_teacher.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_inter_teacher_none.clicked.connect(
            lambda: UIFunctions.home_dark(self))

        # Super User Btn
        self.ui.btn_edit_setting.clicked.connect(
            lambda: UIFunctions.setting_dark(self))

        # Inter and Lower Btn
        self.ui.btn_inter.clicked.connect(
            lambda: UIFunctions.callInter_window_dark(self)
        )
        self.ui.btn_lower.clicked.connect(
            lambda: UIFunctions.callLower_window_dark(self)
        )

        # Connect into btn_ordinary
        self.ui.btn_ordinary.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_lower))
        # Connect into btn_advanced
        self.ui.btn_advanced.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_advan))
        # Connect into btn_primary
        self.ui.btn_primary.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page))
        # Conntect into btn_teahers
        self.ui.btn_teahers.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_inter)
        )
        # Conntect into btn_none_teaher
        self.ui.btn_none_teaher.clicked.connect(
            lambda: UIFunctions.call_input_menu(
                self, self.ui.page_add_inter_none)
        )

        # Go Home Button
        self.ui.btn_go_inter_teacher.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_home_primary.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_home_ad.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_inter_teacher_none.clicked.connect(
            lambda: UIFunctions.home_dark(self))

    def setTheme_for_window_dark(self):
        logger.debug(
            "setTheme Function Actived... [ setTheme_for_window_dark ]")
        self.ui.scrollArea_2.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_resalt.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_3.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_content.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_4.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_add_info.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_advanced_add.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_primary_add.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_lower_add.setStyleSheet(dark.SCROLLAREA)

        self.ui.scrollArea_add_info_none.setStyleSheet(dark.SCROLLAREA)

        self.ui.comboBox_stream_primary.setStyleSheet(dark.COMBO_BOX)

        self.setStyleSheet(dark.MAIN_WINDOW_BACKGROUND)
        self.ui.btn_Toggle.setStyleSheet(dark.TOGGLE_BTN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN)
        self.ui.TopBar.setStyleSheet(dark.TOP_BAR_BACKGROUND)
        self.ui.frame_top.setStyleSheet(dark.TOP_FRAME_BACKGROUND)
        self.ui.frame_return_bar.setStyleSheet(dark.FRAME_RETURN_BAR)
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN)
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN)
        self.ui.frame_backup.setStyleSheet(dark.FRAME_BACKUP)
        self.ui.btn_superuser.setStyleSheet(dark.SUPERUSER_BTN)
        self.ui.frame_left_menu.setStyleSheet(dark.FRAME_LEFT_MENU)
        self.ui.page_add_students.setStyleSheet(dark.PAGE_ADD_STUDENTS)
        self.ui.frame_top_menus.setStyleSheet(dark.FRAME_TOP_MENU)
        self.ui.frame_page.setStyleSheet(dark.FRAME_PAGE)
        self.ui.frame_2.setStyleSheet(dark.FRAME_2)
        self.ui.btn_primary.setStyleSheet(dark.PRIMARY_BTN)
        self.ui.btn_ordinary.setStyleSheet(dark.ORDNARY_BTN)
        self.ui.btn_advanced.setStyleSheet(dark.ADVANCED_BTN)
        self.ui.btn_teahers.setStyleSheet(dark.ADVANCED_BTN)
        self.ui.btn_none_teaher.setStyleSheet(dark.ADVANCED_BTN)
        self.ui.frame_add_btns_inters.setStyleSheet(dark.FRAME_2)

        # INTER USER COMPENTS
        self.ui.scrollArea_add_info.setStyleSheet(dark.ADD_INTER_PAGE_WIDGET)
        self.ui.lineEdit_full_name.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit__name_initial.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_inc_no.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_personal_contact.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_WOP_no.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_agrakara_no.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_spouse_name.setStyleSheet(dark.LINE_EDIT)

        self.ui.lineEdit_nature_of_appoin.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_present_grade.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_appoint_subject.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_personal_contact.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_professional_qualif.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_educational_qualif.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_email_id.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_teaching_regist_no.setStyleSheet(dark.LINE_EDIT)

        self.ui.textEdit_emergency.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_working_address.setStyleSheet(dark.TEXT_EDIT)

        self.ui.dateEdit_present_date.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_increment_date.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_DOB.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_first_appointment_date.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_appointment_date.setStyleSheet(dark.DATE_EDIT)

        self.ui.radioButton_married.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_unmarried.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_male.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.scrollAreaWidgetInfo.setStyleSheet(
            dark.INTER_ADD_TEACHER_BACKGROUND)

        self.ui.label_date_app_to_school_text.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_appointment_data_text.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_DOB_text.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_info_Inter_face.setStyleSheet(
            dark.LABEL_INFO_INTER_FACE)
        self.ui.label_info_user_inter_1.setStyleSheet(
            dark.LABEL_INFO_INTER_USER_1)
        self.ui.label_info_Inter_1.setStyleSheet(dark.LABEL_INFO_INTER_1)
        self.ui.info_inter_left_1.setStyleSheet(dark.LABEL_INFO_INTER_1)
        self.ui.label_info_user_left_inter_1.setStyleSheet(
            dark.LABEL_INFO_INTER_USER_1)
        self.ui.label_icon_inter_teacher.setStyleSheet(dark.LABEL_ICON_INTER)
        self.ui.label_show_roll_number.setStyleSheet(
            dark.LABEL_SHOW_ROLL_INTER)
        self.ui.label_inter_head.setStyleSheet(
            dark.ANALYTICS_LABEL_INTER_HEAD)

        self.ui.groupBox_civil.setStyleSheet(dark.GROUP)
        self.ui.groupBox_gender.setStyleSheet(dark.GROUP)
        self.ui.groupBox_increment_date.setStyleSheet(dark.GROUP)
        self.ui.groupBox_present_grade_and_date.setStyleSheet(dark.GROUP)
        self.ui.groupBox_gender_primary.setStyleSheet(dark.GROUP)
        self.ui.groupBox_gender_advanced.setStyleSheet(dark.GROUP)
        self.ui.groupBox_gender_lower.setStyleSheet(dark.GROUP)

        self.ui.widget_inter_1.setStyleSheet(dark.WIDGET_INTER_1)
        self.ui.widget_inter_left_1.setStyleSheet(dark.WIDGET_INTER_1)

        self.ui.label_info_Inter_face.setStyleSheet(dark.LABEL_ACTIVE_LEFT)
        self.ui.label_info_inter_left_face.setStyleSheet(
            dark.LABEL_ACTIVE_LEFT)

        self.ui.frame_inter_delet_bar_1.setStyleSheet(
            dark.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_inter_left_btns_bar_1.setStyleSheet(
            dark.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_main_inter_info_inter_teacher.setStyleSheet(
            dark.FRMAE_MAIN_INTER_INFO)
        self.ui.frame_inter.setStyleSheet(dark.ANALYTICS_FRAME_INTER)

        self.ui.btn_delete_inter_1.setStyleSheet(dark.DELETE_INTER_BTN_1)
        self.ui.btn_edit_interuser.setStyleSheet(dark.DELETE_INTER_BTN_1)
        self.ui.btn_edit_interuser_left.setStyleSheet(dark.DELETE_INTER_BTN_1)
        self.ui.btn_delete_inter_left_1.setStyleSheet(dark.DELETE_INTER_BTN_1)
        self.ui.btn_upload_image_inter_teacher.setStyleSheet(
            dark.UPLOAD_IMAGE_BTN)
        self.ui.btn_addInter_teacher.setStyleSheet(dark.ADDINTER_BTN)
        self.ui.btn_go_inter_teacher.setStyleSheet(dark.GOHOME_INTER_BTN)

        self.ui.page_add_inter.setStyleSheet(dark.PAGE_ADD_INTER)
        self.ui.page_inter_add.setStyleSheet(dark.PAGE_ADD_INTER)

        # NONE TEACHER USER COMPENTS
        self.ui.lineEdit_nature_of_appoin_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_personal_contact_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_professional_qualif_none.setStyleSheet(
            dark.LINE_EDIT)
        self.ui.lineEdit_educational_qualif_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_email_id_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_full_name_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit__name_initial_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_inc_no_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_personal_contact_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_WOP_no_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_agrakara_no_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_spouse_name_none.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_salary_none.setStyleSheet(dark.LINE_EDIT)

        self.ui.dateEdit_increment_date_none.setStyleSheet(dark.DATE_EDIT)

        self.ui.textEdit_emergency_none.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_working_address_none.setStyleSheet(dark.TEXT_EDIT)

        self.ui.dateEdit_DOB_none.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_first_appointment_date_none.setStyleSheet(
            dark.DATE_EDIT)
        self.ui.dateEdit_appointment_date_none.setStyleSheet(dark.DATE_EDIT)

        self.ui.radioButton_married_none.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_unmarried_none.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_male_none.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female_none.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other_none.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.scrollAreaWidgetInfo.setStyleSheet(
            dark.INTER_ADD_TEACHER_BACKGROUND)

        self.ui.label_date_app_to_school_text_none.setStyleSheet(
            dark.LABEL_COLOR)
        self.ui.label_appointment_data_text_none.setStyleSheet(
            dark.LABEL_COLOR)
        self.ui.label_DOB_text_none.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_icon_none.setStyleSheet(dark.LABEL_ICON_INTER)
        self.ui.label_show_roll_number_none.setStyleSheet(
            dark.LABEL_SHOW_ROLL_INTER)

        self.ui.label_info_user_noneinter.setStyleSheet(
            dark.LABEL_INFO_INTER_USER_1)
        self.ui.label_info_noneinter.setStyleSheet(
            dark.LABEL_INFO_INTER_1)
        self.ui.label_info_NoneInter_face.setStyleSheet(
            dark.LABEL_ACTIVE_LEFT)

        self.ui.btn_delete_noneinter.setStyleSheet(dark.DELETE_INTER_BTN_1)
        self.ui.btn_edit_noneinteruser.setStyleSheet(dark.DELETE_INTER_BTN_1)

        self.ui.label_info_user_noneinter_left.setStyleSheet(
            dark.LABEL_INFO_INTER_USER_1)
        self.ui.label_info_noneinter_left.setStyleSheet(
            dark.LABEL_INFO_INTER_1)
        self.ui.label_info_NoneInter_face_left.setStyleSheet(
            dark.LABEL_ACTIVE_LEFT)

        self.ui.btn_delete_noneinter_left.setStyleSheet(
            dark.DELETE_INTER_BTN_1)
        self.ui.btn_edit_noneinteruser_left.setStyleSheet(
            dark.DELETE_INTER_BTN_1)

        self.ui.page_add_inter_none.setStyleSheet(dark.PAGE_ADD_INTER)

        self.ui.frame_main_inter_info_inter_teache_none.setStyleSheet(
            dark.FRMAE_MAIN_INTER_INFO)
        self.ui.frame_noneinter_delet_bar.setStyleSheet(
            dark.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_noneinter_delet_bar_left.setStyleSheet(
            dark.FRAME_INTER_DELETE_BAR_1)

        self.ui.groupBox_civil_none.setStyleSheet(dark.GROUP)
        self.ui.groupBox_gender_none.setStyleSheet(dark.GROUP)
        self.ui.groupBox_increment_date_none.setStyleSheet(dark.GROUP)

        self.ui.btn_upload_image_inter_teacher_none.setStyleSheet(
            dark.UPLOAD_IMAGE_BTN)
        self.ui.btn_addInter_teacher_none.setStyleSheet(dark.ADDINTER_BTN)
        self.ui.btn_go_inter_teacher_none.setStyleSheet(dark.GOHOME_INTER_BTN)

        self.ui.widget_noneinter.setStyleSheet(dark.WIDGET_INTER_1)
        self.ui.widget_noneinter_left.setStyleSheet(dark.WIDGET_INTER_1)

        # PRIMARY LOWER USER COMPENTS
        self.ui.dateEdit_date_of_birth_primary.setStyleSheet(dark.DATE_EDIT)
        self.ui.lineEdit_religion_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_name_full_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_name_initial_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_name_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_name_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_job_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_job_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.textEdit_address_home.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_address_office.setStyleSheet(dark.TEXT_EDIT)
        self.ui.lineEdit_admission_no_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_parent_contact_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.dateEdit_date_admission_primary.setStyleSheet(dark.DATE_EDIT)
        self.ui.lineEdit_no_siblings_primary.setStyleSheet(dark.LINE_EDIT)

        self.ui.radioButton_male_primary_2.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female_primary_2.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other_primary_2.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.label_inforem_admission_primary.setStyleSheet(
            dark.GLOBAL_LABEL)
        self.ui.label_info_gender_primary.setStyleSheet(dark.GLOBAL_LABEL)
        self.ui.label_inforem_date_of_birth_primary.setStyleSheet(
            dark.GLOBAL_LABEL)
        self.ui.label_info_user_lower_pri.setStyleSheet(
            dark.LABEL_INFO_PRIMARY_USER_1)
        self.ui.label_info_lower_pri.setStyleSheet(dark.LABEL_INFO_PRIMARY_1)
        self.ui.label_icon_primary.setStyleSheet(dark.LABEL_ICON_PRIMARY)
        self.ui.label_show_roll_primary.setStyleSheet(
            dark.LABEL_SHOW_ROLL_PRIMARY)
        self.ui.info_lower_left_pri.setStyleSheet(dark.LABEL_INFO_PRIMARY_1)
        self.ui.label_info_user_left_lower_pri.setStyleSheet(
            dark.LABEL_INFO_PRIMARY_USER_1)

        self.ui.btn_addLower_primary.setStyleSheet(dark.ADDLOWER_PRIMARY_BTN)
        self.ui.btn_go_home_primary.setStyleSheet(dark.GOHOME_PRIMARY_BTN)
        self.ui.btn_delete_lower_pri.setStyleSheet(dark.DELETE_PRIMARY_BTN_1)

        self.ui.frame_inter_delet_bar_pri.setStyleSheet(
            dark.FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.frame_main_content_for_primary.setStyleSheet(
            dark.FRAME_MAIN_CONTENT_FOR_PRIMARY)
        self.ui.frame_coments_ad_2.setStyleSheet(
            dark.FRAME_CONTENT_ADVANCED_2)
        self.ui.frame_lower_btns_bar_pri.setStyleSheet(
            dark.FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.frame_lower_prim.setStyleSheet(dark.ANALYTICS_FRAME_PRIM)

        self.ui.page.setStyleSheet(dark.PAGE_ADD_PRIMARY)

        self.ui.widget_lower_pri.setStyleSheet(dark.WIDGET_PRIMARY_1)
        self.ui.widget_lower_left_pri.setStyleSheet(dark.WIDGET_PRIMARY_1)

        self.ui.label_info_pri_face.setStyleSheet(dark.LABEL_ACTIVE_LEFT)
        self.ui.label_info_pri_left_face.setStyleSheet(dark.LABEL_ACTIVE_LEFT)

        self.ui.btn_delete_lower_left_pri.setStyleSheet(
            dark.DELETE_PRIMARY_BTN_1)
        self.ui.btn_edit_lower.setStyleSheet(dark.DELETE_PRIMARY_BTN_1)
        self.ui.btn_edit_lower_left.setStyleSheet(dark.DELETE_PRIMARY_BTN_1)
        self.ui.btn_upload_image_primary.setStyleSheet(dark.UPLOAD_IMAGE_BTN)

        # ORDNARY LOWER USER COMPENTS
        self.ui.lineEdit_name_full_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_name_initial_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_name_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_name_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_job_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_job_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_no_siblings_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_religion_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.textEdit_address_home_lower.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_address_office_lower.setStyleSheet(dark.TEXT_EDIT)
        self.ui.comboBox_stream_lower.setStyleSheet(dark.COMBO_BOX)
        self.ui.lineEdit_parent_contact_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_admission_no_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.dateEdit_date_admission_lower.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_date_of_birth_lower.setStyleSheet(dark.DATE_EDIT)

        self.ui.radioButton_male_lower_2.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female_lower_2.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other_lower_2.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.frame_inter_delet_bar_3.setStyleSheet(
            dark.FRAME_LOWER_DELETE_BAR_1)
        self.ui.frame_lower_left_btns_bar_1.setStyleSheet(
            dark.FRAME_LOWER_DELETE_BAR_1)
        self.ui.frame_lower.setStyleSheet(dark.ANALYTICS_FRAME_LOWER)
        self.ui.frame_main_lower_info.setStyleSheet(
            dark.FRAME_MAIN_LOWER_INFO)

        self.ui.label_inforem_admission_lower.setStyleSheet(dark.GLOBAL_LABEL)
        self.ui.label_info_gender_lower.setStyleSheet(dark.GLOBAL_LABEL)
        self.ui.label_inforem_date_of_birth_lower.setStyleSheet(
            dark.GLOBAL_LABEL)
        self.ui.label_info_lower_1.setStyleSheet(dark.LABEL_INFO_LOWER_1)
        self.ui.label_info_user_lower_1.setStyleSheet(
            dark.LABEL_INFO_LOWER_USER_1)
        self.ui.info_lower_1.setStyleSheet(dark.LABEL_INFO_LOWER_1)
        self.ui.label_info_user_left_lower_1.setStyleSheet(
            dark.LABEL_INFO_LOWER_USER_1)
        self.ui.label_lower_head.setStyleSheet(
            dark.ANALYTICS_LABEL_LOWER_HEAD)
        self.ui.label_icon_lower.setStyleSheet(dark.LABEL_ICON_LOWER)
        self.ui.label_show_roll_number_lower.setStyleSheet(
            dark.LABEL_SHOW_ROLL_LOWER)

        self.ui.widget_lower_1.setStyleSheet(dark.WIDGET_LOWER_1)
        self.ui.widget_lower_left_1.setStyleSheet(dark.WIDGET_LOWER_1)

        self.ui.label_info_lower_face.setStyleSheet(dark.LABEL_ACTIVE_LEFT)
        self.ui.label_info_lower_left_face.setStyleSheet(
            dark.LABEL_ACTIVE_LEFT)

        self.ui.btn_delete_lower_1.setStyleSheet(dark.DELETE_LOWER_BTN_1)
        self.ui.btn_delete_lower_left_1.setStyleSheet(dark.DELETE_LOWER_BTN_1)
        self.ui.btn_edit_pri.setStyleSheet(dark.DELETE_LOWER_BTN_1)
        self.ui.btn_edit_pri_left.setStyleSheet(dark.DELETE_LOWER_BTN_1)
        self.ui.btn_upload_image_lower.setStyleSheet(dark.UPLOAD_IMAGE_BTN)
        self.ui.btn_addlower.setStyleSheet(dark.ADDLOWER_LOWER_BTN)
        self.ui.btn_go_home_lower.setStyleSheet(dark.GOHOME_LOWER_BTN)

        self.ui.page_add_lower.setStyleSheet(dark.PAGE_ADD_LOWER)

        # ADVANCED LOWER USER COMPENTS
        self.ui.lineEdit_name_initial_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_name_full_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_religion_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_address_office_ad.setStyleSheet(dark.TEXT_EDIT)
        self.ui.lineEdit_home_address_ad.setStyleSheet(dark.TEXT_EDIT)
        self.ui.lineEdit_admission_no_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_name_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_name_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_job_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_job_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_parent_contact_no_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_siblings_ad.setStyleSheet(dark.LINE_EDIT)

        self.ui.comboBox_level_ad.setStyleSheet(dark.COMBO_BOX)
        self.ui.comboBox_stream.setStyleSheet(dark.COMBO_BOX)

        self.ui.dateEdit_date_of_admission_ad.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_date_of_birth_ad.setStyleSheet(dark.DATE_EDIT)

        self.ui.radioButton_male_ad.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female_ad.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other_ad.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.label_inforem_date_of_birth_ad.setStyleSheet(
            dark.GLOBAL_LABEL)
        self.ui.label_icon_.setStyleSheet(dark.LABEL_ICON_)
        self.ui.label_show_roll_ad.setStyleSheet(
            dark.LABEL_SHOW_ROLL_ADVANCED)
        self.ui.label_info_lower_advan.setStyleSheet(
            dark.LABEL_INFO_ADVANCED_1)
        self.ui.label_info_user_lower_advan.setStyleSheet(
            dark.LABEL_INFO_ADVANCED_USER_1)
        self.ui.info_lower_left_advan.setStyleSheet(
            dark.LABEL_INFO_ADVANCED_1)
        self.ui.label_info_user_left_lower_advan.setStyleSheet(
            dark.LABEL_INFO_ADVANCED_USER_1)
        self.ui.label_advanced_level_13.setStyleSheet(
            dark.LABEL_ADVANCED_LEVEL_13)
        self.ui.label_advanced_level_12.setStyleSheet(
            dark.LABEL_ADVANCED_LEVEL_12)
        self.ui.label_gender_ad.setStyleSheet(dark.GLOBAL_LABEL)
        self.ui.label_date_admission_ad.setStyleSheet(dark.GLOBAL_LABEL)

        self.ui.page_add_advan.setStyleSheet(dark.PAGE_ADD_ADVAN)

        self.ui.frame_coments_ad.setStyleSheet(dark.FRAME_CONTENT_ADVANCED)
        self.ui.frame_main_content_for_advance.setStyleSheet(
            dark.FRAME_MAIN_CONTENT_FOR_ADVANCED)
        self.ui.frame_inter_delet_bar_advan.setStyleSheet(
            dark.FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.frame_lower_btns_bar_advan.setStyleSheet(
            dark.FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.frame_lower_advan.setStyleSheet(dark.ANALYTICS_FRAME_ADVAN)
        self.ui.frame_advanced_level_12.setStyleSheet(
            dark.FRAME_ADVANCED_LEVEL_12)
        self.ui.frame_advanced_level_13.setStyleSheet(
            dark.FRAME_ADVANCED_LEVEL_13)

        self.ui.btn_addLower_adv.setStyleSheet(dark.ADDLOWER_ADVANCED_BTN)
        self.ui.btn_go_home_ad.setStyleSheet(dark.GOHOME_ADVANCED_BTN)
        self.ui.btn_delete_lower_advan.setStyleSheet(
            dark.DELETE_ADVANCED_BTN_1)
        self.ui.btn_delete_lower_left_advan.setStyleSheet(
            dark.DELETE_ADVANCED_BTN_1)
        self.ui.btn_edit_advan.setStyleSheet(dark.DELETE_ADVANCED_BTN_1)
        self.ui.btn_edit_advan_left.setStyleSheet(dark.DELETE_ADVANCED_BTN_1)
        self.ui.btn_upload_image_advanced.setStyleSheet(dark.UPLOAD_IMAGE_BTN)

        self.ui.widget_lower_advan.setStyleSheet(dark.WIDGET_ADVANCED_1)
        self.ui.widget_lower_left_advan.setStyleSheet(dark.WIDGET_ADVANCED_1)

        self.ui.label_info_advan_face.setStyleSheet(dark.LABEL_ACTIVE_LEFT)
        self.ui.label_info_advan_left_face.setStyleSheet(
            dark.LABEL_ACTIVE_LEFT)

        # SUPER USER COMPENTS
        self.ui.lineEdit_username_change_input.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_change_email_input.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_contact_number_input.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_passord_input.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_repassword_input.setStyleSheet(dark.LINE_EDIT)

        self.ui.frame_user_name_changer.setStyleSheet(
            dark.SETTING_NAME_CHANGER)
        self.ui.frame_more_options.setStyleSheet(dark.SETTING_FRAME_MORE_OP)
        self.ui.frame_email_changer.setStyleSheet(
            dark.SETTING_FRAME_EMAIL_CHANGER)
        self.ui.frame_contect_number_changer.setStyleSheet(
            dark.SETTING_FRAME_CONTECT_NUM_CHANGER)
        self.ui.frame_password_changer.setStyleSheet(
            dark.SETTING_FRAME_PASSWORD_CHANGER)
        self.ui.frame_super_user.setStyleSheet(dark.FRAME_SUPERUSER)

        self.ui.label_username_title.setStyleSheet(
            dark.SETTING_USER_NAME_TITLE)
        self.ui.label_show_current_username.setStyleSheet(
            dark.SETTING_LABEL_SHOW_CURRENT_USERNAME)
        self.ui.label_title.setStyleSheet(dark.SETTING_LABEL_TITLE)
        self.ui.label_reload_info.setStyleSheet(dark.SETTING_LABEL_RELOAD)
        self.ui.label_reset_info.setStyleSheet(dark.SETTING_LABEL_INFO_RESET)
        self.ui.label_change_email_title.setStyleSheet(
            dark.SETTING_LABEL_CHANGE_EMAIL_TITLE)
        self.ui.label_current_email.setStyleSheet(
            dark.SETTING_LABEL_CURRENT_EMAIL)
        self.ui.label_change_contact_number_title.setStyleSheet(
            dark.SETTING_LABEL_CHANGE_CONTECT_NUM_TITLE)
        self.ui.label_show_current_contact_number.setStyleSheet(
            dark.SETTING_SHOW_CURRENT_CONTECT_NUM)
        self.ui.label_change_password_title.setStyleSheet(
            dark.SETTING_LABEL_CHANGE_PASSWORD_TITLE)
        self.ui.label_super_icon.setStyleSheet(dark.LABEL_SUPERUSER_ICON)
        self.ui.label_infor_super.setStyleSheet(dark.LABEL_INFO_SUPERUSER)

        self.ui.btn_hidden_username_bar.setStyleSheet(
            dark.SETTING_USERNAME_HIDDEN_BTN)
        self.ui.btn_save_username.setStyleSheet(
            dark.SETTING_SAVE_USERNAME_BTN)
        self.ui.btn_hidden_options.setStyleSheet(dark.SETTING_HIDDEN_BTN_OP)
        self.ui.btn_reload.setStyleSheet(dark.SETTING_RELOAD_BTN)
        self.ui.btn_reset.setStyleSheet(dark.SETTING_RESET_BTN)
        self.ui.btn_logout.setStyleSheet(dark.SETTING_LOGOUT_BTN)
        self.ui.btn_hidden_email_bar.setStyleSheet(
            dark.SETTING_HIDDEN_EMAIL_BTN)
        self.ui.btn_save_change_email.setStyleSheet(
            dark.SETTING_SAVE_EMAIL_BTN)
        self.ui.btn_hidden_contact_number_bar.setStyleSheet(
            dark.SETTING_HIDDEN_BTN_CONTECT)
        self.ui.btn_save_contact_number.setStyleSheet(
            dark.SETTING_SAVE_CONTECT_NUM_BTN)
        self.ui.btn_hidden_passowd_changer_bar.setStyleSheet(
            dark.SETTING_PASSWORD_CHANGER_BTN)
        self.ui.btn_save_password.setStyleSheet(
            dark.SETTING_SAVE_PASSWORD_BTN)

        # SOFTWARE COMPENTS
        self.ui.lineEdit_rollSearch.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_nameSearch.setStyleSheet(dark.LINE_EDIT)

        self.ui.btn_nameSearch.setStyleSheet(dark.SEARCH_BAR_BTN)
        self.ui.btn_rollSearch.setStyleSheet(dark.SEARCH_BAR_BTN)
        self.ui.btn_edit_setting.setStyleSheet(dark.EDIT_SETTING_BTN)
        self.ui.btn_hidden_adout.setStyleSheet(dark.HIDDEN_ABOUT_BTN)

        self.ui.frame_main_home_bar.setStyleSheet(dark.FRAME_MAIN_HOME_BAR)
        self.ui.frame_main_left_bar.setStyleSheet(dark.FRAME_MAIN_LEFT_BAR)
        self.ui.frame_main_search_bar.setStyleSheet(
            dark.FRAME_MAIN_SEARCH_BAR)
        self.ui.frame_searching_main.setStyleSheet(dark.FRAME_SEARCHING_MAIN)
        self.ui.frame_title_search.setStyleSheet(dark.FRAME_TITLE_SEARCH)
        self.ui.frame_search_bar_itmes.setStyleSheet(
            dark.FRAME_SEARCH_BAR_ITEMS)
        self.ui.frame_main_setting_bar.setStyleSheet(dark.SETTING_BACKGROUND)
        self.ui.frame.setStyleSheet(dark.SETTING_FRAME)
        self.ui.frame_content.setStyleSheet(dark.ANALYTICS_FRAME_CONTENT)
        self.ui.frame_adout.setStyleSheet(dark.FRAME_ABOUT)
        self.ui.frame_content_adout.setStyleSheet(dark.FRAME_CONTENT_ABOUT)

        self.ui.label_more_info_adout.setStyleSheet(dark.LABEL_MORE_ABOUT)
        self.ui.label.setStyleSheet(dark.SETTING_LABEL)
        self.ui.label_info_adout.setStyleSheet(dark.LABEL_INFO_ABOUT)

        self.ui.page_content_Input.setStyleSheet(dark.PAGE_CONTECT)

        self.ui.scrollAreaWidgetContents.setStyleSheet(dark.SCROLLAREA_WIDGET)
        self.ui.analytics.setStyleSheet(dark.ANALYTICS)

        self.ui.frame_setTheme.setStyleSheet(dark.SETTING_FRAME_SETTHEME)
        self.ui.label_theme_set_info.setStyleSheet(dark.SETTING_LABEL_THEME)
        self.ui.btn_setTheme.setStyleSheet(dark.THEME_BTN)
        self.ui.comboBox_theme_items.setStyleSheet(dark.COMBO_BOX)

        self.ui.scrollAreaWidgetContents_2.setStyleSheet(
            dark.SETTING_FRAME_SETTHEME)

        self.ui.status_prograss.setStyleSheet(dark.PROGRESS_BAR)
        self.ui.label_status_text.setStyleSheet(dark.STATUS_BAR_LABEL)
        self.ui.StatusBar.setStyleSheet(dark.STATUS_BAR_BACKGROUND)

        self.ui.label_status_text.setStyleSheet(dark.STATUS_BAR_LABEL)
        self.ui.analytics_status.setStyleSheet(dark.STATUS_BAR_LABEL)
        self.ui.searching_status.setStyleSheet(dark.STATUS_BAR_LABEL)
        self.ui.other_status.setStyleSheet(dark.STATUS_BAR_LABEL)

    def setIcon_for_window_dark(self):

        logger.debug("setIcon Function Actived... [ setIcon_for_window_dark ]")

        # SET ICON FUNCTION
        def setIcon(widget, path,):
            icon = QIcon()
            icon.addFile(path)
            widget.setIcon(icon)

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        self.setWindowTitle("Findup")
        icon = QIcon()
        icon.addFile(dark.MAIN_WINDOW_TITLE_ICON)
        self.setWindowIcon(icon)

        self.ui.label_icon_inter_teacher.setText(dark.LABEL_ICON_INTER_TEXT)
        self.ui.label_icon_lower.setText(dark.LABEL_ICON_LOWER_TEXT)
        self.ui.label.setText(dark.LABEL_EDIT_TEXT)
        self.ui.label_icon_none.setText(dark.LABEL_ICON_INTER_TEXT)

        self.ui.label_icon_.setText(dark.LABEL_ICON_LOWER_TEXT)

        self.ui.label_inforem_date_of_birth_ad.setText(dark.LABEL_DOB_TEXT)
        self.ui.label_icon_primary.setText(dark.LABEL_ICON_LOWER_TEXT)
        self.ui.label_inforem_date_of_birth_primary.setText(
            dark.LABEL_DOB_TEXT)

        # SUPER USER ICON
        setIcon(self.ui.btn_superuser, dark.ICON_USER)
        setIcon(self.ui.btn_edit_setting, dark.ICON_GO)

        # USER ADD ICONS
        setIcon(self.ui.btn_addInter_teacher, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_addInter_teacher_none, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_addlower, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_adv, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_primary, dark.ICON_ADD_USER)

        setIcon(self.ui.btn_go_inter_teacher, dark.ICON_GO)
        setIcon(self.ui.btn_go_inter_teacher_none, dark.ICON_GO)
        setIcon(self.ui.btn_go_home_lower, dark.ICON_GO)
        setIcon(self.ui.btn_go_home_primary, dark.ICON_GO)
        setIcon(self.ui.btn_go_home_ad, dark.ICON_GO)

        # SETTING BAR HIDDEN ICON BARS
        setIcon(self.ui.btn_hidden_username_bar, dark.BTN_OPENED_ICON)
        setIcon(self.ui.btn_hidden_email_bar, dark.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_contact_number_bar, dark.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_passowd_changer_bar, dark.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_options, dark.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_adout, dark.BTN_HIDDEN_ICON)

        # SEARCH BAR ICON
        setIcon(self.ui.btn_nameSearch, dark.ICON_SEARCH)
        setIcon(self.ui.btn_rollSearch, dark.ICON_SEARCH)

        # ADD INTER USER PAGE ICONS
        if not self.theme_button_pressed:
            logger.debug(
                "Dark icon placer Actived... [ setIcon_for_window_dark ]")
            setIcon_line(self.ui.lineEdit_full_name, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit__name_initial, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_personal_contact, dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_spouse_name, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_agrakara_no, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_WOP_no, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_inc_no, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_email_id, dark.ICON_AT)
            setIcon_line(self.ui.lineEdit_educational_qualif, dark.ICON_QUALIF)
            setIcon_line(self.ui.lineEdit_professional_qualif,
                         dark.ICON_QUALIF)
            setIcon_line(self.ui.lineEdit_teaching_regist_no,
                         dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_appoint_subject, dark.ICON_SUBJECT)

            # ADD INTER NONE USER ICON
            setIcon_line(self.ui.lineEdit_full_name_none, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit__name_initial_none, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_personal_contact_none,
                         dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_spouse_name_none, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_agrakara_no_none, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_WOP_no_none, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_inc_no_none, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_email_id_none, dark.ICON_AT)
            setIcon_line(self.ui.lineEdit_educational_qualif_none,
                         dark.ICON_QUALIF)
            setIcon_line(self.ui.lineEdit_professional_qualif_none,
                         dark.ICON_QUALIF)
            setIcon_line(self.ui.lineEdit_salary_none, dark.ICON_RIG_NUM)

            # ADD LOWER PRIMARY USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_name_full_primary, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_primary, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_parent_contact_primary,
                         dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_no_siblings_primary,
                         dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_primary,
                         dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_name_primary,
                         dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_admission_no_primary,
                         dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_religion_primary, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_mather_job_primary, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_father_job_primary, dark.ICON_JOB)

            # ADD LOWER ORDNARY USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_name_full_lower, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_lower, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_parent_contact_lower,
                         dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_no_siblings_lower, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_lower, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_name_lower, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_job_lower, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_mather_job_lower, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_admission_no_lower,
                         dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_religion_lower, dark.ICON_RIL)

            # ADD LOWER ADVANCED USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_admission_no_ad, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_mather_name_ad, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_ad, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_job_ad, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_father_job_ad, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_parent_contact_no_ad,
                         dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_siblings_ad, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_name_full_ad, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_ad, dark.ICON_USER)

        else:
            print(self.theme_button_pressed)
            logger.debug(
                "Dark icon Replacer Actived... [ setIcon_for_window_dark ]")
            # ADD LOWER PRIMARY USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_name_full_primary, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_primary,
                          dark.ICON_USER)
            setIcon_line_(
                self.ui.lineEdit_parent_contact_primary, dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_no_siblings_primary,
                          dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_primary,
                          dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_name_primary,
                          dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_admission_no_primary,
                          dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_religion_primary, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_mather_job_primary, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_father_job_primary, dark.ICON_JOB)

            # ADD INTER USER PAGE ICON
            setIcon_line_(self.ui.lineEdit_full_name, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit__name_initial, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_personal_contact, dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_spouse_name, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_agrakara_no, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_WOP_no, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_inc_no, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_email_id, dark.ICON_AT)
            setIcon_line_(self.ui.lineEdit_educational_qualif,
                          dark.ICON_QUALIF)
            setIcon_line_(self.ui.lineEdit_professional_qualif,
                          dark.ICON_QUALIF)
            setIcon_line_(self.ui.lineEdit_teaching_regist_no,
                          dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_appoint_subject, dark.ICON_SUBJECT)

            # ADD INTER NONE USER ICON
            setIcon_line_(self.ui.lineEdit_full_name_none, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit__name_initial_none, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_personal_contact_none,
                          dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_spouse_name_none, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_agrakara_no_none, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_WOP_no_none, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_inc_no_none, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_email_id_none, dark.ICON_AT)
            setIcon_line_(
                self.ui.lineEdit_educational_qualif_none, dark.ICON_QUALIF)
            setIcon_line_(self.ui.lineEdit_professional_qualif_none,
                          dark.ICON_QUALIF)
            setIcon_line_(self.ui.lineEdit_salary_none, dark.ICON_RIG_NUM)

            # ADD LOWER ORDNARY USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_name_full_lower, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_lower, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_parent_contact_lower,
                          dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_no_siblings_lower, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_lower, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_name_lower, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_job_lower, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_mather_job_lower, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_admission_no_lower,
                          dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_religion_lower, dark.ICON_RIL)

            # ADD LOWER ADVANCED USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_admission_no_ad, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_mather_name_ad, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_ad, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_job_ad, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_father_job_ad, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_parent_contact_no_ad,
                          dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_siblings_ad, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_name_full_ad, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_ad, dark.ICON_USER)

        # SUPERUSER ICON AND NAME
        self.setTheSuperUserSideBarText_dark()

        # DELETE BTN ICONS
        setIcon(self.ui.btn_delete_inter_1, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_1, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_pri, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_advan, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_noneinter, dark.ICON_DELETE)

        setIcon(self.ui.btn_delete_inter_left_1, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_1, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_advan, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_pri, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_noneinter_left, dark.ICON_DELETE)

        setIcon(self.ui.btn_edit_interuser_left, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_edit_noneinteruser_left, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_edit_lower_left, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_edit_advan_left, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_edit_pri_left, dark.ICON_ADD_USER)

        setIcon(self.ui.btn_edit_interuser, dark.ICON_EDIT)
        setIcon(self.ui.btn_edit_noneinteruser, dark.ICON_EDIT)
        setIcon(self.ui.btn_edit_lower, dark.ICON_EDIT)
        setIcon(self.ui.btn_edit_advan, dark.ICON_EDIT)
        setIcon(self.ui.btn_edit_pri, dark.ICON_EDIT)

        # ABOUT LABEL ICON
        self.ui.label_logo_adout.setText(dark.ICON_LABEL_TEXT)

        # ACTIVE AND LEFT LABEL TEXT
        self.ui.label_info_user_inter_1.setText(dark.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_1.setText(dark.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_pri.setText(dark.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_advan.setText(
            dark.ACTIVE_LABEL_INFO_TEXT)

        self.ui.label_info_user_left_inter_1.setText(
            dark.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_1.setText(
            dark.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_pri.setText(
            dark.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_advan.setText(
            dark.LAFT_LABEL_INFO_TEXT)

    # this allows to change the theme of window
    def setTheme(self):

        if self.ui.comboBox_theme_items.currentIndex() == 0:
            logger.debug("Light theme Thread Actived... [ setTheme ]")
            # Light theme thread
            thread_theme = Thread_Theme()
            thread_theme.connect_function.connect(self.connect_functiom_light)
            thread_theme.connect_theme_styleSheet.connect(
                self.setTheme_for_window_light)
            thread_theme.connect_setIcons.connect(
                self.setIcon_for_window_light)
            thread_theme.start()
            thread_theme.exec_()

            thread_theme.finished.connect(lambda: self.iconButtonPressed(True))
            Thread(target=self.setTheThemeChangesJson,
                   args=["light", ]).start()

        else:
            logger.debug("Dark theme Thread Actived... [ setTheme ]")
            # Dark theme Thread
            thread_theme = Thread_Theme()
            thread_theme.connect_function.connect(self.connect_functiom_dark)
            thread_theme.connect_theme_styleSheet.connect(
                self.setTheme_for_window_dark)
            thread_theme.connect_setIcons.connect(self.setIcon_for_window_dark)
            thread_theme.start()
            thread_theme.exec_()

            thread_theme.finished.connect(lambda: self.iconButtonPressed(True))
            Thread(target=self.setTheThemeChangesJson, args=["dark", ]).start()

    # default theme for window startup

    def default_theme(self):
        logger.debug("set the default theme of findup... [ default_theme ]")
        setting = Setting.load_superuser()
        if setting["Setting"]["Default-theme"] == "light":
            self.setIcon_for_window_light()
            self.setTheme_for_window_light()
            self.connect_functiom_light()
        else:
            self.setIcon_for_window_dark()
            self.setTheme_for_window_dark()
            self.connect_functiom_dark()
        self.theme_button_pressed = True

    # Icon Button pressed Evenet Getter
    def iconButtonPressed(self, prim):
        logger.debug("Theme Icon Replacer Actived... [ iconButtonPressed ]")
        self.theme_button_pressed = prim

    # Set The Theme Changes into Json File
    def setTheThemeChangesJson(self, val):
        logger.debug(
            "The Theme Changes Setted into Json Setting File.... [ setTheThemeChangesJson ]")
        __data = Setting.load_superuser()
        __data[SETTING]["Default-theme"] = val
        Setting.store_superuser(__data[SETTING])
        print(val)

    # Super User Side Bar Text
    def setTheSuperUserSideBarText_dark(self):

        __data = Setting.load_superuser()
        __getuser = Crypto.decrypt_superuser(
            __data[SETTING]["Name"],
            __data[SETTING]["Password"],
            __data[SETTING]["Contact"],
            __data[SETTING]["E-mail"]
        )
        __user = [__getuser[0], __getuser[2], __getuser[-1]]
        dark.setSuperUserIconName(__getuser[0], self.ui.label_super_icon)
        dark.setSuperUserFinform(__user, self.ui.label_infor_super)

##################################################################################################
################################ Password Changer ###################################################
    # Thread For Access Window
    def thread_connecter_access_pwd(self):
        thread = Thread_Access()
        thread.opening_window.connect(self.changeTheUserPwd)
        thread.start()
        thread.exec_()

    # Change the Super Password
    def changeTheUserPwd(self):
        self.__access_window_pwd = Access_Window()
        self.__access_window_pwd.keyPressEvent = self.access_window_event_pwd
        self.__access_window_pwd.ui.btn_verify.clicked.connect(
            self.checkTheCurrentSupuerUserPwd_pwd)

    # Save the Superuser Password Changes
    def save_pwd_changes(self):

        logger.debug(
            "The New Password Is Set to The Software ... [save_pwd_changes]"
        )

        __getpass = self.ui.lineEdit_passord_input.text()
        __getpass_re = self.ui.lineEdit_repassword_input.text()

        if __getpass == __getpass_re:
            if checkThePassword(__getpass):
                __pwd, __pwdKey = Crypto.encrypt_one(__getpass)
                __data = Setting.load_superuser()
                __data[SETTING]["Password"] = [__pwd, __pwdKey]
                Setting.store_superuser(__data[SETTING])

                self.setTheAllLabelText()
                self.ui.lineEdit_repassword_input.clear()
                self.ui.lineEdit_passord_input.clear()

    # Check The User Entered Password And Current Password

    def checkTheCurrentSupuerUserPwd_pwd(self):
        __setting = Setting.load_superuser()
        __pass = Crypto.decrypt_one(
            [__setting[SETTING]["Password"][0], __setting[SETTING]["Password"][-1]]
        )

        getuserinput = self.__access_window_pwd.ui.lineEdit_current_password.text()

        if __pass == getuserinput and getuserinput != '':

            self.save_pwd_changes()
            self.__access_window_pwd.close()
        else:
            self.__access_window_pwd.shacke_window()

    # Access Window Event
    def access_window_event_pwd(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.checkTheCurrentSupuerUserPwd_pwd()

        elif event.key() == Qt.Key_Escape or event.key == Qt.Key_Enter:
            self.__access_window_pwd.close()
##################################################################################################


##################################################################################################
################################ Email Changer ###################################################
    # Thread For Access Window


    def thread_connecter_access_email(self):
        thread = Thread_Access()
        thread.opening_window.connect(self.changeTheUserEmail)
        thread.start()
        thread.exec_()

    # Change the Super Email
    def changeTheUserEmail(self):
        self.__access_window_email = Access_Window()
        self.__access_window_email.keyPressEvent = self.access_window_event_email
        self.__access_window_email.ui.btn_verify.clicked.connect(
            self.checkTheCurrentSupuerUserPwd_email)

    # Save the Superuser Email Changes
    def save_email_changes(self):
        __getemail = self.ui.lineEdit_change_email_input.text()
        logger.debug(
            "The New Email Is Set to The Software ... [save_email_changes]"
        )

        if checkTheEmail(__getemail) and __getemail != '':
            __email, __emailKey = Crypto.encrypt_one(__getemail)
            __data = Setting.load_superuser()
            __data[SETTING]["E-mail"] = [__email, __emailKey]
            Setting.store_superuser(__data[SETTING])

            self.setTheAllLabelText()
            self.ui.lineEdit_change_email_input.clear()

    # Check The User Entered Password And Current Password

    def checkTheCurrentSupuerUserPwd_email(self):
        __setting = Setting.load_superuser()
        __pass = Crypto.decrypt_one(
            [__setting[SETTING]["Password"][0], __setting[SETTING]["Password"][-1]]
        )

        getuserinput = self.__access_window_email.ui.lineEdit_current_password.text()
        if getuserinput != '':
            if __pass == getuserinput:
                self.save_email_changes()
                self.__access_window_email.close()
            else:
                self.__access_window_email.shacke_window()
        else:
            self.__access_window_email.shacke_window()

    # Access Window Event
    def access_window_event_email(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.checkTheCurrentSupuerUserPwd_email()

        elif event.key() == Qt.Key_Escape or event.key == Qt.Key_Enter:
            self.__access_window_email.close()
##################################################################################################

##################################################################################################
################################ Email Changer ###################################################
    # Thread For Access Window
    def thread_connecter_access_cont(self):
        thread = Thread_Access()
        thread.opening_window.connect(self.changeTheUserCont)
        thread.start()
        thread.exec_()

    # Change the Super Email
    def changeTheUserCont(self):
        self.__access_window_cont = Access_Window()
        self.__access_window_cont.keyPressEvent = self.access_window_event_cont
        self.__access_window_cont.ui.btn_verify.clicked.connect(
            self.checkTheCurrentSupuerUserPwd_cont)

    # Save the Superuser Email Changes
    def save_cont_changes(self):
        __getcont = self.ui.lineEdit_contact_number_input.text()

        logger.debug(
            "The New Contact Number Is Set to The Software ... [save_cont_changes]"
        )

        if checkTheContactNum(__getcont) and __getcont != '':
            __cont, __contKey = Crypto.encrypt_one(__getcont)
            __data = Setting.load_superuser()
            __data[SETTING]["Contact"] = [__cont, __contKey]
            Setting.store_superuser(__data[SETTING])

            self.setTheAllLabelText()
            self.ui.lineEdit_contact_number_input.clear()

    # Check The User Entered Password And Current Password

    def checkTheCurrentSupuerUserPwd_cont(self):
        __setting = Setting.load_superuser()
        __pass = Crypto.decrypt_one(
            [__setting[SETTING]["Password"][0], __setting[SETTING]["Password"][-1]]
        )

        getuserinput = self.__access_window_cont.ui.lineEdit_current_password.text()
        if __pass == getuserinput and getuserinput != '':
            self.save_cont_changes()
            self.__access_window_cont.close()
        else:
            self.__access_window_cont.shacke_window()

    # Access Window Event

    def access_window_event_cont(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.checkTheCurrentSupuerUserPwd_cont()

        elif event.key() == Qt.Key_Escape or event.key == Qt.Key_Enter:
            self.__access_window_cont.close()
##################################################################################################


##################################################################################################
################################ Name Changer ###################################################

    # Thread For Access Window

    def thread_connecter_access_name(self):
        thread = Thread_Access()
        thread.opening_window.connect(self.changeTheUserName)
        thread.start()
        thread.exec_()

    # Change the Super User Name
    def changeTheUserName(self):
        self.__access_window = Access_Window()
        self.__access_window.keyPressEvent = self.access_window_event_name
        self.__access_window.ui.btn_verify.clicked.connect(
            self.checkTheCurrentSupuerUserPwd_name)

    # Save the Superuser Name Changes
    def save_username_changes(self):

        __getuserinput = self.ui.lineEdit_username_change_input.text()

        logger.debug(
            "The New User Name Is Set to The Software ... [save_username_changes]"
        )

        if checkTheUserName(__getuserinput):
            __name, __nameKey = Crypto.encrypt_one(__getuserinput)
            __data = Setting.load_superuser()
            __data[SETTING]["Name"] = [__name, __nameKey]
            Setting.store_superuser(__data[SETTING])

            self.setTheAllLabelText()
            self.ui.lineEdit_username_change_input.clear()

    # Check The User Entered Password And Current Password

    def checkTheCurrentSupuerUserPwd_name(self):
        __setting = Setting.load_superuser()
        __pass = Crypto.decrypt_one(
            [__setting[SETTING]["Password"][0], __setting[SETTING]["Password"][-1]]
        )

        getuserinput = self.__access_window.ui.lineEdit_current_password.text()
        if __pass == getuserinput and getuserinput != '':
            self.save_username_changes()
            self.__access_window.close()
        else:
            self.__access_window.shacke_window()

    # Access Window Event
    def access_window_event_name(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.checkTheCurrentSupuerUserPwd_name()

        elif event.key() == Qt.Key_Escape or event.key == Qt.Key_Enter:
            self.__access_window.close()
##################################################################################################

    # Gender Value seter
    def gender_radioButtonClicked(self, obj_male, obj_female, obj_other):
        if obj_male.isChecked():
            self.__gender = "male"
            return True

        elif obj_female.isChecked():
            self.__gender = "female"
            return True

        elif obj_other.isChecked():
            self.__gender = "other"
            return True

        return False

    # Pick Teacher Image From Computer
    def pickImageFromComputer_teachers(self):
        global TEACHER_FACE_IMAGE_CONUT

        obj = PickImageWindow()
        path = obj.getPath()

        if path != "":

            self.__lastRollID = self.generateRollId()
            theUserOutPutImagePath = PATH_STORE_FACE_IMAGE_INTER + \
                self.__lastRollID + IMAGE_FORMAT

            if face_recognition(path, theUserOutPutImagePath,
                                self.ui.status_prograss.setValue, self.ui.label_status_text, change_image(
                                    theUserOutPutImagePath, "ADD TEACHERS"),
                                self.ui.label_icon_inter_teacher, TEACHER_FACE_PATH_LIST) == True:
                logger.debug(
                    "The Face Image is detected.. [pickImageFromComputer_teachers]")

            else:
                error = Error_Window(self)
                error.ui.label_error_text.setText(dark.TEXT_FOR_FACE_DETECTION)
                error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
                logger.warning(
                    "The Face Image is not detected.. [pickImageFromComputer_teachers]")
                self.__lastRollID = str()

    # Pick None-Teacher Image From Computer
    def pickImageFromComputer_teacher_none(self):
        global NONE_TEACHER_FACE_IMAGE_CONUT

        obj = PickImageWindow()
        path = obj.getPath()

        if path != "":

            self.__lastRollID = self.generateRollId()
            theUserOutPutImagePath = PATH_STORE_FACE_IMAGE_INTER_NONE + \
                self.__lastRollID + IMAGE_FORMAT

            if face_recognition(path, theUserOutPutImagePath, self.ui.status_prograss.setValue,
                                self.ui.label_status_text,  change_image(
                                    theUserOutPutImagePath, "ADD TEACHERS"),
                                self.ui.label_icon_none, NONE_TEACHER_FACE_PATH_LIST):
                logger.debug(
                    "The Face Image is detected.. [pickImageFromComputer_teacher_none]")

            else:
                error = Error_Window(self)
                error.ui.label_error_text.setText(dark.TEXT_FOR_FACE_DETECTION)
                error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
                logger.warning(
                    "The Face Image is not detected.. [pickImageFromComputer_teacher_none]")

                self.__lastRollID = str()

    # Pick Primary Image From Computer
    def pickImageFromComputer_primary(self):
        global PRAYMARY_FACE_IMAGE_COUNT

        obj = PickImageWindow()
        path = obj.getPath()

        if path != "":

            self.__lastRollID = self.generateRollId()
            theUserOutPutImagePath = PATH_STORE_FACE_IMAGE_PRIMARY + \
                self.__lastRollID + IMAGE_FORMAT

            if face_recognition(path, theUserOutPutImagePath, self.ui.status_prograss.setValue,
                                self.ui.label_status_text,  change_image(
                                    theUserOutPutImagePath, "ADD SUDENTS"),
                                self.ui.label_icon_primary, PRAYMARY_FACE_PATH_LIST):
                logger.debug(
                    "The Face Image is detected.. [pickImageFromComputer_primary]")

            else:
                error = Error_Window(self)
                error.ui.label_error_text.setText(dark.TEXT_FOR_FACE_DETECTION)
                error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
                logger.warning(
                    "The Face Image is not detected.. [pickImageFromComputer_primary]")
                self.__lastRollID = str()

    # Pick Ordnary Image From Computer
    def pickImageFromComputer_ordnary(self):
        global ORDNARY_FACE_IMAGE_COUNT

        obj = PickImageWindow()
        path = obj.getPath()

        if path != "":

            self.__lastRollID = self.generateRollId()
            theUserOutPutImagePath = PATH_STORE_FACE_IMAGE_ORDNARY + \
                self.__lastRollID + IMAGE_FORMAT

            if face_recognition(path, theUserOutPutImagePath, self.ui.status_prograss.setValue,
                                self.ui.label_status_text,  change_image(
                                    theUserOutPutImagePath, "ADD SUDENTS"),
                                self.ui.label_icon_lower, ORDNARY_FACE_PATH_LIST):
                logger.debug(
                    "The Face Image is detected.. [pickImageFromComputer_ordnary]")

            else:
                error = Error_Window(self)
                error.ui.label_error_text.setText(dark.TEXT_FOR_FACE_DETECTION)
                error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
                logger.warning(
                    "The Face Image is not detected.. [pickImageFromComputer_ordnary]")
                self.__lastRollID = str()

    # Pick Advnaced Image From Computer
    def pickImageFromComputer_advanced(self):
        global ADVANCED_FACE_IMAGE_COUNT

        obj = PickImageWindow()
        path = obj.getPath()

        if path != "":

            self.__lastRollID = self.generateRollId()
            theUserOutPutImagePath = PATH_STORE_FACE_IMAGE_ADVANCED + \
                self.__lastRollID + IMAGE_FORMAT

            if face_recognition(path, theUserOutPutImagePath, self.ui.status_prograss.setValue,
                                self.ui.label_status_text,  change_image(
                                    theUserOutPutImagePath, "ADD SUDENTS"),
                                self.ui.label_icon_, ADVANCED_FACE_PATH_LIST):
                logger.debug(
                    "The Face Image is detected.. [pickImageFromComputer_advanced]")

            else:
                error = Error_Window(self)
                error.ui.label_error_text.setText(dark.TEXT_FOR_FACE_DETECTION)
                error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
                logger.warning(
                    "The Face Image is not detected.. [pickImageFromComputer_advanced]")
                self.__lastRollID = str()

    # Generate Roll Number
    def generateRollId(self):
        return shortuuid.uuid()

    # Status Setter
    def status_radioButtonClicked(self, radio_marr, radio_unmarr):
        if radio_marr.isChecked():
            self.__status = "married"
            return True

        elif radio_unmarr.isChecked():
            self.__status = "unmarried"
            return True

        return False


##################################################################################################
################################ Store The Inter Users ###########################################


    def store_interuser_data(self):

        def clear():
            clear_dict_value(the_layout_of_teachers)
            self.clear_interuser_entries()

        __target_user = self.get_interuser_inputs()
        if __target_user != False:

            thread_store = ThreadStorePrograssBar(dark.LABEL_ICON_INTER_TEXT, the_layout_of_teachers, PATH_STORE_DATA_FILE_INTER,
                                                  INTERUSER, __target_user, rollIDShower(self.__lastRollID), "Storing...")
            thread_store.prograss_bar.connect(self.ui.status_prograss.setValue)
            thread_store.prograss_text.connect(
                self.ui.label_status_text.setText)
            thread_store.encrypt_function.connect(Crypto.encrypt_interuser)
            thread_store.store_function.connect(Store.append_json)
            thread_store.setRollIDLabelText.connect(
                self.ui.label_show_roll_number.setText)
            thread_store.theMainUserImage.connect(
                self.ui.label_icon_inter_teacher.setText)
            thread_store.finished.connect(clear)
            thread_store.start()
            thread_store.exec_()

            logger.debug("The Information is stored [store_interuser_data]")

        else:
            error = Error_Window(self)
            error.ui.label_error_text.setText(dark.TEXT_FOR_SOMETHING_MISSED)
            error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
            logger.warning("The some Entries are empty [store_interuser_data]")

    def clear_interuser_entries(self):
        self.ui.lineEdit_full_name.clear()
        self.ui.lineEdit__name_initial.clear()
        self.ui.lineEdit_inc_no.clear()
        self.ui.lineEdit_personal_contact.clear()
        self.ui.lineEdit_email_id.clear()
        self.ui.lineEdit_WOP_no.clear()
        self.ui.lineEdit_agrakara_no.clear()
        self.ui.lineEdit_spouse_name.clear()
        self.ui.lineEdit_teaching_regist_no.clear()
        self.ui.lineEdit_appoint_subject.clear()
        self.ui.lineEdit_educational_qualif.clear()
        self.ui.lineEdit_professional_qualif.clear()
        self.ui.lineEdit_nature_of_appoin.clear()
        self.ui.textEdit_working_address.clear()
        self.ui.textEdit_emergency.clear()
        self.ui.lineEdit_present_grade.clear()
        self.ui.dateEdit_present_date.clear()

    def get_interuser_inputs(self):

        __image_path = str()
        lastUserID_stored = str()

        try:
            __image_path = TEACHER_FACE_PATH_LIST[-1]
        except IndexError:
            pass

        # Check the Roll ID
        try:
            data_inter = Store.read_json(PATH_STORE_DATA_FILE_INTER)
            lastUserId = data_inter[INTERUSER][-1]
            lastUserId = Crypto.decrypt_ID(lastUserId, lastUserID_stored)
        except IndexError:
            pass
        except FileNotFoundError:
            pass
        except KeyError:
            pass

        finally:

            if self.__lastRollID == '' or self.__lastRollID == lastUserID_stored:
                __rollNumber = self.generateRollId()
            else:
                __rollNumber = self.__lastRollID

            __name_in_full = self.ui.lineEdit_full_name.text()
            __name_with_initial = self.ui.lineEdit__name_initial.text()
            __nic = self.ui.lineEdit_inc_no.text()
            __contact_num = self.ui.lineEdit_personal_contact.text()
            __email_id = self.ui.lineEdit_email_id.text()
            __wop_num = self.ui.lineEdit_WOP_no.text()
            __agrakara_num = self.ui.lineEdit_agrakara_no.text()
            __spouse_name = self.ui.lineEdit_spouse_name.text()
            __teaching_reg_num = self.ui.lineEdit_teaching_regist_no.text()
            __appointed_subject = self.ui.lineEdit_appoint_subject.text()
            __educational_qualifi = self.ui.lineEdit_educational_qualif.text()
            __professional_qualifi = self.ui.lineEdit_professional_qualif.text()
            __nature_of_appointment = self.ui.lineEdit_nature_of_appoin.text()
            __icrement_date = self.ui.dateEdit_increment_date.date().toString()
            __date_of_birth = self.ui.dateEdit_DOB.date().toString()
            __date_first_appoint = self.ui.dateEdit_first_appointment_date.date().toString()
            __address = self.ui.textEdit_working_address.toPlainText()
            __contact_address_emergency = self.ui.textEdit_emergency.toPlainText()
            __present_grade = self.ui.lineEdit_present_grade.text()
            __date_present_grade = self.ui.dateEdit_present_date.text()
            __date_appointment_this_school = self.ui.dateEdit_appointment_date.date().toString()

            if self.gender_radioButtonClicked(
                self.ui.radioButton_male,
                self.ui.radioButton_female,
                self.ui.radioButton_other) and\
                    self.status_radioButtonClicked(self.ui.radioButton_married, self.ui.radioButton_unmarried) and\
                    __name_in_full != '' and __name_with_initial != '' and __address != '' and \
                    __contact_num != '':

                __target_user = [
                    __rollNumber, __name_in_full, __name_with_initial, __nic, __contact_num, __email_id,  __wop_num, __agrakara_num,
                    __spouse_name, __teaching_reg_num, __appointed_subject, __educational_qualifi,
                    __professional_qualifi, __nature_of_appointment, __icrement_date, __date_of_birth,
                    __date_first_appoint, __address, __contact_address_emergency, __present_grade,
                    __date_present_grade, __date_appointment_this_school, self.__status, self.__gender, __image_path
                ]

                self.__lastRollID = __rollNumber

                for index in range(len(__target_user)):
                    if __target_user[index] == '':
                        __target_user[index] = None

                return __target_user

        return False


##################################################################################################
################################ Store The None - Inter Users ####################################


    def store_noneinteruser_data(self):
        def clear():
            clear_dict_value(the_layout_of_none_teacher)
            self.clear_noneinteruser_entries()

        __target_user = self.get_noneinteruser_inputs()
        if __target_user != False:
            thread_store = ThreadStorePrograssBar(dark.LABEL_ICON_INTER_TEXT, the_layout_of_none_teacher, PATH_STORE_DATA_FILE_INTER_NONE,
                                                  NONEINTERUSER, __target_user, rollIDShower(self.__lastRollID), "Storing...")
            thread_store.prograss_bar.connect(self.ui.status_prograss.setValue)
            thread_store.prograss_text.connect(
                self.ui.label_status_text.setText)
            thread_store.encrypt_function.connect(Crypto.encrypt_interuser)
            thread_store.store_function.connect(Store.append_json)
            thread_store.setRollIDLabelText.connect(
                self.ui.label_show_roll_number_none.setText)
            thread_store.theMainUserImage.connect(
                self.ui.label_icon_none.setText)
            thread_store.finished.connect(clear)
            thread_store.start()
            thread_store.exec_()

            logger.debug(
                "The Information is stored [store_noneinteruser_data]")

        else:
            error = Error_Window(self)
            error.ui.label_error_text.setText(dark.TEXT_FOR_SOMETHING_MISSED)
            error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
            logger.warning(
                "The some Entries are empty [store_noneinteruser_data]")

    def clear_noneinteruser_entries(self):
        self.ui.lineEdit_full_name_none.clear()
        self.ui.lineEdit__name_initial_none.clear()
        self.ui.lineEdit_inc_no_none.clear()
        self.ui.lineEdit_personal_contact_none.clear()
        self.ui.lineEdit_email_id_none.clear()
        self.ui.lineEdit_WOP_no_none.clear()
        self.ui.lineEdit_agrakara_no_none.clear()
        self.ui.lineEdit_spouse_name_none.clear()
        self.ui.lineEdit_educational_qualif_none.clear()
        self.ui.lineEdit_professional_qualif_none.clear()
        self.ui.lineEdit_nature_of_appoin_none.clear()
        self.ui.textEdit_working_address_none.clear()
        self.ui.textEdit_emergency_none.clear()
        self.ui.lineEdit_salary_none.clear()

    def get_noneinteruser_inputs(self):

        __image_path = str()
        lastUserID_stored = str()

        try:
            __image_path = NONE_TEACHER_FACE_PATH_LIST[-1]
        except IndexError:
            pass

        # Check the Roll ID
        try:
            data_inter = Store.read_json(PATH_STORE_DATA_FILE_INTER_NONE)
            lastUserId = data_inter[NONEINTERUSER][-1]
            Crypto.decrypt_ID(lastUserId, lastUserID_stored)

        except IndexError:
            pass
        except FileNotFoundError:
            pass
        except KeyError:
            pass

        finally:

            if self.__lastRollID == '' or self.__lastRollID == lastUserID_stored:
                __rollNumber = self.generateRollId()
            else:
                __rollNumber = self.__lastRollID

            __name_in_full = self.ui.lineEdit_full_name_none.text()
            __name_with_initial = self.ui.lineEdit__name_initial_none.text()
            __nic = self.ui.lineEdit_inc_no_none.text()
            __contact_num = self.ui.lineEdit_personal_contact_none.text()
            __email_id = self.ui.lineEdit_email_id_none.text()
            __wop_num = self.ui.lineEdit_WOP_no_none.text()
            __agrakara_num = self.ui.lineEdit_agrakara_no_none.text()
            __spouse_name = self.ui.lineEdit_spouse_name_none.text()
            __educational_qualifi = self.ui.lineEdit_educational_qualif_none.text()
            __professional_qualifi = self.ui.lineEdit_professional_qualif_none.text()
            __nature_of_appointment = self.ui.lineEdit_nature_of_appoin_none.text()
            __icrement_date = self.ui.dateEdit_increment_date_none.date().toString()
            __date_of_birth = self.ui.dateEdit_DOB_none.date().toString()
            __date_first_appoint = self.ui.dateEdit_first_appointment_date_none.date().toString()
            __address = self.ui.textEdit_working_address_none.toPlainText()
            __contact_address_emergency = self.ui.textEdit_emergency_none.toPlainText()
            __date_appointment_this_school = self.ui.dateEdit_appointment_date_none.date().toString()
            __salary_no = self.ui.lineEdit_salary_none.text()

            if self.gender_radioButtonClicked(
                self.ui.radioButton_male_none,
                self.ui.radioButton_female_none,
                self.ui.radioButton_other_none) and\
                    self.status_radioButtonClicked(self.ui.radioButton_married_none, self.ui.radioButton_unmarried_none) and\
                    __name_in_full != '' and __name_with_initial != '' and __address != '' and \
                    __contact_num != '':

                __target_user = [
                    __rollNumber, __name_in_full, __name_with_initial, __nic, __contact_num, __email_id,  __wop_num, __agrakara_num,
                    __spouse_name,  __educational_qualifi, __salary_no,
                    __professional_qualifi, __nature_of_appointment, __icrement_date, __date_of_birth,
                    __date_first_appoint, __address, __contact_address_emergency,  __date_appointment_this_school,
                    self.__status, self.__gender, __image_path
                ]

                self.__lastRollID = __rollNumber

                for index in range(len(__target_user)):
                    if __target_user[index] == '':
                        __target_user[index] = None

                return __target_user

        return False

##################################################################################################
################################ Store The Primary Users #########################################

    def store_primaryuser_data(self):

        def clear():
            clear_dict_value(the_layout_of_primary)
            self.clear_primaryuser_entries()

        __target_user = self.get_primaryuser_inputs()
        if __target_user != False:

            thread_store = ThreadStorePrograssBar(dark.LABEL_ICON_LOWER_TEXT, the_layout_of_primary, PATH_STORE_DATA_FILE_PRIMARY,
                                                  PRIMARYLOWER, __target_user, rollIDShower(self.__lastRollID), "Storing...", self.__level)
            thread_store.prograss_bar.connect(self.ui.status_prograss.setValue)
            thread_store.prograss_text.connect(
                self.ui.label_status_text.setText)
            thread_store.encrypt_function.connect(Crypto.encrypt_interuser)
            thread_store.store_function.connect(Store.append_json)
            thread_store.setRollIDLabelText.connect(
                self.ui.label_show_roll_primary.setText)
            thread_store.theMainUserImage.connect(
                self.ui.label_icon_primary.setText)
            thread_store.finished.connect(clear)
            thread_store.start()
            thread_store.exec_()

            logger.debug(
                "The Information is stored [store_primaryuser_data]")

        else:
            error = Error_Window(self)
            error.ui.label_error_text.setText(dark.TEXT_FOR_SOMETHING_MISSED)
            error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
            logger.warning(
                "The some Entries are empty [store_primaryuser_data]")

    def clear_primaryuser_entries(self):
        self.ui.lineEdit_name_full_primary.clear()
        self.ui.lineEdit_name_initial_primary.clear()
        self.ui.textEdit_address_home.clear()
        self.ui.textEdit_address_office.clear()
        self.ui.lineEdit_father_name_primary.clear()
        self.ui.lineEdit_mather_name_primary.clear()
        self.ui.lineEdit_no_siblings_primary.clear()
        self.ui.lineEdit_religion_primary.clear()
        self.ui.lineEdit_admission_no_primary.clear()
        self.ui.lineEdit_father_job_primary.clear()
        self.ui.lineEdit_mather_job_primary.clear()
        self.ui.lineEdit_parent_contact_primary.clear()

    def get_primaryuser_inputs(self):

        __image_path = str()
        lastUserID_stored = str()

        try:
            __image_path = PRAYMARY_FACE_PATH_LIST[-1]
        except IndexError:
            pass

        # Check the Roll ID
        try:
            data_inter = Store.read_json(PATH_STORE_DATA_FILE_PRIMARY)
            lastUserId = data_inter[PRIMARYLOWER][self.__level][-1]
            Crypto.decrypt_ID(lastUserId, lastUserID_stored)

        except IndexError:
            pass
        except FileNotFoundError:
            pass
        except KeyError:
            pass

        finally:

            if self.__lastRollID == '' or self.__lastRollID == lastUserID_stored:
                __rollNumber = self.generateRollId()
            else:
                __rollNumber = self.__lastRollID

            __name_full = self.ui.lineEdit_name_full_primary.text()
            __name_initial = self.ui.lineEdit_name_initial_primary.text()
            __address = self.ui.textEdit_address_home.toPlainText()
            __address_office = self.ui.textEdit_address_office.toPlainText()
            __father_name = self.ui.lineEdit_father_name_primary.text()
            __mather_name = self.ui.lineEdit_mather_name_primary.text()
            __number_siblings = self.ui.lineEdit_no_siblings_primary.text()
            __level = self.ui.comboBox_stream_primary.currentText()
            __religion = self.ui.lineEdit_religion_primary.text()
            __admission_num = self.ui.lineEdit_admission_no_primary.text()
            __father_job = self.ui.lineEdit_father_job_primary.text()
            __mather_job = self.ui.lineEdit_mather_job_primary.text()
            __perent_guardian_num = self.ui.lineEdit_parent_contact_primary.text()
            __data_birth = self.ui.dateEdit_date_of_birth_primary.date().toString()
            __date_admission = self.ui.dateEdit_date_admission_primary.date().toString()

            if self.gender_radioButtonClicked(
                self.ui.radioButton_male_primary_2,
                self.ui.radioButton_female_primary_2,
                self.ui.radioButton_other_primary_2) and\
                    __name_full != '' and __name_initial != '' and __address != '' and \
                    __perent_guardian_num != '':

                __target_user = [
                    __rollNumber, __name_full, __name_initial, __address, __address_office, __father_name, __mather_name,
                    __number_siblings, __level, __religion, __admission_num, __father_job, __mather_job,
                    __perent_guardian_num, __data_birth, __date_admission, self.__gender, __image_path
                ]

                self.__lastRollID = __rollNumber
                self.__level = __level

                for index in range(len(__target_user)):
                    if __target_user[index] == '':
                        __target_user[index] = None

                return __target_user
        return False

##################################################################################################
################################ Store The Ordnary Users #########################################
    def store_ordnaryuser_data(self):
        def clear():
            clear_dict_value(the_layout_of_ordnary)
            self.clear_ordnaryuser_entries()

        __target_user = self.get_ordnaryuser_inputs()
        if __target_user != False:
            thread_store = ThreadStorePrograssBar(dark.LABEL_ICON_LOWER_TEXT, the_layout_of_ordnary, PATH_STORE_DATA_FILE_ORDNARY,
                                                  ORDNARYLOWER, __target_user, rollIDShower(self.__lastRollID), "Storing...", self.__level)
            thread_store.prograss_bar.connect(self.ui.status_prograss.setValue)
            thread_store.prograss_text.connect(
                self.ui.label_status_text.setText)
            thread_store.encrypt_function.connect(Crypto.encrypt_interuser)
            thread_store.store_function.connect(Store.append_json)
            thread_store.setRollIDLabelText.connect(
                self.ui.label_show_roll_number_lower.setText)
            thread_store.theMainUserImage.connect(
                self.ui.label_icon_lower.setText)
            thread_store.finished.connect(clear)
            thread_store.start()
            thread_store.exec_()

            logger.debug(
                "The Information is stored [store_primaryuser_data]")

        else:
            error = Error_Window(self)
            error.ui.label_error_text.setText(dark.TEXT_FOR_SOMETHING_MISSED)
            error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
            logger.warning(
                "The some Entries are empty [store_ordnaryuser_data]")

    def clear_ordnaryuser_entries(self):
        self.ui.lineEdit_name_full_lower.clear()
        self.ui.lineEdit_name_initial_lower.clear()
        self.ui.textEdit_address_home_lower.clear()
        self.ui.textEdit_address_office_lower.clear()
        self.ui.lineEdit_father_job_lower.clear()
        self.ui.lineEdit_mather_name_lower.clear()
        self.ui.lineEdit_no_siblings_lower.clear()
        self.ui.lineEdit_religion_lower.clear()
        self.ui.lineEdit_admission_no_lower.clear()
        self.ui.lineEdit_father_job_lower.clear()
        self.ui.lineEdit_mather_job_lower.clear()
        self.ui.lineEdit_parent_contact_lower.clear()

    def get_ordnaryuser_inputs(self):
        __image_path = str()
        lastUserID_stored = str()

        try:
            __image_path = ORDNARY_FACE_PATH_LIST[-1]
        except IndexError:
            pass

        # Check the Roll ID
        try:
            data_inter = Store.read_json(PATH_STORE_DATA_FILE_ORDNARY)
            lastUserId = data_inter[ORDNARYLOWER][self.__level][-1]
            Crypto.decrypt_ID(lastUserId, lastUserID_stored)

        except IndexError:
            pass
        except FileNotFoundError:
            pass
        except KeyError:
            pass

        finally:

            if self.__lastRollID == '' or self.__lastRollID == lastUserID_stored:
                __rollNumber = self.generateRollId()
            else:
                __rollNumber = self.__lastRollID

            __name_full = self.ui.lineEdit_name_full_lower.text()
            __name_initial = self.ui.lineEdit_name_initial_lower.text()
            __address = self.ui.textEdit_address_home_lower.toPlainText()
            __address_office = self.ui.textEdit_address_office_lower.toPlainText()
            __father_name = self.ui.lineEdit_father_name_lower.text()
            __mather_name = self.ui.lineEdit_mather_name_lower.text()
            __number_siblings = self.ui.lineEdit_no_siblings_lower.text()
            __level = self.ui.comboBox_stream_lower.currentText()
            __religion = self.ui.lineEdit_religion_lower.text()
            __admission_num = self.ui.lineEdit_admission_no_lower.text()
            __father_job = self.ui.lineEdit_father_job_lower.text()
            __mather_job = self.ui.lineEdit_mather_job_lower.text()
            __perent_guardian_num = self.ui.lineEdit_parent_contact_lower.text()
            __data_birth = self.ui.dateEdit_date_of_birth_lower.date().toString()
            __date_admission = self.ui.dateEdit_date_admission_lower.date().toString()

            if self.gender_radioButtonClicked(
                self.ui.radioButton_male_lower_2,
                self.ui.radioButton_female_lower_2,
                self.ui.radioButton_other_lower_2) and\
                    __name_full != '' and __name_initial != '' and __address != '' and \
                    __perent_guardian_num != '':

                __target_user = [
                    __rollNumber, __name_full, __name_initial, __address, __address_office, __father_name, __mather_name,
                    __number_siblings, __level, __religion, __admission_num, __father_job, __mather_job,
                    __perent_guardian_num, __data_birth, __date_admission, self.__gender, __image_path
                ]

                self.__lastRollID = __rollNumber
                self.__level = __level

                for index in range(len(__target_user)):
                    if __target_user[index] == '':
                        __target_user[index] = None

                return __target_user
        return False

##################################################################################################
################################ Store The Advnaced Users ########################################
    def store_advanceduser_data(self):
        def clear():
            clear_dict_value(the_layout_of_advanced)
            self.clear_advanceduser_entries()

        __target_user = self.get_advnaceduser_inputs()
        if __target_user != False:
            thread_store = ThreadStorePrograssBar(dark.LABEL_ICON_LOWER_TEXT, the_layout_of_advanced, PATH_STORE_DATA_FILE_ADVNACED,
                                                  ADVNACEDLOWER, __target_user, rollIDShower(self.__lastRollID), "Storing...", self.__level, self.__streem.replace(" ", "-"))
            thread_store.prograss_bar.connect(self.ui.status_prograss.setValue)
            thread_store.prograss_text.connect(
                self.ui.label_status_text.setText)
            thread_store.encrypt_function.connect(Crypto.encrypt_interuser)
            thread_store.store_function.connect(Store.append_json)
            thread_store.setRollIDLabelText.connect(
                self.ui.label_show_roll_ad.setText)
            thread_store.theMainUserImage.connect(self.ui.label_icon_.setText)
            thread_store.finished.connect(clear)
            thread_store.start()
            thread_store.exec_()

            logger.debug(
                "The Information is stored [store_advanceduser_data]")

        else:
            error = Error_Window(self)
            error.ui.label_error_text.setText(dark.TEXT_FOR_SOMETHING_MISSED)
            error.ui.label_icon.setPixmap(QPixmap(dark.ICON_WARNING))
            logger.warning(
                "The some Entries are empty [store_advanceduser_data]")

    def clear_advanceduser_entries(self):
        self.ui.lineEdit_name_full_ad.clear()
        self.ui.lineEdit_name_initial_ad.clear()
        self.ui.lineEdit_home_address_ad.clear()
        self.ui.lineEdit_address_office_ad.clear()
        self.ui.lineEdit_father_name_ad.clear()
        self.ui.lineEdit_mather_name_ad.clear()
        self.ui.lineEdit_siblings_ad.clear()
        self.ui.lineEdit_religion_ad.clear()
        self.ui.lineEdit_admission_no_ad.clear()
        self.ui.lineEdit_father_job_ad.clear()
        self.ui.lineEdit_mather_job_ad.clear()
        self.ui.lineEdit_parent_contact_no_ad.clear()

    def get_advnaceduser_inputs(self):
        __image_path = str()
        lastUserID_stored = str()

        try:
            __image_path = ADVANCED_FACE_PATH_LIST[-1]
        except IndexError:
            pass

        # Check the Roll ID
        try:
            data_inter = Store.read_json(PATH_STORE_DATA_FILE_ADVNACED)
            lastUserId = data_inter[ADVNACEDLOWER][self.__level][self.__streem.replace(
                " ", "-")][-1]
            Crypto.decrypt_ID(lastUserId, lastUserID_stored)

        except IndexError:
            pass
        except FileNotFoundError:
            pass
        except KeyError:
            pass

        finally:

            if self.__lastRollID == '' or self.__lastRollID == lastUserID_stored:
                __rollNumber = self.generateRollId()
            else:
                __rollNumber = self.__lastRollID

            __name_full = self.ui.lineEdit_name_full_ad.text()
            __name_initial = self.ui.lineEdit_name_initial_ad.text()
            __address = self.ui.lineEdit_home_address_ad.toPlainText()
            __address_office = self.ui.lineEdit_address_office_ad.toPlainText()
            __father_name = self.ui.lineEdit_father_name_ad.text()
            __mather_name = self.ui.lineEdit_mather_name_ad.text()
            __number_siblings = self.ui.lineEdit_siblings_ad.text()
            __level = self.ui.comboBox_level_ad.currentText()
            __streem = self.ui.comboBox_stream.currentText()
            __religion = self.ui.lineEdit_religion_ad.text()
            __admission_num = self.ui.lineEdit_admission_no_ad.text()
            __father_job = self.ui.lineEdit_father_job_ad.text()
            __mather_job = self.ui.lineEdit_mather_job_ad.text()
            __perent_guardian_num = self.ui.lineEdit_parent_contact_no_ad.text()
            __data_birth = self.ui.dateEdit_date_of_birth_ad.date().toString()
            __date_admission = self.ui.dateEdit_date_of_admission_ad.date().toString()

            if self.gender_radioButtonClicked(
                self.ui.radioButton_male_ad,
                self.ui.radioButton_female_ad,
                self.ui.radioButton_other_ad) and\
                    __name_full != '' and __name_initial != '' and __address != '' and \
                    __perent_guardian_num != '':

                __target_user = [
                    __rollNumber, __name_full, __name_initial, __address, __address_office, __father_name, __mather_name,
                    __number_siblings, __level, __streem, __religion, __admission_num, __father_job, __mather_job,
                    __perent_guardian_num, __data_birth, __date_admission, self.__gender, __image_path
                ]

                self.__lastRollID = __rollNumber
                self.__level = __level
                self.__streem = __streem

                for index in range(len(__target_user)):
                    if __target_user[index] == '':
                        __target_user[index] = None

                return __target_user
        return False
##################################################################################################

    # Event Filter For Press Event
    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent):

        text = None

        if event.type() == QEvent.KeyPress and event == QKeySequence.Copy:

            # Roll Number For Users
            if self.ui.label_show_roll_number.hasSelectedText():
                text = self.ui.label_show_roll_number.selectedText()
            elif self.ui.label_show_roll_number_none.hasSelectedText():
                text = self.ui.label_show_roll_number_none.selectedText()
            elif self.ui.label_show_roll_primary.hasSelectedText():
                text = self.ui.label_show_roll_primary.selectedText()
            elif self.ui.label_show_roll_number_lower.hasSelectedText():
                text = self.ui.label_show_roll_number_lower.selectedText()
            elif self.ui.label_show_roll_ad.hasSelectedText():
                text = self.ui.label_show_roll_ad.selectedText()

            if text != None and text:
                QApplication.clipboard().setText(text)

        elif event.type() == QEvent.ContextMenu and (source is self.ui.label_show_roll_number or
                                                     source is self.ui.label_show_roll_number_none or source is self.ui.label_show_roll_primary or
                                                     source is self.ui.label_show_roll_number_lower or source is self.ui.label_show_roll_ad):

            # Roll Number For Users
            if self.ui.label_show_roll_number.hasSelectedText():
                text = self.ui.label_show_roll_number.selectedText()
            elif self.ui.label_show_roll_number_none.hasSelectedText():
                text = self.ui.label_show_roll_number_none.selectedText()
            elif self.ui.label_show_roll_primary.hasSelectedText():
                text = self.ui.label_show_roll_primary.selectedText()
            elif self.ui.label_show_roll_number_lower.hasSelectedText():
                text = self.ui.label_show_roll_number_lower.selectedText()
            elif self.ui.label_show_roll_ad.hasSelectedText():
                text = self.ui.label_show_roll_ad.selectedText()

            menu = QMenu(self)

            setting = Setting.load_superuser()
            if setting["Setting"]["Default-theme"] == "light":
                menu.setStyleSheet(light.MENU)
            else:
                menu.setStyleSheet(dark.MENU)

            copyAction = menu.addAction("Copy")
            copyAction.setShortcut("Ctrl+C")

            paste = menu.addAction("Paste")
            paste.setShortcut("Ctrl+V")
            paste.setEnabled(False)

            if not text and text is None:
                copyAction.setEnabled(False)

            res = menu.exec_(QCursor.pos())
            if res == copyAction:
                QApplication.clipboard().setText(text)

        return super().eventFilter(source, event)


class Verifier:
    def __init__(self):
        try:

            self.path = os.listdir(PATH_CONFIG_DIR)
            self.verifier = False
            if SETTING_FILE in self.path:
                __data = Setting.load_superuser()
                self.verifier = __data[SETTING]['Create']

        except FileNotFoundError:
            self.verifier = False

    def run(self):
        if self.verifier:
            app = QApplication(sys.argv)
            login = Main_Window()
            app.exec_()

        else:
            app = QApplication(sys.argv)
            create = Create_Window()
            app.exec()


if __name__ == "__main__":
    verifier = Verifier()
    verifier.run()
