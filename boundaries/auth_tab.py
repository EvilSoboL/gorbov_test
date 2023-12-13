from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QButtonGroup, QPushButton

from controllers.database import DataBaseHandler
from boundaries.register_form import RegisterWindow
from boundaries.login_form import LoginWindow


class AuthTab(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setup_ui()

        self.create_window = None

        self.database = DataBaseHandler()

    def setup_ui(self):
        self.main_layout = QGridLayout()
        self.menu_layout = QGridLayout()

        self.menu_widget = QWidget()
        self.menu_widget.setLayout(self.menu_layout)

        self.menu_group = QButtonGroup()

        self.registration_button = QPushButton("Зарегистрироваться")
        self.registration_button.clicked.connect(lambda: self.registration_form())

        self.login_button = QPushButton("Аутентифицироваться")
        self.login_button.clicked.connect(lambda: self.login_form())

        self.menu_layout.addWidget(self.registration_button, 0, 2)
        self.menu_layout.addWidget(self.login_button, 1, 2)

        self.main_widget = QWidget()
        self.main_layout.addWidget(self.menu_widget, 7, 0, 7, 6)
        self.main_widget.setLayout(self.main_layout)

        self.setLayout(self.main_layout)

    def registration_form(self):
        if self.create_window is None:
            self.create_window = RegisterWindow()
        self.create_window.exec()
        self.create_window = None

    def login_form(self):
        if self.create_window is None:
            self.create_window = LoginWindow()
        self.create_window.exec()
        self.create_window = None
