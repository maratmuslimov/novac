# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(600,400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setGeometry(QtCore.QRect(15, 15, 570, 370))
        self.groupbox.setObjectName('groupbox')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticalLayout.setObjectName('verticalLayout')

        self.inputTextLable = QtWidgets.QLabel(self.groupbox)
        self.inputTextLable.setObjectName('inputTextLable')
        self.inputTextLable.setText('Input text')
        self.verticalLayout.addWidget(self.inputTextLable)

        self.inputText = QtWidgets.QLineEdit(self.groupbox)
        # self.inputText.setGeometry(QtCore.QRect(15, 15, 100, 50))
        self.inputText.setMinimumSize(QtCore.QSize(540, 50))
        self.inputText.setMaximumSize(QtCore.QSize(570, 50))
        self.verticalLayout.addWidget(self.inputText)

        self.outputTextLable = QtWidgets.QLabel(self.groupbox)
        self.outputTextLable.setObjectName('outputTextLable')
        self.outputTextLable.setText('Output text')
        self.verticalLayout.addWidget(self.outputTextLable)

        self.outputText = QtWidgets.QLineEdit(self.groupbox)
        # self.inputText.setGeometry(QtCore.QRect(50, 50, 100, 50))
        self.outputText.setMinimumSize(QtCore.QSize(540, 50))
        self.outputText.setMaximumSize(QtCore.QSize(570, 50))
        self.outputText.setReadOnly(True)
        self.verticalLayout.addWidget(self.outputText)

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
