from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QCheckBox

from controllers.database import DataBaseHandler
from controllers.gui_warnings import show_warning_messagebox


class RegisterWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        self.database = DataBaseHandler()

    def setup_ui(self):
        self.setGeometry(800, 400, 300, 300)
        self.setFixedSize(300, 300)
        self.setWindowTitle("Регистрация пользователя")

        self.layout = QVBoxLayout()

        self.login_field = QLineEdit()
        self.login_field.setPlaceholderText("Логин")

        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("Пароль")

        self.admin_checkbox = QCheckBox("Регистрация в качестве администратора")

        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.clicked.connect(self.register)

        self.exit_button = QPushButton("Выход")
        self.exit_button.clicked.connect(self.close)

        self.layout.addWidget(self.login_field)
        self.layout.addWidget(self.password_field)
        self.layout.addWidget(self.admin_checkbox)
        self.layout.addWidget(self.register_button)
        self.layout.addWidget(self.exit_button)

        self.setLayout(self.layout)

    def register(self):
        if not self.login_field.text() or not self.password_field.text():
            show_warning_messagebox("Все поля должны быть заполнены!")
            return
        elif self.admin_checkbox.isChecked():
            self.database.register(self.login_field.text(), self.password_field.text(), 1)
        else:
            self.database.register(self.login_field.text(), self.password_field.text(), 0)
        self.close()

    def clear_inputs(self):
        self.login_field.clear()
        self.password_field.clear()
