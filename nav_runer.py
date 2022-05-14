from findup import *


# MAIN WINDOW WORKER
class UIFunctions(Main_Window):

    # Toggle Menu Button
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # Get Width
            twidth = self.ui.frame_top.width()
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # Set Max Width
            if width == 70 and twidth == 70:
                widthExtended = maxExtend
                self.ui.btn_Toggle.setStyleSheet(TOGGLE_BTN_CLOSE)
            else:
                widthExtended = standard
                self.ui.btn_Toggle.setStyleSheet(TOGGLE_BTN)

            # ANIMATION 1
            self.animation = QPropertyAnimation(
                self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

            # ANIMATION 2
            self.animationToggle = QPropertyAnimation(
                self.ui.frame_top, b"minimumWidth")
            self.animationToggle.setDuration(500)
            self.animationToggle.setStartValue(twidth)
            self.animationToggle.setEndValue(widthExtended)
            self.animationToggle.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animationToggle.start()

    def settingHiddenBar(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
        if enabel:

            standard = 200
            minExtend = 45

            standard_hidden_bar = 150
            minExtend_hidden_bar = 0
            current_hidden_height = 0

            icon = QIcon()

            if current_height == 200:
                heightExtended = minExtend
                heightExtended_hidden_bar = minExtend_hidden_bar
                icon.addFile(path_icon_normal)

            else:
                heightExtended = standard
                heightExtended_hidden_bar = standard_hidden_bar
                icon.addFile(path_icon_active)

            # Set Icon
            btn_obj.setIcon(icon)

            ##### Main Bar #####
            # Minimum Size for Main Frame
            self.animation_hidden = QPropertyAnimation(
                frame_obj, b"minimumHeight")
            self.animation_hidden.setDuration(500)
            self.animation_hidden.setStartValue(current_height)
            self.animation_hidden.setEndValue(heightExtended)
            self.animation_hidden.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden.start()

            #  Maximum Size Main Frame
            self.animation_hidden_two = QPropertyAnimation(
                frame_obj, b"maximumHeight")
            self.animation_hidden_two.setDuration(500)
            self.animation_hidden_two.setStartValue(current_height)
            self.animation_hidden_two.setEndValue(heightExtended)
            self.animation_hidden_two.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_two.start()

            ##### Hidden Bar #####
            # Minimum Size For Hidden Frame
            self.animation_hidden_frame = QPropertyAnimation(
                hidden_frame, b"minimumHeight")
            self.animation_hidden_frame.setDuration(500)
            self.animation_hidden_frame.setStartValue(current_hidden_height)
            self.animation_hidden_frame.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_frame.start()

            # Maximum Size For Hidden Frame
            self.animation_hidden_frame_two = QPropertyAnimation(
                hidden_frame, b"maximumHeight")
            self.animation_hidden_frame_two.setDuration(500)
            self.animation_hidden_frame_two.setStartValue(
                current_hidden_height)
            self.animation_hidden_frame_two.setEndValue(
                heightExtended_hidden_bar)
            self.animation_hidden_frame_two.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_frame_two.start()

    def settingHiddenBar_two(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
        if enabel:

            standard = 250
            minExtend = 45

            standard_hidden_bar = 200
            minExtend_hidden_bar = 0
            current_hidden_height = 0

            icon = QIcon()

            if current_height == 250:
                heightExtended = minExtend
                heightExtended_hidden_bar = minExtend_hidden_bar
                icon.addFile(path_icon_normal)

            else:
                heightExtended = standard
                heightExtended_hidden_bar = standard_hidden_bar
                icon.addFile(path_icon_active)

            # Set Icon
            btn_obj.setIcon(icon)

            ##### Main Bar #####
            # Minimum Size for Main Frame
            self.animation_hidden = QPropertyAnimation(
                frame_obj, b"minimumHeight")
            self.animation_hidden.setDuration(500)
            self.animation_hidden.setStartValue(current_height)
            self.animation_hidden.setEndValue(heightExtended)
            self.animation_hidden.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden.start()

            #  Maximum Size Main Frame
            self.animation_hidden_two = QPropertyAnimation(
                frame_obj, b"maximumHeight")
            self.animation_hidden_two.setDuration(500)
            self.animation_hidden_two.setStartValue(current_height)
            self.animation_hidden_two.setEndValue(heightExtended)
            self.animation_hidden_two.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_two.start()

            ##### Hidden Bar #####
            # Minimum Size For Hidden Frame
            self.animation_hidden_frame = QPropertyAnimation(
                hidden_frame, b"minimumHeight")
            self.animation_hidden_frame.setDuration(500)
            self.animation_hidden_frame.setStartValue(current_hidden_height)
            self.animation_hidden_frame.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_frame.start()

            # Maximum Size For Hidden Frame
            self.animation_hidden_frame_two = QPropertyAnimation(
                hidden_frame, b"maximumHeight")
            self.animation_hidden_frame_two.setDuration(500)
            self.animation_hidden_frame_two.setStartValue(
                current_hidden_height)
            self.animation_hidden_frame_two.setEndValue(
                heightExtended_hidden_bar)
            self.animation_hidden_frame_two.setEasingCurve(
                QtCore.QEasingCurve.InOutQuart)
            self.animation_hidden_frame_two.start()

    def userSideBar_toggle(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_super_user.width()
            maxExtend = maxWidth
            standard = 0

            if width == 0:
                widthExtended = maxExtend
                self.ui.btn_superuser.setStyleSheet(SUPERUSER_BTN_CLOSE)
            else:
                widthExtended = standard
                self.ui.btn_superuser.setStyleSheet(SUPERUSER_BTN)

            self.animation = QPropertyAnimation(
                self.ui.frame_super_user, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    # Get Courrent page set

    def home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.btn_lower.setStyleSheet(LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN_OPEN)
        self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN)

    def left(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_left)
        self.ui.btn_lower.setStyleSheet(LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN_OPEN)
        self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN)

    def search(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_search)
        self.ui.btn_lower.setStyleSheet(LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN_OPEN)
        self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN)

    def setting(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting)
        self.ui.btn_lower.setStyleSheet(LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN_OPEN)
        self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN)

    def analytics(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.analytics)
        self.ui.btn_lower.setStyleSheet(LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(INTER_BTN)
        self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN_OPEN)
        self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN)

    def current_page(self):
        if self.ui.stackedWidget.currentIndex() == 3:
            self.ui.btn_inter.setStyleSheet(INTER_BTN)
            self.ui.btn_lower.setStyleSheet(LOWER_BTN)
            self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN_OPEN)
            self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN)
            self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN)
            self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN)
            self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN)

    def addInter_page(self):
        self.ui.btn_inter.setStyleSheet(INTER_BTN_OPEN)
        self.ui.btn_lower.setStyleSheet(LOWER_BTN)
        self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN)

    def addLower_page(self):
        self.ui.btn_lower.setStyleSheet(LOWER_BTN_OPEN)
        self.ui.btn_inter.setStyleSheet(INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(ANALYTICS_PAGE_BTN)

    def callInter_window(self):
        UIFunctions.addInter_page(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_inter)

    def callLower_window(self):
        UIFunctions.addLower_page(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_students)

    
    def call_input_menu(self, obj):
        self.ui.stackedWidget.setCurrentWidget(obj)
