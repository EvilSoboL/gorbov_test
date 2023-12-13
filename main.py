import sys
from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet

from boundaries.main_window import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    screen = app.primaryScreen()
    size = screen.size()
    window = Window(size.width(), size.height())
    sys.exit(app.exec())
