#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import requests


continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

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
        print('UID: ',uid)
        print(type(uid[0]))
        rfid = ''.join([str(hex(i))[2:] if i>16 else '0'+str(hex(i))[2:] for i in uid ])[:-2]
        print('c',rfid)
        #rfid = str(hex(uid[3]))[2:]+str(hex(uid[2]))[2:]+str(hex(uid[1]))[2:]+str(hex(uid[0]))[2:]
        rfid = str(hex(uid[0]))[2:]+str(hex(uid[1]))[2:]+str(hex(uid[2]))[2:]+str(hex(uid[3]))[2:]
        print(rfid)
        #r = requests.post("https://redlabuc.herokuapp.com/records", data={'rfid':rfid,'tipo':"ingreso"})
        #print(r)
        

