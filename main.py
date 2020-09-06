import multiprocessing as mlti
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QObject, QRunnable, QThreadPool, pyqtSlot
from PyQt5.QtWidgets import QInputDialog, QApplication
from PyQt5 import QtWidgets, uic, QtCore, QtGui

from Wsspammer.spam import UI2

from Wsspammer.settigs import UI1


class WorkerGUI(QRunnable):
    def __init__(self, InFunc):
        super(WorkerGUI, self).__init__()
        self.Func = InFunc

    @pyqtSlot()
    def run(self):
        self.Func()


def Process1():
    MainThred = QApplication([])
    SettingsGui = UI1()
    SettingsGui.show()
    sys.exit(MainThred.exec_())


def Process2():
    MainThred = QApplication([])
    SpamGUI = UI2()
    SpamGUI.show()
    sys.exit(MainThred.exec_())


if __name__ == "__main__":
    multiprcess1 = mlti.Process(target=Process1)
    multiprcess2 = mlti.Process(target=Process2)

    multiprcess1.start()
    multiprcess2.start()