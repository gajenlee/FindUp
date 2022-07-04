import json
import os
from logging_findup import *


# Paths For Saveing
PATH_CONFIG_DIR = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/config/user/")


# DATA LOCATION
PATH_STORE_DATA_DIR_ACTIVE = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/active/")
PATH_STORE_DATA_DIR_RECYCLE = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/recycle/")

# Store Face Images
PATH_STORE_FACE_IMAGE_INTER = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/active/inter/")
PATH_STORE_FACE_IMAGE_INTER_NONE = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/active/none_inter/")

PATH_STORE_FACE_IMAGE_PRIMARY = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/active/primary/")
PATH_STORE_FACE_IMAGE_ORDNARY = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/active/ordnary/")
PATH_STORE_FACE_IMAGE_ADVANCED = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/active/advanced/")

# Store Face Images Left
PATH_STORE_FACE_IMAGE_INTER_LEFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/left/inter/")
PATH_STORE_FACE_IMAGE_INTER_NONE_LEFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/left/none_inter/")

PATH_STORE_FACE_IMAGE_PRIMARY_LEFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/left/primary/")
PATH_STORE_FACE_IMAGE_ORDNARY_LEFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/left/ordnary/")
PATH_STORE_FACE_IMAGE_ADVANCED_LEFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/faces/left/advanced/")

IMAGE_FORMAT = ".png"


# Lower data Location
PATH_STORE_DATA_FILE_INTER = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/active/Idata.json")
PATH_STORE_DATA_FILE_INTER_NONE = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/active/INdata.json")
PATH_STORE_DATA_FILE_PRIMARY = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/active/Pdata.json")
PATH_STORE_DATA_FILE_ORDNARY = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/active/Odata.json")
PATH_STORE_DATA_FILE_ADVNACED = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/active/Adata.json")

# Lower data Location FOR RECYLE
PATH_STORE_DATA_FILE_INTER_LIFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/recycle/LIdata.json")
PATH_STORE_DATA_FILE_INTER_LIFT_NONE = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/active/LINdata.json")
PATH_STORE_DATA_FILE_PRIMARY_LIFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/recycle/LPdata.json")
PATH_STORE_DATA_FILE_ORDNARY_LIFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/recycle/LOdata.json")
PATH_STORE_DATA_FILE_ADVNACED_LIFT = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/store/recycle/LAdata.json")

# Super User Setting data loaction
PATH_STORE_DATA_SETTING = os.path.join(
    f"C:/Users/{os.getlogin()}/.findup/config/user/setting.json")


# Names For Files
SETTING_FILE = "setting.json"

INTER_FILE = 'Idata.json'
NONEINTER_FILE = 'INdata.json'
PRIMARY_FILE = 'Pdata.json'
ORDNARY_FILE = 'Odata.json'
ADVANCED_FILE = 'Adata.json'

INTER_FILE_LEFT = 'LIdata.json'
NONEINTER_FILE_LEFT = 'LINdata.json'
PRIMARY_FILE_LEFT = 'LPdata.json'
ORDNARY_FILE_LEFT = 'LOdata.json'
ADVANCED_FILE_LEFT = 'LAdata.json'

# User Key Word
SETTING = 'Setting'
INTERUSER = 'INTERUSER'
NONEINTERUSER = 'NONEINTERUSER'
PRIMARYLOWER = 'Lower-User-Primary'
ORDNARYLOWER = 'Lower-User-Ordinary'
ADVNACEDLOWER = 'Lower-User-Advanced'


# SETTING CLASS
class Setting:

    @staticmethod
    def init():
        logger.debug(
            "The Setting class json function is runing... [ init ]"
        )
        # Create Fplder For Setting
        try:
            os.makedirs(PATH_CONFIG_DIR)

        except FileExistsError:
            logger.exception("The Setting File Already Exists Error [ init ]")

        except Exception as p:
            print(p)
            logger.exception("Something went wrong [ init ]")

    @staticmethod
    def store_superuser(obj):
        if SETTING_FILE not in os.listdir(PATH_CONFIG_DIR):
            data = {"Setting": {}}
            Store.write_json(data, PATH_STORE_DATA_SETTING)

        data = Store.read_json(PATH_STORE_DATA_SETTING)
        data[SETTING] = obj
        Store.write_json(data, PATH_STORE_DATA_SETTING)

    @staticmethod
    def load_superuser():
        return Store.read_json(PATH_STORE_DATA_SETTING)


# STORE CLASS
class Store(object):

    @staticmethod
    def init():

        # Create Folder For Data
        try:
            # Folder Makeing functions
            os.makedirs(PATH_STORE_FACE_IMAGE_INTER)
            os.makedirs(PATH_STORE_FACE_IMAGE_INTER_NONE)
            os.makedirs(PATH_STORE_FACE_IMAGE_PRIMARY)
            os.makedirs(PATH_STORE_FACE_IMAGE_ORDNARY)
            os.makedirs(PATH_STORE_FACE_IMAGE_ADVANCED)

            os.makedirs(PATH_STORE_FACE_IMAGE_INTER_LEFT)
            os.makedirs(PATH_STORE_FACE_IMAGE_INTER_NONE_LEFT)
            os.makedirs(PATH_STORE_FACE_IMAGE_PRIMARY_LEFT)
            os.makedirs(PATH_STORE_FACE_IMAGE_ORDNARY_LEFT)
            os.makedirs(PATH_STORE_FACE_IMAGE_ADVANCED_LEFT)

            os.makedirs(PATH_STORE_DATA_DIR_ACTIVE)
            os.makedirs(PATH_STORE_DATA_DIR_RECYCLE)

        except FileExistsError:
            logger.exception("The File Already Exists... [init]")

        logger.debug("The store class is runing... [init]")

        # Active user Data
        if INTER_FILE not in os.listdir(PATH_STORE_DATA_DIR_ACTIVE):
            data = {'INTERUSER': []}
            Store.write_json(data, PATH_STORE_DATA_FILE_INTER)

        if NONEINTER_FILE not in os.listdir(PATH_STORE_DATA_DIR_ACTIVE):
            data = {'NONEINTERUSER': []}
            Store.write_json(data, PATH_STORE_DATA_FILE_INTER_NONE)

        if PRIMARY_FILE not in os.listdir(PATH_STORE_DATA_DIR_ACTIVE):
            data = {
                "Lower-User-Primary":
                {
                    "Level - 01": [],
                    "Level - 02": [],
                    "Level - 03": [],
                    "Level - 04": [],
                    "Level - 05": [],

                }
            }
            Store.write_json(data, PATH_STORE_DATA_FILE_PRIMARY)

        if ORDNARY_FILE not in os.listdir(PATH_STORE_DATA_DIR_ACTIVE):
            data = {
                "Lower-User-Ordinary":
                {
                    "Level - 06": [],
                    "Level - 07": [],
                    "Level - 08": [],
                    "Level - 09": [],
                    "Level - 10": [],
                    "Level - 11": []
                }
            }
            Store.write_json(data, PATH_STORE_DATA_FILE_ORDNARY)

        if ADVANCED_FILE not in os.listdir(PATH_STORE_DATA_DIR_ACTIVE):
            data = {
                "Lower-User-Advanced": {
                    "Level - 12": {
                        "Mathematics": [],
                        "Science": [],
                        "Engineering-Technology": [],
                        "Bio-Technology": [],
                        "Commerce": [],
                        "Art": []
                    },
                    "Level - 13": {
                        "Mathematics": [],
                        "Science": [],
                        "Engineering-Technology": [],
                        "Bio-Technology": [],
                        "Commerce": [],
                        "Art": []
                    }
                }
            }
            Store.write_json(data, PATH_STORE_DATA_FILE_ADVNACED)

        # Recycle user Data
        if INTER_FILE_LEFT not in os.listdir(PATH_STORE_DATA_DIR_RECYCLE):
            data = {'INTERUSER': []}
            Store.write_json(
                data, PATH_STORE_DATA_FILE_INTER_LIFT)

        if NONEINTER_FILE_LEFT not in os.listdir(PATH_STORE_DATA_DIR_RECYCLE):
            data = {'NONEINTERUSER': []}
            Store.write_json(data, PATH_STORE_DATA_FILE_INTER_LIFT_NONE)

        if PRIMARY_FILE_LEFT not in os.listdir(PATH_STORE_DATA_DIR_RECYCLE):
            data = {"Lower-User-Primary": []}
            Store.write_json(
                data, PATH_STORE_DATA_FILE_PRIMARY_LIFT)

        if ORDNARY_FILE_LEFT not in os.listdir(PATH_STORE_DATA_DIR_RECYCLE):
            data = {"Lower-User-Ordinary": []}
            Store.write_json(
                data, PATH_STORE_DATA_FILE_ORDNARY_LIFT)

        if ADVANCED_FILE_LEFT not in os.listdir(PATH_STORE_DATA_DIR_RECYCLE):
            data = {"Lower-User-Advanced": []}
            Store.write_json(data, PATH_STORE_DATA_FILE_ADVNACED_LIFT)

    @staticmethod
    def write_json(data, filePath):
        logger.debug(
            "The store class write json function is runing... [write_json]")
        with open(filePath, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def read_json(filePath):
        logger.debug(
            "The store class read json function is runing... [read_json]")
        with open(filePath, 'r') as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def append_json(data, filePath, userType, levelKey=None, streemKey=None):

        if levelKey != None and streemKey != None:

            logger.debug(
                "The store class append json level streem function is runing... [append_json]")
            loaded_data = Store.read_json(filePath)
            loaded_data[userType][levelKey][streemKey].append(data)
            Store.write_json(loaded_data, filePath)

        elif levelKey != None and streemKey == None:

            logger.debug(
                "The store class append json level function is runing... [append_json]")
            loaded_data = Store.read_json(filePath)
            print(levelKey, filePath)
            loaded_data[userType][levelKey].append(data)
            Store.write_json(loaded_data, filePath)

        else:

            logger.debug(
                "The store class append json function is runing.. [append_json]")
            loaded_data = Store.read_json(filePath)
            loaded_data[userType].append(data)
            Store.write_json(loaded_data, filePath)
