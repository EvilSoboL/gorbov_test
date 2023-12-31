from PyQt5.QtWidgets import QWidget, QGridLayout, QButtonGroup, QPushButton, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from datetime import datetime

from controllers.gui_settings import Black, Red, Cell, menu_buttons
from controllers.cells_generator import create_normalize_matrix
from controllers.gui_warnings import show_info_messagebox
from entity.user import user
from entity.result import Result


class TestTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Флаги и переменные для разметки этапов тестирования
        self.first_part = False
        self.second_part = False
        self.third_part = False
        self.color_flag = Black
        self.shuffle_once_flag = False
        self.fp = 1
        self.sp = 24
        self.errors = 0

        # Таймер
        self.timer = QTimer()
        self.timer_flag = False
        self.count = 0
        self.timer.timeout.connect(self.show_time)
        self.timer.start(100)
        self.first_part_time = 0
        self.second_part_time = 0

        # Разметка окна
        self.setup_ui()
        self.result = Result()

    def setup_ui(self):
        # Сетка главного окна
        self.main_layout = QGridLayout()
        self.cells_layout = QGridLayout()
        self.menu_layout = QGridLayout()

        self.cells_widget = QWidget()
        self.cells_widget.setLayout(self.cells_layout)
        self.menu_widget = QWidget()
        self.menu_widget.setLayout(self.menu_layout)

        self.cells_group = QButtonGroup()
        self.create_cells()
        self.cells_group.buttonClicked[int].connect(self.on_button_clicked)

        self.menu_group = QButtonGroup()

        # Кнопки меню
        self.start_button = QPushButton("Начать тест")
        self.start_button.clicked.connect(lambda: self.logic_switch("start"))

        self.random_button = QPushButton("Перемешать ячейки")
        self.random_button.clicked.connect(self.shuffle_cells)

        self.stop_button = QPushButton("Остановить тест")
        self.stop_button.clicked.connect(lambda: self.logic_switch("stop"))

        # Вёрстка таймера
        self.timer_label = QLabel("0:00")
        #self.timer_label.setFont(QFont('Times', 30))
        self.timer_label.setAlignment(Qt.AlignLeft)

        self.group_menu_buttons()

        self.menu_layout.addWidget(self.start_button, 0, 0)
        self.menu_layout.addWidget(self.stop_button, 1, 0)
        self.menu_layout.addWidget(self.random_button, 2, 0)
        self.menu_layout.addWidget(self.timer_label, 1, 1, 2, 2)

        self.main_widget = QWidget()
        self.main_layout.addWidget(self.cells_widget, 0, 0, 6, 6)
        self.main_layout.addWidget(self.menu_widget, 7, 0, 7, 6)
        self.main_widget.setLayout(self.main_layout)

        self.setLayout(self.main_layout)

    def group_menu_buttons(self):
        self.menu_group.addButton(self.start_button)
        self.menu_group.addButton(self.stop_button)
        self.menu_group.addButton(self.random_button)

        #for button in self.menu_group.buttons():
            #button.setStyleSheet(menu_buttons)

    def create_cells(self):
        """ Создаём поле с черно-красными карточками в неслучайном случайном порядке"""
        matrix = create_normalize_matrix()

        for i in range(len(matrix)):
            if matrix[i] <= 25:
                black_button = Cell(Black, matrix[i])
                self.cells_group.addButton(black_button, black_button.vl)
                self.cells_layout.addWidget(black_button, i//7, i % 7)
            else:
                red_button = Cell(Red, matrix[i] - 25)
                self.cells_group.addButton(red_button, red_button.vl + 25)
                self.cells_layout.addWidget(red_button, i//7, i % 7)

    def logic_switch(self, flag):
        """Вызов различных сценариев работы приложения"""
        if flag == "start":
            if not user.is_authorized:
                show_info_messagebox("Вам необходимо аутентифицироваться в системе!")
                return
            self.count = 0
            self.random_button.setEnabled(False)
            self.start_button.setEnabled(False)
            self.first_part = True
            self.fp = 1
            self.sp = 24
            show_info_messagebox("Последовательно нажмите на чёрные числа в порядке возрастания")

        elif flag == "stop":
            self.start_button.setEnabled(True)
            self.random_button.setEnabled(True)
            self.first_part = False
            self.second_part = False
            self.third_part = False
            self.shuffle_once_flag = False
            self.fp = 1
            self.sp = 24
            self.timer_flag = False
            self.count = 0

        elif flag == "reset":
            self.errors = 0

    def shuffle_cells(self):
        """Перемешивание элементов теста"""
        for i in reversed(range(self.cells_layout.count())):
            tmp = self.cells_layout.itemAt(i).widget()
            self.cells_layout.removeWidget(tmp)
            tmp.setParent(None)
            tmp.deleteLater()
        self.create_cells()

    def on_button_clicked(self, button_id):
        if self.first_part:
            if self.cells_group.button(button_id).initial_color == Black and self.cells_group.button(button_id).vl == self.fp:
                if not self.timer_flag:
                    self.timer_flag = True
                    self.show_time()

                self.cells_group.button(button_id).animate_color(QColor("green"), duration=900)
                self.fp += 1

            else:
                self.cells_group.button(button_id).animate_color(QColor("white"), duration=900)
                self.errors += 1

            if self.fp == 26:
                self.first_part = False
                self.second_part = True
                self.fp = 49
                self.timer_flag = False
                show_info_messagebox("Последовательно нажмите на красные числа в порядке убывания")

        if self.second_part:
            if self.cells_group.button(button_id).initial_color == Red and self.cells_group.button(button_id).vl + 25 == self.fp:
                if not self.timer_flag:
                    self.timer_flag = True

                self.cells_group.button(button_id).animate_color(QColor("green"), duration=900)
                self.fp -= 1

            else:
                self.cells_group.button(button_id).animate_color(QColor("white"), duration=900)
                self.errors += 1

            if self.fp == 25:
                self.first_part_time = self.count/10
                self.second_part = False
                self.third_part = True
                self.fp = 1
                self.timer_flag = False
                show_info_messagebox("Поочерёдно нажимайте на чёрные числа в порядке возрастания, а красные в порядке убывания")

        if self.third_part:

            if not self.shuffle_once_flag:
                self.shuffle_cells()
                self.shuffle_once_flag = True

            if self.color_flag == Black:
                if self.cells_group.button(button_id).initial_color == Black and self.cells_group.button(button_id).vl == self.fp:
                    if not self.timer_flag:
                        self.timer_flag = True
                    self.cells_group.button(button_id).animate_color(QColor("green"), duration=900)
                    self.fp += 1
                    self.color_flag = Red

                else:
                    self.cells_group.button(button_id).animate_color(QColor("white"), duration=900)
                    self.errors += 1

            elif self.color_flag == Red:
                if self.cells_group.button(button_id).initial_color == Red and self.cells_group.button(button_id).vl == self.sp:
                    self.cells_group.button(button_id).animate_color(QColor("green"), duration=900)
                    self.sp -= 1
                    self.color_flag = Black

                else:
                    self.cells_group.button(button_id).animate_color(QColor("white"), duration=900)
                    self.errors += 1

            if self.fp == 26 and self.sp == 0:
                self.second_part_time = (self.count/10) - self.first_part_time
                self.timer_flag = False
                self.third_part = False
                self.logic_switch("stop")

                date = datetime.now().date()
                switching = self.second_part_time - self.first_part_time

                self.result.save_result(
                    user.id,
                    date,
                    self.first_part_time,
                    self.second_part_time,
                    self.errors,
                    switching
                )
                self.logic_switch("reset")

    def show_time(self):
        if self.timer_flag:
            self.count += 1

        text = str(self.count / 10)
        self.timer_label.setText(text)
