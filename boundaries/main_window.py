from PyQt5.QtWidgets import QMainWindow

from boundaries.tab_widget import TabWidget


class Window(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.width_size = 1080
        self.height_size = 720

        self.setWindowTitle("Тест Горбова")
        self.setGeometry((width-self.width_size)//2, (height-self.height_size)//2, self.width_size, self.height_size)
        self.setFixedSize(self.width_size, self.height_size+80)

        self.tab_widget = TabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()