import sys
from PyQt5.QtWidgets import QApplication

from boundaries.main_window import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    window = Window(size.width(), size.height())
    sys.exit(app.exec())
