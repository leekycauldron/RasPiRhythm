from gpiozero_pwm_buzzer import init, play_music, notes
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


buzzer = init(20)
DUST_BPM = 180
STOP_BPM = 188

leds1 = [23,18,15,14]

leds3 = [5,11,9,10]

# Setup each LED
for led in leds1:
        GPIO.setup(led,GPIO.OUT)
        GPIO.output(led,GPIO.LOW)


for led in leds3:
        GPIO.setup(led,GPIO.OUT)
        GPIO.output(led,GPIO.LOW)

dust_notes = []
stop_notes = []

notes_indexes = ['C','C#','Db','D','D#','Eb','E','F','F#','Gb','G','G#','Ab','A','A#','Bb','B']

dust = ['F4:0.25','E4:0.25','C4:1','C4:1','C4:1','R:0.375','C4:0.125',
        'C4:0.5','C4:0.5','E4:0.5','C4:0.25','F4:1.25','R:0.25',
        'F4:0.25','E4:0.25','C4:1','C4:1','C4:1','R:0.375','C4:0.125',
        'C4:0.5','C4:0.5','E4:0.5','C4:0.25','F4:1.25','R:0.25',
        'F4:0.25','E4:0.25','E4:0.25','E4:0.25','E4:0.5','E4:0.25','E4:0.25',
        'E4:0.25','G4:0.75','E4:0.5','E4:0.5','E4:0.25','E4:0.25','B4:0.5','B4:0.5',
        'A4:0.25','B4:0.5','A4:1.25','R:0.5','E4:0.25','E4:0.25','E4:0.5',
        'E4:0.5','E4:0.5','E4:0.25','E4:0.25','G4:0.25','G4:0.25','G4:0.25',
        'A4:1','A4:0.25','B4:0.5','B4:0.5','B4:0.25','B4:0.25','B4:0.25',
        'A4:1.75','B4:0.25','B4:0.25','C5:0.25','C5:0.5','C5:0.75','C5:0.25','C5:0.25',
        'D5:0.25','D5:0.25','D5:0.25','F5:0.75','G4:0.25','G4:0.25','C5:0.25',
        'C5:0.25','C5:0.25','C5:0.25','C5:0.25','C5:0.25','C5:0.25','D5:1.25','R:1',
        'C5:0.25','C5:0.25','C5:0.25','C5:0.5','C5:0.5','C5:0.25','D5:0.25','D5:0.5',
        'D5:1.25','R:0.5','A4:0.25','A4:0.25','A4:0.25','A4:0.25','A4:0.25','B4:1.25',
        'G4:0.5','F4:0.25','E4:0.25','C4:1','C4:1','C4:1','R:0.75','C4:0.25',
        'E4:0.25','E4:0.25','E4:0.5','G4:0.5','E4:0.25','A4:1.25','R:0.5','F4:0.25','E4:0.25',
        'C4:1','C4:1','C4:1','R:0.75','C4:0.25', 'E4:0.25','E4:0.25','E4:0.5','G4:0.5',
        'E4:0.25','A4:1.25','R:0.5','B4:0.25','B4:0.25','A4:0.25','A4:0.25','G4:0.5',
        'E4:0.5','B4:0.25','B4:0.25','A4:0.25','A4:0.25','G4:0.5','E4:0.75','B4:0.25',
        'B4:0.25','B4:0.25','B4:0.5','B4:0.25','B4:0.25','A4:1.5','F4:1.25',
        'F4:0.25','F4:0.25','F4:0.25','A4:0.5','A4:0.5','A4:0.75','A4:0.25', 
        'E4:0.25','E4:0.25','E4:0.5','G4:0.5', 'E4:0.25','A4:1.25','F4:0.25','E4:0.25','C4:0.5']
dust_notes = [[0,0,1,1,1,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0]]

stop = ['G4:0.5','G4:0.5','F4:1','F4:0.5','F4:0.5','A4:0.5','C5:0.5','F5:0.5',
        'E5:1','R:0.5','C5:0.5','A4:0.5','G4:1','F4:1.5','R:1.5','A4:0.25','G4:0.75',
        'G4:0.25','E4:0.25','G4:1','D4:0.5','A4:1','B4:1','C5:2.5','R:1','D5:0.5','E5:0.5',
        'F5:3','R:0.5','F4:0.5','A5:1','B5:0.5','A5:1','G5:1','F5:2','D5:1.5','R:0.5',
        'F4:0.5','A5:0.5','A5:0.5','B5:0.5','A5:1.5','R:0.5','G5:0.5','F#5:0.5','G5:1',
        'A5:1.5','D5:1','B5:0.5','R:1','A5:0.5','R:0.5','G5:0.5','R:0.5','B4:2.5'] # Ended on the first "Dont stop me now" long note



# TODO: THIS IS FOR USING MULTIPLE LEDS.
# Generate the notes for the leds.
def gen_notes(song,bpm,notes_list):
        heights = []
        high = 0
        low = 0
        for note in song:
                note_id = note.split(":")[0] # Cut off the note length.
                if note_id != "R":
                        raw_note = note_id[:-1]
                        heights.append(notes_indexes.index(raw_note))
                        heights.sort(reverse=True)
                        # Get the highest and lowest note that appear in the song.
                        high = heights[0]
                        low = heights[-1]
        for note in song:
                
                note_id = note.split(":")[0] # Cut off the note length.
                note_length = note.split(":")[1]
                # append the amount of time that the led will lead up to the "go" led
                # also append the amount of time that the "go" led will light up
                if note_id == "R":
                        notes_list.append(float(note_length) * 69) # encode it so that when the notes are played it can be reversed 
                        # multiplying by a big number will allow it to exceed the threshold
                else:
                        raw_note = note_id[:-1] # remove the last character which  is the number that says what octave the note is in.
                        idx = notes_indexes.index(raw_note)
                        diff_high = high - idx
                        diff_low = idx - low
                        if diff_high <= diff_low: # The note is higher because it is closer to the highest note.
                                print("high")
                                notes_list.append(float(note_length) * (60 / bpm) / 2)
                        elif diff_low < diff_high: # Note is lower if closer/equal to lowest note.
                                print("low")
                                notes_list.append((float(note_length) * (60 / bpm) / 2) * -1) # Change to negtive to differ a high note from a low note.
                
        return notes_list

def play_notes(notes_list):
  
        for note in range(len(notes_list)):
                if notes_list[note] < 10:
                        if notes_list[note] < 0: # Play on low (left) LED row.
                                # Dividing the negative length by -1 will turn to positive which gives the true note length.

                               
                    
                                
                                GPIO.output(leds1[3],GPIO.HIGH)
                                time.sleep(notes_list[note] * -1 )
                                GPIO.output(leds1[3],GPIO.LOW)
                                time.sleep(notes_list[note] * -1)
                        else: # Play on high (right) LED row
                                
                      
                                
                                GPIO.output(leds3[3],GPIO.HIGH)
                                time.sleep(notes_list[note])
                                GPIO.output(leds3[3],GPIO.LOW)
                                time.sleep(notes_list[note])

                else: # Rest during rests
                        time.sleep(notes_list[note] / 69)

                
                
dust_notes = gen_notes(dust,DUST_BPM, dust_notes)
def t1():
        play_music(dust,DUST_BPM,buzzer)
def t2():
        play_notes(dust_notes)

stop_notes = gen_notes(stop,STOP_BPM, stop_notes)
def t3():
        play_music(stop,STOP_BPM,buzzer)
def t4():
        play_notes(stop_notes)

threading.Thread(target=t1).start()
threading.Thread(target=t2).start()
#play_music(stop,188,buzzer)


