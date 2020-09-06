import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtWidgets, uic, QtCore, QtGui

import pyautogui as pag
import keyboard
import pyperclip
import openpyxl as opx
from time import sleep as sl
from datetime import datetime


Spamform, _ = uic.loadUiType("spam.ui")


class UI2(QtWidgets.QDialog, Spamform):

    def __init__(self):
        super().__init__()
        self.startspam.clicked.connect(self.spammer)

    def spammer(self, mapToData, how_many=0, start_time=datetime.now()):
        WORKBOOK_PATH = mapToData  # Путь к вашей базе которую вы импортировали в эмулятор , но лучше
        # чтобы база и скрипт были в одной папке
        workbook = opx.load_workbook(WORKBOOK_PATH)

        first_sheet = workbook.worksheets[0]
        x1 = self.lineEdit_2.text()
        x1 = int(x1)
        x2 = self.lineEdit_4.text()
        x2 = int(x2)
        x3 = self.lineEdit_7.text()
        x3 = int(x3)
        y1 = self.lineEdit_3.text()
        y1 = int(y1)
        y2 = self.lineEdit_6.text()
        y2 = int(y2)
        y3 = self.lineEdit_5.text()
        y3 = int(y3)

        for row in first_sheet.rows:
            phone = row[1].value  # Телефон
            name = row[0].value  # Название

            sl(1)

            speach = f"Здравствуйте , на насчёт объявления '{name}' , ещё актуально ?"  # Спич

            pyperclip.copy(phone)

            pag.click(x=x1, y=y1, interval=2)  # Поиск по контакту , 1 значение
            keyboard.press_and_release('ctrl+v')  # Вставляем номер
            sl(1)

            pag.click(x=x2, y=y2, interval=2)  # Входим в личку , 2 значение
            sl(1)

            pyperclip.copy(speach)  # Копируем спич
            keyboard.press_and_release('ctrl+v')  # Вставляем спич
            sl(1)
            keyboard.press_and_release('enter')
            sl(1)

            pag.click(x=x3, y=y3, interval=2)  # Выход с лички , 3 значение
            how_many += 1
            status = f'Кол-во сообщений: {how_many}\nПрошло времени: {datetime.now() - start_time}'

            self.statuslabel.setText(str(status))
