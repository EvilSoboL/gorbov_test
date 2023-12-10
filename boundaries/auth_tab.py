from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QButtonGroup, QPushButton

from controllers.database import DataBaseHandler
from boundaries.register_form import RegisterWindow


class AuthTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.main_layout = QVBoxLayout()
        self.setup_ui()

        self.create_window = None

        self.database = DataBaseHandler

    def setup_ui(self):
        self.main_layout = QGridLayout()
        self.menu_layout = QGridLayout()

        self.menu_widget = QWidget()
        self.menu_widget.setLayout(self.menu_layout)

        self.menu_group = QButtonGroup()

        self.create_applicant_button = QPushButton("Зарегистрироваться")
        self.create_applicant_button.clicked.connect(lambda: self.registration_form())

        self.update_apllicant_button = QPushButton("Аутентифицироваться")
        self.update_apllicant_button.clicked.connect(lambda: None)

        self.menu_layout.addWidget(self.create_applicant_button, 0, 2)
        self.menu_layout.addWidget(self.update_apllicant_button, 1, 2)

        self.main_widget = QWidget()
        self.main_layout.addWidget(self.menu_widget, 7, 0, 7, 6)
        self.main_widget.setLayout(self.main_layout)

        self.setLayout(self.main_layout)

    def registration_form(self):
        if self.create_window is None:
            self.create_window = RegisterWindow()
        self.create_window.exec()