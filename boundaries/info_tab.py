from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from controllers.gui_settings import info_text


class InfoTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.main_layout = QVBoxLayout()
        """Блок с информацией о тесте"""
        self.about = QLabel()
        self.about.setFont(QFont('Arial', 15))
        self.about.setTextFormat(Qt.RichText)
        self.about.setWordWrap(True)
        self.about.setText(info_text)
        self.about.setAlignment(Qt.AlignJustify)
        """Блок с информацией о результатах тестирования"""
        self.results = QLabel()
        self.results.setFont(QFont('Arial', 15))

        self.main_layout.addWidget(self.about)
        self.main_layout.addWidget(self.results)
        self.setLayout(self.main_layout)