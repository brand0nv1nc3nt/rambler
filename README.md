# rambler
Simulates a microphone jammer, specifically, the IProtect Rabbler, a ~$400 device.

# Slicing
Before you start rambling, you need to create "slices", 1 second audio clips that the rambler will use.<br />
To slice, simply run the script with the -s arguement<br />
<br />
<code>./rambler.py -s sound.wav</code><br />
<br /
This will create the slices and store them in a directory titled "slices"<br />
NOTE: the script only accepts wav files!

# Rambling
To start rambling, run the script without arguements <br />
<br />
<code>./rambler.py</code><br />
<br />
In order to use the rambler script to the fullest effect, give the script audio slices from everyone you want to protect from microphone surveilance, and use it at high volume.
