# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QMessageBox, QComboBox, QStyle
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, QTime, QDateTime, pyqtSignal, QThread, Qt, QRect, QMetaObject, QCoreApplication
from PyQt5.QtTest import QTest
import datetime
import time
import sys
import requests
import urllib.request
from localdbmanager import recordsWriter, visitsRecordsWriter
import RPi.GPIO as GPIO
import MFRC522
      

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(20)
font_but.setWeight(200) 


def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.request.URLError as err: 
        return False

class visitsRecords(QMainWindow):
    sig = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(visitsRecords, self).__init__(parent=parent)
        self.setupUi()
        
    def setupUi(self):
        self.lab_id = 1
        self.setStyleSheet("border-image: url(images/VisitRecordBG.png)")
        self.resize(1920, 1080)
        self.pushButton_v = QPushButton(self)
        self.pushButton_v.setGeometry(QRect(70,55,370,110))
        self.pushButton_v.setStyleSheet("border-image: none; border: 0px; outline: none; ")
        self.pushButton_v.setObjectName("v")
        self.labelrut = QLabel(self)
        self.labelrut.setGeometry(QRect(240, 263 , 480, 100))
        self.labelrut.setStyleSheet("border-image: none; background :rgba(255,255, 255,0); font: 38pt \"MS Shell Dlg 2\";")
        self.pushButton_7 = QPushButton(self)
        self.pushButton_7.setGeometry(QRect(230, 400, 150, 100))
        self.pushButton_7.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_7.setObjectName("7")
        self.pushButton_8 = QPushButton(self)
        self.pushButton_8.setGeometry(QRect(445, 400, 155, 100))
        self.pushButton_8.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_8.setObjectName("8")
        self.pushButton_9 = QPushButton(self)
        self.pushButton_9.setGeometry(QRect(660, 400, 155, 100))
        self.pushButton_9.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_9.setObjectName("9")
        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setGeometry(QRect(230, 555, 155, 100))
        self.pushButton_4.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_4.setObjectName("4")
        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setGeometry(QRect(445, 555, 155, 100))
        self.pushButton_5.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_5.setObjectName("5")
        self.pushButton_6 = QPushButton(self)
        self.pushButton_6.setGeometry(QRect(660, 555, 155, 100))
        self.pushButton_6.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_6.setObjectName("6")
        self.pushButton_1 = QPushButton(self)
        self.pushButton_1.setGeometry(QRect(230, 710, 155, 100))
        self.pushButton_1.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_1.setObjectName("1")
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setGeometry(QRect(445, 710, 155, 100))
        self.pushButton_2.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_2.setObjectName("2")
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setGeometry(QRect(660, 710, 155, 100))
        self.pushButton_3.setStyleSheet("border-image: none; background: transparent; border: 0px; ")
        self.pushButton_3.setObjectName("3")
        self.pushButton_k = QPushButton(self)
        self.pushButton_k.setGeometry(QRect(230, 865, 155, 100))
        self.pushButton_k.setStyleSheet("border-image: none; background: transparent; border: 0px;outline: none ")
        self.pushButton_k.setObjectName("k")
        self.pushButton_0 = QPushButton(self)
        self.pushButton_0.setGeometry(QRect(445, 865, 155, 100))
        self.pushButton_0.setStyleSheet("border-image: none; background: transparent; border: 0px; outline: none")
        self.pushButton_0.setObjectName("0")
        self.pushButton_d = QPushButton(self)
        self.pushButton_d.setGeometry(QRect(660, 865, 155, 100))
        self.pushButton_d.setStyleSheet("border-image: none; background: transparent; border: 0px; outline: none;")
        self.pushButton_d.setObjectName("d")
        self.pushButton_s = QPushButton(self)
        self.pushButton_s.setGeometry(QRect(1190, 870, 370, 100))
        self.pushButton_s.setStyleSheet("border-image: none; background: transparent; border: 0px; outline: none;")
        self.pushButton_s.setObjectName("s")
        self.motivo = QLabel(self)
        self.motivo.setGeometry(QRect(1200, 190, 300, 61))
        self.motivo.setText('Motivo de visita')
        self.motivo.setStyleSheet("border-image: none; background :rgba(255,255, 255,0); font: 24pt \"MS Shell Dlg 2\"; color: white")
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(1200, 295, 400, 100))
        self.comboBox.setStyleSheet("border-image: none;font: 21pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.institucion = QLabel(self)
        self.institucion.setGeometry(QRect(1200, 500, 700, 61))
        self.institucion.setStyleSheet("border-image: none; background :rgba(255,255, 255,0); font: 24pt \"MS Shell Dlg 2\"; color: white")
        self.institucion.setText('Insititucion que pertenece')
        self.comboBox_1 = QComboBox(self)
        self.comboBox_1.setGeometry(QRect(1200, 595, 400, 100))
        self.comboBox_1.setStyleSheet("border-image: none; font: 21pt \"MS Shell Dlg 2\";")
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.pushButton_1.clicked.connect(self.clickedButton)
        self.pushButton_2.clicked.connect(self.clickedButton)
        self.pushButton_3.clicked.connect(self.clickedButton)
        self.pushButton_4.clicked.connect(self.clickedButton)
        self.pushButton_5.clicked.connect(self.clickedButton)
        self.pushButton_6.clicked.connect(self.clickedButton)
        self.pushButton_7.clicked.connect(self.clickedButton)
        self.pushButton_8.clicked.connect(self.clickedButton)
        self.pushButton_9.clicked.connect(self.clickedButton)
        self.pushButton_d.clicked.connect(self.clickedButton)
        self.pushButton_s.clicked.connect(self.send)
        self.pushButton_v.clicked.connect(self.clickedButton)
        self.pushButton_k.clicked.connect(self.clickedButton)
        self.pushButton_0.clicked.connect(self.clickedButton)
        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Investigación"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Personal"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Emprendimiento"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Curso"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Taller"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Otro"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "Pontificia Universidad Católica de Chile"))

    def clickedButton(self):
        button = self.sender()
        value = button.objectName()
        if value == 'd':
            if self.labelrut.text():
                self.labelrut.setText(self.labelrut.text()[:-1])
                return
        elif value == 'v':
            self.close()
            return
        self.labelrut.setText(self.labelrut.text() + '{}'.format(value))
    
    def send(self):
        self.close()
        if self.labelrut.text():
            rut = self.labelrut.text()[:-1]+'-'+self.labelrut.text()[-1]
            data = {'rut': rut, 
                    'motivo': self.comboBox.currentText(),
                    'institucion': self.comboBox_1.currentText(),
                    'lab_id': self.lab_id}
            self.sig.emit(data)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1202, 676)
        self.setStyleSheet("QWidget {border-image: url(images/InitialBG.png)}")
        self.lab_id = 1
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(1250, 290, 400, 380))
        self.pushButton.setStyleSheet("border-image: none; background: transparent; border: 0px; outline: none; ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.recordVisit)
        self.labeltext = QLabel(self.centralwidget)
        self.labeltext.setGeometry(QRect(456, 166, 300,400))
        self.labeltext.setStyleSheet("font: 40pt \"MS Shell Dlg 2\";\n"
        "background :rgba(255,255, 255,0); color: white")
        self.labeltext.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.showFullScreen()
        self.thread = Reader()
        self.thread.sig1.connect(self.screenResponse)
        self.thread.sig2.connect(self.screenResponse)
        self.thread.start()
        self.imageCase = {'enrollIn':'images/Enroll.png',
                          'nonEnroll':'images/NonEnroll.png',
                          'nonSystemEnroll':'images/NonSystemEnroll.png',
                          'enrollOut':'images/EnrollOut.png',
                          'visit':'images/Visit.png',
                          'baned':'images/Baned'}
        self.generateInstance()


    def generateInstance(self):
        self.visit = visitsRecords()
        self.signal = self.visit.sig.connect(self.send)


    def send(self, data):
        url = 'https://redlabuc.herokuapp.com/visits'
        if internet_on():
            response = requests.post(url, data).json()
            if response['type'] == 'student':
                self.studentCase(response)
                self.generateInstance()
            else:
                dataset = {'name':'', 'image': self.imageCase['visit']}
                self.changeScreen(dataset)
                self.generateInstance()

        else:
            visitsRecordsWriter(data)
            dataset = {'name':'', 'image': self.imageCase['Visit.png']}
            self.changeScreen(dataset)


    def screenResponse(self, value):
        if isinstance(value, dict):
            self.studentCase(value)
        else:
            dataset = {'name':'', 'image': self.imageCase['nonSystemEnroll']}
            self.changeScreen(dataset)

    def changeScreen(self, dataset):   
        string = "QWidget {border-image: url(%s)}" % (dataset['image'])
        self.setStyleSheet(string)
        self.labeltext.setVisible(True)
        self.labeltext.setText(dataset['name'])
        QTest.qWait(3000)
        self.labeltext.setVisible(False)
        self.setStyleSheet("QWidget {border-image: url(images/InitialBG.png)}")



    def studentCase(self, value):
        print('studenCase', value['data']['laboratory'])
        enroll = False
        labs = [x['id'] for x in value['data']['laboratory']]
        if self.lab_id in labs:
            enroll = True
        if enroll:
            dataset = {'name': value['data']['student']['nombre'],
                       'image': self.imageCase['enrollIn'] if value['data']['student']['status'] else self.imageCase['enrollOut']}
        else:
            dataset = {'name': value['data']['student']['nombre'],
                       'image': self.imageCase['nonEnroll']}
        
        self.changeScreen(dataset)

            
            
       
    def recordVisit(self):
        self.generateInstance()
        self.visit.showFullScreen()
        self.visit.show()

    def retranslateUi(self, MainWindow):
        pass




class Reader(QThread):

    sig1 = pyqtSignal(dict)
    sig2 = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    
    def run(self):
        url = 'https://redlabuc.herokuapp.com/records'
        continue_reading = True
        # Create an object of the class MFRC522
        MIFAREReader = MFRC522.MFRC522()
        # Welcome message
        print("Welcome to the MFRC522 data read example")
        print("Press Ctrl-C to stop.")

        # This loop keeps checking for chips. If one is near it will get the UID and authenticate
        while continue_reading:
            
            # Scan for cards    
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            # If a card is found
            if status == MIFAREReader.MI_OK:
                print("Card detected")
            
            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == MIFAREReader.MI_OK:

                # Print UID
                print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
                print(uid)
                rfid = str(hex(uid[0]))[2:]+str(hex(uid[1]))[2:]+str(hex(uid[2]))[2:]+str(hex(uid[3]))[2:]
                try:
                    req = requests.post(url, {'rfid':rfid,'lab_id':1}).json()
                    if not req:
                        req = ''
                        self.sig2.emit(req)
                    else:
                        self.sig1.emit(req)
     
                except:
                    req = 'Not Internet Conection'
                    self.sig2.emit(req)
            
                time.sleep(5)
                GPIO.cleanup()




if __name__ == "__main__":  
    app = QApplication(sys.argv)
    desktop = QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = MainWindow()
    myapp.show()
    myapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())


