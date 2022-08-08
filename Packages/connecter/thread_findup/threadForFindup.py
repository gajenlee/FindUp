from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from time import sleep

import cv2 as cv
import shutil
import numpy as np

from importlib_metadata import os


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
    button = pyqtSignal(bool)

    theMainUserImage = pyqtSignal(str)

    def __init__(self, text_value, setting_img_text, file_path, output_file_path, xml_file, error_code):
        super().__init__()
        self.text_value = text_value
        self.setting_img_text = setting_img_text
        self.file_path = file_path
        self.output_file_path = output_file_path
        self.xml_file = xml_file
        self.error_code = error_code

    def run(self):
        self.button.emit(False)
        self.prograss_text.emit(self.text_value)
        self.face_recognition()
        self.prograss_text.emit("Complete...")

        if self.error_code == []:
            self.theMainUserImage.emit(self.setting_img_text)

        self.prograss_bar.emit(0)
        sleep(2)
        self.button.emit(True)

    def face_recognition(self):
        img = cv.imread(self.file_path)
        imageGry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_cascade = cv.CascadeClassifier(self.xml_file)
        faces = face_cascade.detectMultiScale(imageGry, 1.1, 4)

        if len(faces) == 1:
            for index, (x, y, w, h) in enumerate(faces):
                faces = img[y - 50: y + h + 50, x - 50: x + w + 50]
                img = cv.resize(faces, (75, 75), interpolation=cv.INTER_AREA)
                cv.imwrite(self.output_file_path, img)
                self.prograss_bar.emit(index + 100)
                sleep(.5)
        else:
            self.error_code.clear()
            self.error_code.append(-1)


# The PrograssBar For Store The Information
class ThreadStorePrograssBar(QThread):

    prograss_bar = pyqtSignal(int)
    prograss_text = pyqtSignal(str)
    button = pyqtSignal(bool)

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
            self.button.emit(False)
            self.prograss_text.emit(self.pro_text)
            self.encrypt_function.emit(self.target_list, self.data_dict)
            self.store_function_inter.emit(
                self.data_dict, self.path, self.userType)

            self.prograss_bar.emit(100)
            sleep(.5)

            self.prograss_text.emit("Complete...")
            self.setRollIDLabelText.emit(self.rollIdText)
            sleep(1)
            self.prograss_bar.emit(0)
            self.theMainUserImage.emit(self.setting_image)
            self.button.emit(True)

        elif self.level != None and self.streem == None:
            self.button.emit(False)
            self.prograss_text.emit(self.pro_text)
            self.encrypt_function.emit(self.target_list, self.data_dict)
            self.store_function_ord.emit(
                self.data_dict, self.path, self.userType, self.level)

            self.prograss_bar.emit(100)
            sleep(.5)

            self.prograss_text.emit("Complete...")
            self.setRollIDLabelText.emit(self.rollIdText)
            sleep(1)
            self.prograss_bar.emit(0)
            self.theMainUserImage.emit(self.setting_image)
            self.button.emit(True)

        else:
            self.button.emit(False)
            self.prograss_text.emit(self.pro_text)
            self.encrypt_function.emit(self.target_list, self.data_dict)
            self.store_function_advan.emit(
                self.data_dict, self.path, self.userType, self.level, self.streem)

            self.prograss_bar.emit(100)
            sleep(.5)

            self.prograss_text.emit("Complete...")
            self.setRollIDLabelText.emit(self.rollIdText)
            sleep(1)
            self.prograss_bar.emit(0)
            self.theMainUserImage.emit(self.setting_image)
            self.button.emit(True)


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

        self.randomizer.emit()
        self.prograss_bar.emit(100)
        sleep(.3)

        self.prograss_bar.emit(0)
        self.prograss_label.emit("Complete...")
        sleep(1)
        self.prograss_label.emit("")


# Delete Randomise Data From Active
class DeleteRandomiseFromActiove(QThread):

    prograss_bar = pyqtSignal(int)
    prograss_label = pyqtSignal(str)
    delete_button = pyqtSignal(bool)

    def __init__(self, store_data,  userType, activeFile, leftFile, random_list, writeStoreLeft, status_label_text, decrypt_fun, save_path, encrypt_fun):
        super().__init__()
        self.store_data = store_data
        self.activeFile = activeFile
        self.leftFile = leftFile
        self.random_list = random_list
        self.userType = userType
        self.status_label_text = status_label_text
        self.writeStoreLeft = writeStoreLeft
        self.decrypt_fun = decrypt_fun
        self.save_path = save_path
        self.encrypt_fun = encrypt_fun

    def run(self):
        if self.userType == 'INTERUSER' or self.userType == 'NONEINTERUSER':
            self.delete_button.emit(False)
            self.prograss_label.emit(self.status_label_text)

            activeData = self.store_data(self.activeFile)
            leftData = self.store_data(self.leftFile)

            imagePath = self.copyAndDeleteImage(
                activeData[self.userType][self.random_list[-1]])
            imagePath = self.encrypt_fun(imagePath)

            if imagePath != '':
                activeData[self.userType][self.random_list[-1]
                                          ]["Image"] = imagePath
            else:
                activeData[self.userType][self.random_list[-1]]["Image"] = None

            leftData[self.userType].append(
                activeData[self.userType][self.random_list[-1]])
            self.writeStoreLeft(leftData, self.leftFile)

            del(activeData[self.userType][self.random_list[-1]])
            self.writeStoreLeft(activeData, self.activeFile)
            self.prograss_bar.emit(100)
            sleep(1)

            self.prograss_bar.emit(0)
            self.prograss_label.emit("Complete...")
            sleep(1)
            self.prograss_label.emit("")
            self.delete_button.emit(True)

        elif self.userType == 'Lower-User-Primary' or self.userType == 'Lower-User-Ordinary':
            self.delete_button.emit(False)
            self.prograss_label.emit(self.status_label_text)
            activeData = self.store_data(self.activeFile)
            leftData = self.store_data(self.leftFile)

            imagePath = self.copyAndDeleteImage(
                activeData[self.userType][self.random_list[-1][0]][self.random_list[-1][-1]])
            imagePath = self.encrypt_fun(imagePath)
            if imagePath != '':
                activeData[self.userType][self.random_list[-1][0]
                                          ][self.random_list[-1][-1]]["Image"] = imagePath
            else:
                activeData[self.userType][self.random_list[-1][0]
                                          ][self.random_list[-1][-1]]["Image"] = None

            leftData[self.userType].append(
                activeData[self.userType][self.random_list[-1][0]][self.random_list[-1][-1]])
            self.writeStoreLeft(leftData, self.leftFile)

            del(activeData[self.userType]
                [self.random_list[-1][0]][self.random_list[-1][-1]])
            self.writeStoreLeft(activeData, self.activeFile)

            self.prograss_bar.emit(100)
            sleep(1)

            self.prograss_bar.emit(0)
            self.prograss_label.emit("Complete...")
            sleep(1)
            self.prograss_label.emit("")
            self.delete_button.emit(True)

        else:
            self.delete_button.emit(False)
            self.prograss_label.emit(self.status_label_text)
            activeData = self.store_data(self.activeFile)
            leftData = self.store_data(self.leftFile)

            imagePath = self.copyAndDeleteImage(
                activeData[self.userType][self.random_list[-1][0][0]][self.random_list[-1][0][-1]][self.random_list[-1][-1]])
            imagePath = self.encrypt_fun(imagePath)
            if imagePath != '':
                activeData[self.userType][self.random_list[-1][0][0]][self.random_list[-1]
                                                                      [0][-1]][self.random_list[-1][-1]]["Image"] = imagePath
            else:
                activeData[self.userType][self.random_list[-1][0][0]
                                          ][self.random_list[-1][0][-1]][self.random_list[-1][-1]]["Image"] = None

            leftData[self.userType].append(
                activeData[self.userType][self.random_list[-1][0][0]][self.random_list[-1][0][-1]][self.random_list[-1][-1]])
            self.writeStoreLeft(leftData, self.leftFile)

            del(activeData[self.userType][self.random_list[-1][0][0]]
                [self.random_list[-1][0][-1]][self.random_list[-1][-1]])
            self.writeStoreLeft(activeData, self.activeFile)

            self.prograss_bar.emit(100)
            sleep(1)

            self.prograss_bar.emit(0)
            self.prograss_label.emit("Complete...")
            sleep(1)
            self.prograss_label.emit("")
            self.delete_button.emit(True)

    def copyAndDeleteImage(self, userData):
        userImageFromActive = str()

        for keyValue in userData:
            if keyValue == "Image" and userData[keyValue] != None:
                userImageFromActive = self.decrypt_fun(userData[keyValue])

        if userImageFromActive != '':
            path = shutil.copy(userImageFromActive, self.save_path)
            os.remove(userImageFromActive)

            userImageFromActive = path

        print(userImageFromActive)
        return userImageFromActive


# Delete Randomise Data From Left
class DeleteRandomiseFromLeft(QThread):

    prograss_bar = pyqtSignal(int)
    prograss_status_text = pyqtSignal(str)
    delete_button = pyqtSignal(bool)

    def __init__(self, random_target_list,  read_data, userType, status_label_text, write_data_fun, leftPath):
        super().__init__()

        self.random_target_list = random_target_list
        self.userType = userType
        self.status_label_text = status_label_text
        self.write_data_fun = write_data_fun
        self.read_data = read_data
        self.leftPath = leftPath

    def run(self):

        self.prograss_status_text.emit(self.status_label_text)
        self.delete_button.emit(False)

        leftData = self.read_data(self.leftPath)
        print(type(self.random_target_list))
        del(leftData[self.userType][self.random_target_list[-1]])
        self.write_data_fun(leftData, self.leftPath)

        self.prograss_bar.emit(100)
        sleep(1)

        self.prograss_status_text.emit("Complete...")
        sleep(1)
        self.prograss_bar.emit(0)
        self.prograss_status_text.emit("")
        self.delete_button.emit(True)


# Search User Information
class SearchUserInformation(QThread):

    prograss_bar = pyqtSignal(int)
    prograss_status = pyqtSignal(str)
    button = pyqtSignal(bool)

    def __init__(self, theLabelOfUserInput, decrypt_fun, userType_list):
        super().__init__()
        self.theLabelOfUserInput = theLabelOfUserInput
        self.decrypt_fun = decrypt_fun
        self.userType_list = userType_list

    def loading_animation(self, text, prieat):
        self.prograss_status.emit(text + prieat)
        sleep(.5)

    def run(self):
        userInput = self.theLabelOfUserInput.text()

        self.button.emit(False)
        self.prograss_status.emit("Searching.....")

        for userType in self.userType_list:

            if userType == "INTERUSER":
                prieat = "."
                for _ in range(0, 100):
                    if len(prieat) == 6:
                        prieat = ""
                    self.loading_animation("Searching Teahers", prieat)
                    prieat += "."

            if userType == "NONEINTERUSER":
                self.prograss_status.emit("Searching None-Teahers...")
                sleep(.5)

            if userType == 'Lower-User-Primary':
                self.prograss_status.emit("Searching Primary...")
                sleep(.5)

            if userType == 'Lower-User-Ordinary':
                self.prograss_status.emit("Searching Ordinary...")
                sleep(.5)

            if userType == 'Lower-User-Advanced':
                self.prograss_status.emit("Searching Advanced...")
                sleep(.5)

        self.prograss_status.emit("")
        self.button.emit(True)
        sleep(.5)

    def nameSearchAlgorithm(self, matching_name, target):
        rows = len(matching_name) + 1
        cols = len(target) + 1
        distance = np.zeros((rows, cols), dtype=int)

        for i in range(1, rows):
            for k in range(1, cols):
                distance[i][0] = i
                distance[0][k] = k

        for col in range(1, cols):
            for row in range(1, rows):
                if matching_name[row-1] == target[col-1]:
                    cost = 0
                else:
                    cost = 2

                distance[row][col] = min(distance[row-1][col]+1,
                                         distance[row][col-1] + 1,
                                         distance[row-1][col-1] + cost)
        Ratio = ((len(matching_name)+len(target)) -
                 distance[row][col]) / (len(matching_name)+len(target)) * 100
        return Ratio
