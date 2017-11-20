#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import Window
import zerorpc
import sys
import json

class Client():
    def createClient(self, text):
        c = zerorpc.Client()
        c.connect("tcp://127.0.0.1:4242")
        result = c.streaming_range(text)
        return(result)

app = Window.QtWidgets.QApplication(sys.argv)
MainWindow = Window.QtWidgets.QMainWindow()
ui = Window.Ui_MainWindow()
ui.setupUi(MainWindow)

def sendText():
    text = ui.inputText.text()
    client = Client()
    c = client.createClient(text)
    ui.outputText.setText(c)

t = '{"C_nkpr": 16, "t_vsp": 16, "q": 1.5, "T": 120.0, "V_ap": 5.0, "P_2": 50.0, "P_1": 50.0, "t_r": 50.0, "M": 7.0, "Q_sg": 40.0, "Z": 0.1, "r": 30.0, "calcObject": "EG"}'
ui.inputText.setText(t)
ui.inputText.editingFinished.connect(sendText)
MainWindow.show()
sys.exit(app.exec_())
