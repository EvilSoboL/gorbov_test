from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton

from controllers.database import DataBaseHandler
from controllers.gui_warnings import show_warning_messagebox, show_info_messagebox
from controllers.gui_settings import menu_lines, menu_buttons
from entity.user import user
from boundaries.test_tab import TestTab


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        self.test_tab = TestTab()
        self.database = DataBaseHandler()

    def setup_ui(self):
        self.setGeometry(800, 400, 300, 300)
        self.setFixedSize(300, 300)
        self.setWindowTitle("Аутентификация пользователя")

        self.layout = QVBoxLayout()

        self.login_field = QLineEdit()
        self.login_field.setPlaceholderText("Логин")

        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("Пароль")

        self.register_button = QPushButton("Войти в аккаунт")
        self.register_button.clicked.connect(self.login)

        self.exit_button = QPushButton("Выход")
        self.exit_button.clicked.connect(self.close)

        self.layout.addWidget(self.login_field)
        self.layout.addWidget(self.password_field)
        self.layout.addWidget(self.register_button)
        self.layout.addWidget(self.exit_button)

        self.setLayout(self.layout)

    def login(self):
        if not self.login_field.text() or not self.password_field.text():
            show_warning_messagebox("Все поля должны быть заполнены!")
            return
        user_id, is_admin = self.database.login(self.login_field.text(), self.password_field.text())
        if not (user_id, is_admin):
            show_warning_messagebox("Логин или пароль не найдены!")
        if is_admin:
            show_info_messagebox('Вы успешно вошли в аккаунт как администратор!')
            user.authorized(user_id, 1)
            self.clear_inputs()
            self.close()

        else:
            show_info_messagebox('Вы успешно вошли в аккаунт как тестируемый!')
            user.authorized(user_id, 0)
            self.clear_inputs()
            self.close()

    def clear_inputs(self):
        self.login_field.clear()
        self.password_field.clear()