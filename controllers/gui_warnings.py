from PyQt5.QtWidgets import QMessageBox


def show_warning_messagebox(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(text)
    msg.setWindowTitle("Ошибка")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def show_info_messagebox(text):
    """ Всплывающее окно с инструкциями к тесту"""
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Инструкция")
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()