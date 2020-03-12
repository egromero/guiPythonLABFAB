import RPi.GPIO as GPIO
import MFRC522
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from soundplayer import SoundPlayer
import time
import credentials
from check_internet_connection import check
import local_manager


lab_id = 1
gral_url = 'http://peaceful-cove-91834.herokuapp.com/'

class Reader(QThread):
    
    sig1 = pyqtSignal(dict)
    sig2 = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        
    
    def run(self):
        url = gral_url+"records"
        continue_reading = True
        
        MIFAREReader = MFRC522.MFRC522()
        
        while continue_reading:
            
   
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            
            if check():  
                if status == MIFAREReader.MI_OK:
                    rfid = ''.join([str(hex(i))[2:] if i>16 else '0'+str(hex(i))[2:] for i in uid ])[:-2]
                    rfid = rfid.upper()
                    print(rfid)
                    p = SoundPlayer("/home/pi/guiPythonLABFAB/sounds/BeepIn.mp3", 0)
                    p.play(1)
                    time.sleep(0.001)
                
                    req = requests.post(url, {'rfid':rfid,'lab_id':lab_id}, headers=credentials.totem_credential).json()
                    if not req:
                        req = rfid
                        self.sig2.emit(req)                
                    else:
                        self.sig1.emit(req)
                        time.sleep(5)
            else:
                local_manager.NumberPad.show()
#      
               # except:
               #     req = 'Not Internet Conection'
               #     self.sig2.emit(req)
                    
                

            
                    
                GPIO.cleanup()
    