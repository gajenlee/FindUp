import re
import os

from Packages.connecter.cryptography.crypto import *


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
