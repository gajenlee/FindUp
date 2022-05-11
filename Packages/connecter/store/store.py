import json
import os

# ENCRPTION
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


# Paths For Saveing
PATH_CONFIG_DIR = os.path.join(f"C:/Users/{os.getlogin()}/.findup/config/")
PATH_STORE_DATA_DIR = os.path.join(f"C:/Users/{os.getlogin()}/.findup/store/")

PATH_CONFIG_FILE = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/config/config.bin")
PATH_STORE_DATA_FILE = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/data.json")
PATH_STORE_DATA_BIN_FILE = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/recycleBin.json")
PATH_STORE_DATA_SETTING = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/setting.json")


class ReadBinary(object):

    __fileName = PATH_CONFIG_FILE

    @staticmethod
    def read_binary_file():
        with open(ReadBinary.__fileName, 'r+b') as file:
            data = file.read()
        return data.decode('utf-8')

    @staticmethod
    def write_binary_file(text):
        with open(ReadBinary.__fileName, 'w+b') as file:
            file.write(text.encode('utf-8'))


class Store(object):

    __fileName = PATH_STORE_DATA_FILE
    __fileNameForLeft = PATH_STORE_DATA_BIN_FILE
    __fileSetting = PATH_STORE_DATA_SETTING

    # MAKE JSON FILE AND INIT FUNCTION
    @staticmethod
    def init():

        if "setting.json" not in os.listdir(PATH_STORE_DATA_DIR):
            data = {
                "Super-User": []
            }
            Store.write_super_user(data)

        if "data.json" not in os.listdir(PATH_STORE_DATA_DIR):
            data = {
                "Inter-User": [],
                "Lower-User-Primary":
                {
                    "Level - 01": [],
                    "Level - 02": [],
                    "Level - 03": [],
                    "Level - 04": [],
                    "Level - 05": [],
                
                },
                "Lower-User-Ordinary":
                {
                    "Level - 01": [],
                    "Level - 02": [],
                    "Level - 03": [],
                    "Level - 04": [],
                    "Level - 05": [],
                    "Level - 06": [],
                    "Level - 07": [],
                    "Level - 08": [],
                    "Level - 09": [],
                    "Level - 10": [],
                    "Level - 11": []
                },
                "Lower-User-Advanced":{
                    "Level - 12": {
                        "Mathematics":[],
                        "Science":[],
                        "Engineering-Technology":[],
                        "Bio-Technology":[],
                        "Commerce":[],
                        "Art":[]
                    },
                    "Level - 13": {
                        "Mathematics":[],
                        "Science":[],
                        "Engineering-Technology":[],
                        "Bio-Technology":[],
                        "Commerce":[],
                        "Art":[]
                    }
                }

            }
            Store.write_json(data)

        if "recycleBin.json" not in os.listdir(PATH_STORE_DATA_DIR):
            data = {

                "Inter-User": [],
                "Lower-User-Primary": [],
                "Lower-User-Ordinary": [],
                "Lower-User-Advanced":[]

            }
            Store.write_json_for_left(data)
        else:
            print(" !! Ready for data set !! ")

    # READ JSON DATA
    @staticmethod
    def read_json():
        with open(Store.__fileName, 'r') as file:
            data = json.load(file)
        return data

    # UPDATE INTER USER DATAS
    @staticmethod
    def update_json(dataValue, userType):
        data = Store.read_json()
        temp = data[userType]
        temp.append(dataValue)
        Store.write_json(data)

    # WRITE JSON DATA
    @staticmethod
    def write_json(data):
        with open(Store.__fileName, 'w') as file:
            json.dump(data, file, indent=4)

    # UPDATE LOWER CLASS DATA
    @staticmethod
    def update_json_for_lower(dataValue, userType, levelClass):
        with open(Store.__fileName, 'r') as file:
            data = json.load(file)
            print(userType, levelClass)
            temp = data[userType][levelClass]
            temp.append(dataValue)
        Store.write_json(data)

    # Update Advance Lower Data
    @staticmethod
    def update_json_for_advance_lower(userType, data, level, stream):
        data = Store.read_json()
        data[userType][level][stream].append(data)
        Store.write_json(data)

    # LEFT STATUS USAGE
    @staticmethod
    def write_json_for_left(data):
        with open(Store.__fileNameForLeft, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def read_json_for_left():
        with open(Store.__fileNameForLeft, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def update_json_for_left(dataValue, userType):
        data = Store.read_json_for_left()
        temp = data[userType]
        temp.append(dataValue)
        Store.write_json_for_left(data)

    @staticmethod
    def write_super_user(data):
        with open(Store.__fileSetting, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def read_super_user():
        with open(Store.__fileSetting, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def update_super_user(dataValue):
        data = Store.read_super_user()
        temp = data["Super-User"]
        temp.append(dataValue)
        Store.write_super_user(data)


class Secure(object):

    # CREATE NEW KEY FOR 1000000 TIMES
    def __init__(self):
        salt = os.urandom(16)
        __password = b'12345_t_200'

        generatorKey = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1000000,
            backend=default_backend()
        )
        self.__key = base64.urlsafe_b64encode(generatorKey.derive(__password))

    # ENCRYPT DATA
    def encrypt(self, data):
        data = data.encode('utf-8')
        self.fran = Fernet(self.__key)
        encrypt = self.fran.encrypt(data)
        return encrypt.decode('utf-8'), self.__key.decode('utf-8')

    # DECRYPT DATA
    def decrypt(self, encrypted, key):
        encrypted = encrypted.encode('utf-8')
        __key = key.encode('utf-8')

        self.fran = Fernet(__key)
        decrypted = self.fran.decrypt(encrypted)
        return decrypted.decode('utf-8')
