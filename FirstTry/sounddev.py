# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:48:41 2020

@author: qtckp
"""


import sounddevice as sd
import numpy as np

sd.default.samplerate = 44100
sd.default.device = 3

myarray = np.random.randint(0,1000,1000)

sd.play(myarray)



