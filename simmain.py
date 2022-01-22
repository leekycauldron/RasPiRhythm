from tkgpio import TkCircuit


configuration = {
    "width": 500,
    "height": 250,

    "buzzers": [
        {"x": 50, "y": 170, "name": "Buzzer", "pin": 18}
    ]
}

circuit = TkCircuit(configuration)
@circuit.run
def main ():
    
    from gpiozero import Buzzer
    from time import sleep
    bz = Buzzer(18)
    bpm = 120 #usually 120

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

    def buzz(pitch, duration):
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
            
    def play_note(note, beat):
        '''
        Cause the buzzer to produce a buzz according to a musical note in a particular
        octave for a number of beats.
        Musical note in  a particular octave is a string value in upper case letter followed
        by the octave number.
        Sharp and flat notes are represented by lower case 'b' and '#' respectively.
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
        buzz(curr_pitch, duration)
        sleep(duration * 0.5)

    def play_music(scores):
        '''
        Buzzer will play a list of scores in string.
        To play the middle octave with sharp or flat notes for one beat each:
        >>> middle_octave = ['C4:1', 'C#4:1', 'D4:1', 'Eb4:1', 'E4:1', 'F4:1', 'F#4:1', 'G4:1', 'Ab4:1', 'A4:1', 'A#4:1', 'B4:1']
        >>> play_music(middle_octave)
        '''
        for curr_note in scores:
            tune = curr_note.split(':')[0]
            beat = float(curr_note.split(':')[1])
            play_note(tune, beat)

    happy_bday = ['D4:0.75', 'D4:0.25', 'E4:1', 'D4:1', 'G4:1', 'F#4:2',
                'D4:0.75', 'D4:0.25', 'E4:1', 'D4:1', 'A4:1', 'G4:2',
                'D4:0.75', 'D4:0.25', 'D5:1', 'B4:1', 'G4:1', 'F#4:1', 'E4:1',
                'C5:0.75', 'C5:0.25', 'B4:1', 'G4:1', 'A4:1', 'G4:2']

    play_music(happy_bday)

    ode = ['E4:1', 'E4:1', 'F4:1', 'G4:1', 'G4:1', 'F4:1', 'E4:1', 'D4:1',
        'C4:1', 'C4:1', 'D4:1', 'E4:1', 'E4:1.5', 'D4:0.5', 'D4:2',
        'E4:1', 'E4:1', 'F4:1', 'G4:1', 'G4:1', 'F4:1', 'E4:1', 'D4:1',
        'C4:1', 'C4:1', 'D4:1', 'E4:1', 'D4:1.5', 'C4:0.5', 'C4:2',
        'D4:1', 'D4:1', 'E4:1', 'C4:1', 'D4:1', 'F4:1', 'E4:1', 'C4:1',
        'D4:1', 'F4:1', 'E4:1', 'D4:1', 'C4:1', 'D4:1', 'G4:2',
        'E4:1', 'E4:1', 'F4:1', 'G4:1', 'G4:1', 'F4:1', 'E4:1', 'D4:1',
        'C4:1', 'C4:1', 'D4:1', 'E4:1', 'D4:1.5', 'C4:0.5', 'C4:2',]

    #play_music(ode)

    rondo = ['B4:0.25', 'A4:0.25', 'G#4:0.25', 'A4:0.25', 'C5:0.5', 'R:0.5',
            'D5:0.25', 'C5:0.25', 'B4:0.25', 'C5:0.25', 'E5:0.5', 'R:0.5',
            'F5:0.25', 'E5:0.25', 'D#5:0.25', 'E5:0.25', 'B5:0.25', 'A5:0.25', 'G#5:0.25',
            'A5:0.25', 'B5:0.25', 'A5:0.25', 'G#5:0.25', 'A5:0.25', 'C6:1']
    
    #play_music(rondo)

    """def exit():
        time.sleep(1)
        #GPIO.cleanup()
        sys.exit()

    time.sleep(1)
    def playSong(songId):
        for section in range(len(songs.songs[songId][0])): # This is to get each "verse" or section
            
            for repeats in range(songs.songs[songId][0][section][1]): # This will repeat the "section" of notes a specified amount of times
                for i in range(len(songs.songs[songId][0][section][0])): # This goes through all the notes
                    idx = notes[songs.songs[songId][0][section][0][i]]
                    if songs.songs[songId][0][section][0][i] != -1:
                        #buzzer.ChangeFrequency(idx)
                        #buzzer.frequency = idx
                        buzzer.value = idx /100
               
                        time.sleep(songs.songs[songId][1][section][i])
           
                        buzzer.value = 0
                    else:
                        time.sleep(songs.songs[songId][1][section][i])

            
                    buzzer.value = 0
                    time.sleep(0.05)



    try:
        while True:
            playSong(int(input("What number?")))

    except KeyboardInterrupt as e:
        print("Ctrl+C invoked, exiting program...")
        exit()    """


    

main()

