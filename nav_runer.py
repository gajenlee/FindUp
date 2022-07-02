from findup import *


# MAIN WINDOW WORKER
class UIFunctions(Main_Window):

    def thread_connecter_light(self, maxWidth, enable):

        thread_toggle = Thread_Toggle()
        thread_toggle.button_function.connect(
            lambda: UIFunctions.toggleMenu_light(self, maxWidth, enable))
        thread_toggle.start()
        thread_toggle.exec_()

    def thread_connecter_dark(self, maxWidth, enable):

        thread_toggle = Thread_Toggle()
        thread_toggle.button_function.connect(
            lambda: UIFunctions.toggleMenu_dark(self, maxWidth, enable))
        thread_toggle.start()
        thread_toggle.exec_()

    def userSide_toggle_light_connecter(self, maxWidth, enable):
        thread_toggle = Thread_Toggle()
        thread_toggle.button_function.connect(
            lambda: UIFunctions.userSideBar_toggle_light(self, maxWidth, enable))
        thread_toggle.start()
        thread_toggle.exec_()

    def userSide_toggle_dark_connecter(self, maxWidth, enable):
        thread_toggle = Thread_Toggle()
        thread_toggle.button_function.connect(
            lambda: UIFunctions.userSideBar_toggle_dark(self, maxWidth, enable))
        thread_toggle.start()
        thread_toggle.exec_()

    def settingHiddenBar_light_connecter(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
        thread_toggle = Thread_Toggle()
        thread_toggle.button_function.connect(lambda: UIFunctions.settingHiddenBar_light(
            self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active))
        thread_toggle.start()
        thread_toggle.exec_()

    def settingHiddenBar_dark_connecter(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
        thread_toggle = Thread_Toggle()
        thread_toggle.button_function.connect(lambda: UIFunctions.settingHiddenBar_dark(
            self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active))
        thread_toggle.start()
        thread_toggle.exec_()

    def settingHiddenBar_two_light_connecter(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
        thread_toggle = Thread_Toggle()
        thread_toggle.button_function.connect(lambda: UIFunctions.settingHiddenBar_light(
            self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active))
        thread_toggle.start()
        thread_toggle.exec_()

    def settingHiddenBar_two_dark_connecter(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
        thread_toggle = Thread_Toggle()
        thread_toggle.button_function.connect(lambda: UIFunctions.settingHiddenBar_dark(
            self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active))
        thread_toggle.start()
        thread_toggle.exec_()

    # Toggle Menu Button
    def toggleMenu_light(self, maxWidth, enable):
        if enable:

            # Get Width
            twidth = self.ui.frame_top.width()
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # Set Max Width
            if width == 70 and twidth == 70:
                widthExtended = maxExtend
                self.ui.btn_Toggle.setStyleSheet(light.TOGGLE_BTN_CLOSE)
            else:
                widthExtended = standard
                self.ui.btn_Toggle.setStyleSheet(light.TOGGLE_BTN)

            # ANIMATION 1
            self.animation = QPropertyAnimation(
                self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

            # ANIMATION 2
            self.animationToggle = QPropertyAnimation(
                self.ui.frame_top, b"minimumWidth")
            self.animationToggle.setDuration(500)
            self.animationToggle.setStartValue(twidth)
            self.animationToggle.setEndValue(widthExtended)
            self.animationToggle.setEasingCurve(QEasingCurve.InOutQuart)
            self.animationToggle.start()

    def settingHiddenBar_light(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
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
                QEasingCurve.InOutQuart)
            self.animation_hidden.start()

            #  Maximum Size Main Frame
            self.animation_hidden_two = QPropertyAnimation(
                frame_obj, b"maximumHeight")
            self.animation_hidden_two.setDuration(500)
            self.animation_hidden_two.setStartValue(current_height)
            self.animation_hidden_two.setEndValue(heightExtended)
            self.animation_hidden_two.setEasingCurve(
                QEasingCurve.InOutQuart)
            self.animation_hidden_two.start()

            ##### Hidden Bar #####
            # Minimum Size For Hidden Frame
            self.animation_hidden_frame = QPropertyAnimation(
                hidden_frame, b"minimumHeight")
            self.animation_hidden_frame.setDuration(500)
            self.animation_hidden_frame.setStartValue(current_hidden_height)
            self.animation_hidden_frame.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame.setEasingCurve(
                QEasingCurve.InOutQuart)
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
                QEasingCurve.InOutQuart)
            self.animation_hidden_frame_two.start()

    def settingHiddenBar_two_light(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
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
                QEasingCurve.InOutQuart)
            self.animation_hidden.start()

            #  Maximum Size Main Frame
            self.animation_hidden_two = QPropertyAnimation(
                frame_obj, b"maximumHeight")
            self.animation_hidden_two.setDuration(500)
            self.animation_hidden_two.setStartValue(current_height)
            self.animation_hidden_two.setEndValue(heightExtended)
            self.animation_hidden_two.setEasingCurve(
                QEasingCurve.InOutQuart)
            self.animation_hidden_two.start()

            ##### Hidden Bar #####
            # Minimum Size For Hidden Frame
            self.animation_hidden_frame = QPropertyAnimation(
                hidden_frame, b"minimumHeight")
            self.animation_hidden_frame.setDuration(500)
            self.animation_hidden_frame.setStartValue(current_hidden_height)
            self.animation_hidden_frame.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame.setEasingCurve(
                QEasingCurve.InOutQuart)
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
                QEasingCurve.InOutQuart)
            self.animation_hidden_frame_two.start()

    def userSideBar_toggle_light(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_super_user.width()
            maxExtend = maxWidth
            standard = 0

            if width == 0:
                widthExtended = maxExtend
                self.ui.btn_superuser.setStyleSheet(light.SUPERUSER_BTN_CLOSE)
            else:
                widthExtended = standard
                self.ui.btn_superuser.setStyleSheet(light.SUPERUSER_BTN)

            self.animation = QPropertyAnimation(
                self.ui.frame_super_user, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # Get Courrent page set

    def home_light(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN_OPEN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN)

    def left_light(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_left)
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN_OPEN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN)

    def search_light(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_search)
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN_OPEN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN)

    def setting_light(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting)
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN_OPEN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN)

    def analytics_light(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.analytics)
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN_OPEN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN)

    def current_page_light(self):
        if self.ui.stackedWidget.currentWidget() == self.ui.Home:
            UIFunctions.home_light(self)

        if self.ui.stackedWidget.currentWidget() == self.ui.page_left:
            UIFunctions.left_light(self)

        if self.ui.stackedWidget.currentWidget() == self.ui.page_search:
            UIFunctions.search_light(self)

        if self.ui.stackedWidget.currentWidget() == self.ui.page_setting:
            UIFunctions.setting_light(self)

        if self.ui.stackedWidget.currentWidget() == self.ui.analytics:
            UIFunctions.analytics_light(self)

    def addInter_page_light(self):
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN_OPEN)
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN)

    def addLower_page_light(self):
        self.ui.btn_lower.setStyleSheet(light.LOWER_BTN_OPEN)
        self.ui.btn_inter.setStyleSheet(light.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(light.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(light.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(light.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(light.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(light.ANALYTICS_PAGE_BTN)

    def callInter_window_light(self):
        UIFunctions.addInter_page_light(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inter_add)

    def callLower_window_light(self):
        UIFunctions.addLower_page_light(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_students)

    def call_input_menu(self, obj):
        self.ui.stackedWidget.setCurrentWidget(obj)
        self.button_shortcutKey_connecter()

    # dark theme window
    # Toggle Menu Button
    def toggleMenu_dark(self, maxWidth, enable):
        if enable:

            # Get Width
            twidth = self.ui.frame_top.width()
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # Set Max Width
            if width == 70 and twidth == 70:
                widthExtended = maxExtend
                self.ui.btn_Toggle.setStyleSheet(dark.TOGGLE_BTN_CLOSE)
            else:
                widthExtended = standard
                self.ui.btn_Toggle.setStyleSheet(dark.TOGGLE_BTN)

            # ANIMATION 1
            self.animation = QPropertyAnimation(
                self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

            # ANIMATION 2
            self.animationToggle = QPropertyAnimation(
                self.ui.frame_top, b"minimumWidth")
            self.animationToggle.setDuration(500)
            self.animationToggle.setStartValue(twidth)
            self.animationToggle.setEndValue(widthExtended)
            self.animationToggle.setEasingCurve(QEasingCurve.InOutQuart)
            self.animationToggle.start()

    def settingHiddenBar_dark(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
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
                QEasingCurve.InOutQuart)
            self.animation_hidden.start()

            #  Maximum Size Main Frame
            self.animation_hidden_two = QPropertyAnimation(
                frame_obj, b"maximumHeight")
            self.animation_hidden_two.setDuration(500)
            self.animation_hidden_two.setStartValue(current_height)
            self.animation_hidden_two.setEndValue(heightExtended)
            self.animation_hidden_two.setEasingCurve(
                QEasingCurve.InOutQuart)
            self.animation_hidden_two.start()

            ##### Hidden Bar #####
            # Minimum Size For Hidden Frame
            self.animation_hidden_frame = QPropertyAnimation(
                hidden_frame, b"minimumHeight")
            self.animation_hidden_frame.setDuration(500)
            self.animation_hidden_frame.setStartValue(current_hidden_height)
            self.animation_hidden_frame.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame.setEasingCurve(
                QEasingCurve.InOutQuart)
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
                QEasingCurve.InOutQuart)
            self.animation_hidden_frame_two.start()

    def settingHiddenBar_two_dark(self,  current_height, frame_obj, hidden_frame,  enabel, btn_obj, path_icon_normal, path_icon_active):
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
                QEasingCurve.InOutQuart)
            self.animation_hidden.start()

            #  Maximum Size Main Frame
            self.animation_hidden_two = QPropertyAnimation(
                frame_obj, b"maximumHeight")
            self.animation_hidden_two.setDuration(500)
            self.animation_hidden_two.setStartValue(current_height)
            self.animation_hidden_two.setEndValue(heightExtended)
            self.animation_hidden_two.setEasingCurve(
                QEasingCurve.InOutQuart)
            self.animation_hidden_two.start()

            ##### Hidden Bar #####
            # Minimum Size For Hidden Frame
            self.animation_hidden_frame = QPropertyAnimation(
                hidden_frame, b"minimumHeight")
            self.animation_hidden_frame.setDuration(500)
            self.animation_hidden_frame.setStartValue(current_hidden_height)
            self.animation_hidden_frame.setEndValue(heightExtended_hidden_bar)
            self.animation_hidden_frame.setEasingCurve(
                QEasingCurve.InOutQuart)
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
                QEasingCurve.InOutQuart)
            self.animation_hidden_frame_two.start()

    def userSideBar_toggle_dark(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_super_user.width()
            maxExtend = maxWidth
            standard = 0

            if width == 0:
                widthExtended = maxExtend
                self.ui.btn_superuser.setStyleSheet(dark.SUPERUSER_BTN_CLOSE)
            else:
                widthExtended = standard
                self.ui.btn_superuser.setStyleSheet(dark.SUPERUSER_BTN)

            self.animation = QPropertyAnimation(
                self.ui.frame_super_user, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # Get Courrent page set

    def home_dark(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN_OPEN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN)

    def left_dark(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_left)
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN_OPEN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN)

    def search_dark(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_search)
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN_OPEN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN)

    def setting_dark(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting)
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN_OPEN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN)

    def analytics_dark(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.analytics)
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN)
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN_OPEN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN)

    def current_page_dark(self):
        if self.ui.stackedWidget.currentWidget() == self.ui.Home:
            UIFunctions.home_dark(self)

        if self.ui.stackedWidget.currentWidget() == self.ui.page_left:
            UIFunctions.left_dark(self)

        if self.ui.stackedWidget.currentWidget() == self.ui.page_search:
            UIFunctions.search_dark(self)

        if self.ui.stackedWidget.currentWidget() == self.ui.page_setting:
            UIFunctions.setting_dark(self)

        if self.ui.stackedWidget.currentWidget() == self.ui.analytics:
            UIFunctions.analytics_dark(self)

    def addInter_page_dark(self):
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN_OPEN)
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN)

    def addLower_page_dark(self):
        self.ui.btn_lower.setStyleSheet(dark.LOWER_BTN_OPEN)
        self.ui.btn_inter.setStyleSheet(dark.INTER_BTN)
        self.ui.btn_page_home.setStyleSheet(dark.HOME_PAGE_BTN)
        self.ui.btn_page_left.setStyleSheet(dark.HOME_LEFT_PAGE_BTN)
        self.ui.btn_page_search.setStyleSheet(dark.SEARCH_PAGE_BRN)
        self.ui.btn_setting.setStyleSheet(dark.SETTING_PAGE_BTN)
        self.ui.btn_page_analytics.setStyleSheet(dark.ANALYTICS_PAGE_BTN)

    def callInter_window_dark(self):
        UIFunctions.addInter_page_dark(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inter_add)

    def callLower_window_dark(self):
        UIFunctions.addLower_page_dark(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_students)
