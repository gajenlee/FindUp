import re
import cv2 as cv
from rsa import decrypt
from Packages.connecter.cryptography.crypto import *
from Packages.connecter.thread_findup.threadForFindup import *

# Check the Password digit, Global function


def checkThePassword(pwd):
    if pwd:
        if len(pwd) > 5 and \
                re.search("[a-z]", pwd) and \
            re.search("[A-Z]", pwd) and \
                re.search("[0-9]", pwd) and\
                not re.search("\s", pwd):
            return True
    return False


# Check the E-mail, Global function
def checkTheEmail(mail):
    if mail != '':
        upper = [char for char in mail if char.isupper()]
        if re.findall('\S+@\S+', mail) and upper == []:
            return True
        else:
            return False
    else:
        return None


# Check the Contact Number, Global function
def checkTheContactNum(co_num):
    if co_num != '':
        if co_num[0:2] == "07" or co_num[0:2] == "94" or co_num[0:2] == "+9":
            if 10 <= len(co_num) <= 13:
                return True
    return False


# Check the User Name, Global function
def checkTheUserName(name):
    upper = [char for char in name if char.isupper()]
    if name != '':
        if upper == [] and len(name) >= 5:
            return True
    return False


# Super User Object layout
def superUserLayoutStore(name: list, password: list, contact: list, email=None):

    if email != None:
        obj = {
            "Name": name,
            "Password": password,
            "Contact": contact,
            "E-mail": email,
            "Default-theme": "light",
            "Create": True
        }

    else:
        obj = {
            "Name": name,
            "Password": password,
            "Contact": contact,
            "E-mail": None,
            "Default-theme": "light",
            "Create": True
        }

    return obj


# Path of user image
path_userImage = str()


# Inter User Object layout
the_layout_of_teachers = {
    "ID": list(),
    "Name-full": list(),
    "Name-Initial": list(),
    "NIC": list(),
    "Contact-Number": list(),
    "E-Mail": list(),
    "WOP-Number": list(),
    "Agrakara-Number": list(),
    "Spouse-Name": list(),
    "Teaching-Reg-Number": list(),
    "Appointed-Subject": list(),
    "Educational-Qulification": list(),
    "Professional-Qulification": list(),
    "Nature-Appointment": list(),
    "Increment-Date": list(),
    "Date-Birth": list(),
    "First-Appointment-Date": list(),
    "Address": list(),
    "Emergency": list(),
    "Present-Grade": list(),
    "Date-Present-Grade": list(),
    "Date-Appointment-To-School": list(),
    "Civil-Status": list(),
    "Gender": list(),
    "Image": list()
}

# None-Inter user Object Layout
the_layout_of_none_teacher = {
    "ID": list(),
    "Name-full": list(),
    "Name-Initial": list(),
    "NIC": list(),
    "Contact-Number": list(),
    "E-Mail": list(),
    "WOP-Number": list(),
    "Agrakara-Number": list(),
    "Spouse-Name": list(),
    "Educational-Qulification": list(),
    "Salary-Number": list(),
    "Professional-Qulification": list(),
    "Nature-Appointment": list(),
    "Increment-Date": list(),
    "Date-Birth": list(),
    "First-Appointment-Date": list(),
    "Address": list(),
    "Emergency": list(),
    "Date-Appointment-To-School": list(),
    "Civil-Status": list(),
    "Gender": list(),
    "Image": list()
}

# Primary user Object layout
the_layout_of_primary = {
    "ID": list(),
    "Name-full": list(),
    "Name-Initial": list(),
    "Address": list(),
    "Address-Office": list(),
    "Father-Name": list(),
    "Mather-Name": list(),
    "Number-Siblings": list(),
    "Level": list(),
    "Religion": list(),
    "Admission-Number": list(),
    "Father-Job": list(),
    "Mather-Job": list(),
    "Parent-Number": list(),
    "Date-Birth": list(),
    "Date-Admission": list(),
    "Gender": list(),
    "Image": list()
}

# Ordnary user Object layout
the_layout_of_ordnary = {
    "ID": list(),
    "Name-full": list(),
    "Name-Initial": list(),
    "Address": list(),
    "Address-Office": list(),
    "Father-Name": list(),
    "Mather-Name": list(),
    "Number-Siblings": list(),
    "Level": list(),
    "Religion": list(),
    "Admission-Number": list(),
    "Father-Job": list(),
    "Mather-Job": list(),
    "Parent-Number": list(),
    "Date-Birth": list(),
    "Date-Admission": list(),
    "Gender": list(),
    "Image": list()
}

# Advanced user Object layout
the_layout_of_advanced = {
    "ID": list(),
    "Name-full": list(),
    "Name-Initial": list(),
    "Address": list(),
    "Address-Office": list(),
    "Father-Name": list(),
    "Mather-Name": list(),
    "Number-Siblings": list(),
    "Level": list(),
    "Streem": list(),
    "Religion": list(),
    "Admission-Number": list(),
    "Father-Job": list(),
    "Mather-Job": list(),
    "Parent-Number": list(),
    "Date-Birth": list(),
    "Date-Admission": list(),
    "Gender": list(),
    "Image": list()
}

# Face Recognition XML File Path
FACE_RECOGNITION_XML_PATH = "./src/xml/haarcascade_frontalface_alt2.xml"


# Roll Id Shower
def rollIDShower(number):
    return f"""
        <html>
            <head/>
            <body>
                <p>
                    <span style=\" font-size:12pt; font-weight:600;\">
                        Roll ID : {number}
                    </span>
                </p>
            </body>
        </html>
    """


# FaceImage Path List
TEACHER_FACE_PATH_LIST = []

NONE_TEACHER_FACE_PATH_LIST = []

PRAYMARY_FACE_PATH_LIST = []

ORDNARY_FACE_PATH_LIST = []


ADVANCED_FACE_PATH_LIST = []


# Face Recognition
def face_recognition(file_path, output_file_path, prograssbar, prograssbar_text, setting_text,  image_label, list_users):

    def final_func():
        list_users.append(output_file_path)
        prograssbar_text.setText("")

    list_users.clear()

    img = cv.imread(file_path)
    imageGry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier(FACE_RECOGNITION_XML_PATH)
    faces = face_cascade.detectMultiScale(imageGry, 1.1, 4)

    if faces != [] and faces != ():
        thread = Thread_Prograss("Image Processing...", setting_text,
                                 file_path, output_file_path, FACE_RECOGNITION_XML_PATH)
        thread.prograss_bar.connect(prograssbar)
        thread.prograss_text.connect(prograssbar_text.setText)
        thread.theMainUserImage.connect(image_label.setText)
        thread.finished.connect(final_func)
        thread.start()
        thread.exec_()

        return True

    else:
        return False

# User Change Image


def change_image(imgPath, userTypeFormalText):
    text = f"""
        <html>
            <head/>
            <body>
                <p align=\"center\">
                    <img src=\"{imgPath}\"/>
                </p>
                <p align=\"center\">
                    <span style=\" font-size:10pt; font-weight:600;\">
                        {userTypeFormalText}
                    </span>
                </p>
            </body>
        </html>
    """
    return text


# Clear The Dict Value
def clear_dict_value(the_dict_value: dict):
    for value in the_dict_value:
        the_dict_value[value] = None


# Encrypt and Decrypt Data
class Crypto:

    # Encrypt and Decrypt Object
    __secure = Secure()

    @classmethod
    def encrypt_superuser(cal, name: str, pwd: str, contact: str, email=None):

        __name, __namekey = cal.__secure.encrypt(name)
        __pwd, __pwdkey = cal.__secure.encrypt(pwd)
        __contact, __contactkey = cal.__secure.encrypt(contact)

        if email != None:
            __email, __emailkey = cal.__secure.encrypt(email)
            obj = superUserLayoutStore(
                [__name, __namekey],
                [__pwd, __pwdkey],
                [__contact, __contactkey],
                [__email, __emailkey]
            )

        else:

            obj = superUserLayoutStore(
                [__name, __namekey],
                [__pwd, __pwdkey],
                [__contact, __contactkey]
            )

        return obj

    @classmethod
    def decrypt_superuser(cal, name: list, pwd: list, cont: list, email=None):

        __name = cal.__secure.decrypt(name[0], name[-1])
        __pwd = cal.__secure.decrypt(pwd[0], pwd[-1])
        __cont = cal.__secure.decrypt(cont[0], cont[-1])

        if email != None:
            __email = cal.__secure.decrypt(email[0], email[-1])
            return [__name, __pwd, __email, __cont]

        return [__name, __pwd, None, __cont]

    @classmethod
    def decrypt_superuser_user(cal, name: list, pwd: list):
        __pwd = cal.__secure.decrypt(pwd[0], pwd[-1])
        __name = cal.__secure.decrypt(name[0], name[-1])

        return [__name, __pwd]

    @classmethod
    def decrypt_one(cal, any_obj: list):
        __data = cal.__secure.decrypt(any_obj[0], any_obj[-1])
        return __data

    @classmethod
    def encrypt_one(cal, any_obj: str):
        __data = cal.__secure.encrypt(any_obj)
        return __data

    @classmethod
    def encrypt_interuser(cal, data_obj: list, the_dict: dict):
        the_layout_key = [value for value in the_dict]

        for index in range(len(the_layout_key)):
            if data_obj[index] == None:
                the_dict[the_layout_key[index]] = None
            else:
                encrypted, key = cal.encrypt_one(data_obj[index])
                the_dict[the_layout_key[index]] = [
                    encrypted, key]

    @classmethod
    def decrypt_interuser(cal, the_dict: dict, append_dict: dict):
        key_value = [key for key in the_dict]

        for index in range(len(key_value)):
            if the_dict[key_value[index]] == None:
                append_dict[key_value[index]] = None
            else:
                decrypted = cal.decrypt_one(the_dict[key_value[index]])
                append_dict[key_value[index]] = decrypted

    @classmethod
    def decrypt_ID(cal, the_dict: dict, append: str):
        key_value = [key for key in the_dict]

        for index in range(len(key_value)):
            if key_value[index] == "ID":
                decrypted = cal.decrypt_one(the_dict[key_value[index]])
                append = decrypted
