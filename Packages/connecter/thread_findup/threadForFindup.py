from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from time import sleep

import cv2 as cv
import random

from httpx import stream


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


# The Main Window Opening Thread
class Thread_Open(QThread):
    opening_window = pyqtSignal()

    def run(self):
        self.opening_window.emit()


# The Access Window Opening Window Thread
class Thread_Access(QThread):
    opening_window = pyqtSignal()

    def run(self):
        self.opening_window.emit()


# The PrograssBar
class Thread_Prograss(QThread):

    prograss_bar = pyqtSignal(int)
    prograss_text = pyqtSignal(str)

    theMainUserImage = pyqtSignal(str)

    def __init__(self, text_value, setting_img_text, file_path, output_file_path, xml_file):
        super().__init__()
        self.text_value = text_value
        self.setting_img_text = setting_img_text
        self.file_path = file_path
        self.output_file_path = output_file_path
        self.xml_file = xml_file

    def run(self):
        self.prograss_text.emit(self.text_value)
        self.face_recognition()
        for i in range(0, 101, 30):
            sleep(.5)
            self.prograss_bar.emit(i)
        self.prograss_text.emit("Complete...")
        self.theMainUserImage.emit(self.setting_img_text)
        self.prograss_bar.emit(0)
        sleep(2)

    def face_recognition(self):
        img = cv.imread(self.file_path)
        imageGry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_cascade = cv.CascadeClassifier(self.xml_file)
        faces = face_cascade.detectMultiScale(imageGry, 1.1, 4)

        for (x, y, w, h) in faces:
            faces = img[y - 50: y + h + 50, x - 50: x + w + 50]
            img = cv.resize(faces, (75, 75), interpolation=cv.INTER_AREA)
            cv.imwrite(self.output_file_path, img)


# The PrograssBar For Store The Information
class ThreadStorePrograssBar(QThread):

    prograss_bar = pyqtSignal(int)
    prograss_text = pyqtSignal(str)

    store_function_inter = pyqtSignal(dict, str, str)
    store_function_ord = pyqtSignal(dict, str, str, str)
    store_function_advan = pyqtSignal(dict, str, str, str, str)

    encrypt_function = pyqtSignal(list, dict)
    setRollIDLabelText = pyqtSignal(str)

    theMainUserImage = pyqtSignal(str)

    def __init__(self, setting_image, data_dict, path, userType, target_list, rollIdText, pro_text, level=None, streem=None):
        super().__init__()
        self.data_dict = data_dict
        self.path = path
        self.userType = userType
        self.target_list = target_list
        self.rollIdText = rollIdText
        self.pro_text = pro_text
        self.setting_image = setting_image

        self.level = level
        self.streem = streem

    def run(self):

        if self.level == None and self.streem == None:

            self.prograss_text.emit(self.pro_text)
            self.encrypt_function.emit(self.target_list, self.data_dict)
            self.store_function_inter.emit(
                self.data_dict, self.path, self.userType)

            for i in range(0, 101, 30):
                sleep(.5)
                self.prograss_bar.emit(i)
            self.prograss_text.emit("Complete...")
            self.setRollIDLabelText.emit(self.rollIdText)
            sleep(1)
            self.prograss_bar.emit(0)
            self.theMainUserImage.emit(self.setting_image)

        elif self.level != None and self.streem == None:

            self.prograss_text.emit(self.pro_text)
            self.encrypt_function.emit(self.target_list, self.data_dict)
            self.store_function_ord.emit(
                self.data_dict, self.path, self.userType, self.level)

            for i in range(0, 101, 30):
                sleep(.5)
                self.prograss_bar.emit(i)
            self.prograss_text.emit("Complete...")
            self.setRollIDLabelText.emit(self.rollIdText)
            sleep(1)
            self.prograss_bar.emit(0)
            self.theMainUserImage.emit(self.setting_image)

        else:

            self.prograss_text.emit(self.pro_text)
            self.encrypt_function.emit(self.target_list, self.data_dict)
            self.store_function_advan.emit(
                self.data_dict, self.path, self.userType, self.level, self.streem)

            for i in range(0, 101, 30):
                sleep(.5)
                self.prograss_bar.emit(i)
            self.prograss_text.emit("Complete...")
            self.setRollIDLabelText.emit(self.rollIdText)
            sleep(1)
            self.prograss_bar.emit(0)
            self.theMainUserImage.emit(self.setting_image)


# The Randomise For Stored Data
class Thread_Randomize(QThread):

    prograss_bar = pyqtSignal(int)
    prograss_label = pyqtSignal(str)

    randomizer = pyqtSignal()

    def __init__(self, status_label_text):
        super().__init__()
        self.status_label_text = status_label_text

    def run(self):
        self.prograss_label.emit(self.status_label_text)

        for i in range(0, 101, 50):
            self.prograss_bar.emit(i)
            sleep(.5)

        self.randomizer.emit()

        self.prograss_bar.emit(0)
        self.prograss_label.emit("Complete...")
        sleep(1)
        self.prograss_label.emit("")
