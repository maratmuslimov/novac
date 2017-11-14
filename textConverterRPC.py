import Window
import zerorpc
import sys

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

ui.inputText.setText('25; 15; 11; 123; 67; 234, 13, 234')
ui.inputText.editingFinished.connect(sendText)
MainWindow.show()
sys.exit(app.exec_())
