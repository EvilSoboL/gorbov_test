from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from boundaries.auth_tab import AuthTab


class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Инициализация вкладок
        self.tabs = QTabWidget()
        self.auth_tab = AuthTab()

        self.tabs.addTab(self.auth_tab, "Аутентификация")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
