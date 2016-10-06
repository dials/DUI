import sys
from Queue import Queue
from python_qt_bind import *

# The new Stream Object which replaces the default stream associated with sys.stdout
# This object just puts data in a queue!
class WriteStream(object):
    def __init__(self,queue):
        self.queue = queue

    def write(self, text):
        self.queue.put(text)

# A QObject (to be run in a QThread) which sits waiting for data to come through a Queue.Queue().
# It blocks until data is available, and one it has got something from the queue, it sends
# it to the "MainThread" by emitting a Qt Signal
class MyReceiver(QObject):
    mysignal = pyqtSignal(str)

    def __init__(self,queue ):
        QObject.__init__(self )
        self.queue = queue

    def run(self):
        while True:
            text = self.queue.get()
            self.mysignal.emit(text)

# An example QObject (to be run in a QThread) which outputs information with print
class Running_iDIALS_stuff(QThread):
    def run(self):
        for i in range(30):
            print i

        print "end for loop"

class MyApp(QWidget):
    def __init__(self ):
        QWidget.__init__(self )


        # Create Queue and redirect sys.stdout to this queue
        tmp_queue = Queue()
        sys.stdout = WriteStream(tmp_queue)

        # Create thread that will listen on the other end of the queue, and send the text to the textedit in our application
        self.outher_thread = QThread()
        my_receiver = MyReceiver(tmp_queue)
        my_receiver.mysignal.connect(self.append_text)
        my_receiver.moveToThread(self.outher_thread)
        self.outher_thread.started.connect(my_receiver.run)
        self.outher_thread.start()


        self.layout = QVBoxLayout(self)
        self.textedit = QTextEdit()
        self.button = QPushButton('start long running thread')
        self.button.clicked.connect(self.start_thread)
        self.layout.addWidget(self.textedit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.show()

    def append_text(self,text):
        self.textedit.moveCursor(QTextCursor.End)
        self.textedit.insertPlainText( text )

    def start_thread(self):
        self.thread = QThread()
        self.idials_thread = Running_iDIALS_stuff()
        self.idials_thread.moveToThread(self.thread)
        self.thread.started.connect(self.idials_thread.run)
        self.thread.start()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())