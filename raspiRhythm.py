"""
A rhythm game! Choose from 11 different songs of different difficulties to play from. The player can preview and choose the song they want.
When playing the song, the user will click the button every seventh beat (look at LEDs to help).
After each song, the program calculates the score based on when the user pressed the button each time.


Written By: Bryson Lee-Kwen
Date: 2022-01-24
"""


import RPi.GPIO as GPIO
from gpiozero import Buzzer
from time import sleep
import time, sys
from beatsongs import songs, songs_bpm, songs_difficulty


'''


********!!!LIBRARY!!!********


This section plays the musical notes on a Piezo Buzzer using gpiozero library instead of RPi.GPIO
Special thanks to:
https://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/
3 functions:
- buzz(pitch, duration)
- play_note(note, beat)
- play_music(scores)


**!IMPORTANT**


THIS LIBRARY WAS WRITTEN BY: fongkahchun86
Link to library: https://github.com/fongkahchun86/gpiozero_pwm_buzzer
**COMMENTS created by the author are kept in the code**


This library was modified to work with the project needs.
'''

def init(pin):
    return Buzzer(pin)

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
    global mute
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
        if not mute:
            bz.on()
        sleep(delay)
        if not mute:
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
        if playMode and preview:
            return False
    return True
'''
End of library.
'''
        

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


buzzer = init(20)


mute = False # Mutes the buzzer.

seventh_notes = []
user_notes = []

leds = [25,11,10,23,18,15,14]
score_leds = [6,21,19]

beatBtn = GPIO.setup(3,GPIO.IN, pull_up_down=GPIO.PUD_UP) # This button is used for playing the game and selecting the song.
nextBtn = GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_UP) # This button is used to skip songs when selecting a song.
endBtn = GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP) # This button is used to end the program.

skipSong = False # Used for skipping songs when the user previews them
playMode = False # This is used to switch between different modes with the beatBtn. (play beat/select song.3)
currentPreview = 0 # Used to keep track of which song the user is previewing.
selectedSong = 0 # Used to store which song the user wants to play.
timeOfLastSelection = time.time() # Used to debounce button signal when selecting a song.


# In preview mode, used to select songs.
# In play mode, used to click on every seventh beat.
def beatBtnCallback(x):
    global user_notes,playMode, currentPreview, selectedSong, timeOfLastSelection
    if playMode:
        try:
            if time.time() - timeOfLastSelection > 0.2:
                if time.time() - user_notes[-1] > 1: # some debounce checking because duplicates are sometimes given.
                    user_notes.append(time.time())

        except: # This means that the first button press has occured and there is nothing else to compare it to.
            user_notes.append(time.time())

    else:
        # save selected song and switch to play mode.
        timeOfLastSelection = time.time()
        selectedSong = currentPreview
        playMode = True

# Used in preview mode to skip the preview of songs.
def skipBtnCallback(x):
    global skipSong
    skipSong = True

# Used to turn off all LED and safely exit the program.
def endBtnCallback(x):
    for led in leds:
        GPIO.output(led,GPIO.LOW)
    for led in score_leds:
        GPIO.output(led,GPIO.LOW)
    GPIO.cleanup(GPIO.BCM)
    sys.exit()

# Gets the score based on when the seventh beats appear in the song and when the user pressed the button.
def getScore(seventh_notes,user_notes):
    score = len(seventh_notes) # Every seventh note brings the start score up by one. (This is to allow fairness betweeen shorter and longer songs)
    ogscore = score # Used for comparing final score (score) with original score (ogscore).
    toKeep = [] # keeps track of the which button presses can be related to a seventh beat. All other button presses not in this list will lower score.
    for note in seventh_notes:
        closest = 999 # This is placeholder. High number(999) means the score will be a negative and not just a perfect score if no buttons are pressed BECAUSE this variable is being subctracted from the score.
        toAppend = 0
        for unote in user_notes:
            
            if abs(note - unote) < closest: # If the difference in time is closest to the beat then that is the note that is related to the seventh beat (so far).
                closest = abs(note - unote) # Difference in seconds from when the user is supposed to click the beat and when the user DOES click the beat.
                toAppend = closest
        toKeep.append(note - closest) # get the the time that the user pressed the button by undoing the subtraction equation.
        score -= closest # remove the difference in time from the seventh beat to when the button press occurs from the score.

    # This for loop below is to prevent users from just spamming the button.
    # The old system allowed for button spamming to give a decent score but now, for every time the button was pressed and a seventh beat did NOT play, the score will be lowered.
    # This also means that accidentally pressing a button at the wrong note can be punished harshly IF the user attempts to fix their mistake.
    # It is SOMETIMES better to not play a note at all than it is to try to fix a mistake.
    # If the mistake was made 0.5 seconds away or more from the green LED then fixing the mistake will be OK because it can't get worse.
    # If the mistake was made less than 0.5 seconds away from the green LED then fixing the mistake will penalize the score MORE because no matter what 0.5 will be deducted including the time when the user fixes the mistake.
    for _ in range(len(user_notes) - len(toKeep)):
        score -= 0.5 

    return score, ogscore



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



if __name__ == "__main__":

    while True:


        for led in score_leds: # This resets the score/difficulty display.
            GPIO.output(led,GPIO.LOW)
        playMode = False
        seventh_notes = [] # this contains the time for everytime a seventh beat appears.
        user_notes = [] # this contains the time for everytime the user presses the button (in play mode).


        while not playMode:

            # Get the users selected song.
            for i in range(len(songs)):
                currentPreview = i

                # Display the difficulty.
                for num in songs_difficulty[i]:
                    GPIO.output(score_leds[num],GPIO.HIGH)

                # Go through each part in the song (some songs have multiple parts so a for loop will go through each part.)
                for j in range(len(songs[i])): 
                    #                song         bpm            buzzer  preview mode
                    tmp = play_music(songs[i][j],songs_bpm[i][j],buzzer, True)


                    if not tmp: # Prevents the skip button from just skipping to the next part of multipart songs and instead moves on to the next song.
                        break


                if playMode: # If the song has been chosen, playmode will be true and preview mode will be broken out of.
                    break

                # Reset the difficulty indicator LEDs after each song preview.
                for led in score_leds:
                    GPIO.output(led,GPIO.LOW)
            #############################
        
        
        time.sleep(1)

        for led in score_leds: # This resets the difficulty display and will be now used to display score.
            GPIO.output(led,GPIO.LOW)

        # play the song selected.
        for i in range(len(songs[selectedSong])):
            play_music(songs[selectedSong][i],songs_bpm[selectedSong][i],buzzer,False)
   

        # retrieve the score by comparing times of seventh notes and when the button was pressed
        score, ogscore = getScore(seventh_notes,user_notes)


        # Show different LED based on score.
        if score >= ogscore * 0.9: # keeping >90% of original score will give full points.
            GPIO.output(score_leds[0],GPIO.HIGH)
            GPIO.output(score_leds[1],GPIO.HIGH)
            GPIO.output(score_leds[2],GPIO.HIGH)
        elif score >= ogscore * 0.7: # > 70% of original score give 2/3 points.
            GPIO.output(score_leds[0],GPIO.HIGH)
            GPIO.output(score_leds[1],GPIO.HIGH)
        else: # everything below is 1/3 points.
            GPIO.output(score_leds[0],GPIO.HIGH)
        time.sleep(3)
