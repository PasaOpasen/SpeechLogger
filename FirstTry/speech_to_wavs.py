# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:45:36 2020

@author: qtckp

https://overcoder.net/q/801086/python-запись-звука-на-обнаруженный-звук
"""


import pyaudio
import math
import struct
import wave
import sys

#Assuming Energy threshold upper than 30 dB
Threshold = 30

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2
Max_Seconds = 10
TimeoutSignal=math.floor((RATE / chunk * Max_Seconds) + 2)
silence = True
FileNameTmp = 'some.wav'
Time=0
alls =[]

def GetStream(chunk):
    return stream.read(chunk)

def rms(frame):
    count = len(frame)/swidth
    formats = "%dh"%(count)
    shorts = struct.unpack( formats, frame )

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n
        rms = math.pow(sum_squares/count,0.5);

        return rms * 1000


def WriteSpeech(WriteData):
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(FileNameTmp, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(WriteData)
    wf.close()


def KeepRecord(TimeoutSignal, LastBlock):
    alls.append(LastBlock)
    for i in range(0, TimeoutSignal):
        try:
            data = GetStream(chunk)
        except:
            continue
        #I chage here (new Ident)
        alls.append(data)

    print("end record after timeout")
    data = bytearray(''.join([b.hex() for b in alls]), "ascii")
    #data= ''.join(alls)
    print("write to File")
    WriteSpeech(data)
    silence = True
    Time=0
    listen(silence,Time)     


def listen(silence,Time):
    print("waiting for Speech")
    while silence:
        try:
            input = GetStream(chunk)
        except:
            continue
        rms_value = rms(input)
        if (rms_value > Threshold):
            silence=False
            LastBlock=input
            print("hello ederwander I'm Recording....")
            KeepRecord(TimeoutSignal, LastBlock)
        Time = Time + 1
        if (Time > TimeoutSignal):
            print("Time Out No Speech Detected")
            #sys.exit()

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = chunk)

listen(silence,Time)












