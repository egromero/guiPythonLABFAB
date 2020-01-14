# Sound1a.py

import time
from soundplayer import SoundPlayer

# Use device with ID 1  (mostly USB audio adapter)
#p = SoundPlayer("//home/pi/Desktop/Sonido/Beep1.mp3", 0)
#p = SoundPlayer("//home/pi/Desktop/Sonido/Beep2.mp3", 0)
#p = SoundPlayer("//home/pi/Desktop/Sonido/Alarm.mp3", 0)
p = SoundPlayer("//home/pi/Desktop/Sonido/John Cena - My Time Is Now.mp3", 0)  
print ("play for 10 s with volume 0.5")
p.play(0.5) # non-blocking, volume = 0.5 (0 a 1)
##print ("isPlaying:", p.isPlaying())
time.sleep(1)
##print ("pause for 5 s")
##p.pause()
##print ("isPlaying:", p.isPlaying())
##time.sleep(5)
##print ("resume for 10 s")
##p.resume()
##time.sleep(10)
##print ("stop")
##p.stop()
##print ("isPlaying:", p.isPlaying())
##print ("done")

