# RasPiRhythm
A rhythm game similar to rhythm doctor but on raspberry pi and with complicated wiring.


Uses open source library by [fongkahchun86](https://github.com/fongkahchun86): https://github.com/fongkahchun86/gpiozero_pwm_buzzer


# IMPORTANT FILES #
`raspiRhythm.py` is the main file, this is the most up to date file and is the file that should be run. Uses the current library (in file gpiozero_pwm_buzzer.py) however this library was modified and will not work with that file and the library is already inside this file so no need to use other files (just this and beatsongs.py).
<br />
<br />
`beatsongs.py` is another mandatory file, this contains all the songs, their bpm and difficulty (use with raspiRhythm.py and beattest.py (beattest is outdated))
<br />
<br />
`beattest.py` is an outdated version of the raspiRhythm.py file. This was to change the file name to a more specific name.
<br />
<br />
`main.py` uses an outdated library (i made) with an outdated way of creating songs. utils.py and songs.py are needed.
<br />
<br />
`maintest.py` a rough design of the original plan to have multiple(3) note lanes. Low notes left, rests middle, High notes right. Uses current library (gpiozero_pwm_buzzer.py needed)
<br />
<br />
`simmain.py`unfinished outdated design that tried to use the tkgpio with the buzzers but did not work well. This version will not work as lots of important code was either commented out or removed entirely. This is just a "testing/experiment" file.
