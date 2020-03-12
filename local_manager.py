import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QStyle, QApplication, QGroupBox, QMainWindow,QDesktopWidget, QSizePolicy, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QMessageBox, QStyle
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, QTime, QDateTime, pyqtSignal, QThread, Qt, QRect, QMetaObject, QCoreApplication, QSize
from PyQt5.QtTest import QTest
from itertools import cycle


      
        

class NumberPad(QWidget):
    def __init__(self):
        super().__init__()
        self.lab_id = 1
        self.grid_layout = QGridLayout()
        self.runlabel = QLabel(self)
        self.message = QLabel(self)
        self.message.setText("SISTEMA SIN ACCESO A INTERNET! \nUSAR INGRESO MANUAL.")
        self.message.setStyleSheet("font: 18pt \"MS Shell Dlg 2\"; color:red;")
        self.title = QLabel(self)
        self.title.setText("INGRESE RUN: ")
        self.title.setStyleSheet("padding-top:400px; font: 24pt \"MS Shell Dlg 2\";")
        self.setStyleSheet("background-color: 'white';")
        self.runlabel.setStyleSheet("padding-left:25px; font: 28pt \"MS Shell Dlg 2\";")
        self.grid_layout.addWidget(self.message, 0,0)
        self.grid_layout.addWidget(self.title, 0,1)
        self.grid_layout.addWidget(self.runlabel, 1,1)
        self.grid_layout.addWidget(self.createNumberPad(), 2,1)
        self.setLayout(self.grid_layout)
        leftspace = QGroupBox()
        rigthspace = QGroupBox()
        buttomspace = QGroupBox()
        space = QVBoxLayout()
        leftspace.setLayout(space)
        rigthspace.setLayout(space)
        buttomspace.setLayout(space)
        self.submit = QPushButton("Enviar")
        self.submit.clicked.connect(self.sendData)
        self.grid_layout.addWidget(self.submit, 3,1)
        self.grid_layout.addWidget(leftspace, 1,0)
        self.grid_layout.addWidget(rigthspace, 1,2)
        self.grid_layout.addWidget(buttomspace, 4,1)
        self.showFullScreen()
        
    def createNumberPad(self):
        group_box = QGroupBox()
        grid = QGridLayout()
        for x in range(3):
            for y in range(3):
                button = QPushButton(str(str((3*x+y)+1)))
                button.setObjectName(str(str((3*x+y)+1)))
                button.clicked.connect(self.clickedButton)
                grid.addWidget(button, x, y)
        deletebutton = QPushButton("Borrar")
        deletebutton.setObjectName(" ")
        deletebutton.clicked.connect(self.clickedButton)
        kbutton = QPushButton("K")
        kbutton.setObjectName("K")
        kbutton.clicked.connect(self.clickedButton)
        zerobutton = QPushButton("0")
        zerobutton.setObjectName("0")
        zerobutton.clicked.connect(self.clickedButton)
        grid.addWidget(deletebutton, 4,0)
        grid.addWidget(zerobutton, 4,1)
        grid.addWidget(kbutton, 4,2)
        group_box.setLayout(grid)
        return group_box
    
    def sendData(self):
        run = self.runlabel.text()
        if self.checkRun(run):
            run = self.runlabel.text()[:-1]+'-'+self.runlabel.text()[-1]
            data = {'rut': run,
                    'lab_id': self.lab_id}
            print("data:", data)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Rut ingresado correctamente")
            msg.setWindowTitle("Success")
            msg.setBaseSize(QSize(780,350))
            msg.setStyleSheet("font-size:30px;")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Rut ingresado es incorrecto")
            msg.setWindowTitle("ERROR")
            msg.setBaseSize(QSize(780,350))
            msg.setStyleSheet("font-size:45px;")
            msg.exec()
        self.runlabel.setText("")
            
        
    
    def checkRun(self, run):
        if len(run)>9:
            return False
        run = run.upper()
        aux = run[:-1]
        dv = run[-1:]
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
        if str(res) == dv:
            return True
        elif dv=="K" and res==10:
            return True
        else:
            return False        
        
        
    
    def clickedButton(self):
        button = self.sender()
        value = button.objectName()
        if value == ' ':
            if self.runlabel.text():
                self.runlabel.setText(self.runlabel.text()[:-1])
                return
        elif value == 'v':
            self.close()
            return
        if len(self.runlabel.text()) < 10:
            self.runlabel.setText(self.runlabel.text() + '{}'.format(value))
            

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    myapp =NumberPad()
    myapp.show()
    sys.exit(app.exec_())
