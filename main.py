import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import QThread, QObject


class MsgBox(QWidget):
    
    def __init__(self):
        super(MsgBox, self).__init__()
        #self.message = message
        self.setFixedSize(200, 50)
        self.location_on_the_screen()
        self.setWindowTitle('Сообщение')
        self.lbl = QtWidgets.QLabel('', self)
        self.lbl.setOpenExternalLinks(True)
        print("here")
        self.lbl.setText("12345")
    
        
    def location_on_the_screen(self):
        ag = QtWidgets.QDesktopWidget().availableGeometry()
        sg = QtWidgets.QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x-15, y)

class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.initUi()

        self.low = 0
        self.high = 100

        self.show()


    def initUi(self):


        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.do_work)
        self.thread.finished.connect(self.thread.deleteLater)

        self.button = QPushButton(
                'Start long running task')

        self.button.clicked.connect(self.thread.start)

        self.layout = QGridLayout()        
        self.layout.addWidget(self.button, 0, 0)
        self.setLayout(self.layout)



class Worker(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    def do_work(self):
        counter = 0
        while True:
            counter+=1
            print('running . . .')
            QThread.sleep(2)
            if counter==5:
                self.call_window()



    def call_window(self):
        self.subwindow = MsgBox()
        self.subwindow.show()

def main(args):

    app = QApplication(args)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
