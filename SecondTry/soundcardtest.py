# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:15:43 2020

@author: qtckp


https://pypi.org/project/SoundCard/
"""


import soundcard as sc


# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones()
# get the current default microphone on your system:
default_mic = sc.default_microphone()


import numpy

# record and play back one second of audio:
data = default_mic.record(samplerate=48000, numframes=48000)
default_speaker.play(data/numpy.max(data), samplerate=48000)


# alternatively, get a `Recorder` and `Player` object
# and play or record continuously:
with default_mic.recorder(samplerate=48000) as mic, default_speaker.player(samplerate=48000) as sp:
    for _ in range(100):
        data = mic.record(numframes=1024)
        sp.play(data)






