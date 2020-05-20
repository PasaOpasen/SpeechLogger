# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:31:55 2020

@author: qtckp

https://sprosi.pro/questions/44594/vhod-vyihod-audio-v-realnom-vremeni-v-python-s-pyaudio
"""


import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as signal



CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
fulldata = np.array([])
dry_data = np.array([])

def main():
    stream = p.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    input=True,
                    stream_callback=callback)
    
    stream.start_stream()
    
    while stream.is_active():
        time.sleep(10)
        stream.stop_stream()
    stream.close()
    
    numpydata = np.hstack(fulldata)
    plt.plot(numpydata)
    plt.title("Wet")
    plt.show()
    
    
    numpydata = np.hstack(dry_data)
    plt.plot(numpydata)
    plt.title("Dry")
    plt.show()
    
    
    p.terminate()

def callback(in_data, frame_count, time_info, flag):
    global b,a,fulldata,dry_data,frames 
    audio_data = np.fromstring(in_data, dtype=np.float32)
    dry_data = np.append(dry_data,audio_data)
    #do processing here
    fulldata = np.append(fulldata,audio_data)
    return (audio_data, pyaudio.paContinue)

main()

