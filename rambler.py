#! /usr/bin/env python3
# plays overlapping audio clips to simulate a microphone jammer

from pydub import AudioSegment
from playsound import playsound
from multiprocessing import Process
import time
import random
import os
import sys

def slice(): # takes a file and slices it into 1s segments, then stores them in slices directory
	try:
		whole = AudioSegment.from_wav(sys.argv[2])
	except:
		print("Wrong filename or bad permissions")
		exit()

	for fromtime in range(len(os.listdir("slices")), int(int(whole.duration_seconds) - 1) + len(os.listdir("slices"))):
	        clip = whole[int(fromtime * 1000):int(fromtime * 1000 + 1000)]
	        clip.export("slices/"+str(fromtime)+".wav", format="wav")

def rabble(): # plays a slice every .1s, causing an overlap
	while True:
		files = len(os.listdir("slices"))

		if files < 1:
			print("No sound slices! Make some with: rambler -s <file> ")
			exit()

		randint = random.randint(0, files - 1)
		p = Process(target=playsound, args=("slices/"+str(randint)+".wav",))
		p.start()
		time.sleep(.1)

try:
	slicedir = os.listdir("slices")
except:
	print("slices dir not found, creating...")
	os.system("mkdir slices")

if len(sys.argv) > 2:
	if sys.argv[1] == "-s":
		slice()
else:
	rabble()
