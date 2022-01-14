from glob import glob
import RPi.GPIO as GPIO
from gpiozero import Buzzer
from time import sleep
import time, sys


def init(pin): # Simply intilializes the buzzer to be used for playing songs.
    return Buzzer(pin)



'''
This section plays the musical notes on a Piezo Buzzer using gpiozero library instead of RPi.GPIO
Special thanks to:
https://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/
3 functions:
- buzz(pitch, duration)
- play_note(note, beat)
- play_music(scores)


This library was written by: fongkahchun86
Link to library: https://github.com/fongkahchun86/gpiozero_pwm_buzzer/security

This library was modified to work with the project needs.
'''

#Note's frequency based on Scientific pitch number
#Rest is denoted as 'R'.
#URL: https://en.wikipedia.org/wiki/Scientific_pitch_notation#Table_of_note_frequencies
notes = {'C'  : [16.352, 32.703, 65.406, 130.81, 261.63, 523.25, 1046.5, 2093.0, 4186.0, 8372.0, 16744],
         'C#' : [17.324, 34.648, 69.296, 138.59, 277.18, 554.37, 1108.7, 2217.5, 4434.9, 8869.8, 17740],
         'Db' : [17.324, 34.648, 69.296, 138.59, 277.18, 554.37, 1108.7, 2217.5, 4434.9, 8869.8, 17740],
         'D'  : [18.354, 36.708, 73.418, 146.83, 293.66, 587.33, 1174.7, 2349.3, 4698.6, 9397.3, 18795],
         'D#' : [19.445, 38.891, 77.782, 155.56, 311.13, 622.25, 1244.5, 2489.0, 4978.0, 9956.1, 19912],
         'Eb' : [19.445, 38.891, 77.782, 155.56, 311.13, 622.25, 1244.5, 2489.0, 4978.0, 9956.1, 19912],
         'E'  : [20.602, 41.203, 82.407, 164.81, 329.63, 659.26, 1318.5, 2637.0, 5274.0, 10548, 21096],
         'F'  : [21.827, 43.654, 87.307, 174.61, 349.23, 698.46, 1396.9, 2793.8, 5587.7, 11175, 22351],
         'F#' : [23.125, 46.294, 92.499, 185.00, 369.99, 739.99, 1480.0, 2960.0, 5919.9, 11840, 23680],
         'Gb' : [23.125, 46.294, 92.499, 185.00, 369.99, 739.99, 1480.0, 2960.0, 5919.9, 11840, 23680],
         'G'  : [24.500, 48.999, 97.999, 196.00, 392.00, 783.99, 1568.0, 3136.0, 6271.9, 12544, 25088],
         'G#' : [25.957, 51.913, 103.83, 207.65, 415.30, 830.61, 1661.2, 3322.4, 6644.9, 13290, 26580],
         'Ab' : [25.957, 51.913, 103.83, 207.65, 415.30, 830.61, 1661.2, 3322.4, 6644.9, 13290, 26580],
         'A'  : [27.500, 55.000, 110.00, 220.00, 440.00, 880.00, 1760.0, 3520.0, 7040.0, 14080, 28160],
         'A#' : [29.135, 58.270, 116.54, 233.08, 466.16, 932.33, 1864.7, 3729.3, 7458.6, 14917, 29834],
         'Bb' : [29.135, 58.270, 116.54, 233.08, 466.16, 932.33, 1864.7, 3729.3, 7458.6, 14917, 29834],
         'B'  : [30.868, 61.735, 123.47, 246.94, 493.88, 987.77, 1975.5, 3951.1, 7902.1, 15804, 31609],
         'R'  : 0
            }

def buzz(pitch, duration,bz):
    '''
    Cause the buzzer to produce a buzz according to a pitch in a note frequency number (Hz)
    for a duration in seconds.
    To produce a C4 note for half a second.
    >>> buzz(261.63, 0.5)
    '''
    if pitch == 0:
        sleep(duration)
        return
    period = 1.0 / pitch #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
    delay = period / 2 #calculate the time for half of the wave
    cycles = int(round(duration * pitch, 0)) #the number of waves to produce is the duration times the frequency
    
    for i in range(cycles):
        bz.on()
        sleep(delay)
        bz.off()
        sleep(delay)
        
def play_note(note, beat,bpm,bz):
    '''
    Cause the buzzer to produce a buzz according to a musical note in a particular
    octave for a number of beats.
    Musical note in  a particular octave is a string value in upper case letter followed
    by the octave number.
    Sharp and flat notes are represented by '#' and lower case 'b' respectively.
    Duration of a beat depends on the bpm variable. Default bpm = 120
    
    To produce middle C for a beat:
    >>> play_note('C4', 1)
    To produce middle F# for 2 beats:
    >>> play_note('F#4', 2)
    To produce middle B flat for half a beat:
    >>> play_note('Bb4', 0.5)
    '''
    duration = beat * (60 / bpm)
    if note != 'R':
        curr_pitch = notes[note[:-1]][int(note[-1])]
    else:
        curr_pitch = 0
    buzz(curr_pitch, duration,bz)
    sleep(duration * 0.5)

def play_music(scores,bpm,bz, preview):
    global seventh_notes, skipSong, playMode
    '''
    Buzzer will play a list of scores in string.
    To play the middle octave with sharp or flat notes for one beat each:
    >>> middle_octave = ['C4:1', 'C#4:1', 'D4:1', 'Eb4:1', 'E4:1', 'F4:1', 'F#4:1', 'G4:1', 'Ab4:1', 'A4:1', 'A#4:1', 'B4:1']
    >>> play_music(middle_octave)
    '''
    counter = 0
    for i in range(len(scores)):
        print(counter)
        curr_note = scores[i]
        tune = curr_note.split(':')[0]
        beat = float(curr_note.split(':')[1])
        if tune != "R":
            if counter >= 6 and not preview:
                seventh_notes.append(time.time()) # only the time of the seventh notes is recorded.
            GPIO.output(leds[counter],GPIO.HIGH)
            play_note(tune, beat,bpm,bz) # This doubles as a "wait until note stops playing to continue"
            GPIO.output(leds[counter],GPIO.LOW)

            if counter >= 6:
                
                counter = 0
            
            else:
                counter += 1
        else: 
            play_note(tune, beat,bpm,bz)
        if skipSong and preview: # The user can only skip songs during the preview, not when they are playing.
            skipSong = False
            return False
        if playMode:
            return False
    return True
'''
End of library.
'''
        


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


buzzer = init(20)
DUST_BPM = 150
STOP1_BPM = 188
STOP2_BPM = 300
TAKE_BPM = 338

leds = [25,11,10,23,18,15,14]
score_leds = [6,13,19]

beatBtn = GPIO.setup(3,GPIO.IN, pull_up_down=GPIO.PUD_UP) # This button is used for playing the game and selecting the song.
nextBtn = GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_UP) # This button is used to skip songs when selecting a song.
endBtn = GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP) # This button is used to end the program.

skipSong = False # Used for skipping songs when the user previews them
playMode = False # This is used to switch between different modes with the beatBtn. (play beat/select song.3)
currentPreview = 0 # Used to keep track of which song the user is previewing.
selectedSong = 0 # Used to store which song the user wants to play.
timeOfLastSelection = time.time() # Used to debounce button signal when selecting a song.


def beatBtnCallback(x):
    global user_notes,playMode, currentPreview, selectedSong, timeOfLastSelection
    if playMode:
        try:
            if time.time() - timeOfLastSelection > 0.2:
                if time.time() - user_notes[-1] > 1: # some debounce checking because duplicates are sometimes given.
                    print('Button pressed! This event has been logged.')
                    user_notes.append(time.time())
        except: # This means that the first button press will be logged. There is nothing else to compare it to.
  
            print('Button pressed! This FIRST event has been logged.')
            user_notes.append(time.time())
    else:
        print("selected song")
        timeOfLastSelection = time.time()
        selectedSong = currentPreview
        playMode = True

def skipBtnCallback(x):
    global skipSong
    print("Skipping Song...")
    skipSong = True

def endBtnCallback(x):
    print('Ending program')
    for led in leds:
        GPIO.output(led,GPIO.LOW)
    for led in score_leds:
        GPIO.output(led,GPIO.LOW)
    GPIO.cleanup(GPIO.BCM)
    sys.exit()

GPIO.add_event_detect(3,GPIO.RISING,callback=beatBtnCallback)
GPIO.add_event_detect(4,GPIO.RISING,callback=skipBtnCallback)
GPIO.add_event_detect(2,GPIO.RISING,callback=endBtnCallback)


# Setup each LED
for led in leds:
        GPIO.setup(led,GPIO.OUT)
        GPIO.output(led,GPIO.LOW)
for led in score_leds:
        GPIO.setup(led,GPIO.OUT)
        GPIO.output(led,GPIO.LOW)

dust_notes = []


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

stop1 = ['G4:0.5','G4:0.5','F4:1','F4:0.5','F4:0.5','A4:0.5','C5:0.5','F5:0.5',
        'E5:1','R:0.5','C5:0.5','A4:0.5','G4:1','F4:1.5','R:0.25','A4:0.25','G4:0.75',
        'G4:0.25','E4:0.25','G4:1','D4:0.5','A4:1','B4:1','C5:2.5','R:1','D5:0.5','E5:0.5',
        'F5:3','R:0.5','F4:0.5','A5:1','B5:0.5','A5:1','G5:1','F5:2','D5:1.5','R:0.5',
        'F4:0.5','A5:0.5','A5:0.5','B5:0.5','A5:1.5','R:0.5','G5:0.5','F#5:0.5','G5:1',
        'A5:1.5','D5:1','B5:0.5','R:1','A5:0.5','R:0.5','G5:0.5','R:0.5','B4:2.5','B5:0.5',
        'R:1','A5:0.5','R:0.5','G5:0.5','G5:0.5','G5:0.5'] # After this note BPM changes.
    
stop2 = ['B4:0.5','B4:0.5','B4:0.5','C5:1','D5:1.5','E5:0.5','E5:0.5','E5:0.5',
         'F5:1','G5:0.5','A4:0.5','A4:0.5','G4:0.5','F4:0.5','F4:1','F4:0.5','A4:0.5',
         'C5:0.5','F5:0.5','E5:2.5','C5:0.5','A4:0.5','G4:1','F4:0.5','R:0.5','F4:0.5',
         'A4:0.5','G4:0.5','F4:0.5','G4:1','G4:1.5','A4:0.5','B4:1','C5:2.5','R:1',
         'A4:0.5','A4:0.5','G4:0.5','F4:0.5','F4:1','R:0.5','C5:0.5','F5:0.5','E5:2','C5:0.5',
         'A5:0.5','A5:0.5','A5:0.5','G5:1','F5:1.5','R:0.5','A4:0.5','G4:0.5','F4:0.5','G4:0.5',
         'R:1','A4:0.5','R:1','B4:1','R:0.5','C5:1','C5:0.5','D5:0.5','E5:1','F5:3','R:0.5',
         'C5:0.5','A5:1','B5:0.5','A5:1','G5:1','F5:2','D5:1.5','R:0.5','A5:0.5','A5:0.5',
         'A5:0.5','B5:0.5','A5:1','G5:0.5','G5:0.5','G5:0.5','F#5:0.5','F#5:0.5','F#5:0.5',
         'F#5:0.5','G5:0.5','A5:0.5','R:0.5','A5:3'] 

take = ['F5:0.5','F5:0.5','D5:0.5','B4:0.5','R:0.5','B4:0.5','R:0.5','E5:0.5',
        'R:0.5','E5:0.5','R:0.5','E5:0.5','G5:0.5','G5:0.5','A5:0.5','B5:0.5',
        'A5:0.5','A5:0.5','A5:0.5','E5:0.5','R:0.5','D5:0.5','R:0.5','F5:0.5',
        'R:0.5','F5:0.5','R:0.5','F5:0.5','E5:0.5','E5:0.5','F5:0.5','E5:0.5',
        'F5:0.5','F5:0.6','D5:0.5','B4:0.5','R:0.5','B4:0.5','R:0.5','E5:0.5',
        'R:0.5','E5:0.5','R:0.5','E5:0.5','G5:0.5','G5:0.5','A5:0.5','B5:0.5',
        'A5:0.5','A5:0.5','A5:0.5','E5:0.5','R:0.5','D5:0.5','R:0.5','F5:0.5',
        'R:0.5','F5:0.5','R:0.5','F5:0.5','E5:0.5','E5:0.5','F5:0.5','E5:0.5',
        'F5:0.5','F5:0.6','D5:0.5','B4:0.5','R:0.5','B4:0.5','R:0.5','E5:0.5',
        'R:0.5','E5:0.5','R:0.5','E5:0.5','G5:0.5','G5:0.5','A5:0.5','B5:0.5',
        'A5:0.5','A5:0.5','A5:0.5','E5:0.5','R:0.5','D5:0.5','R:0.5','F5:0.5',
        'R:0.5','F5:0.5','R:0.5','F5:0.5','E5:0.5','E5:0.5','F5:0.5','E5:0.5',
        'D4:1.5','D4:0.5','R:0.5','C4:0.5','B3:1','R:2','C4:0.5','C4:0.5',
        'R:0.5','C4:0.5','R:0.5','A3:0.5','R:1','R:0.5','F4:0.5','R:0.5','F4:0.5',
        'F4:1','E4:1','D4:1','D4:0.5','D4:0.5','C4:0.5','R:0.5','B3:0.5','R:3.5',
        'B3:0.5','C4:1','D4:0.5','C4:0.5','R:0.5','B3:0.5','R:0.5','A3:0.5','R:0.5',
        'B3:0.5','R:0.5','C4:0.5','B3:1','A3:1','D4:1','D4:1','D4:0.5','D4:0.5','R:5',
        'A3:0.5','A3:0.5','A3:0.5','A3:0.5','A3:0.5','A3:0.5','A3:0.5','G3:0.5','R:1',
        'G3:0.5','F3:0.5','R:1','C4:4','G4:4','A4:4','E4:1','R:0.5','F4:0.5','R:1','E4:1',
        'A4:4','E5:4','F5:4','E4:1','R:0.5','F4:0.5','R:1','E4:1','C5:4','G5:4','A5:4','R:1',
        'G5:0.5','A5:1','G5:0.5','F5:1','R:1','C6:6']

songs = [
    [dust],
    [stop1,stop2], 
    [take]
]

songs_bpm = {
    0: [DUST_BPM],
    1: [STOP1_BPM,STOP2_BPM],
    2: [TAKE_BPM]
}

if __name__ == "__main__":
    while True:
        playMode = False
        seventh_notes = [] # this contains the time for everytime a seventh note appears
        user_notes = [] # this contains the time for everytime the user presses the button
        while not playMode:
            # Get the users selected song.
            for i in range(len(songs)):
                currentPreview = i
                for j in range(len(songs[i])): # This is for songs with multiple parts
                    print("Playing song with BPM:",str(songs_bpm[i])) # DELETE
                    
                    tmp = play_music(songs[i][j],songs_bpm[i][j],buzzer, True)
                    if not tmp: # This is needed because for multi-part songs, the user might just skip to the next part and not the next song.
                        break
                if playMode:
                    break

        print("Selected song is song number",str(selectedSong))
        #print(seventh_notes)
        #print(user_notes)
        time.sleep(1)
