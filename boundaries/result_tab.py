from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QPushButton, QTableWidgetItem

from controllers.database import DataBaseHandler
from boundaries.register_form import RegisterWindow
from boundaries.login_form import LoginWindow
from controllers.user import user
from controllers.gui_warnings import show_info_messagebox


class ResultTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.main_layout = QVBoxLayout()
        self.setup_ui()

        #self.create_window = None

        self.database = DataBaseHandler()

    def setup_ui(self):
        self.table_widget = QTableWidget(self)

        self.update_button = QPushButton("Обновить")
        self.update_button.clicked.connect(lambda: self.get_result())

        self.main_layout.addWidget(self.table_widget)
        self.main_layout.addWidget(self.update_button)

        self.setLayout(self.main_layout)

    def get_result(self):
        if not user.is_authorized:
            show_info_messagebox("Вам необходимо аутентифицироваться в системе!")
            return
        result = self.database.get_results(user.id)
        self.table_widget.setRowCount(len(result))
        self.table_widget.setColumnCount(len(result[0]))

        for row_num, row_data in enumerate(result):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.table_widget.setItem(row_num, col_num, item)
