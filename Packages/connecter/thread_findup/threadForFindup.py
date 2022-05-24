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