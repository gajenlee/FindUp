import cv2 as cv
import sys
import pandas as pd
import matplotlib as mtp
import numpy as np
import json

from threading import Thread

from Packages.uis.access.ui_access import *
from Packages.uis.backup.ui_backup import *
from Packages.uis.create.ui_create import *
from Packages.uis.login.ui_login import *
from Packages.uis.main.ui_main import *

from Packages.connecter.cryptography.crypto import *
from Packages.connecter.progressBar.circular_progress import *
from Packages.connecter.store.store import *
from Packages.connecter.thread_findup.threadForFindup import *

from src.style import dark
from src.style import light


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from nav_runer import *


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

    # window started theme [If it's True, change the theme light]
    theme_button_pressed = False

    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Run Default Theme runer
        self.default_theme()

        # Button activity connecter
        self.btnToFunctionConnecter()

    def btnToFunctionConnecter(self):

        # THEME BUTTON FOE CHAMGE THEME
        self.ui.btn_setTheme.clicked.connect(self.setTheme)

    # light theme of window
    def connect_functiom_light(self):

        # Toggle Burguer Menu
        self.ui.btn_Toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu_light(self, 200, True))

        # Setting Bar Animation
        self.ui.btn_hidden_username_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_light(self,  self.ui.frame_user_name_changer.height(
        ), self.ui.frame_user_name_changer, self.ui.frame_name_changer_content_page, True, self.ui.btn_hidden_username_bar, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))
        self.ui.btn_hidden_email_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_light(self,  self.ui.frame_email_changer.height(
        ), self.ui.frame_email_changer, self.ui.frame_email_changer_content_bar, True, self.ui.btn_hidden_email_bar, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))
        self.ui.btn_hidden_contact_number_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_light(self,  self.ui.frame_contect_number_changer.height(
        ), self.ui.frame_contect_number_changer, self.ui.frame_contect_number_changer_content_bar, True, self.ui.btn_hidden_contact_number_bar, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))
        self.ui.btn_hidden_passowd_changer_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_light(self,  self.ui.frame_password_changer.height(
        ), self.ui.frame_password_changer, self.ui.frame_password_changer_content_bar, True, self.ui.btn_hidden_passowd_changer_bar, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))

        self.ui.btn_hidden_options.clicked.connect(lambda: UIFunctions.settingHiddenBar_two_light(self,  self.ui.frame_more_options.height(
        ), self.ui.frame_more_options, self.ui.frame_more_options_contect_bar, True, self.ui.btn_hidden_options, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))
        self.ui.btn_hidden_adout.clicked.connect(lambda: UIFunctions.settingHiddenBar_two_light(self, self.ui.frame_adout.height(
        ), self.ui.frame_adout, self.ui.frame_content_adout, True, self.ui.btn_hidden_adout, light.BTN_HIDDEN_ICON, light.BTN_OPENED_ICON))

        # SUPER USER BTN
        self.ui.btn_superuser.clicked.connect(
            lambda: UIFunctions.userSideBar_toggle_light(self, 300, True))

        # BUTTONE CONNECTER
        UIFunctions.current_page_light(self)

        self.ui.btn_page_home.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_page_left.clicked.connect(
            lambda: UIFunctions.left_light(self))
        self.ui.btn_page_search.clicked.connect(
            lambda: UIFunctions.search_light(self))
        self.ui.btn_setting.clicked.connect(
            lambda: UIFunctions.setting_light(self))
        self.ui.btn_page_analytics.clicked.connect(
            lambda: UIFunctions.analytics_light(self))
        self.ui.btn_go_home.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home_light(self))

        # Super User Btn
        self.ui.btn_edit_setting.clicked.connect(
            lambda: UIFunctions.setting_light(self))

        # Inter and Lower Btn
        self.ui.btn_inter.clicked.connect(
            lambda: UIFunctions.callInter_window_light(self)
        )
        self.ui.btn_lower.clicked.connect(
            lambda: UIFunctions.callLower_window_light(self)
        )

        # Connect into btn_ordinary
        self.ui.btn_ordinary.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_lower))
        # Connect into btn_advanced
        self.ui.btn_advanced.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_advan))
        # Connect into btn_primary
        self.ui.btn_primary.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page))

        # Go Home Button
        self.ui.btn_go_home.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_home_primary.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home_light(self))
        self.ui.btn_go_home_ad.clicked.connect(
            lambda: UIFunctions.home_light(self))

    def setTheme_for_window_light(self):

        self.ui.scrollArea_2.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_resalt.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_3.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_content.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_4.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_add_info.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_advanced_add.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_primary_add.setStyleSheet(light.SCROLLAREA)
        self.ui.scrollArea_lower_add.setStyleSheet(light.SCROLLAREA)

        self.ui.comboBox_stream_primary.setStyleSheet(light.COMBO_BOX)

        self.setStyleSheet(light.MAIN_WINDOW_BACKGROUND)
        self.ui.btn_Toggle.setStyleSheet(light.TOGGLE_BTN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN)
        self.ui.TopBar.setStyleSheet(light.TOP_BAR_BACKGROUND)
        self.ui.frame_top.setStyleSheet(light.TOP_FRAME_BACKGROUND)
        self.ui.frame_return_bar.setStyleSheet(light.FRAME_RETURN_BAR)
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN)
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN)
        self.ui.frame_backup.setStyleSheet(light.FRAME_BACKUP)
        self.ui.btn_superuser.setStyleSheet(light.SUPERUSER_BTN)
        self.ui.frame_left_menu.setStyleSheet(light.FRAME_LEFT_MENU)
        self.ui.page_add_students.setStyleSheet(light.PAGE_ADD_STUDENTS)
        self.ui.frame_top_menus.setStyleSheet(light.FRAME_TOP_MENU)
        self.ui.frame_page.setStyleSheet(light.FRAME_PAGE)
        self.ui.frame_2.setStyleSheet(light.FRAME_2)
        self.ui.btn_primary.setStyleSheet(light.PRIMARY_BTN)
        self.ui.btn_ordinary.setStyleSheet(light.ORDNARY_BTN)
        self.ui.btn_advanced.setStyleSheet(light.ADVANCED_BTN)

        # INTER USER COMPENTS
        self.ui.lineEdit_full_name.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit__name_initial.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_inc_no.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_office_no.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_personal_contact.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_WOP_no.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_agrakara_no.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_spouse_name.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_contact_no_offiec_home.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_no_of_children.setStyleSheet(light.LINE_EDIT)

        self.ui.textEdit_permanent_address.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_working_address.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_other.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_nature_appointment.setStyleSheet(light.TEXT_EDIT)

        self.ui.dateEdit_DOB.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_first_appointment_date.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_appointment_date.setStyleSheet(light.DATE_EDIT)

        self.ui.radioButton_married.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_unmarried.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_male.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other.setStyleSheet(light.RASIO_BUTTON)

        self.ui.label_civil_text.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_gender_text.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_date_app_to_school_text.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_appointment_data_text.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_DOB_text.setStyleSheet(light.LABEL_COLOR)
        self.ui.label_info_Inter_face.setStyleSheet(
            light.LABEL_INFO_INTER_FACE)
        self.ui.label_info_user_inter_1.setStyleSheet(
            light.LABEL_INFO_INTER_USER_1)
        self.ui.label_info_Inter_1.setStyleSheet(light.LABEL_INFO_INTER_1)
        self.ui.info_inter_left_1.setStyleSheet(light.LABEL_INFO_INTER_1)
        self.ui.label_info_user_left_inter_1.setStyleSheet(
            light.LABEL_INFO_INTER_USER_1)
        self.ui.label_icon_inter.setStyleSheet(light.LABEL_ICON_INTER)
        self.ui.label_show_roll_number.setStyleSheet(
            light.LABEL_SHOW_ROLL_INTER)
        self.ui.label_inter_head.setStyleSheet(
            light.ANALYTICS_LABEL_INTER_HEAD)

        self.ui.groupBox_civil.setStyleSheet(light.GROUP)
        self.ui.groupBox_gender.setStyleSheet(light.GROUP)

        self.ui.widget_inter_1.setStyleSheet(light.WIDGET_INTER_1)
        self.ui.widget_inter_left_1.setStyleSheet(light.WIDGET_INTER_1)

        self.ui.frame_inter_delet_bar_1.setStyleSheet(
            light.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_inter_left_btns_bar_1.setStyleSheet(
            light.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_main_inter_info.setStyleSheet(
            light.FRMAE_MAIN_INTER_INFO)
        self.ui.frame_inter.setStyleSheet(light.ANALYTICS_FRAME_INTER)

        self.ui.btn_delete_inter_1.setStyleSheet(light.DELETE_INTER_BTN_1)
        self.ui.btn_delete_inter_left_1.setStyleSheet(light.DELETE_INTER_BTN_1)
        self.ui.btn_upload_image.setStyleSheet(light.UPLOAD_IMAGE_BTN)
        self.ui.btn_addInter.setStyleSheet(light.ADDINTER_BTN)
        self.ui.btn_go_home.setStyleSheet(light.GOHOME_INTER_BTN)

        self.ui.page_add_inter.setStyleSheet(light.PAGE_ADD_INTER)

        # PRIMARY LOWER USER COMPENTS
        self.ui.dateEdit_date_of_birth_primary.setStyleSheet(light.DATE_EDIT)
        self.ui.lineEdit_religion_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_name_full_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_name_initial_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_name_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_name_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_job_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_job_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.textEdit_address_home.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_address_office.setStyleSheet(light.TEXT_EDIT)
        self.ui.lineEdit_admission_no_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_parent_contact_primary.setStyleSheet(light.LINE_EDIT)
        self.ui.dateEdit_date_admission_primary.setStyleSheet(light.DATE_EDIT)
        self.ui.lineEdit_no_siblings_primary.setStyleSheet(light.LINE_EDIT)

        self.ui.radioButton_male_primary_2.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female_primary_2.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other_primary_2.setStyleSheet(light.RASIO_BUTTON)

        self.ui.label_inforem_admission_primary.setStyleSheet(
            light.GLOBAL_LABEL)
        self.ui.label_info_gender_primary.setStyleSheet(light.GLOBAL_LABEL)
        self.ui.label_inforem_date_of_birth_primary.setStyleSheet(
            light.GLOBAL_LABEL)
        self.ui.label_info_user_lower_pri.setStyleSheet(
            light.LABEL_INFO_PRIMARY_USER_1)
        self.ui.label_info_lower_pri.setStyleSheet(light.LABEL_INFO_PRIMARY_1)
        self.ui.label_icon_primary.setStyleSheet(light.LABEL_ICON_PRIMARY)
        self.ui.label_show_roll_primary.setStyleSheet(
            light.LABEL_SHOW_ROLL_PRIMARY)
        self.ui.info_lower_left_pri.setStyleSheet(light.LABEL_INFO_PRIMARY_1)
        self.ui.label_info_user_left_lower_pri.setStyleSheet(
            light.LABEL_INFO_PRIMARY_USER_1)

        self.ui.btn_addLower_primary.setStyleSheet(light.ADDLOWER_PRIMARY_BTN)
        self.ui.btn_go_home_primary.setStyleSheet(light.GOHOME_PRIMARY_BTN)
        self.ui.btn_delete_lower_pri.setStyleSheet(light.DELETE_PRIMARY_BTN_1)

        self.ui.frame_inter_delet_bar_pri.setStyleSheet(
            light.FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.frame_main_content_for_primary.setStyleSheet(
            light.FRAME_MAIN_CONTENT_FOR_PRIMARY)
        self.ui.frame_coments_ad_2.setStyleSheet(
            light.FRAME_CONTENT_ADVANCED_2)
        self.ui.frame_lower_btns_bar_pri.setStyleSheet(
            light.FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.frame_lower_prim.setStyleSheet(light.ANALYTICS_FRAME_PRIM)

        self.ui.page.setStyleSheet(light.PAGE_ADD_PRIMARY)

        self.ui.widget_lower_pri.setStyleSheet(light.WIDGET_PRIMARY_1)
        self.ui.widget_lower_left_pri.setStyleSheet(light.WIDGET_PRIMARY_1)

        self.ui.btn_delete_lower_left_pri.setStyleSheet(
            light.DELETE_PRIMARY_BTN_1)
        self.ui.btn_upload_image_primary.setStyleSheet(light.UPLOAD_IMAGE_BTN)

        # ORDNARY LOWER USER COMPENTS
        self.ui.lineEdit_name_full_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_name_initial_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_name_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_name_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_job_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_job_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_no_siblings_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_religion_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.textEdit_address_home_lower.setStyleSheet(light.TEXT_EDIT)
        self.ui.textEdit_address_office_lower.setStyleSheet(light.TEXT_EDIT)
        self.ui.comboBox_stream_lower.setStyleSheet(light.COMBO_BOX)
        self.ui.lineEdit_parent_contact_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_admission_no_lower.setStyleSheet(light.LINE_EDIT)
        self.ui.dateEdit_date_admission_lower.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_date_of_birth_lower.setStyleSheet(light.DATE_EDIT)

        self.ui.radioButton_male_lower_2.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female_lower_2.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other_lower_2.setStyleSheet(light.RASIO_BUTTON)

        self.ui.frame_inter_delet_bar_3.setStyleSheet(
            light.FRAME_LOWER_DELETE_BAR_1)
        self.ui.frame_lower_left_btns_bar_1.setStyleSheet(
            light.FRAME_LOWER_DELETE_BAR_1)
        self.ui.frame_lower.setStyleSheet(light.ANALYTICS_FRAME_LOWER)
        self.ui.frame_main_lower_info.setStyleSheet(
            light.FRAME_MAIN_LOWER_INFO)

        self.ui.label_inforem_admission_lower.setStyleSheet(light.GLOBAL_LABEL)
        self.ui.label_info_gender_lower.setStyleSheet(light.GLOBAL_LABEL)
        self.ui.label_inforem_date_of_birth_lower.setStyleSheet(
            light.GLOBAL_LABEL)
        self.ui.label_info_lower_1.setStyleSheet(light.LABEL_INFO_LOWER_1)
        self.ui.label_info_user_lower_1.setStyleSheet(
            light.LABEL_INFO_LOWER_USER_1)
        self.ui.info_lower_1.setStyleSheet(light.LABEL_INFO_LOWER_1)
        self.ui.label_info_user_left_lower_1.setStyleSheet(
            light.LABEL_INFO_LOWER_USER_1)
        self.ui.label_lower_head.setStyleSheet(
            light.ANALYTICS_LABEL_LOWER_HEAD)
        self.ui.label_icon_lower.setStyleSheet(light.LABEL_ICON_LOWER)
        self.ui.label_show_roll_number_lower.setStyleSheet(
            light.LABEL_SHOW_ROLL_LOWER)

        self.ui.widget_lower_1.setStyleSheet(light.WIDGET_LOWER_1)
        self.ui.widget_lower_left_1.setStyleSheet(light.WIDGET_LOWER_1)

        self.ui.btn_delete_lower_1.setStyleSheet(light.DELETE_LOWER_BTN_1)
        self.ui.btn_delete_lower_left_1.setStyleSheet(light.DELETE_LOWER_BTN_1)
        self.ui.btn_upload_image_lower.setStyleSheet(light.UPLOAD_IMAGE_BTN)
        self.ui.btn_addlower.setStyleSheet(light.ADDLOWER_LOWER_BTN)
        self.ui.btn_go_home_lower.setStyleSheet(light.GOHOME_LOWER_BTN)

        self.ui.page_add_lower.setStyleSheet(light.PAGE_ADD_LOWER)

        # ADVANCED LOWER USER COMPENTS
        self.ui.lineEdit_name_initial_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_name_full_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_religion_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_address_office_ad.setStyleSheet(light.TEXT_EDIT)
        self.ui.lineEdit_home_address_ad.setStyleSheet(light.TEXT_EDIT)
        self.ui.lineEdit_admission_no_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_name_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_name_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_father_job_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_mather_job_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_parent_contact_no_ad.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_siblings_ad.setStyleSheet(light.LINE_EDIT)

        self.ui.comboBox_level_ad.setStyleSheet(light.COMBO_BOX)
        self.ui.comboBox_stream.setStyleSheet(light.COMBO_BOX)

        self.ui.dateEdit_date_of_admission_ad.setStyleSheet(light.DATE_EDIT)
        self.ui.dateEdit_date_of_birth_ad.setStyleSheet(light.DATE_EDIT)

        self.ui.radioButton_male_ad.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_female_ad.setStyleSheet(light.RASIO_BUTTON)
        self.ui.radioButton_other_ad.setStyleSheet(light.RASIO_BUTTON)

        self.ui.label_inforem_date_of_birth_ad.setStyleSheet(
            light.GLOBAL_LABEL)
        self.ui.label_icon_.setStyleSheet(light.LABEL_ICON_)
        self.ui.label_show_roll_ad.setStyleSheet(
            light.LABEL_SHOW_ROLL_ADVANCED)
        self.ui.label_info_lower_advan.setStyleSheet(
            light.LABEL_INFO_ADVANCED_1)
        self.ui.label_info_user_lower_advan.setStyleSheet(
            light.LABEL_INFO_ADVANCED_USER_1)
        self.ui.info_lower_left_advan.setStyleSheet(
            light.LABEL_INFO_ADVANCED_1)
        self.ui.label_info_user_left_lower_advan.setStyleSheet(
            light.LABEL_INFO_ADVANCED_USER_1)
        self.ui.label_advanced_level_13.setStyleSheet(
            light.LABEL_ADVANCED_LEVEL_13)
        self.ui.label_advanced_level_12.setStyleSheet(
            light.LABEL_ADVANCED_LEVEL_12)
        self.ui.label_gender_ad.setStyleSheet(light.GLOBAL_LABEL)
        self.ui.label_date_admission_ad.setStyleSheet(light.GLOBAL_LABEL)

        self.ui.page_add_advan.setStyleSheet(light.PAGE_ADD_ADVAN)

        self.ui.frame_coments_ad.setStyleSheet(light.FRAME_CONTENT_ADVANCED)
        self.ui.frame_main_content_for_advance.setStyleSheet(
            light.FRAME_MAIN_CONTENT_FOR_ADVANCED)
        self.ui.frame_inter_delet_bar_advan.setStyleSheet(
            light.FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.frame_lower_btns_bar_advan.setStyleSheet(
            light.FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.frame_lower_advan.setStyleSheet(light.ANALYTICS_FRAME_ADVAN)
        self.ui.frame_advanced_level_12.setStyleSheet(
            light.FRAME_ADVANCED_LEVEL_12)
        self.ui.frame_advanced_level_13.setStyleSheet(
            light.FRAME_ADVANCED_LEVEL_13)

        self.ui.btn_addLower_adv.setStyleSheet(light.ADDLOWER_ADVANCED_BTN)
        self.ui.btn_go_home_ad.setStyleSheet(light.GOHOME_ADVANCED_BTN)
        self.ui.btn_delete_lower_advan.setStyleSheet(
            light.DELETE_ADVANCED_BTN_1)
        self.ui.btn_delete_lower_left_advan.setStyleSheet(
            light.DELETE_ADVANCED_BTN_1)
        self.ui.btn_upload_image_advanced.setStyleSheet(light.UPLOAD_IMAGE_BTN)

        self.ui.widget_lower_advan.setStyleSheet(light.WIDGET_ADVANCED_1)
        self.ui.widget_lower_left_advan.setStyleSheet(light.WIDGET_ADVANCED_1)

        # SUPER USER COMPENTS
        self.ui.lineEdit_username_change_input.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_change_email_input.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_contact_number_input.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_passord_input.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_repassword_input.setStyleSheet(light.LINE_EDIT)

        self.ui.frame_user_name_changer.setStyleSheet(
            light.SETTING_NAME_CHANGER)
        self.ui.frame_more_options.setStyleSheet(light.SETTING_FRAME_MORE_OP)
        self.ui.frame_email_changer.setStyleSheet(
            light.SETTING_FRAME_EMAIL_CHANGER)
        self.ui.frame_contect_number_changer.setStyleSheet(
            light.SETTING_FRAME_CONTECT_NUM_CHANGER)
        self.ui.frame_password_changer.setStyleSheet(
            light.SETTING_FRAME_PASSWORD_CHANGER)
        self.ui.frame_super_user.setStyleSheet(light.FRAME_SUPERUSER)

        self.ui.label_username_title.setStyleSheet(
            light.SETTING_USER_NAME_TITLE)
        self.ui.label_show_current_username.setStyleSheet(
            light.SETTING_LABEL_SHOW_CURRENT_USERNAME)
        self.ui.label_title.setStyleSheet(light.SETTING_LABEL_TITLE)
        self.ui.label_reload_info.setStyleSheet(light.SETTING_LABEL_RELOAD)
        self.ui.label_reset_info.setStyleSheet(light.SETTING_LABEL_INFO_RESET)
        self.ui.label_change_email_title.setStyleSheet(
            light.SETTING_LABEL_CHANGE_EMAIL_TITLE)
        self.ui.label_current_email.setStyleSheet(
            light.SETTING_LABEL_CURRENT_EMAIL)
        self.ui.label_change_contact_number_title.setStyleSheet(
            light.SETTING_LABEL_CHANGE_CONTECT_NUM_TITLE)
        self.ui.label_show_current_contact_number.setStyleSheet(
            light.SETTING_SHOW_CURRENT_CONTECT_NUM)
        self.ui.label_change_password_title.setStyleSheet(
            light.SETTING_LABEL_CHANGE_PASSWORD_TITLE)
        self.ui.label_super_icon.setStyleSheet(light.LABEL_SUPERUSER_ICON)
        self.ui.label_infor_super.setStyleSheet(light.LABEL_INFO_SUPERUSER)

        self.ui.btn_hidden_username_bar.setStyleSheet(
            light.SETTING_USERNAME_HIDDEN_BTN)
        self.ui.btn_save_username.setStyleSheet(
            light.SETTING_SAVE_USERNAME_BTN)
        self.ui.btn_hidden_options.setStyleSheet(light.SETTING_HIDDEN_BTN_OP)
        self.ui.btn_reload.setStyleSheet(light.SETTING_RELOAD_BTN)
        self.ui.btn_reset.setStyleSheet(light.SETTING_RESET_BTN)
        self.ui.btn_logout.setStyleSheet(light.SETTING_LOGOUT_BTN)
        self.ui.btn_hidden_email_bar.setStyleSheet(
            light.SETTING_HIDDEN_EMAIL_BTN)
        self.ui.btn_save_change_email.setStyleSheet(
            light.SETTING_SAVE_EMAIL_BTN)
        self.ui.btn_hidden_contact_number_bar.setStyleSheet(
            light.SETTING_HIDDEN_BTN_CONTECT)
        self.ui.btn_save_contact_number.setStyleSheet(
            light.SETTING_SAVE_CONTECT_NUM_BTN)
        self.ui.btn_hidden_passowd_changer_bar.setStyleSheet(
            light.SETTING_PASSWORD_CHANGER_BTN)
        self.ui.btn_save_password.setStyleSheet(
            light.SETTING_SAVE_PASSWORD_BTN)

        # SOFTWARE COMPENTS
        self.ui.lineEdit_rollSearch.setStyleSheet(light.LINE_EDIT)
        self.ui.lineEdit_nameSearch.setStyleSheet(light.LINE_EDIT)

        self.ui.btn_nameSearch.setStyleSheet(light.SEARCH_BAR_BTN)
        self.ui.btn_rollSearch.setStyleSheet(light.SEARCH_BAR_BTN)
        self.ui.btn_edit_setting.setStyleSheet(light.EDIT_SETTING_BTN)
        self.ui.btn_hidden_adout.setStyleSheet(light.HIDDEN_ABOUT_BTN)

        self.ui.frame_main_home_bar.setStyleSheet(light.FRAME_MAIN_HOME_BAR)
        self.ui.frame_main_left_bar.setStyleSheet(light.FRAME_MAIN_LEFT_BAR)
        self.ui.frame_main_search_bar.setStyleSheet(
            light.FRAME_MAIN_SEARCH_BAR)
        self.ui.frame_searching_main.setStyleSheet(light.FRAME_SEARCHING_MAIN)
        self.ui.frame_title_search.setStyleSheet(light.FRAME_TITLE_SEARCH)
        self.ui.frame_search_bar_itmes.setStyleSheet(
            light.FRAME_SEARCH_BAR_ITEMS)
        self.ui.frame_main_setting_bar.setStyleSheet(light.SETTING_BACKGROUND)
        self.ui.frame.setStyleSheet(light.SETTING_FRAME)
        self.ui.frame_content.setStyleSheet(light.ANALYTICS_FRAME_CONTENT)
        self.ui.frame_adout.setStyleSheet(light.FRAME_ABOUT)
        self.ui.frame_content_adout.setStyleSheet(light.FRAME_CONTENT_ABOUT)

        self.ui.label_more_info_adout.setStyleSheet(light.LABEL_MORE_ABOUT)
        self.ui.label.setStyleSheet(light.SETTING_LABEL)
        self.ui.label_info_adout.setStyleSheet(light.LABEL_INFO_ABOUT)

        self.ui.page_content_Input.setStyleSheet(light.PAGE_CONTECT)

        self.ui.scrollAreaWidgetContents.setStyleSheet(light.SCROLLAREA_WIDGET)
        self.ui.analytics.setStyleSheet(light.ANALYTICS)

        self.ui.frame_setTheme.setStyleSheet(light.SETTING_FRAME_SETTHEME)
        self.ui.label_theme_set_info.setStyleSheet(light.SETTING_LABEL_THEME)
        self.ui.btn_setTheme.setStyleSheet(light.THEME_BTN)
        self.ui.comboBox_theme_items.setStyleSheet(light.COMBO_BOX)

        self.ui.scrollAreaWidgetContents_2.setStyleSheet(
            light.SETTING_FRAME_SETTHEME)

    def setIcon_for_window_light(self):

        # SET ICON FUNCTION
        def setIcon(widget, path,):
            icon = QIcon()
            icon.addFile(path)
            widget.setIcon(icon)

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        self.setWindowTitle("Findup")
        icon = QIcon()
        icon.addFile(light.MAIN_WINDOW_TITLE_ICON)
        self.setWindowIcon(icon)

        self.ui.label_icon_inter.setText(light.LABEL_ICON_INTER_TEXT)
        self.ui.label_icon_lower.setText(light.LABEL_ICON_LOWER_TEXT)
        self.ui.label.setText(light.LABEL_EDIT_TEXT)

        self.ui.label_icon_.setText(light.LABEL_ICON_LOWER_TEXT)

        self.ui.label_inforem_date_of_birth_ad.setText(
            light.LABEL_DOB_TEXT)
        self.ui.label_icon_primary.setText(light.LABEL_ICON_LOWER_TEXT)
        self.ui.label_inforem_date_of_birth_primary.setText(
            light.LABEL_DOB_TEXT)

        # SUPER USER ICON
        setIcon(self.ui.btn_superuser, light.ICON_USER)
        setIcon(self.ui.btn_edit_setting, light.ICON_GO)

        # USER ADD ICONS
        setIcon(self.ui.btn_addInter, light.ICON_ADD_USER)
        setIcon(self.ui.btn_addlower, light.ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_adv, light.ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_primary, light.ICON_ADD_USER)

        setIcon(self.ui.btn_go_home, light.ICON_GO)
        setIcon(self.ui.btn_go_home_lower, light.ICON_GO)
        setIcon(self.ui.btn_go_home_primary, light.ICON_GO)
        setIcon(self.ui.btn_go_home_ad, light.ICON_GO)

        # SETTING BAR HIDDEN ICON BARS
        setIcon(self.ui.btn_hidden_username_bar, light.BTN_OPENED_ICON)
        setIcon(self.ui.btn_hidden_email_bar, light.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_contact_number_bar,
                light.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_passowd_changer_bar,
                light.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_options, light.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_adout, light.BTN_HIDDEN_ICON)

        # SEARCH BAR ICON
        setIcon(self.ui.btn_nameSearch, light.ICON_SEARCH)
        setIcon(self.ui.btn_rollSearch, light.ICON_SEARCH)

        if not self.theme_button_pressed:

            # ADD INTER USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_full_name, light.ICON_USER)
            setIcon_line(self.ui.lineEdit__name_initial, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_office_no, light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_personal_contact, light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_contact_no_offiec_home,
                         light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_spouse_name, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_no_of_children, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_agrakara_no, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_WOP_no, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_inc_no, light.ICON_RIG_NUM)

            # ADD LOWER PRIMARY USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_name_full_primary, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_primary,
                         light.ICON_USER)
            setIcon_line(self.ui.lineEdit_parent_contact_primary,
                         light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_no_siblings_primary,
                         light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_primary,
                         light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_name_primary,
                         light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_admission_no_primary,
                         light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_religion_primary, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_mather_job_primary, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_father_job_primary, light.ICON_JOB)

            # ADD LOWER ORDNARY USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_name_full_lower, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_lower, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_parent_contact_lower,
                         light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_no_siblings_lower, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_lower, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_name_lower, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_job_lower, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_mather_job_lower, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_admission_no_lower,
                         light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_religion_lower, light.ICON_RIL)

            # ADD LOWER ADVANCED USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_admission_no_ad, light.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_mather_name_ad, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_ad, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_job_ad, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_father_job_ad, light.ICON_JOB)
            setIcon_line(self.ui.lineEdit_parent_contact_no_ad,
                         light.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_siblings_ad, light.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_name_full_ad, light.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_ad, light.ICON_USER)

        else:

            # ADD INTER USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_full_name, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit__name_initial, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_office_no, light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_personal_contact, light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_contact_no_offiec_home,
                          light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_spouse_name, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_no_of_children, light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_agrakara_no, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_WOP_no, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_inc_no, light.ICON_RIG_NUM)

            # ADD LOWER PRIMARY USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_name_full_primary, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_primary,
                          light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_parent_contact_primary,
                          light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_no_siblings_primary,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_primary,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_name_primary,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_admission_no_primary,
                          light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_religion_primary,
                          light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_mather_job_primary, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_father_job_primary, light.ICON_JOB)

            # ADD LOWER ORDNARY USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_name_full_lower, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_lower, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_parent_contact_lower,
                          light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_no_siblings_lower,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_lower,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_name_lower,
                          light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_job_lower, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_mather_job_lower, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_admission_no_lower,
                          light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_religion_lower, light.ICON_RIL)

            # ADD LOWER ADVANCED USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_admission_no_ad, light.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_mather_name_ad, light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_ad, light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_job_ad, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_father_job_ad, light.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_parent_contact_no_ad,
                          light.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_siblings_ad, light.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_name_full_ad, light.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_ad, light.ICON_USER)

        # SUPERUSER ICON AND NAME
        light.setSuperUserIconName(None, self.ui.label_super_icon)

        # DELETE BTN ICONS
        setIcon(self.ui.btn_delete_inter_1, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_1, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_pri, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_advan, light.ICON_DELETE)

        setIcon(self.ui.btn_delete_inter_left_1, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_1, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_advan, light.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_pri, light.ICON_DELETE)

        # ABOUT LABEL ICON
        self.ui.label_logo_adout.setText(light.ICON_LABEL_TEXT)

        # ACTIVE AND LEFT LABEL TEXT
        self.ui.label_info_user_inter_1.setText(
            light.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_1.setText(
            light.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_pri.setText(
            light.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_advan.setText(
            light.ACTIVE_LABEL_INFO_TEXT)

        self.ui.label_info_user_left_inter_1.setText(
            light.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_1.setText(
            light.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_pri.setText(
            light.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_advan.setText(
            light.LAFT_LABEL_INFO_TEXT)

    # this dark theme of window
    def connect_functiom_dark(self):
        # Toggle Burguer Menu
        self.ui.btn_Toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu_light(self, 200, True))

        # Setting Bar Animation
        self.ui.btn_hidden_username_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_dark(self,  self.ui.frame_user_name_changer.height(
        ), self.ui.frame_user_name_changer, self.ui.frame_name_changer_content_page, True, self.ui.btn_hidden_username_bar, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))
        self.ui.btn_hidden_email_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_dark(self,  self.ui.frame_email_changer.height(
        ), self.ui.frame_email_changer, self.ui.frame_email_changer_content_bar, True, self.ui.btn_hidden_email_bar, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))
        self.ui.btn_hidden_contact_number_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_dark(self,  self.ui.frame_contect_number_changer.height(
        ), self.ui.frame_contect_number_changer, self.ui.frame_contect_number_changer_content_bar, True, self.ui.btn_hidden_contact_number_bar, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))
        self.ui.btn_hidden_passowd_changer_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar_dark(self,  self.ui.frame_password_changer.height(
        ), self.ui.frame_password_changer, self.ui.frame_password_changer_content_bar, True, self.ui.btn_hidden_passowd_changer_bar, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))

        self.ui.btn_hidden_options.clicked.connect(lambda: UIFunctions.settingHiddenBar_two_dark(self,  self.ui.frame_more_options.height(
        ), self.ui.frame_more_options, self.ui.frame_more_options_contect_bar, True, self.ui.btn_hidden_options, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))
        self.ui.btn_hidden_adout.clicked.connect(lambda: UIFunctions.settingHiddenBar_two_dark(self, self.ui.frame_adout.height(
        ), self.ui.frame_adout, self.ui.frame_content_adout, True, self.ui.btn_hidden_adout, dark.BTN_HIDDEN_ICON, dark.BTN_OPENED_ICON))

        # SUPER USER BTN
        self.ui.btn_superuser.clicked.connect(
            lambda: UIFunctions.userSideBar_toggle_dark(self, 300, True))

        # BUTTONE CONNECTER
        UIFunctions.current_page_light(self)

        self.ui.btn_page_home.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_page_left.clicked.connect(
            lambda: UIFunctions.left_dark(self))
        self.ui.btn_page_search.clicked.connect(
            lambda: UIFunctions.search_dark(self))
        self.ui.btn_setting.clicked.connect(
            lambda: UIFunctions.setting_dark(self))
        self.ui.btn_page_analytics.clicked.connect(
            lambda: UIFunctions.analytics_dark(self))
        self.ui.btn_go_home.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home_dark(self))

        # Super User Btn
        self.ui.btn_edit_setting.clicked.connect(
            lambda: UIFunctions.setting_dark(self))

        # Inter and Lower Btn
        self.ui.btn_inter.clicked.connect(
            lambda: UIFunctions.callInter_window_dark(self)
        )
        self.ui.btn_lower.clicked.connect(
            lambda: UIFunctions.callLower_window_dark(self)
        )

        # Connect into btn_ordinary
        self.ui.btn_ordinary.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_lower))
        # Connect into btn_advanced
        self.ui.btn_advanced.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page_add_advan))
        # Connect into btn_primary
        self.ui.btn_primary.clicked.connect(
            lambda: UIFunctions.call_input_menu(self, self.ui.page))

        # Go Home Button
        self.ui.btn_go_home.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_home_primary.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home_dark(self))
        self.ui.btn_go_home_ad.clicked.connect(
            lambda: UIFunctions.home_dark(self))

    def setTheme_for_window_dark(self):
        self.ui.scrollArea_2.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_resalt.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_3.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_content.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_4.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_add_info.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_advanced_add.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_primary_add.setStyleSheet(dark.SCROLLAREA)
        self.ui.scrollArea_lower_add.setStyleSheet(dark.SCROLLAREA)

        self.ui.comboBox_stream_primary.setStyleSheet(dark.COMBO_BOX)

        self.setStyleSheet(dark.MAIN_WINDOW_BACKGROUND)
        self.ui.btn_Toggle.setStyleSheet(dark.TOGGLE_BTN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN)
        self.ui.TopBar.setStyleSheet(dark.TOP_BAR_BACKGROUND)
        self.ui.frame_top.setStyleSheet(dark.TOP_FRAME_BACKGROUND)
        self.ui.frame_return_bar.setStyleSheet(dark.FRAME_RETURN_BAR)
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN)
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN)
        self.ui.frame_backup.setStyleSheet(dark.FRAME_BACKUP)
        self.ui.btn_superuser.setStyleSheet(dark.SUPERUSER_BTN)
        self.ui.frame_left_menu.setStyleSheet(dark.FRAME_LEFT_MENU)
        self.ui.page_add_students.setStyleSheet(dark.PAGE_ADD_STUDENTS)
        self.ui.frame_top_menus.setStyleSheet(dark.FRAME_TOP_MENU)
        self.ui.frame_page.setStyleSheet(dark.FRAME_PAGE)
        self.ui.frame_2.setStyleSheet(dark.FRAME_2)
        self.ui.btn_primary.setStyleSheet(dark.PRIMARY_BTN)
        self.ui.btn_ordinary.setStyleSheet(dark.ORDNARY_BTN)
        self.ui.btn_advanced.setStyleSheet(dark.ADVANCED_BTN)

        # INTER USER COMPENTS
        self.ui.lineEdit_full_name.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit__name_initial.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_inc_no.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_office_no.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_personal_contact.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_WOP_no.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_agrakara_no.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_spouse_name.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_contact_no_offiec_home.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_no_of_children.setStyleSheet(dark.LINE_EDIT)

        self.ui.textEdit_permanent_address.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_working_address.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_other.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_nature_appointment.setStyleSheet(dark.TEXT_EDIT)

        self.ui.dateEdit_DOB.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_first_appointment_date.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_appointment_date.setStyleSheet(dark.DATE_EDIT)

        self.ui.radioButton_married.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_unmarried.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_male.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.label_civil_text.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_gender_text.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_date_app_to_school_text.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_appointment_data_text.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_DOB_text.setStyleSheet(dark.LABEL_COLOR)
        self.ui.label_info_Inter_face.setStyleSheet(
            dark.LABEL_INFO_INTER_FACE)
        self.ui.label_info_user_inter_1.setStyleSheet(
            dark.LABEL_INFO_INTER_USER_1)
        self.ui.label_info_Inter_1.setStyleSheet(dark.LABEL_INFO_INTER_1)
        self.ui.info_inter_left_1.setStyleSheet(dark.LABEL_INFO_INTER_1)
        self.ui.label_info_user_left_inter_1.setStyleSheet(
            dark.LABEL_INFO_INTER_USER_1)
        self.ui.label_icon_inter.setStyleSheet(dark.LABEL_ICON_INTER)
        self.ui.label_show_roll_number.setStyleSheet(
            dark.LABEL_SHOW_ROLL_INTER)
        self.ui.label_inter_head.setStyleSheet(
            dark.ANALYTICS_LABEL_INTER_HEAD)

        self.ui.groupBox_civil.setStyleSheet(dark.GROUP)
        self.ui.groupBox_gender.setStyleSheet(dark.GROUP)

        self.ui.widget_inter_1.setStyleSheet(dark.WIDGET_INTER_1)
        self.ui.widget_inter_left_1.setStyleSheet(dark.WIDGET_INTER_1)

        self.ui.frame_inter_delet_bar_1.setStyleSheet(
            dark.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_inter_left_btns_bar_1.setStyleSheet(
            dark.FRAME_INTER_DELETE_BAR_1)
        self.ui.frame_main_inter_info.setStyleSheet(
            dark.FRMAE_MAIN_INTER_INFO)
        self.ui.frame_inter.setStyleSheet(dark.ANALYTICS_FRAME_INTER)

        self.ui.btn_delete_inter_1.setStyleSheet(dark.DELETE_INTER_BTN_1)
        self.ui.btn_delete_inter_left_1.setStyleSheet(dark.DELETE_INTER_BTN_1)
        self.ui.btn_upload_image.setStyleSheet(dark.UPLOAD_IMAGE_BTN)
        self.ui.btn_addInter.setStyleSheet(dark.ADDINTER_BTN)
        self.ui.btn_go_home.setStyleSheet(dark.GOHOME_INTER_BTN)

        self.ui.page_add_inter.setStyleSheet(dark.PAGE_ADD_INTER)

        # PRIMARY LOWER USER COMPENTS
        self.ui.dateEdit_date_of_birth_primary.setStyleSheet(dark.DATE_EDIT)
        self.ui.lineEdit_religion_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_name_full_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_name_initial_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_name_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_name_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_job_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_job_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.textEdit_address_home.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_address_office.setStyleSheet(dark.TEXT_EDIT)
        self.ui.lineEdit_admission_no_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_parent_contact_primary.setStyleSheet(dark.LINE_EDIT)
        self.ui.dateEdit_date_admission_primary.setStyleSheet(dark.DATE_EDIT)
        self.ui.lineEdit_no_siblings_primary.setStyleSheet(dark.LINE_EDIT)

        self.ui.radioButton_male_primary_2.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female_primary_2.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other_primary_2.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.label_inforem_admission_primary.setStyleSheet(
            dark.GLOBAL_LABEL)
        self.ui.label_info_gender_primary.setStyleSheet(dark.GLOBAL_LABEL)
        self.ui.label_inforem_date_of_birth_primary.setStyleSheet(
            dark.GLOBAL_LABEL)
        self.ui.label_info_user_lower_pri.setStyleSheet(
            dark.LABEL_INFO_PRIMARY_USER_1)
        self.ui.label_info_lower_pri.setStyleSheet(dark.LABEL_INFO_PRIMARY_1)
        self.ui.label_icon_primary.setStyleSheet(dark.LABEL_ICON_PRIMARY)
        self.ui.label_show_roll_primary.setStyleSheet(
            dark.LABEL_SHOW_ROLL_PRIMARY)
        self.ui.info_lower_left_pri.setStyleSheet(dark.LABEL_INFO_PRIMARY_1)
        self.ui.label_info_user_left_lower_pri.setStyleSheet(
            dark.LABEL_INFO_PRIMARY_USER_1)

        self.ui.btn_addLower_primary.setStyleSheet(dark.ADDLOWER_PRIMARY_BTN)
        self.ui.btn_go_home_primary.setStyleSheet(dark.GOHOME_PRIMARY_BTN)
        self.ui.btn_delete_lower_pri.setStyleSheet(dark.DELETE_PRIMARY_BTN_1)

        self.ui.frame_inter_delet_bar_pri.setStyleSheet(
            dark.FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.frame_main_content_for_primary.setStyleSheet(
            dark.FRAME_MAIN_CONTENT_FOR_PRIMARY)
        self.ui.frame_coments_ad_2.setStyleSheet(
            dark.FRAME_CONTENT_ADVANCED_2)
        self.ui.frame_lower_btns_bar_pri.setStyleSheet(
            dark.FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.frame_lower_prim.setStyleSheet(dark.ANALYTICS_FRAME_PRIM)

        self.ui.page.setStyleSheet(dark.PAGE_ADD_PRIMARY)

        self.ui.widget_lower_pri.setStyleSheet(dark.WIDGET_PRIMARY_1)
        self.ui.widget_lower_left_pri.setStyleSheet(dark.WIDGET_PRIMARY_1)

        self.ui.btn_delete_lower_left_pri.setStyleSheet(
            dark.DELETE_PRIMARY_BTN_1)
        self.ui.btn_upload_image_primary.setStyleSheet(dark.UPLOAD_IMAGE_BTN)

        # ORDNARY LOWER USER COMPENTS
        self.ui.lineEdit_name_full_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_name_initial_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_name_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_name_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_job_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_job_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_no_siblings_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_religion_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.textEdit_address_home_lower.setStyleSheet(dark.TEXT_EDIT)
        self.ui.textEdit_address_office_lower.setStyleSheet(dark.TEXT_EDIT)
        self.ui.comboBox_stream_lower.setStyleSheet(dark.COMBO_BOX)
        self.ui.lineEdit_parent_contact_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_admission_no_lower.setStyleSheet(dark.LINE_EDIT)
        self.ui.dateEdit_date_admission_lower.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_date_of_birth_lower.setStyleSheet(dark.DATE_EDIT)

        self.ui.radioButton_male_lower_2.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female_lower_2.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other_lower_2.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.frame_inter_delet_bar_3.setStyleSheet(
            dark.FRAME_LOWER_DELETE_BAR_1)
        self.ui.frame_lower_left_btns_bar_1.setStyleSheet(
            dark.FRAME_LOWER_DELETE_BAR_1)
        self.ui.frame_lower.setStyleSheet(dark.ANALYTICS_FRAME_LOWER)
        self.ui.frame_main_lower_info.setStyleSheet(
            dark.FRAME_MAIN_LOWER_INFO)

        self.ui.label_inforem_admission_lower.setStyleSheet(dark.GLOBAL_LABEL)
        self.ui.label_info_gender_lower.setStyleSheet(dark.GLOBAL_LABEL)
        self.ui.label_inforem_date_of_birth_lower.setStyleSheet(
            dark.GLOBAL_LABEL)
        self.ui.label_info_lower_1.setStyleSheet(dark.LABEL_INFO_LOWER_1)
        self.ui.label_info_user_lower_1.setStyleSheet(
            dark.LABEL_INFO_LOWER_USER_1)
        self.ui.info_lower_1.setStyleSheet(dark.LABEL_INFO_LOWER_1)
        self.ui.label_info_user_left_lower_1.setStyleSheet(
            dark.LABEL_INFO_LOWER_USER_1)
        self.ui.label_lower_head.setStyleSheet(
            dark.ANALYTICS_LABEL_LOWER_HEAD)
        self.ui.label_icon_lower.setStyleSheet(dark.LABEL_ICON_LOWER)
        self.ui.label_show_roll_number_lower.setStyleSheet(
            dark.LABEL_SHOW_ROLL_LOWER)

        self.ui.widget_lower_1.setStyleSheet(dark.WIDGET_LOWER_1)
        self.ui.widget_lower_left_1.setStyleSheet(dark.WIDGET_LOWER_1)

        self.ui.btn_delete_lower_1.setStyleSheet(dark.DELETE_LOWER_BTN_1)
        self.ui.btn_delete_lower_left_1.setStyleSheet(dark.DELETE_LOWER_BTN_1)
        self.ui.btn_upload_image_lower.setStyleSheet(dark.UPLOAD_IMAGE_BTN)
        self.ui.btn_addlower.setStyleSheet(dark.ADDLOWER_LOWER_BTN)
        self.ui.btn_go_home_lower.setStyleSheet(dark.GOHOME_LOWER_BTN)

        self.ui.page_add_lower.setStyleSheet(dark.PAGE_ADD_LOWER)

        # ADVANCED LOWER USER COMPENTS
        self.ui.lineEdit_name_initial_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_name_full_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_religion_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_address_office_ad.setStyleSheet(dark.TEXT_EDIT)
        self.ui.lineEdit_home_address_ad.setStyleSheet(dark.TEXT_EDIT)
        self.ui.lineEdit_admission_no_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_name_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_name_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_father_job_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_mather_job_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_parent_contact_no_ad.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_siblings_ad.setStyleSheet(dark.LINE_EDIT)

        self.ui.comboBox_level_ad.setStyleSheet(dark.COMBO_BOX)
        self.ui.comboBox_stream.setStyleSheet(dark.COMBO_BOX)

        self.ui.dateEdit_date_of_admission_ad.setStyleSheet(dark.DATE_EDIT)
        self.ui.dateEdit_date_of_birth_ad.setStyleSheet(dark.DATE_EDIT)

        self.ui.radioButton_male_ad.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_female_ad.setStyleSheet(dark.RASIO_BUTTON)
        self.ui.radioButton_other_ad.setStyleSheet(dark.RASIO_BUTTON)

        self.ui.label_inforem_date_of_birth_ad.setStyleSheet(
            dark.GLOBAL_LABEL)
        self.ui.label_icon_.setStyleSheet(dark.LABEL_ICON_)
        self.ui.label_show_roll_ad.setStyleSheet(
            dark.LABEL_SHOW_ROLL_ADVANCED)
        self.ui.label_info_lower_advan.setStyleSheet(
            dark.LABEL_INFO_ADVANCED_1)
        self.ui.label_info_user_lower_advan.setStyleSheet(
            dark.LABEL_INFO_ADVANCED_USER_1)
        self.ui.info_lower_left_advan.setStyleSheet(
            dark.LABEL_INFO_ADVANCED_1)
        self.ui.label_info_user_left_lower_advan.setStyleSheet(
            dark.LABEL_INFO_ADVANCED_USER_1)
        self.ui.label_advanced_level_13.setStyleSheet(
            dark.LABEL_ADVANCED_LEVEL_13)
        self.ui.label_advanced_level_12.setStyleSheet(
            dark.LABEL_ADVANCED_LEVEL_12)
        self.ui.label_gender_ad.setStyleSheet(dark.GLOBAL_LABEL)
        self.ui.label_date_admission_ad.setStyleSheet(dark.GLOBAL_LABEL)

        self.ui.page_add_advan.setStyleSheet(dark.PAGE_ADD_ADVAN)

        self.ui.frame_coments_ad.setStyleSheet(dark.FRAME_CONTENT_ADVANCED)
        self.ui.frame_main_content_for_advance.setStyleSheet(
            dark.FRAME_MAIN_CONTENT_FOR_ADVANCED)
        self.ui.frame_inter_delet_bar_advan.setStyleSheet(
            dark.FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.frame_lower_btns_bar_advan.setStyleSheet(
            dark.FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.frame_lower_advan.setStyleSheet(dark.ANALYTICS_FRAME_ADVAN)
        self.ui.frame_advanced_level_12.setStyleSheet(
            dark.FRAME_ADVANCED_LEVEL_12)
        self.ui.frame_advanced_level_13.setStyleSheet(
            dark.FRAME_ADVANCED_LEVEL_13)

        self.ui.btn_addLower_adv.setStyleSheet(dark.ADDLOWER_ADVANCED_BTN)
        self.ui.btn_go_home_ad.setStyleSheet(dark.GOHOME_ADVANCED_BTN)
        self.ui.btn_delete_lower_advan.setStyleSheet(
            dark.DELETE_ADVANCED_BTN_1)
        self.ui.btn_delete_lower_left_advan.setStyleSheet(
            dark.DELETE_ADVANCED_BTN_1)
        self.ui.btn_upload_image_advanced.setStyleSheet(dark.UPLOAD_IMAGE_BTN)

        self.ui.widget_lower_advan.setStyleSheet(dark.WIDGET_ADVANCED_1)
        self.ui.widget_lower_left_advan.setStyleSheet(dark.WIDGET_ADVANCED_1)

        # SUPER USER COMPENTS
        self.ui.lineEdit_username_change_input.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_change_email_input.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_contact_number_input.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_passord_input.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_repassword_input.setStyleSheet(dark.LINE_EDIT)

        self.ui.frame_user_name_changer.setStyleSheet(
            dark.SETTING_NAME_CHANGER)
        self.ui.frame_more_options.setStyleSheet(dark.SETTING_FRAME_MORE_OP)
        self.ui.frame_email_changer.setStyleSheet(
            dark.SETTING_FRAME_EMAIL_CHANGER)
        self.ui.frame_contect_number_changer.setStyleSheet(
            dark.SETTING_FRAME_CONTECT_NUM_CHANGER)
        self.ui.frame_password_changer.setStyleSheet(
            dark.SETTING_FRAME_PASSWORD_CHANGER)
        self.ui.frame_super_user.setStyleSheet(dark.FRAME_SUPERUSER)

        self.ui.label_username_title.setStyleSheet(
            dark.SETTING_USER_NAME_TITLE)
        self.ui.label_show_current_username.setStyleSheet(
            dark.SETTING_LABEL_SHOW_CURRENT_USERNAME)
        self.ui.label_title.setStyleSheet(dark.SETTING_LABEL_TITLE)
        self.ui.label_reload_info.setStyleSheet(dark.SETTING_LABEL_RELOAD)
        self.ui.label_reset_info.setStyleSheet(dark.SETTING_LABEL_INFO_RESET)
        self.ui.label_change_email_title.setStyleSheet(
            dark.SETTING_LABEL_CHANGE_EMAIL_TITLE)
        self.ui.label_current_email.setStyleSheet(
            dark.SETTING_LABEL_CURRENT_EMAIL)
        self.ui.label_change_contact_number_title.setStyleSheet(
            dark.SETTING_LABEL_CHANGE_CONTECT_NUM_TITLE)
        self.ui.label_show_current_contact_number.setStyleSheet(
            dark.SETTING_SHOW_CURRENT_CONTECT_NUM)
        self.ui.label_change_password_title.setStyleSheet(
            dark.SETTING_LABEL_CHANGE_PASSWORD_TITLE)
        self.ui.label_super_icon.setStyleSheet(dark.LABEL_SUPERUSER_ICON)
        self.ui.label_infor_super.setStyleSheet(dark.LABEL_INFO_SUPERUSER)

        self.ui.btn_hidden_username_bar.setStyleSheet(
            dark.SETTING_USERNAME_HIDDEN_BTN)
        self.ui.btn_save_username.setStyleSheet(
            dark.SETTING_SAVE_USERNAME_BTN)
        self.ui.btn_hidden_options.setStyleSheet(dark.SETTING_HIDDEN_BTN_OP)
        self.ui.btn_reload.setStyleSheet(dark.SETTING_RELOAD_BTN)
        self.ui.btn_reset.setStyleSheet(dark.SETTING_RESET_BTN)
        self.ui.btn_logout.setStyleSheet(dark.SETTING_LOGOUT_BTN)
        self.ui.btn_hidden_email_bar.setStyleSheet(
            dark.SETTING_HIDDEN_EMAIL_BTN)
        self.ui.btn_save_change_email.setStyleSheet(
            dark.SETTING_SAVE_EMAIL_BTN)
        self.ui.btn_hidden_contact_number_bar.setStyleSheet(
            dark.SETTING_HIDDEN_BTN_CONTECT)
        self.ui.btn_save_contact_number.setStyleSheet(
            dark.SETTING_SAVE_CONTECT_NUM_BTN)
        self.ui.btn_hidden_passowd_changer_bar.setStyleSheet(
            dark.SETTING_PASSWORD_CHANGER_BTN)
        self.ui.btn_save_password.setStyleSheet(
            dark.SETTING_SAVE_PASSWORD_BTN)

        # SOFTWARE COMPENTS
        self.ui.lineEdit_rollSearch.setStyleSheet(dark.LINE_EDIT)
        self.ui.lineEdit_nameSearch.setStyleSheet(dark.LINE_EDIT)

        self.ui.btn_nameSearch.setStyleSheet(dark.SEARCH_BAR_BTN)
        self.ui.btn_rollSearch.setStyleSheet(dark.SEARCH_BAR_BTN)
        self.ui.btn_edit_setting.setStyleSheet(dark.EDIT_SETTING_BTN)
        self.ui.btn_hidden_adout.setStyleSheet(dark.HIDDEN_ABOUT_BTN)

        self.ui.frame_main_home_bar.setStyleSheet(dark.FRAME_MAIN_HOME_BAR)
        self.ui.frame_main_left_bar.setStyleSheet(dark.FRAME_MAIN_LEFT_BAR)
        self.ui.frame_main_search_bar.setStyleSheet(
            dark.FRAME_MAIN_SEARCH_BAR)
        self.ui.frame_searching_main.setStyleSheet(dark.FRAME_SEARCHING_MAIN)
        self.ui.frame_title_search.setStyleSheet(dark.FRAME_TITLE_SEARCH)
        self.ui.frame_search_bar_itmes.setStyleSheet(
            dark.FRAME_SEARCH_BAR_ITEMS)
        self.ui.frame_main_setting_bar.setStyleSheet(dark.SETTING_BACKGROUND)
        self.ui.frame.setStyleSheet(dark.SETTING_FRAME)
        self.ui.frame_content.setStyleSheet(dark.ANALYTICS_FRAME_CONTENT)
        self.ui.frame_adout.setStyleSheet(dark.FRAME_ABOUT)
        self.ui.frame_content_adout.setStyleSheet(dark.FRAME_CONTENT_ABOUT)

        self.ui.label_more_info_adout.setStyleSheet(dark.LABEL_MORE_ABOUT)
        self.ui.label.setStyleSheet(dark.SETTING_LABEL)
        self.ui.label_info_adout.setStyleSheet(dark.LABEL_INFO_ABOUT)

        self.ui.page_content_Input.setStyleSheet(dark.PAGE_CONTECT)

        self.ui.scrollAreaWidgetContents.setStyleSheet(dark.SCROLLAREA_WIDGET)
        self.ui.analytics.setStyleSheet(dark.ANALYTICS)

        self.ui.frame_setTheme.setStyleSheet(dark.SETTING_FRAME_SETTHEME)
        self.ui.label_theme_set_info.setStyleSheet(dark.SETTING_LABEL_THEME)
        self.ui.btn_setTheme.setStyleSheet(dark.THEME_BTN)
        self.ui.comboBox_theme_items.setStyleSheet(dark.COMBO_BOX)

        self.ui.scrollAreaWidgetContents_2.setStyleSheet(
            dark.SETTING_FRAME_SETTHEME)

    def setIcon_for_window_dark(self):

        # SET ICON FUNCTION
        def setIcon(widget, path,):
            icon = QIcon()
            icon.addFile(path)
            widget.setIcon(icon)

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        def setIcon_line_(widget, path):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.findChild(QAction).setIcon(icon)

        self.setWindowTitle("Findup")
        icon = QIcon()
        icon.addFile(dark.MAIN_WINDOW_TITLE_ICON)
        self.setWindowIcon(icon)

        self.ui.label_icon_inter.setText(dark.LABEL_ICON_INTER_TEXT)
        self.ui.label_icon_lower.setText(dark.LABEL_ICON_LOWER_TEXT)
        self.ui.label.setText(dark.LABEL_EDIT_TEXT)

        self.ui.label_icon_.setText(dark.LABEL_ICON_LOWER_TEXT)

        self.ui.label_inforem_date_of_birth_ad.setText(dark.LABEL_DOB_TEXT)
        self.ui.label_icon_primary.setText(dark.LABEL_ICON_LOWER_TEXT)
        self.ui.label_inforem_date_of_birth_primary.setText(
            dark.LABEL_DOB_TEXT)

        # SUPER USER ICON
        setIcon(self.ui.btn_superuser, dark.ICON_USER)
        setIcon(self.ui.btn_edit_setting, dark.ICON_GO)

        # USER ADD ICONS
        setIcon(self.ui.btn_addInter, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_addlower, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_adv, dark.ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_primary, dark.ICON_ADD_USER)

        setIcon(self.ui.btn_go_home, dark.ICON_GO)
        setIcon(self.ui.btn_go_home_lower, dark.ICON_GO)
        setIcon(self.ui.btn_go_home_primary, dark.ICON_GO)
        setIcon(self.ui.btn_go_home_ad, dark.ICON_GO)

        # SETTING BAR HIDDEN ICON BARS
        setIcon(self.ui.btn_hidden_username_bar, dark.BTN_OPENED_ICON)
        setIcon(self.ui.btn_hidden_email_bar, dark.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_contact_number_bar, dark.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_passowd_changer_bar, dark.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_options, dark.BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_adout, dark.BTN_HIDDEN_ICON)

        # SEARCH BAR ICON
        setIcon(self.ui.btn_nameSearch, dark.ICON_SEARCH)
        setIcon(self.ui.btn_rollSearch, dark.ICON_SEARCH)

        # ADD INTER USER PAGE ICONS
        icon = QIcon()
        icon.addFile(dark.ICON_USER)
        self.ui.lineEdit_full_name.findChild(QAction).setIcon(
            icon
        )
        if not self.theme_button_pressed:
            setIcon_line(self.ui.lineEdit_full_name, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit__name_initial, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_office_no, dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_personal_contact, dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_contact_no_offiec_home,
                         dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_spouse_name, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_no_of_children, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_agrakara_no, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_WOP_no, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_inc_no, dark.ICON_RIG_NUM)

            # ADD LOWER PRIMARY USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_name_full_primary, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_primary, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_parent_contact_primary,
                         dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_no_siblings_primary,
                         dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_primary,
                         dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_name_primary,
                         dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_admission_no_primary,
                         dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_religion_primary, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_mather_job_primary, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_father_job_primary, dark.ICON_JOB)

            # ADD LOWER ORDNARY USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_name_full_lower, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_lower, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_parent_contact_lower,
                         dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_no_siblings_lower, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_lower, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_name_lower, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_job_lower, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_mather_job_lower, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_admission_no_lower,
                         dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_religion_lower, dark.ICON_RIL)

            # ADD LOWER ADVANCED USER PAGE ICONS
            setIcon_line(self.ui.lineEdit_admission_no_ad, dark.ICON_RIG_NUM)
            setIcon_line(self.ui.lineEdit_mather_name_ad, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_father_name_ad, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_mather_job_ad, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_father_job_ad, dark.ICON_JOB)
            setIcon_line(self.ui.lineEdit_parent_contact_no_ad,
                         dark.ICON_PHONE)
            setIcon_line(self.ui.lineEdit_siblings_ad, dark.ICON_PEOPLE)
            setIcon_line(self.ui.lineEdit_name_full_ad, dark.ICON_USER)
            setIcon_line(self.ui.lineEdit_name_initial_ad, dark.ICON_USER)

        else:
            # ADD LOWER PRIMARY USER PAGE ICONS
            print("LOWRE PRIMARY USER ICON ADDPAGE COMPLETE ....")
            setIcon_line_(self.ui.lineEdit_name_full_primary, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_primary,
                          dark.ICON_USER)
            setIcon_line_(
                self.ui.lineEdit_parent_contact_primary, dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_no_siblings_primary,
                          dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_primary,
                          dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_name_primary,
                          dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_admission_no_primary,
                          dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_religion_primary, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_mather_job_primary, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_father_job_primary, dark.ICON_JOB)

            # ADD INTER USER PAGE ICON
            print("INTER USER ICON ADDPAGE COMPLETE ....")
            setIcon_line_(self.ui.lineEdit_full_name, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit__name_initial, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_office_no, dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_personal_contact, dark.ICON_PHONE)
            setIcon_line_(
                self.ui.lineEdit_contact_no_offiec_home, dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_spouse_name, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_no_of_children, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_agrakara_no, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_WOP_no, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_inc_no, dark.ICON_RIG_NUM)

            # ADD LOWER ORDNARY USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_name_full_lower, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_lower, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_parent_contact_lower,
                          dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_no_siblings_lower, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_lower, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_name_lower, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_job_lower, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_mather_job_lower, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_admission_no_lower,
                          dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_religion_lower, dark.ICON_RIL)

            # ADD LOWER ADVANCED USER PAGE ICONS
            setIcon_line_(self.ui.lineEdit_admission_no_ad, dark.ICON_RIG_NUM)
            setIcon_line_(self.ui.lineEdit_mather_name_ad, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_father_name_ad, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_mather_job_ad, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_father_job_ad, dark.ICON_JOB)
            setIcon_line_(self.ui.lineEdit_parent_contact_no_ad,
                          dark.ICON_PHONE)
            setIcon_line_(self.ui.lineEdit_siblings_ad, dark.ICON_PEOPLE)
            setIcon_line_(self.ui.lineEdit_name_full_ad, dark.ICON_USER)
            setIcon_line_(self.ui.lineEdit_name_initial_ad, dark.ICON_USER)

        # SUPERUSER ICON AND NAME
        dark.setSuperUserIconName(None, self.ui.label_super_icon)

        # DELETE BTN ICONS
        setIcon(self.ui.btn_delete_inter_1, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_1, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_pri, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_advan, dark.ICON_DELETE)

        setIcon(self.ui.btn_delete_inter_left_1, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_1, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_advan, dark.ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_pri, dark.ICON_DELETE)

        # ABOUT LABEL ICON
        self.ui.label_logo_adout.setText(dark.ICON_LABEL_TEXT)

        # ACTIVE AND LEFT LABEL TEXT
        self.ui.label_info_user_inter_1.setText(dark.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_1.setText(dark.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_pri.setText(dark.ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_advan.setText(
            dark.ACTIVE_LABEL_INFO_TEXT)

        self.ui.label_info_user_left_inter_1.setText(
            dark.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_1.setText(
            dark.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_pri.setText(
            dark.LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_advan.setText(
            dark.LAFT_LABEL_INFO_TEXT)

    # this allows to change the theme of window
    def setTheme(self):
        if self.ui.comboBox_theme_items.currentIndex() == 0:

            # Light theme thread
            thread_theme = Thread_Theme()
            thread_theme.connect_function.connect(self.connect_functiom_light)
            thread_theme.connect_theme_styleSheet.connect(
                self.setTheme_for_window_light)
            thread_theme.connect_setIcons.connect(
                self.setIcon_for_window_light)
            thread_theme.start()
            thread_theme.finished.connect(lambda: self.iconButtonPressed(True))
            thread_theme.exec()
            print("True")

        else:

            # Dark theme Thread
            thread_theme = Thread_Theme()
            thread_theme.connect_function.connect(self.connect_functiom_dark)
            thread_theme.connect_theme_styleSheet.connect(
                self.setTheme_for_window_dark)
            thread_theme.connect_setIcons.connect(self.setIcon_for_window_dark)
            thread_theme.start()
            thread_theme.finished.connect(lambda: self.iconButtonPressed(True))
            thread_theme.exec()
            print("False")

    # default theme for window startup

    def default_theme(self):
        self.setIcon_for_window_light()
        self.setTheme_for_window_light()
        self.connect_functiom_light()
        self.theme_button_pressed = True

    # Icon Button pressed Evenet Getter
    def iconButtonPressed(self, prim):
        self.theme_button_pressed = prim


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main_Window()
    main.show()
    app.exec_()
