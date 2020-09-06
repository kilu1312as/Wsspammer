import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QObject, QRunnable, QThreadPool, pyqtSlot
from PyQt5.QtWidgets import QInputDialog, QApplication
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import webbrowser
import pyautogui as pag
import keyboard
import pyperclip
import openpyxl as opx
from time import sleep as sl
from datetime import datetime
import multiprocessing as mlti

Form, _ = uic.loadUiType("untitled.ui")


class UI1(QtWidgets.QDialog, Form):
    def __init__(self):
        super().__init__()
        self.pushButton_2.clicked.connect(self.showDialog)
        self.pushButton.clicked.connect(self.setXY)

        self.pushButton_9.clicked.connect(lambda: webbrowser.open('http://www.google.com'))
        setcoor = self.pushButton
        setcoor.setShortcut(QtGui.QKeySequence("Ctrl+Space"))

    def showDialog(self):
        mapToData, ok = QInputDialog.getText(self, 'Input Dialog',
                                             'Вставте путь к базе :')
        if ok:
            self.label_4.setText(str(mapToData))

    def setXY(self):
        pos = pag.position()
        self.label_6.setText(str(pos))


