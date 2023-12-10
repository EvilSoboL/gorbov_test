from PyQt5.QtWidgets import QMessageBox


def show_warning_messagebox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(text)
    msg.setWindowTitle("Ошибка")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()