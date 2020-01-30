# -*- coding: utf-8 -*-
#!/usr/bin/env python 
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QDesktopWidget, QSizePolicy, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QMessageBox, QComboBox, QStyle
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, QTime, QDateTime, pyqtSignal, QThread, Qt, QRect, QMetaObject, QCoreApplication, QSize
from PyQt5.QtTest import QTest
import reader
import api_call
import requests
import credentials

lab_id=1
gral_url= 'http://peaceful-cove-91834.herokuapp.com/'
class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi()
    
    def setupUi(self):
        #self.setStyleSheet("QWidget {border-image: url(/home/pi/guiPythonLABFAB/images/Baned.png)}")
        self.setVisible(False)
        self.imageCase = {'enrollIn':'images/Enroll.png',
                          'nonEnroll':'images/NonEnroll.png',
                          'nonSystemEnroll':'images/NonSystemEnroll.png',
                          'enrollOut':'images/EnrollOut.png',
                          'visit':'images/Visit.png',
                          'baned':'images/Baned',
                          'enrolling': 'images/Enrrolling.png',
                          'waiting': 'Wait.png'}
        self.labeltext = QLabel(self)
        self.labeltext.setStyleSheet("border-image: none; font: 80pt; color: white;")
        self.labeltext.setVisible(False)
        self.thread = reader.Reader()
        self.thread.sig1.connect(self.screenResponse)
        self.thread.sig2.connect(self.screenResponse)
        self.thread.start()
        self.lab_id = 1
        
         

#     def send(self, data):
#         url = gral_url+"visits"
#         if internet_on():
#             response = requests.post(url, data, headers=credentials.totem_credential).json()
#             if response['type'] == 'student':
#                 self.studentCase(response)
#                 self.generateInstance()
#             else:
#                 dataset = {'name':'', 'image': self.imageCase['visit']}
#                 self.changeScreen(dataset)
#                 self.generateInstance()
# 
#         else:
#             visitsRecordsWriter(data)
#             print('Sin conexión a internet, generando base de datos local...')
#             dataset = {'name':'', 'image': self.imageCase['Visit.png']}
#             self.changeScreen(dataset)


    def screenResponse(self, value):
#         self.setStyleSheet("QWidget {border-image: url(images/Wait.png)}")
#         QTest.qWait(1)
#         self.showFullScreen()
#         QTest.qWait(100)
        if isinstance(value, dict):
            self.studentCase(value)
        else:
            if not self.checkUcDB(value):
                dataset = {'name':'', 'image': self.imageCase['nonSystemEnroll']}
                self.changeScreen(dataset)


    def checkUcDB(self,rfid):
        self.setStyleSheet("QWidget {border-image: url(images/Enrrolling.png)}")
        QTest.qWait(1)
        self.showFullScreen()
        QTest.qWait(1000)
        data = api_call.get_data(rfid)
        if isinstance(data, str):
            return None
        student = requests.post(gral_url+'students/created_from_totem', data, headers=credentials.totem_credential)
        record = requests.post(gral_url+'records', {'rfid':data['rfid'],'lab_id':1}, headers=credentials.totem_credential).json()
        QTest.qWait(2000)
        self.studentCase(record)
        return True


    def changeScreen(self, dataset):   
        string = "QWidget {border-image: url(%s)}" % (dataset['image'])
        self.setStyleSheet(string)
        QTest.qWait(10)
        #self.labeltext.setVisible(True)
        #high = 750 if dataset['image'] == 'images/NonEnroll.png' else 450
        #leters = len(dataset['name'].split(' ')[0])
        #width = leters if leters<=10 else 10
        #offset = 16 if leters>10 else 0
        #self.labeltext.setGeometry(QRect(200,200,100,100))
        #self.labeltext.setText(dataset['name'].split(' ')[0])
        self.showFullScreen()
        QTest.qWait(2000)
        self.setStyleSheet("QWidget {border-image: none}")
        QTest.qWait(10)
        self.setVisible(False)
        

    def studentCase(self, value):
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
           
       
#     def recordVisit(self):
#         self.generateInstance()
#         self.visit.showFullScreen()
#         self.visit.show()


if __name__ == "__main__":  
    app = QApplication(sys.argv)
    myapp = MainWindow()
    sys.exit(app.exec_())    
