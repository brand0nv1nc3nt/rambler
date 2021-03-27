#! /usr/bin/env python3
# Brandon Vincent 3/27/21
# plays overlapping audio clips to simulate a microphone jammer
# syntax: rambler.py [-s] <file>

# GPLv2 statement
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


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

        for fromtime in range(len(os.listdir("slices")), int(int(whole.duration_seconds) - 1) + len(os.listdir("slice>
                clip = whole[int(fromtime * 1000):int(fromtime * 1000 + 1000)]
                clip.export("slices/"+str(fromtime)+".wav", format="wav")

def rabble(): # plays a slice every .1s, causing an overlap
        while True:
                files = len(os.listdir("slices"))

                if files < 1:
                        print("No sound slices! Make some with: rambler.py -s <file> ")
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
