from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# THREAD FOR THEME CHANGER BUTTON


class Thread_Theme(QThread):
    connect_function = pyqtSignal()
    connect_theme_styleSheet = pyqtSignal()
    connect_setIcons = pyqtSignal()

    def run(self):
        self.connect_function.emit()
        self.connect_theme_styleSheet.emit()
        self.connect_setIcons.emit()

# THREAD FOR LOGIN THREAD EVENT GETTER


class Thread_Loading(QThread):
    prograss_function = pyqtSignal()

    def run(self):
        self.prograss_function.emit()

# The Toggle Button


class Thread_Toggle(QThread):
    button_function = pyqtSignal()

    def run(self):
        self.button_function.emit()
