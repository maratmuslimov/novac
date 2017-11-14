import Window
import zmq
import sys

class Client():
    def createClient(self, text):
        port = "5556"

        context = zmq.Context()
        print("Connecting to server...")
        socket = context.socket(zmq.REQ)
        socket.connect ("tcp://localhost:%s" % port)

        for request in range (1):
            print("Sending request ", request,"...")
            socket.send_string(text)
            #  Get the reply.
            message = socket.recv_string()
        return(message)

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
