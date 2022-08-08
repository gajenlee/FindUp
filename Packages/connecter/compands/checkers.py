from distutils.log import error
import re
import cv2 as cv
from numpy import True_
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
                        Roll ID : {number.replace(" ", "")}
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

# Randomize Index
TEACHER_RANDOM_INDEX = []
NONE_TEACHER_RANDOM_INDEX = []
PRAYMARY_RANDOM_INDEX = []
ORDNARY_RANDOM_INDEX = []
ADVANCED_RANDOM_INDEX = []

TEACHER_RANDOM_INDEX_LEFT = []
NONE_TEACHER_RANDOM_INDEX_LEFT = []
PRAYMARY_RANDOM_INDEX_LEFT = []
ORDNARY_RANDOM_INDEX_LEFT = []
ADVANCED_RANDOM_INDEX_LEFT = []

# Target User Dict
TEACHER_TARGET = {}
NONE_TEACHER_TARGET = {}
PRIMARY_TARGET = {}
ORNARY_TARGET = {}
ADVANCED_TARGET = {}

TEACHER_TARGET_LEFT = {}
NONE_TEACHER_TARGET_LEFT = {}
PRIMARY_TARGET_LEFT = {}
ORNARY_TARGET_LEFT = {}
ADVANCED_TARGET_LEFT = {}


error_code_inter = []
error_code_noneinter = []
error_code_primary = []
error_code_ordnary = []
error_code_advanced = []

# Make Html Normal Object
def make_html_objNormal(dict_obj: dict, userType, label_list: list):
    label_list[0].setVisible(True)
    label_list[1].setVisible(True)
    label_list[2].setVisible(True)
    label_list[3].setVisible(True)
    label_list[4].setVisible(True)

    if userType == 'INTERUSER':

        rollid = dict_obj["ID"]
        fullName = dict_obj["Name-full"]
        contact_num = dict_obj["Contact-Number"]
        email = dict_obj["E-Mail"]
        address = dict_obj["Address"]

        label_list[0].setText(
            f"<p align=\'center\'>Roll ID        : {rollid}</p>")
        label_list[1].setText(
            f"<p align=\'center\'>Full Name      : {fullName}</p>")
        label_list[2].setText(
            f"<p align=\'center\'>Contact Number : {contact_num}</p>")
        label_list[3].setText(
            f"<p align=\'center\'>Email          : {email}</p>")
        label_list[4].setText(
            f"<p align=\'center\'>Address        : {address}</p>")

    elif userType == 'NONEINTERUSER':

        rollid = dict_obj["ID"]
        fullname = dict_obj["Name-full"]
        contact_num = dict_obj["Contact-Number"]
        email = dict_obj["E-Mail"]
        address = dict_obj["Address"]

        label_list[0].setText(
            f"<p align=\'center\'>Roll ID        : {rollid}</p>")
        label_list[1].setText(
            f"<p align=\'center\'>Full Name      : {fullname}</p>")
        label_list[2].setText(
            f"<p align=\'center\'>Contact Number : {contact_num}</p>")
        label_list[3].setText(
            f"<p align=\'center\'>Email          : {email}</p>")
        label_list[4].setText(
            f"<p align=\'center\'>Address        : {address}</p>")

    elif userType == 'Lower-User-Primary':

        rollid = dict_obj["ID"]
        fullname = dict_obj["Name-full"]
        contact_num = dict_obj["Parent-Number"]
        level = dict_obj["Level"]
        address = dict_obj["Address"]

        label_list[0].setText(
            f"<p align=\'center\'>Roll ID        : {rollid}</p>")
        label_list[1].setText(
            f"<p align=\'center\'>Full Name      : {fullname}</p>")
        label_list[2].setText(
            f"<p align=\'center\'>Parent / Guardian Contact Number : {contact_num}</p>")
        label_list[3].setText(
            f"<p align=\'center\'>Level          : {level}</p>")
        label_list[4].setText(
            f"<p align=\'center\'>Address        : {address}</p>")

    elif userType == 'Lower-User-Ordinary':

        rollid = dict_obj["ID"]
        fullname = dict_obj["Name-full"]
        contact_num = dict_obj["Parent-Number"]
        level = dict_obj["Level"]
        address = dict_obj["Address"]

        label_list[0].setText(
            f"<p align=\'center\'>Roll ID        : {rollid}</p>")
        label_list[1].setText(
            f"<p align=\'center\'>Full Name      : {fullname}</p>")
        label_list[2].setText(
            f"<p align=\'center\'>Parent / Guardian Contact Number : {contact_num}</p>")
        label_list[3].setText(
            f"<p align=\'center\'>Level          : {level}</p>")
        label_list[4].setText(
            f"<p align=\'center\'>Address        : {address}</p>")

    else:

        rollid = dict_obj["ID"]
        fullname = dict_obj["Name-full"]
        contact_num = dict_obj["Parent-Number"]
        level = dict_obj["Level"]
        streem = dict_obj["Streem"]
        address = dict_obj["Address"]

        label_list[0].setText(
            f"<p align=\'center\'>Roll ID        : {rollid}</p>")
        label_list[1].setText(
            f"<p align=\'center\'>Full Name      : {fullname}</p>")
        label_list[2].setText(
            f"<p align=\'center\'>Parent / Guardian Contact Number : {contact_num}</p>")
        label_list[3].setText(
            f"<p align=\'center\'>Level & Streem       : {level}, {streem}</p>")
        label_list[4].setText(
            f"<p align=\'center\'>Address        : {address}</p>")


# Make Html Object
def make_html_obj(dict_obj: dict, userType):

    if userType == 'INTERUSER':
        return f"""

        <html>
            </head>

            <body style=\'margin: 20px;\'>
                <p style=\'
                    display: inline-block;
                    padding-left: 20px;
                    padding-right: 20px;
                    margin: 20px;
                    font-size: 20px;
                    font-weight: 500;
                \'> Roll ID :{dict_obj["ID"]}</p> 
                <p> Name In Full :{dict_obj["Name-full"]}</p>
                <p> Name With Initial :{dict_obj["Name-Initial"]}</p>
                <p> NIC :{dict_obj["NIC"]}</p>
                <p> Contact Number :{dict_obj["Contact-Number"]}</p>
                <p> E-Mail :{dict_obj["E-Mail"]}</p>
                <p> W&OP Number :{dict_obj["WOP-Number"]}</p>
                <p> Agrakara Number :{dict_obj["Agrakara-Number"]}</p>
                <p> Spouse Name :{dict_obj["Spouse-Name"]}</p>
                <p> Teaching Registration Number :{dict_obj["Teaching-Reg-Number"]}</p>
                <p> Appointed Subject :{dict_obj["Appointed-Subject"]}</p>
                <p> Educational Qulification :{dict_obj["Educational-Qulification"]}</p>
                <p> Professional Qulification :{dict_obj["Professional-Qulification"]}</p>
                <p> Nature Of Appointment :{dict_obj["Nature-Appointment"]}</p>
                <p> Increment Date :{dict_obj["Increment-Date"]}</p>
                <p> Date Of Birth :{dict_obj["Date-Birth"]}</p>
                <p> First Appointment Date :{dict_obj["First-Appointment-Date"]}</p>
                <p> Address :{dict_obj["Address"]}</p>
                <p> Emergency Address and Contact :{dict_obj["Emergency"]}</p>
                <p> Present Grade :{dict_obj["Present-Grade"]}</p>
                <p> Date Present Grade :{dict_obj["Date-Present-Grade"]}</p>
                <p> Date Of Appointment To This School :{dict_obj["Date-Appointment-To-School"]}</p>
                <p> Civil Status :{dict_obj["Civil-Status"]}</p>
                <p> Gender :{dict_obj["Gender"]}</p>
            <body>
        """

    elif userType == 'NONEINTERUSER':
        return f"""

        <html>
            </head>

            <body>
                <p> Roll ID :{dict_obj["ID"]}</p> 
                <p> Name In Full :{dict_obj["Name-full"]}</p>
                <p> Name With Initial :{dict_obj["Name-Initial"]}</p>
                <p> NIC :{dict_obj["NIC"]}</p>
                <p> Contact Number :{dict_obj["Contact-Number"]}</p>
                <p> E-Mail :{dict_obj["E-Mail"]}</p>
                <p> W&OP Number :{dict_obj["WOP-Number"]}</p>
                <p> Agrakara Number :{dict_obj["Agrakara-Number"]}</p>
                <p> Spouse Name :{dict_obj["Spouse-Name"]}</p>
                <p> Educational Qulification :{dict_obj["Educational-Qulification"]}</p>
                <p> Professional Qulification :{dict_obj["Professional-Qulification"]}</p>
                <p> Salary Number :{dict_obj["Salary-Number"]}</p>
                <p> Nature Of Appointment :{dict_obj["Nature-Appointment"]}</p>
                <p> Increment Date :{dict_obj["Increment-Date"]}</p>
                <p> Date Of Birth :{dict_obj["Date-Birth"]}</p>
                <p> First Appointment Date :{dict_obj["First-Appointment-Date"]}</p>
                <p> Address :{dict_obj["Address"]}</p>
                <p> Emergency Address and Contact :{dict_obj["Emergency"]}</p>
                <p> Date Of Appointment To This School :{dict_obj["Date-Appointment-To-School"]}</p>
                <p> Civil Status :{dict_obj["Civil-Status"]}</p>
                <p> Gender :{dict_obj["Gender"]}</p>
            <body>
        """

    elif userType == 'Lower-User-Primary':
        return f"""

        <html>
            </head>
            <body>
                <p> Roll ID :{dict_obj["ID"]}</p> 
                <p> Name In Full :{dict_obj["Name-full"]}</p>
                <p> Name With Initial :{dict_obj["Name-Initial"]}</p>
                <p> Home Address :{dict_obj["Address"]}</p>
                <p> Office Address :{dict_obj["Address-Office"]}</p>
                <p> Father Name :{dict_obj["Father-Name"]}</p>
                <p> Mather Name :{dict_obj["Mather-Name"]}</p>
                <p> Number Of Siblings :{dict_obj["Number-Siblings"]}</p>
                <p> Level :{dict_obj["Level"]}</p>
                <p> Religion :{dict_obj["Religion"]}</p>
                <p> Admission Number :{dict_obj["Admission-Number"]}</p>
                <p> Father's Nature Of Job :{dict_obj["Father-Job"]}</p>
                <p> Mather's Nature Of Job :{dict_obj["Mather-Job"]}</p>
                <p> Parent / Guardian Contact Number :{dict_obj["Parent-Number"]}</p>
                <p> Date Of Birth :{dict_obj["Date-Birth"]}</p>
                <p> Date Of Admission :{dict_obj["Date-Admission"]}</p>
                <p> Gender :{dict_obj["Gender"]}</p>
            <body>
        """

    elif userType == 'Lower-User-Ordinary':
        return f"""

        <html>
            </head>
            <body>
                <p> Roll ID :{dict_obj["ID"]}</p> 
                <p> Name In Full :{dict_obj["Name-full"]}</p>
                <p> Name With Initial :{dict_obj["Name-Initial"]}</p>
                <p> Home Address :{dict_obj["Address"]}</p>
                <p> Office Address :{dict_obj["Address-Office"]}</p>
                <p> Father Name :{dict_obj["Father-Name"]}</p>
                <p> Mather Name :{dict_obj["Mather-Name"]}</p>
                <p> Number Of Siblings :{dict_obj["Number-Siblings"]}</p>
                <p> Level :{dict_obj["Level"]}</p>
                <p> Religion :{dict_obj["Religion"]}</p>
                <p> Admission Number :{dict_obj["Admission-Number"]}</p>
                <p> Father's Nature Of Job :{dict_obj["Father-Job"]}</p>
                <p> Mather's Nature Of Job :{dict_obj["Mather-Job"]}</p>
                <p> Parent / Guardian Contact Number :{dict_obj["Parent-Number"]}</p>
                <p> Date Of Birth :{dict_obj["Date-Birth"]}</p>
                <p> Date Of Admission :{dict_obj["Date-Admission"]}</p>
                <p> Gender :{dict_obj["Gender"]}</p>
            <body>
        """

    else:
        return f"""

        <html>
            </head>
            <body>
                <p> Roll ID :{dict_obj["ID"]}</p> 
                <p> Name In Full :{dict_obj["Name-full"]}</p>
                <p> Name With Initial :{dict_obj["Name-Initial"]}</p>
                <p> Home Address :{dict_obj["Address"]}</p>
                <p> Office Address :{dict_obj["Address-Office"]}</p>
                <p> Father Name :{dict_obj["Father-Name"]}</p>
                <p> Mather Name :{dict_obj["Mather-Name"]}</p>
                <p> Number Of Siblings :{dict_obj["Number-Siblings"]}</p>
                <p> Level :{dict_obj["Level"]}</p>
                <p> Streem :{dict_obj["Streem"]}</p>
                <p> Religion :{dict_obj["Religion"]}</p>
                <p> Admission Number :{dict_obj["Admission-Number"]}</p>
                <p> Father's Nature Of Job :{dict_obj["Father-Job"]}</p>
                <p> Mather's Nature Of Job :{dict_obj["Mather-Job"]}</p>
                <p> Parent / Guardian Contact Number :{dict_obj["Parent-Number"]}</p>
                <p> Date Of Birth :{dict_obj["Date-Birth"]}</p>
                <p> Date Of Admission :{dict_obj["Date-Admission"]}</p>
                <p> Gender :{dict_obj["Gender"]}</p>
            <body>
        """


# Face Recognition
def face_recognition(file_path, output_file_path, prograssbar, prograssbar_text, setting_text,  image_label, list_users, button, error_code):

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
                                 file_path, output_file_path, FACE_RECOGNITION_XML_PATH, error_code)
        thread.prograss_bar.connect(prograssbar)
        thread.prograss_text.connect(prograssbar_text.setText)
        thread.theMainUserImage.connect(image_label.setText)
        thread.button.connect(button.setEnabled)
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

        for num in range(len(key_value)):
            index = key_value[num]

            if the_dict[index] == None:
                append_dict[index] = None
            else:
                decrypted = cal.decrypt_one(the_dict[index])
                append_dict[index] = decrypted

    @classmethod
    def decrypt_ID(cal, the_dict: dict, append: str):
        key_value = [key for key in the_dict]

        for index in range(len(key_value)):
            if key_value[index] == "ID":
                decrypted = cal.decrypt_one(the_dict[key_value[index]])
                append = decrypted
