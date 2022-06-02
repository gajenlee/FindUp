from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.max_value = 100
        self.progress_color = 0xff79c6
        # Text
        self.enable_text = True
        self.font_family = "./src/font/segoeui.ttf"
        self.font_size = 15
        self.suffix = "%"
        self.text_color = 0xff79c6

        # Greeting Text
        self.label_greeting = None
        self.label_greeting_img = []

        # BG
        self.enable_bg = True
        self.bg_color = 0x44475a

        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)

    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 80))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()  # Render progress bar after change value

    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)

    def paintEvent(self, e):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)  # remove pixelated edges

        font = QFont()
        font.setFamily(self.font_family)
        font.setPointSize(self.font_size)
        font.setBold(True)
        paint.setFont(font)

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # PEN
        pen = QPen()
        pen.setWidth(self.progress_width)
        # Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # ENABLE BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        # CREATE ARC / CIRCULAR PROGRESS
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawArc(margin, margin, width,
                      height, -90 * 16, -value * 16)

        # CREATE TEXT
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter,
                           f"{self.value}{self.suffix}")

            if self.label_greeting != None:
                try:
                    pix = QPixmap(self.label_greeting_img[round(self.value/30)])
                    self.label_greeting.resize(pix.width(), pix.height())
                    self.label_greeting.setPixmap(pix)
                    self.label_greeting.setAlignment(Qt.AlignCenter)

                except Exception as p:
                    print(p)

        # END
        paint.end()

    def animation(self):
        self.ani = QPropertyAnimation(self.opac, b"opacity")
        self.ani.setDuration(3000)
        self.ani.setLoopCount(2)
        self.ani.setStartValue(.9)
        self.ani.setEndValue(.0)
        self.ani.start()


if __name__ == "__main__":
    progress = CircularProgress()
    progress.__init__()
