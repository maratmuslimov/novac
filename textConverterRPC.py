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

t = '{"P_1": 50.0, "V_ap": 5.0, "q": 1.5, "T": 120.0, "P_2": 50.0, "dL": [0.024, 6.0, 0.024, 6.0]}'
ui.inputText.setText(t)
ui.inputText.editingFinished.connect(sendText)
MainWindow.show()
sys.exit(app.exec_())
