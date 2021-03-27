# rambler
Simulates a microphone jammer, specifically, the IProtect Rabbler, a ~$400 device.

# Slicing
Before you start rambling, you need to create "slices", 1 second audio clips that the rambler will use.<br />
To slice, simply run the script with the -s arguement and the filename of a recorded wav clip of you or someone else speaking. The wav file should be a minimum of 5 minutes long to make the output sound more random<br />
<br />
<code>./rambler.py -s sound.wav</code><br />
<br />
This will create the slices and store them in a directory titled "slices"<br />
NOTE: the script only accepts wav files!

# Rambling
To start rambling, run the script without arguements. This will play 1 slice per .1 seconds, creating an overlap.<br />
<br />
<code>./rambler.py</code><br />
<br />
In order to use the rambler script to the fullest effect, give the script audio slices from everyone you want to protect from microphone surveilance, and use it at high volume.
