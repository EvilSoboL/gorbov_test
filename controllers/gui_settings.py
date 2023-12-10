from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import *
from PyQt5.QtCore import QPropertyAnimation

Black = "rgba(20, 20, 20, 1)"
Black_initial = QColor(20, 20, 20)
Red = "rgba(201, 44, 44, 1)"
Red_initial = QColor(201, 44, 44)
White = "rgba(255, 255, 255, 1)"

black_default = """
background-color: rgba(20, 20, 20, 1);
max-height: 60px;
max-width: 60px;
margin: 0px;
padding: 15px;
color: white;
font-size: 40px;
border: 3px solid rgba(20, 20, 20, 1);
border-radius: 15px;
"""


red_default = """
background-color: rgba(201, 44, 44, 1);
max-height: 60px;
max-width: 60px;
margin: 0px;
padding: 15px;
color: white;
font-size: 40px;
border: 3px solid rgba(201, 44, 44, 1);
border-radius: 15px;
"""

menu_buttons = """QPushButton {
            background-color: white;
            min-height: 30px;
            min-width: 150px;
            color: rgba(20, 20, 20, 1);
            border-radius: 5px;
            font-weight: 900;
            }
            QPushButton::hover {
            background-color: rgba(150, 150, 150, 1);
            }
            QPushButton::pressed {
            border: 2px solid rgba(110, 110, 110, 1);
            }
            QPushButton::disabled {
            background-color: rgba(110, 110, 110, 1);
            }"""

menu_lines = """QLineEdit{
            background-color: white;
            min-height: 30px;
            max-width: 300px;
            color: rgba(20, 20, 20, 1);
            border-radius: 5px;
            font-weight: 900;
            }
            QLineEdit::hover {
            background-color: rgba(150, 150, 150, 1);
            }
            QLineEdit::pressed {
            border: 2px solid rgba(110, 110, 110, 1);
            }
            QLineEdit::disabled {
            background-color: rgba(110, 110, 110, 1);
            }"""

chose_line = """QComboBox{
            background-color: white;
            min-height: 30px;
            max-width: 300px;
            color: rgba(20, 20, 20, 1);
            border-radius: 5px;
            font-weight: 900;
            }
            QLineEdit::hover {
            background-color: rgba(150, 150, 150, 1);
            }
            QLineEdit::pressed {
            border: 2px solid rgba(110, 110, 110, 1);
            }
            QLineEdit::disabled {
            background-color: rgba(110, 110, 110, 1);
            }"""


class Cell(QPushButton):
    """ Класс объекта кнопки с цифрой"""
    def __init__(self, initial_color, val):
        super().__init__()
        self.initial_color = initial_color
        self.vl = val
        self.init_style_sheet = None
        self.setAutoFillBackground(True)
        self.setText(str(self.vl))

        if self.initial_color == Black:
            self.color_anim = Black_initial
            self.init_style_sheet = black_default
            self.setStyleSheet(black_default)

        elif self.initial_color == Red:
            self.color_anim = Red_initial
            self.init_style_sheet = red_default
            self.setStyleSheet(red_default)

        self.animation = QPropertyAnimation(self)
        self.animation.setTargetObject(self)
        self.animation.setPropertyName(b'color_anim')
        self.animation.finished.connect(self.clear_style_sheet)

    def clear_style_sheet(self):
        self.setStyleSheet(self.init_style_sheet)

    @pyqtProperty(QColor)
    def color_anim(self):
        return self._color_anim

    @color_anim.setter
    def color_anim(self, color):
        self._color_anim = color
        new_style = f"background-color: {color.name()};"
        merged_style = f'{self.init_style_sheet}\n{new_style}'
        self.setStyleSheet(merged_style)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

    def animate_color(self, end_color, duration):
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(duration)
        self.animation.setStartValue(end_color)
        if self.initial_color == Black:
            self.animation.setEndValue(Black_initial)
        else:
            self.animation.setEndValue(Red_initial)
        self.animation.start()