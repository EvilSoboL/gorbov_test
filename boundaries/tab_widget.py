from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from boundaries.auth_tab import AuthTab
from boundaries.test_tab import TestTab


class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Инициализация вкладок
        self.tabs = QTabWidget()
        self.auth_tab = AuthTab()
        self.test_tab = TestTab()

        self.tabs.addTab(self.auth_tab, "Аутентификация")
        self.tabs.addTab(self.test_tab, "Тестрирование")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
