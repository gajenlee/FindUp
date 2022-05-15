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
from style.dark import *


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
    def __init__(self, parent=None, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setIcon_for_window()
        # self.setTheme_for_window()
        self.connect_functiom()

    def connect_functiom(self):

        # Toggle Burguer Menu
        self.ui.btn_Toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 200, True))

        # Setting Bar Animation
        self.ui.btn_hidden_username_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar(self,  self.ui.frame_user_name_changer.height(
        ), self.ui.frame_user_name_changer, self.ui.frame_name_changer_content_page, True, self.ui.btn_hidden_username_bar, BTN_HIDDEN_ICON, BTN_OPENED_ICON))
        self.ui.btn_hidden_email_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar(self,  self.ui.frame_email_changer.height(
        ), self.ui.frame_email_changer, self.ui.frame_email_changer_content_bar, True, self.ui.btn_hidden_email_bar, BTN_HIDDEN_ICON, BTN_OPENED_ICON))
        self.ui.btn_hidden_contact_number_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar(self,  self.ui.frame_contect_number_changer.height(
        ), self.ui.frame_contect_number_changer, self.ui.frame_contect_number_changer_content_bar, True, self.ui.btn_hidden_contact_number_bar, BTN_HIDDEN_ICON, BTN_OPENED_ICON))
        self.ui.btn_hidden_passowd_changer_bar.clicked.connect(lambda: UIFunctions.settingHiddenBar(self,  self.ui.frame_password_changer.height(
        ), self.ui.frame_password_changer, self.ui.frame_password_changer_content_bar, True, self.ui.btn_hidden_passowd_changer_bar, BTN_HIDDEN_ICON, BTN_OPENED_ICON))

        self.ui.btn_hidden_options.clicked.connect(lambda: UIFunctions.settingHiddenBar_two(self,  self.ui.frame_more_options.height(
        ), self.ui.frame_more_options, self.ui.frame_more_options_contect_bar, True, self.ui.btn_hidden_options, BTN_HIDDEN_ICON, BTN_OPENED_ICON))
        self.ui.btn_hidden_adout.clicked.connect(lambda: UIFunctions.settingHiddenBar_two(self, self.ui.frame_adout.height(
        ), self.ui.frame_adout, self.ui.frame_content_adout, True, self.ui.btn_hidden_adout, BTN_HIDDEN_ICON, BTN_OPENED_ICON))

        # SUPER USER BTN
        self.ui.btn_superuser.clicked.connect(
            lambda: UIFunctions.userSideBar_toggle(self, 300, True))

        # BUTTONE CONNECTER
        UIFunctions.current_page(self)

        self.ui.btn_page_home.clicked.connect(lambda: UIFunctions.home(self))
        self.ui.btn_page_left.clicked.connect(lambda: UIFunctions.left(self))
        self.ui.btn_page_search.clicked.connect(
            lambda: UIFunctions.search(self))
        self.ui.btn_setting.clicked.connect(lambda: UIFunctions.setting(self))
        self.ui.btn_page_analytics.clicked.connect(
            lambda: UIFunctions.analytics(self))
        self.ui.btn_go_home.clicked.connect(lambda: UIFunctions.home(self))
        self.ui.btn_go_home_lower.clicked.connect(
            lambda: UIFunctions.home(self))

        # Super User Btn
        self.ui.btn_edit_setting.clicked.connect(
            lambda: UIFunctions.setting(self))

        # Inter and Lower Btn
        self.ui.btn_inter.clicked.connect(
            lambda: UIFunctions.callInter_window(self)
        )
        self.ui.btn_lower.clicked.connect(
            lambda: UIFunctions.callLower_window(self)
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

    def setTheme_for_window(self):
        self.ui.scrollArea_2.setStyleSheet(SCROLLAREA)
        self.ui.scrollArea.setStyleSheet(SCROLLAREA)
        self.ui.scrollArea_resalt.setStyleSheet(SCROLLAREA)
        self.ui.scrollArea_3.setStyleSheet(SCROLLAREA)
        self.ui.scrollArea_content.setStyleSheet(SCROLLAREA)
        self.ui.scrollArea_4.setStyleSheet(SCROLLAREA)
        self.ui.scrollArea_add_info.setStyleSheet(SCROLLAREA)

        self.ui.comboBox_stream.setStyleSheet(COMBO_BOX)
        self.ui.comboBox_stream_primary.setStyleSheet(COMBO_BOX)
        self.ui.lineEdit_level_ad.setStyleSheet(COMBO_BOX)
        self.ui.lineEdit_level_lower.setStyleSheet(COMBO_BOX)

        self.setStyleSheet(MAIN_WINDOW_BACKGROUND)
        self.ui.btn_Toggle.setStyleSheet(TOGGLE_BTN)
        self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN)
        self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN)
        self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN)
        self.ui.TopBar.setStyleSheet(TOP_BAR_BACKGROUND)
        self.ui.frame_top.setStyleSheet(TOP_FRAME_BACKGROUND)
        self.ui.frame_return_bar.setStyleSheet(FRAME_RETURN_BAR)
        self.ui.btn_inter.setStyleSheet(INTER_BTN)
        self.ui.btn_lower.setStyleSheet(LOWER_BTN)
        self.ui.frame_backup.setStyleSheet(FRAME_BACKUP)
        self.ui.btn_superuser.setStyleSheet(SUPERUSER_BTN)
        self.ui.frame_left_menu.setStyleSheet(FRAME_LEFT_MENU)
        self.ui.frame_top_menus.setStyleSheet(FRAME_TOP_MENU)
        self.ui.frame_page.setStyleSheet(FRAME_PAGE)
        self.ui.frame_2.setStyleSheet(FRAME_2)
        self.ui.btn_primary.setStyleSheet(PRIMARY_BTN)
        self.ui.btn_ordinary.setStyleSheet(ORDNARY_BTN)
        self.ui.btn_advanced.setStyleSheet(ADVANCED_BTN)
        self.ui.frame_main_content_for_primary.setStyleSheet(
            FRAME_MAIN_CONTENT_FOR_PRIMARY)
        self.ui.label_icon_primary.setStyleSheet(LABEL_ICON_PRIMARY)
        self.ui.label_show_roll_primary.setStyleSheet(LABEL_SHOW_ROLL_PRIMARY)
        self.ui.frame_coments_ad_2.setStyleSheet(FRAME_CONTENT_ADVANCED_2)

        self.ui.dateEdit_date_of_birth_primary.setStyleSheet(DATE_EDIT)
        self.ui.dateEdit_date_of_birth_ad.setStyleSheet(DATE_EDIT)
        self.ui.dateEdit_data_of_birth.setStyleSheet(DATE_EDIT)

        self.ui.dateEdit_DOB.setStyleSheet(DATE_EDIT)
        self.ui.dateEdit_first_appointment_date.setStyleSheet(DATE_EDIT)
        self.ui.dateEdit_appointment_date.setStyleSheet(DATE_EDIT)

        self.ui.lineEdit_full_name.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit__name_initial.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_inc_no.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_office_no.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_personal_contact.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_WOP_no.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_agrakara_no.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_spouse_name.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_contact_no_offiec_home.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_no_of_children.setStyleSheet(LINE_EDIT)

        self.ui.textEdit_permanent_address.setStyleSheet(TEXT_EDIT)
        self.ui.textEdit_working_address.setStyleSheet(TEXT_EDIT)
        self.ui.textEdit_other.setStyleSheet(TEXT_EDIT)
        self.ui.textEdit_nature_appointment.setStyleSheet(TEXT_EDIT)
        self.ui.textEdit_appointmen_school.setStyleSheet(TEXT_EDIT)

        self.ui.radioButton_married.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_unmarried.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_male.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_female.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_other.setStyleSheet(RASIO_BUTTON)

        self.ui.lineEdit_contect_primary.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_contect_ad.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_contect_lower.setStyleSheet(LINE_EDIT)

        self.ui.label_civil_text.setStyleSheet(LABEL_COLOR)
        self.ui.label_gender_text.setStyleSheet(LABEL_COLOR)
        self.ui.label_date_app_to_school_text.setStyleSheet(LABEL_COLOR)
        self.ui.label_appointment_data_text.setStyleSheet(LABEL_COLOR)
        self.ui.label_DOB_text.setStyleSheet(LABEL_COLOR)

        self.ui.groupBox_civil.setStyleSheet(GROUP)
        self.ui.groupBox_gender.setStyleSheet(GROUP)

        self.ui.lineEdit_address_ad.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_address_primary.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_address_lower.setStyleSheet(LINE_EDIT)

        self.ui.lineEdit_name_ad.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_name_lower.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_name_primary.setStyleSheet(LINE_EDIT)

        self.ui.lineEdit_email_ad.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_email_lower.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_email_primary.setStyleSheet(LINE_EDIT)

        self.ui.lineEdit_father.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_father_ad.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_father_primary.setStyleSheet(LINE_EDIT)

        self.ui.lineEdit_mather.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_mather_ad.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_mather_primary.setStyleSheet(LINE_EDIT)

        self.ui.lineEdit_religion.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_religion_ad.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_religion_primary.setStyleSheet(LINE_EDIT)

        self.ui.lineEdit_registration_primary.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_registration_ad.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_ragis_number.setStyleSheet(LINE_EDIT)

        self.ui.lineEdit_username_change_input.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_change_email_input.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_contact_number_input.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_passord_input.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_rollSearch.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_nameSearch.setStyleSheet(LINE_EDIT)
        self.ui.lineEdit_repassword_input.setStyleSheet(LINE_EDIT)

        self.ui.label_inforem_date_of_birth_ad_2.setStyleSheet(
            LABEL_INFO_DOB_ADVANCED_2)

        self.ui.radioButton_male_primary.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_female_primary.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_other_primary.setStyleSheet(RASIO_BUTTON)

        self.ui.radioButton_male_ad.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_female_ad.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_other_ad.setStyleSheet(RASIO_BUTTON)

        self.ui.radioButton_male_lower.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_female_lower.setStyleSheet(RASIO_BUTTON)
        self.ui.radioButton_other_lower.setStyleSheet(RASIO_BUTTON)

        self.ui.btn_addLower_primary.setStyleSheet(ADDLOWER_PRIMARY_BTN)
        self.ui.btn_go_home_primary.setStyleSheet(GOHOME_PRIMARY_BTN)

        self.ui.frame_main_content_for_advance.setStyleSheet(
            FRAME_MAIN_CONTENT_FOR_ADVANCED)

        self.ui.label_icon_.setStyleSheet(LABEL_ICON_)

        self.ui.frame_coments_ad.setStyleSheet(FRAME_CONTENT_ADVANCED)

        self.ui.label_inforem_date_of_birth_ad.setStyleSheet(
            LABEL_INFO_DOB_ADVANCED)

        self.ui.label_show_roll_ad.setStyleSheet(LABEL_SHOW_ROLL_ADVANCED)

        self.ui.btn_addLower_adv.setStyleSheet(ADDLOWER_ADVANCED_BTN)
        self.ui.btn_go_home_ad.setStyleSheet(GOHOME_ADVANCED_BTN)

        self.ui.frame_main_home_bar.setStyleSheet(FRAME_MAIN_HOME_BAR)

        self.ui.page_content_Input.setStyleSheet(PAGE_CONTECT)
        self.ui.widget_inter_1.setStyleSheet(WIDGET_INTER_1)
        self.ui.label_info_Inter_face.setStyleSheet(LABEL_INFO_INTER_FACE)
        self.ui.label_info_Inter_1.setStyleSheet(LABEL_INFO_INTER_1)
        self.ui.frame_inter_delet_bar_1.setStyleSheet(FRAME_INTER_DELETE_BAR_1)
        self.ui.label_info_user_inter_1.setStyleSheet(LABEL_INFO_INTER_USER_1)
        self.ui.btn_delete_inter_1.setStyleSheet(DELETE_INTER_BTN_1)

        self.ui.widget_lower_1.setStyleSheet(WIDGET_LOWER_1)
        self.ui.label_info_lower_1.setStyleSheet(LABEL_INFO_LOWER_1)
        self.ui.frame_inter_delet_bar_3.setStyleSheet(FRAME_LOWER_DELETE_BAR_1)
        self.ui.label_info_user_lower_1.setStyleSheet(LABEL_INFO_LOWER_USER_1)
        self.ui.btn_delete_lower_1.setStyleSheet(DELETE_LOWER_BTN_1)

        self.ui.widget_lower_pri.setStyleSheet(WIDGET_PRIMARY_1)
        self.ui.label_info_lower_pri.setStyleSheet(LABEL_INFO_PRIMARY_1)
        self.ui.frame_inter_delet_bar_pri.setStyleSheet(
            FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.label_info_user_lower_pri.setStyleSheet(
            LABEL_INFO_PRIMARY_USER_1)
        self.ui.btn_delete_lower_pri.setStyleSheet(DELETE_PRIMARY_BTN_1)

        self.ui.widget_lower_advan.setStyleSheet(WIDGET_ADVANCED_1)
        self.ui.label_info_lower_advan.setStyleSheet(LABEL_INFO_ADVANCED_1)
        self.ui.frame_inter_delet_bar_advan.setStyleSheet(
            FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.label_info_user_lower_advan.setStyleSheet(
            LABEL_INFO_ADVANCED_USER_1)
        self.ui.btn_delete_lower_advan.setStyleSheet(DELETE_ADVANCED_BTN_1)

        self.ui.frame_main_left_bar.setStyleSheet(FRAME_MAIN_LEFT_BAR)
        self.ui.scrollAreaWidgetContents.setStyleSheet(SCROLLAREA_WIDGET)
        self.ui.widget_inter_left_1.setStyleSheet(WIDGET_INTER_1)
        self.ui.info_inter_left_1.setStyleSheet(LABEL_INFO_INTER_1)
        self.ui.frame_inter_left_btns_bar_1.setStyleSheet(
            FRAME_INTER_DELETE_BAR_1)
        self.ui.label_info_user_left_inter_1.setStyleSheet(
            LABEL_INFO_INTER_USER_1)
        self.ui.btn_delete_inter_left_1.setStyleSheet(DELETE_INTER_BTN_1)

        self.ui.widget_lower_left_1.setStyleSheet(WIDGET_LOWER_1)
        self.ui.info_lower_1.setStyleSheet(LABEL_INFO_LOWER_1)
        self.ui.frame_lower_left_btns_bar_1.setStyleSheet(
            FRAME_LOWER_DELETE_BAR_1)
        self.ui.label_info_user_left_lower_1.setStyleSheet(
            LABEL_INFO_LOWER_USER_1)
        self.ui.btn_delete_lower_left_1.setStyleSheet(DELETE_LOWER_BTN_1)

        self.ui.widget_lower_left_pri.setStyleSheet(WIDGET_PRIMARY_1)
        self.ui.info_lower_left_pri.setStyleSheet(LABEL_INFO_PRIMARY_1)
        self.ui.frame_lower_btns_bar_pri.setStyleSheet(
            FRAME_PRIMARY_DELETE_BAR_1)
        self.ui.label_info_user_left_lower_pri.setStyleSheet(
            LABEL_INFO_PRIMARY_USER_1)
        self.ui.btn_delete_lower_left_pri.setStyleSheet(DELETE_PRIMARY_BTN_1)

        self.ui.widget_lower_left_advan.setStyleSheet(WIDGET_ADVANCED_1)
        self.ui.info_lower_left_advan.setStyleSheet(LABEL_INFO_ADVANCED_1)
        self.ui.frame_lower_btns_bar_advan.setStyleSheet(
            FRAME_ADVANCED_DELETE_BAR_1)
        self.ui.label_info_user_left_lower_advan.setStyleSheet(
            LABEL_INFO_ADVANCED_USER_1)
        self.ui.btn_delete_lower_left_advan.setStyleSheet(
            DELETE_ADVANCED_BTN_1)

        self.ui.frame_main_search_bar.setStyleSheet(FRAME_MAIN_SEARCH_BAR)
        self.ui.frame_searching_main.setStyleSheet(FRAME_SEARCHING_MAIN)
        self.ui.frame_title_search.setStyleSheet(FRAME_TITLE_SEARCH)
        self.ui.frame_search_bar_itmes.setStyleSheet(FRAME_SEARCH_BAR_ITEMS)
        self.ui.btn_nameSearch.setStyleSheet(SEARCH_BAR_BTN)
        self.ui.btn_rollSearch.setStyleSheet(SEARCH_BAR_BTN)

        self.ui.frame.setStyleSheet(SETTING_FRAME)
        self.ui.label.setStyleSheet(SETTING_LABEL)
        self.ui.frame_user_name_changer.setStyleSheet(SETTING_NAME_CHANGER)
        self.ui.label_username_title.setStyleSheet(SETTING_USER_NAME_TITLE)
        self.ui.btn_hidden_username_bar.setStyleSheet(
            SETTING_USERNAME_HIDDEN_BTN)
        self.ui.label_show_current_username.setStyleSheet(
            SETTING_LABEL_SHOW_CURRENT_USERNAME)
        self.ui.btn_save_username.setStyleSheet(SETTING_SAVE_USERNAME_BTN)
        self.ui.frame_more_options.setStyleSheet(SETTING_FRAME_MORE_OP)
        self.ui.label_title.setStyleSheet(SETTING_LABEL_TITLE)
        self.ui.btn_hidden_options.setStyleSheet(SETTING_HIDDEN_BTN_OP)
        self.ui.label_reload_info.setStyleSheet(SETTING_LABEL_RELOAD)
        self.ui.btn_reload.setStyleSheet(SETTING_RELOAD_BTN)
        self.ui.label_reset_info.setStyleSheet(SETTING_LABEL_INFO_RESET)
        self.ui.btn_reset.setStyleSheet(SETTING_RESET_BTN)
        self.ui.btn_logout.setStyleSheet(SETTING_LOGOUT_BTN)
        self.ui.frame_email_changer.setStyleSheet(SETTING_FRAME_EMAIL_CHANGER)
        self.ui.label_change_email_title.setStyleSheet(
            SETTING_LABEL_CHANGE_EMAIL_TITLE)
        self.ui.btn_hidden_email_bar.setStyleSheet(SETTING_HIDDEN_EMAIL_BTN)
        self.ui.label_current_email.setStyleSheet(SETTING_LABEL_CURRENT_EMAIL)
        self.ui.btn_save_change_email.setStyleSheet(SETTING_SAVE_EMAIL_BTN)
        self.ui.frame_contect_number_changer.setStyleSheet(
            SETTING_FRAME_CONTECT_NUM_CHANGER)
        self.ui.label_change_contact_number_title.setStyleSheet(
            SETTING_LABEL_CHANGE_CONTECT_NUM_TITLE)
        self.ui.btn_hidden_contact_number_bar.setStyleSheet(
            SETTING_HIDDEN_BTN_CONTECT)
        self.ui.label_show_current_contact_number.setStyleSheet(
            SETTING_SHOW_CURRENT_CONTECT_NUM)
        self.ui.btn_save_contact_number.setStyleSheet(
            SETTING_SAVE_CONTECT_NUM_BTN)
        self.ui.frame_password_changer.setStyleSheet(
            SETTING_FRAME_PASSWORD_CHANGER)
        self.ui.label_change_password_title.setStyleSheet(
            SETTING_LABEL_CHANGE_PASSWORD_TITLE)
        self.ui.btn_hidden_passowd_changer_bar.setStyleSheet(
            SETTING_PASSWORD_CHANGER_BTN)
        self.ui.btn_save_password.setStyleSheet(SETTING_SAVE_PASSWORD_BTN)
        self.ui.frame_main_inter_info.setStyleSheet(FRMAE_MAIN_INTER_INFO)
        self.ui.label_icon_inter.setStyleSheet(LABEL_ICON_INTER)
        self.ui.btn_upload_image.setStyleSheet(UPLOAD_IMAGE_BTN)
        self.ui.label_show_roll_number.setStyleSheet(LABEL_SHOW_ROLL_INTER)
        self.ui.btn_addInter.setStyleSheet(ADDINTER_BTN)
        self.ui.btn_go_home.setStyleSheet(GOHOME_INTER_BTN)
        self.ui.btn_upload_image_lower.setStyleSheet(UPLOAD_IMAGE_BTN)
        self.ui.btn_upload_image_primary.setStyleSheet(UPLOAD_IMAGE_BTN)
        self.ui.btn_upload_image_advanced.setStyleSheet(UPLOAD_IMAGE_BTN)

        self.ui.frame_content.setStyleSheet(ANALYTICS_FRAME_CONTENT)
        self.ui.label_inter_head.setStyleSheet(ANALYTICS_LABEL_INTER_HEAD)
        self.ui.frame_inter.setStyleSheet(ANALYTICS_FRAME_INTER)
        self.ui.label_lower_head.setStyleSheet(ANALYTICS_LABEL_LOWER_HEAD)
        self.ui.frame_lower.setStyleSheet(ANALYTICS_FRAME_LOWER)
        self.ui.frame_lower_prim.setStyleSheet(ANALYTICS_FRAME_PRIM)
        self.ui.frame_lower_advan.setStyleSheet(ANALYTICS_FRAME_ADVAN)

        self.ui.frame_main_lower_info.setStyleSheet(FRAME_MAIN_LOWER_INFO)
        self.ui.label_icon_lower.setStyleSheet(LABEL_ICON_LOWER)
        self.ui.label_show_roll_number_lower.setStyleSheet(
            LABEL_SHOW_ROLL_LOWER)
        self.ui.btn_addlower.setStyleSheet(ADDLOWER_LOWER_BTN)
        self.ui.btn_go_home_lower.setStyleSheet(GOHOME_LOWER_BTN)

        self.ui.label_advanced_level_12.setStyleSheet(LABEL_ADVANCED_LEVEL_12)
        self.ui.frame_advanced_level_12.setStyleSheet(FRAME_ADVANCED_LEVEL_12)
        self.ui.label_advanced_level_13.setStyleSheet(LABEL_ADVANCED_LEVEL_13)
        self.ui.frame_advanced_level_13.setStyleSheet(FRAME_ADVANCED_LEVEL_13)
        self.ui.frame_super_user.setStyleSheet(FRAME_SUPERUSER)
        self.ui.label_super_icon.setStyleSheet(LABEL_SUPERUSER_ICON)
        self.ui.label_infor_super.setStyleSheet(LABEL_INFO_SUPERUSER)
        self.ui.btn_edit_setting.setStyleSheet(EDIT_SETTING_BTN)
        self.ui.frame_adout.setStyleSheet(FRAME_ABOUT)
        self.ui.label_info_adout.setStyleSheet(LABEL_INFO_ABOUT)

        self.ui.btn_hidden_adout.setStyleSheet(HIDDEN_ABOUT_BTN)
        self.ui.frame_content_adout.setStyleSheet(FRAME_CONTENT_ABOUT)
        self.ui.label_more_info_adout.setStyleSheet(LABEL_MORE_ABOUT)

    def setIcon_for_window(self):
        self.setWindowTitle("Findup")
        icon = QIcon()
        icon.addFile(MAIN_WINDOW_TITLE_ICON)
        self.setWindowIcon(icon)

        self.ui.label_icon_inter.setText(LABEL_ICON_INTER_TEXT)
        self.ui.label_icon_lower.setText(LABEL_ICON_LOWER_TEXT)
        self.ui.label_dateofbirth_info.setText(LABEL_DOB_TEXT)
        self.ui.label.setText(LABEL_EDIT_TEXT)

        self.ui.label_icon_.setText(LABEL_ICON_LOWER_TEXT)

        self.ui.label_inforem_date_of_birth_ad.setText(LABEL_DOB_TEXT)
        self.ui.label_icon_primary.setText(LABEL_ICON_LOWER_TEXT)
        self.ui.label_inforem_date_of_birth_ad_2.setText(LABEL_DOB_TEXT)

        # SET ICON FUNCTION

        def setIcon(widget, path,):
            icon = QIcon()
            icon.addFile(path)
            widget.setIcon(icon)

        def setIcon_line(widget, path,):
            icon = QIcon()
            icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
            widget.addAction(icon, QLineEdit.LeadingPosition)

        # SUPER USER ICON
        setIcon(self.ui.btn_superuser, ICON_USER)
        setIcon(self.ui.btn_edit_setting, ICON_GO)

        # USER ADD ICONS
        setIcon(self.ui.btn_addInter, ICON_ADD_USER)
        setIcon(self.ui.btn_addlower, ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_adv, ICON_ADD_USER)
        setIcon(self.ui.btn_addLower_primary, ICON_ADD_USER)

        setIcon(self.ui.btn_go_home, ICON_GO)
        setIcon(self.ui.btn_go_home_lower, ICON_GO)
        setIcon(self.ui.btn_go_home_primary, ICON_GO)
        setIcon(self.ui.btn_go_home_ad, ICON_GO)

        # SETTING BAR HIDDEN ICON BARS
        setIcon(self.ui.btn_hidden_username_bar, BTN_OPENED_ICON)
        setIcon(self.ui.btn_hidden_email_bar, BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_contact_number_bar, BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_passowd_changer_bar, BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_options, BTN_HIDDEN_ICON)
        setIcon(self.ui.btn_hidden_adout, BTN_HIDDEN_ICON)

        # SEARCH BAR ICON
        setIcon(self.ui.btn_nameSearch, ICON_SEARCH)
        setIcon(self.ui.btn_rollSearch, ICON_SEARCH)

        # ADD INTER USER PAGE ICONS

        # ADD LOWER USER PAGE ICONS
        setIcon_line(self.ui.lineEdit_name_lower, ICON_USER)
        setIcon_line(self.ui.lineEdit_address_lower, ICON_LOCATION)
        setIcon_line(self.ui.lineEdit_father, ICON_PEOPLE)
        setIcon_line(self.ui.lineEdit_mather, ICON_PEOPLE)
        setIcon_line(self.ui.lineEdit_contect_lower, ICON_PHONE)
        setIcon_line(self.ui.lineEdit_ragis_number, ICON_RIG_NUM)
        setIcon_line(self.ui.lineEdit_email_lower, ICON_AT)
        setIcon_line(self.ui.lineEdit_religion, ICON_RIL)

        # ADD LOWER USER PAGE ICONS FOR ADVANS
        setIcon_line(self.ui.lineEdit_name_ad, ICON_USER)
        setIcon_line(self.ui.lineEdit_address_ad, ICON_LOCATION)
        setIcon_line(self.ui.lineEdit_father_ad, ICON_PEOPLE)
        setIcon_line(self.ui.lineEdit_mather_ad, ICON_PEOPLE)
        setIcon_line(self.ui.lineEdit_contect_ad, ICON_PHONE)
        setIcon_line(self.ui.lineEdit_registration_ad, ICON_RIG_NUM)
        setIcon_line(self.ui.lineEdit_email_ad, ICON_AT)
        setIcon_line(self.ui.lineEdit_religion_ad, ICON_RIL)

        # ADD LOWER USER PAGE ICONS FOR PRIMARY
        setIcon_line(self.ui.lineEdit_name_primary, ICON_USER)
        setIcon_line(self.ui.lineEdit_address_primary, ICON_LOCATION)
        setIcon_line(self.ui.lineEdit_father_primary, ICON_PEOPLE)
        setIcon_line(self.ui.lineEdit_mather_primary, ICON_PEOPLE)
        setIcon_line(self.ui.lineEdit_contect_primary, ICON_PHONE)
        setIcon_line(self.ui.lineEdit_registration_primary, ICON_RIG_NUM)
        setIcon_line(self.ui.lineEdit_email_primary, ICON_AT)
        setIcon_line(self.ui.lineEdit_religion_primary, ICON_RIL)

        # SUPERUSER ICON AND NAME
        setSuperUserIconName(None, self.ui.label_super_icon)

        # DELETE BTN ICONS
        setIcon(self.ui.btn_delete_inter_1, ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_1, ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_pri, ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_advan, ICON_DELETE)

        setIcon(self.ui.btn_delete_inter_left_1, ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_1, ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_advan, ICON_DELETE)
        setIcon(self.ui.btn_delete_lower_left_pri, ICON_DELETE)

        # ABOUT LABEL ICON
        self.ui.label_logo_adout.setText(ICON_LABEL_TEXT)

        # ACTIVE AND LEFT LABEL TEXT
        self.ui.label_info_user_inter_1.setText(ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_1.setText(ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_pri.setText(ACTIVE_LABEL_INFO_TEXT)
        self.ui.label_info_user_lower_advan.setText(ACTIVE_LABEL_INFO_TEXT)

        self.ui.label_info_user_left_inter_1.setText(LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_1.setText(LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_pri.setText(LAFT_LABEL_INFO_TEXT)
        self.ui.label_info_user_left_lower_advan.setText(LAFT_LABEL_INFO_TEXT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main_Window()
    main.show()
    app.exec_()
