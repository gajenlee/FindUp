from importlib_metadata import sys
from Packages.uis.access.ui_access import *
from Packages.uis.backup.ui_backup import *
from Packages.uis.create.ui_create import *
from Packages.uis.login.ui_login import *
from Packages.uis.main.ui_main import *

from Packages.connecter.cryptography.crypto import *
from Packages.connecter.progressBar.circular_progress import *
from Packages.connecter.store.store import *


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Access_Window(QDialog):
    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Access()
        self.ui.setupUi(self)
        self.show()


class Backup_Window(QDialog):
    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Backup()
        self.ui.setupUi(self)
        self.show()


class Create_Window(QMainWindow):
    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Create()
        self.ui.setupUi(self)
        self.show()


class Login_Window(QMainWindow):
    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.show()


class Main_Window(QMainWindow):
    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main_Window()
    app.exec_()
