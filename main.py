import time, sys
import RPi.GPIO as GPIO
from gpiozero import Button
import songs
from utils import notes
from gpiozero_pwm_buzzer import notes

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
buzzer = GPIO.PWM(21, 440)
buzzer1 = GPIO.PWM(20, 440)  
endBtn = GPIO.setup(2, GPIO.IN)

preview_interrupt = False # will interrupt the song previews if the user exits or chooses a song

def endProgram(pin):
    global preview_interrupt
    preview_interrupt = True #just end song for now (skip button)
    print("skipping...",pin)

GPIO.add_event_detect(2,GPIO.RISING,callback=endProgram)


DC = 75


def exit():
        time.sleep(1)
        #GPIO.cleanup()
        sys.exit()


def playSong(songId):
    global preview_interrupt

    for section in range(len(songs.songs[songId][0])): # This is to get each "verse" or section
            
        for repeats in range(songs.songs[songId][0][section][1]): # This will repeat the "section" of notes a specified amount of times
            for i in range(len(songs.songs[songId][0][section][0])): # This goes through all the notes
                idx = notes[songs.songs[songId][0][section][0][i]]
                if songs.songs[songId][0][section][0][i] != -1:
                    buzzer.ChangeFrequency(idx)
                    buzzer1.ChangeFrequency(idx)
                    buzzer.start(DC)
                    buzzer1.start(DC)
                    time.sleep(songs.songs[songId][1][section][i])
                    buzzer.stop()
                    buzzer1.stop()
                else:       
                    time.sleep(songs.songs[songId][1][section][i])
                if preview_interrupt:
                    preview_interrupt = False
                    return 0


while True:
    for i in range(11):
        try:
            playSong(i)
        except: pass

