"""
File containing all 11 songs with their bpm and difficulty.


Written by: Bryson Lee-Kwen
Date: 2022-01-24

Song List (in order of creation but not how it shows up in-game.):
1. Another One Bites the Dust.
2. Don't Stop Me Now.
3. Take On Me.
4. The Scale.
5. Somebody To Love.
6. Fly Me To The Moon.
7. Jingle Bell Rock.
8. Never Gonna Give You Up.
9. All Of Me.
10. Dance of The Sugar Plum Fairy.
11. Jojo's Bizarre Adventure: Golden Wind - Giorno's Theme Ver. 2.
"""

dust = ['F4:0.25','E4:0.25','C4:1','C4:1','C4:1','R:0.375','C4:0.125', # Another One Bites the Dust.
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

stop1 = ['G4:0.5','G4:0.5','F4:1','F4:0.5','F4:0.5','A4:0.5','C5:0.5','F5:0.5', # Don't Stop Me Now.
        'E5:1','R:0.5','C5:0.5','A4:0.5','G4:1','F4:1.5','R:0.25','A4:0.25','G4:0.75',
        'G4:0.25','E4:0.25','G4:1','D4:0.5','A4:1','B4:1','C5:2.5','R:1','D5:0.5','E5:0.5',
        'F5:3','R:0.5','F4:0.5','A5:1','B5:0.5','A5:1','G5:1','F5:2','D5:1.5','R:0.5',
        'F4:0.5','A5:0.5','A5:0.5','B5:0.5','A5:1.5','R:0.5','G5:0.5','F#5:0.5','G5:1',
        'A5:1.5','D5:1','B5:0.5','R:1','A5:0.5','R:0.5','G5:0.5','R:0.5','B4:2.5','B5:0.5',
        'R:1','A5:0.5','R:0.5','G5:0.5','G5:0.5','G5:0.5'] # After this note BPM changes so this song is split into two parts.
    
stop2 = ['B4:0.5','B4:0.5','B4:0.5','C5:1','D5:1.5','E5:0.5','E5:0.5','E5:0.5', # Don't Stop Me Now (fast part).
         'F5:1','G5:0.5','A4:0.5','A4:0.5','G4:0.5','F4:0.5','F4:1','F4:0.5','A4:0.5',
         'C5:0.5','F5:0.5','E5:2.5','C5:0.5','A4:0.5','G4:1','F4:0.5','R:0.5','F4:0.5',
         'A4:0.5','G4:0.5','F4:0.5','G4:1','G4:1.5','A4:0.5','B4:1','C5:2.5','R:1',
         'A4:0.5','A4:0.5','G4:0.5','F4:0.5','F4:1','R:0.5','C5:0.5','F5:0.5','E5:2','C5:0.5',
         'A5:0.5','A5:0.5','A5:0.5','G5:1','F5:1.5','R:0.5','A4:0.5','G4:0.5','F4:0.5','G4:0.5',
         'R:1','A4:0.5','R:1','B4:1','R:0.5','C5:1','C5:0.5','D5:0.5','E5:1','F5:3','R:0.5',
         'C5:0.5','A5:1','B5:0.5','A5:1','G5:1','F5:2','D5:1.5','R:0.5','A5:0.5','A5:0.5',
         'A5:0.5','B5:0.5','A5:1','G5:0.5','G5:0.5','G5:0.5','F#5:0.5','F#5:0.5','F#5:0.5',
         'F#5:0.5','G5:0.5','A5:0.5','R:0.5','A5:3'] 

take = ['F5:0.5','F5:0.5','D5:0.5','B4:0.5','R:0.5','B4:0.5','R:0.5','E5:0.5', # Take on Me.
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

easy = ['C4:1','D4:1','E4:1','F4:1','G4:1','A4:1','B4:1','C5:2','B4:1','A4:1','G4:1','F4:1', # Scale.
        'E4:1','D4:1','C4:1'] # Starter song.

love = ['E5:0.5','G5:0.5','E5:0.5','D5:0.5','G5:0.5','D5:0.5','C5:0.5','E5:0.5','C5:0.5','C5:0.5','A4:0.5','C5:0.5', # Somebody to love. (Doesn't sound that good, not all songs can be recreated on buzzer.)
        'A4:0.5','F4:0.5','A4:0.5','F4:0.5','A4:0.5','F4:0.5','A4:0.5','F4:0.5','B4:0.5','G4:0.5','C5:0.5','G4:1', 'G4:0.5','E4:0.5',
        'E4:0.5','E4:0.5','D4:0.5','D4:0.5','D4:0.5','D4:0.5','C4:0.5','C4:0.5','C4:1','C5:0.5','C5:1','C5:0.5','D5:0.5','D5:0.5','D5:0.5',
        'B4:0.5','A4:0.5','G4:1','G4:0.5','F4:0.5','E4:1.5','D4:1','F4:0.25','E4:0.25','C4:0.5','C4:0.5','E4:0.5','C4:1.5','R:0.5','D4:0.5',
        'D4:0.25','D4:0.25','C4:0.5','C4:0.5','C4:0.5','B3:1.5','R:1','E4:0.25','E4:0.25','E4:0.5','E4:0.5','E4:0.5','F#4:0.5','F#4:0.5','F#4:0.5',
        'G4:0.5','G4:0.5','G4:0.5','R:0.5','G4:0.5','G4:0.5','G4:1','G4:0.5','A4:0.5','A4:0.5','A4:0.5','B4:1.5','C5:01.5','E5:0.5','D5:0.5','C5:2','A5:0.5',
        'A5:0.5','A5:0.5','E5:0.5','D5:0.5','C5:1.5','A5:0.5','A5:0.5','F4:0.5','E4:1','E4:0.5','F4:1','F4:0.5','G4:1.5','C5:1.5','E5:1','E5:0.5','D5:0.5','D5:0.5',
        'D5:0.5','C5:0.5','E4:0.5','G4:0.5','C5:0.5','G4:0.5','E4:0.5','E5:0.5','E4:0.5','G4:0.5','C5:0.5','G4:0.5','E4:0.5','E5:0.5','E4:0.5','G4:0.5','C5:0.5','G4:0.5',
        'E4:0.5','A4:0.5','F4:0.5','A4:0.5','A4:0.5','A4:0.5','A4:0.5','B4:0.5:2']

moon = ['C5:1','B4:1','A4:1','G4:0.5','F4:2','G4:0.5','A4:1','C5:1','B4:1','A4:1','G4:1','F4:0.5','E4:4.5', # Fly Me to the Moon.
        'A4:0.5','G4:1','F4:1','E4:0.5','D4:2','E4:0.5','F4:1','A4:0.5','G#4:1.5','F4:1','E4:1','D4:0.5','C4:3','C#4:0.5',
        'D4:0.5','A4:0.5','A4:2','B4:1','B4:1','B4:1','B4:1','C5:1','B4:0.5','G4:6'] 

jingle = ['E5:0.5','E5:0.5','E5:0.1','E5:0.5','E5:0.5','E5:1','E5:0.5','G5:0.5','C5:0.5','D5:0.5','E5:0.5','D5:0.5','C5:0.5','A4:0.5', # Jingle Bell Rock.
          'G4:6','R:2','C5:0.5','C5:0.5','C5:1','B4:0.5','B4:0.5','B4:1','A4:0.5','B4:0.5','A4:1','E4:2','A4:0.5','B4:0.5','A4:1',
          'E4:1','G4:1','A4:0.5','B4:1','F4:2','D4:0.5','E4:1','F4:0.5','G4:0.5','A4:1','G4:0.5','D4:0.5','E4:0.5','F4:2','R:1','A4:0.5','G#4:0.5',
          'A4:0.5','G#4:0.5','A4:1','A4:1','D#4:0.5','D#4:2.5','C5:0.5','C5:0.5','C5:1','B4:0.5','B4:0.5','B4:1','A4:0.5','B4:0.5','A4:1','E4:2',
          'A4:0.5','B4:0.5','A4:1','E4:1','G4:1','A4:0.5','B4:0.5','A4:1','F4:2','D4:0.5','E4:1','F4:0.5','G4:0.5','A4:1','G4:0.5','D4:0.5','E4:0.5',
          'F4:1','G4:2','R:1','F#4:0.5','A4:0.5','F4:1','G4:0.5','C5:3']

never = ['F4:1.5','G4:2.5','C4:1','G4:1.5','A4:1.5','C5:0.25','B4:0.25','A4:0.5','F4:1.5','G4:2.5','C4:1','E4:0.5','F4:0.5','F4:1','R:1','F4:0.25','F4:0.5','F4:0.25', # Never Gonna Give You Up.
         'R:1','D4:0.5','E4:0.5','F4:1','G4:0.5','E4:0.75','D4:0.25','C4:2.5','R:1.5','D4:0.5','D4:0.5','E4:0.5','F4:0.5','D4:1','C4:0.5','C5:0.5','R:0.5','C5:0.5','G4:2','R:1',
         'D4:0.5','D4:0.5','E4:0.5','F4:0.5','D4:0.5','F4:0.5','G4:0.5','R:0.5','E4:0.5','D4:0.5','C4:1.5','R:1.5','D4:1','E4:0.5','F4:0.5','D4:0.5','C4:1','G4:0.5','G4:0.5','G4:0.5',
         'A4:0.5','G4:1','R:1','F4:2.5','G4:0.5','A4:0.5','F4:0.5','G4:0.5','G4:0.5','G4:0.5','A4:0.5','G4:1','C4:1','G3:0.5','G4:0.5','G3:0.5','G4:0.5','D4:0.5','E4:0.5','F4:0.5','D4:0.5',
         'R:0.5','G4:0.5','A4:0.5','G4:1.5','C4:0.25','D4:0.25','F4:0.25','D4:0.25','A4:0.75','A4:0.75','G4:1.5','C4:0.25','D4:0.25','F4:0.25','D4:0.25','G4:0.75','G4:0.75','F4:0.75','F4:0.75',
         'E4:0.25','D4:0.5','C4:0.25','D4:0.25','F4:0.25','D4:0.25','F4:1','G4:0.5','E4:0.75','D4:0.25','C4:1','C4:0.5','G4:1','F4:2','C4:0.25','D4:0.25','F4:0.25','D4:0.25','A4:0.75','A4:0.75',
         'G4:1.5','C4:0.25','D4:0.25','F4:0.25','D4:0.25','C5:1','E4:0.5','F4:0.75','E4:0.25','D4:0.5','C4:0.25','D4:0.25','F4:0.25','D4:0.25','F4:1','G4:0.5','E4:0.75','D4:0.25','C4:1','C4:0.5',
         'G4:1','F4:2']

all = ['C5:1.5','C5:1.5','C5:1','D5:1.5','D5:1.5','D5:1','C5:1.5','C5:1.5','C5:1','B4:1.5','B4:1.5','B4:1','C5:1.5','C5:1.5','C5:1','D5:1.5','D5:1.5','D5:1','C5:1.5','C5:1.5','C5:1', # All Of Me.
       'B4:1.5','B4:1.5','B4:1','C5:2','B4:0.5','C5:0.5','C5:1','C5:0.5','C5:0.5','C5:1','C5:0.5','B4:0.5','A4:0.5','A4:2.5','B4:0.5','C5:0.5','C5:1','E5:0.5','D5:0.5','C5:1','C5:0.5',
       'B4:0.5','A4:0.5','A4:0.5','F4:2','C5:0.5','C5:1.5','D5:2','C5:0.5','A4:1.5','D5:2','C5:0.5','A4:1','A4:0.5','B4:0.5','C5:0.5','B4:1.5','F4:2','B4:0.5','C5:0.5','C5:1','C5:1','C5:1',
       'C5:0.5','B4:0.5','A4:0.5','A4:2.5','B4:0.5','C5:0.5','C5:1','E5:0.5','D5:0.5','C5:1','C5:0.5','B4:0.5','A4:0.5','A4:0.5','F4:2','C5:0.5','C5:1.5','D5:2','C5:0.5','A4:1.5',
       'D5:2','C5:0.5','A4:1','A4:0.5','B4:2','C5:0.5','B4:1','D5:3.5','F4:0.5','F5:2','E5:0.5','D5:1','C5:2','B4:1','A4:1.5','G4:2','F4:0.5','E4:1','F4:3.5','F4:0.5','F5:2','F5:0.5',
       'E5:0.5','D5:0.5','C5:2.5','C5:0.5','B4:0.5','A4:0.5','B4:3.5','C5:0.5','E5:2.5','C5:0.5','F5:2.5','C5:2','B4:2.5','A4:0.5','C5:2.5','C5:0.5','C5:1.5','B4:1','B4:1','B4:1','A4:0.5',
       'B4:0.5','B4:2','C5:0.5','C5:1.5','B4:1','B4:1','B4:1','A4:0.5','B4:0.5','B4:2','C5:0.5','C5:1.5','B4:1','B4:1','B4:1','A4:0.5','B4:0.5','B4:2','C5:0.5','D5:0.5','E5:0.5','A5:2',
       'G5:2','F5:2','E5:1.5','C5:0.5','C5:4.5','B4:2','C5:0.5','D5:0.5','E5:0.5','A5:2','G5:2','F5:2','E5:1.5','C5:0.5','C5:2','C5:0.5','B4:4.5']

sugar = ['C5:1','G5:1','C5:1','A5:1','C5:1','A#5:1','C5:1','A5:1','C5:1','G5:1','C5:1','A5:1','C5:1','A#5:1','C5:1','A5:1','C5:1','G5:0.5','E5:0.5','G5:1','F5:1','D#5:1','E5:1','D5:0.5',
         'D5:0.5','D5:1','C#5:0.5','C#5:0.5','C5:1','C5:0.5','C5:0.5','C5:1','B4:0.5','E5:0.5','C5:0.5','E5:0.5','B4:1','C6:0.25','B5:0.25','A5:0.25','G5:0.25','F#5:1','G4:0.5','E4:0.5',
         'G4:1','F4:1','C5:1','B4:1','G5:0.5','G5:0.5','G5:1','F5:0.5','F5:0.5','F5:1','E5:0.5','E5:0.5','E5:1','D#5:0.5','F5:0.5','E5:0.5','F5:0.5','D5:1','G5:0.25','F5:0.25','E5:0.25','D5:0.25',
         'C5:1','G5:0.5','E5:0.5','G5:1','F5:1','D#5:1','E5:1','D5:0.5','D5:0.5','D5:1','C#5:0.5','C#5:0.5','C#5:1','C5:0.5','C5:0.5','C5:1','B4:0.5','E5:0.5','C5:0.5','E5:0.5','B4:1',
         'G4:0.25','F4:0.25','E4:0.25','D4:0.25','C#4:1','E5:0.5','C#5:0.5','E5:1','F4:0.25','E4:0.25','D#4:0.25','C4:0.25','B3:1','D5:0.5','B5:0.5','D5:1','E4:0.25','D4:0.25','C#4:0.25','B3:0.25',
         'A3:1','C5:0.5','A4:0.5','C5:1','D4:0.25','C4:0.25','B3:0.25','A3:0.25','G3:1','B3:0.5','F4:0.5','G4:1','C4:1']

theme = ['B3:0.5','B3:0.5','B3:0.25','A3:0.25','R:0.25','B3:0.25','R:0.25','D4:0.25','R:0.25','B3:0.25','R:0.25','F#3:0.25','A3:0.5','B3:0.5','B3:0.5','B3:0.25','A3:0.25','R:0.25','B3:0.25','R:0.25','F4:0.25','R:0.25','E4:0.25','R:0.25','D4:0.25','A3:0.5', #Jojo's Bizarre Adventure: Golden Wind - Giorno's Theme Ver. 2.
         'B3:0.5','B3:0.5','B3:0.25','A3:0.25','R:0.25','B3:0.25','R:0.25','D4:0.25','R:0.25','B3:0.25','R:0.25','F#3:0.25','A3:0.5','B3:0.5','B3:0.5','B3:0.25','A3:0.25','R:0.25','B3:0.25','R:0.25','F4:0.25','R:0.25','E4:0.25','R:0.25','D4:0.25','A3:0.5',
         'B3:0.5','B3:0.5','B3:0.25','A3:0.25','R:0.25','B3:0.25','R:0.25','D4:0.25','R:0.25','B3:0.25','R:0.25','F#3:0.25','A3:0.5','B3:0.5','B3:0.5','B3:0.25','A3:0.25','R:0.25','B3:0.25','R:0.25','F4:0.25','R:0.25','E4:0.25','R:0.25','D4:0.25','A3:0.5',
         'B3:0.5','B3:0.5','B3:0.25','A3:0.25','R:0.25','B3:0.25','R:0.25','D4:0.25','R:0.25','B3:0.25','R:0.25','F#3:0.25','A3:0.5','B3:0.5','B3:0.5','B3:0.5','A3:0.25','B3:0.25',
         'F#5:1.5','F5:1.5','R:0.5','D5:0.25','E5:0.25','F5:0.75','E5:0.75','D5:0.5','C#5:0.75','D5:0.75','E5:0.5','F#5:1.5','B5:1.5','B4:0.5','C#5:0.5','D5:0.75','E5:0.75','D5:0.5','C#5:0.75','A5:0.75',
         'G5:0.5','F#5:1.5','F5:1.5','R:0.5','D5:0.25','E5:0.25','F5:0.75','E5:0.75','D5:0.5','C5:0.75','D5:0.75','E5:0.5','F#5:1.5','B5:1.5','B5:0.5','A#5:0.5','D5:0.75','E5:0.75','G4:0.5','F#4:0.75',
         'D5:0.75','E5:0.5','F#5:1.5','F5:1.5','R:0.5','D5:0.25','E5:0.25','F5:0.75','E5:0.75','D5:0.5','C#5:0.75','D5:0.75','E5:0.5','F#5:1.5','B5:1.5','B4:0.5','C5:0.5','D5:0.75','E5:0.75','D5:0.5','C#5:0.75','A5:0.75',
         'G5:0.5','F#5:1.5','F5:1.5','R:0.5','D5:0.25','E5:0.25','F#5:1.5','B5:1.5','B4:0.5','C#5:0.5','D5:0.75','G5:0.75','F#5:0.5','F5:0.75','D6:0.75','A#5:0.5','B5:1']

songs = [
    [easy],
    [theme],
    [sugar],
    [all],
    [dust],
    [stop1,stop2], 
    [take],
    [love],
    [jingle],
    [moon],
    [never],
]

# BPM for each song. Because the notes are played at half the time, the BPM is doubled from the song's orginal BPM.
songs_bpm = [
    [240],
    [260],
    [180],
    [240], 
    [150],
    [188,300],
    [338],
    [152],
    [240],
    [240],
    [240],
    
]

# Uses the score LED to indicate song difficult in preview mode.
# 2 = green which is easiest all the way to 1 = red which is hardest.
songs_difficulty = [
    [2],
    [2,1,0],
    [2],
    [2,1],
    [2,1],
    [2,1],
    [2,1,0],
    [2,1,0],
    [2,1],
    [2],
    [2,1,0],
]
