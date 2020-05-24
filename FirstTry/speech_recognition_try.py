# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:28:23 2020

@author: qtckp

source https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426

langs https://cloud.google.com/speech-to-text/docs/languages

russian = 'ru-RU'
english = 'en-US'
farsi = 'fa-IR'

"""

import speech_recognition as sr
import soundcard as sc
from scipy.io.wavfile import write
import numpy as np

din = sc.all_microphones(include_loopback=True)[1]

def speech_to_text_from_speaker(speaker,time = 100_000,samplerate = 48000,lang = 'ru-RU'):
    with speaker.recorder(samplerate=samplerate) as mic:
        print('Listen')
        dt = mic.record(time)        
        print('Okay. Wait')
        write("tmp.wav", 
              samplerate, 
              np.int16(dt * (32767/np.max(np.abs(np.array([dt.min(),dt.max()]))))))
    
    return speech_to_text_from_wav(lang)



def speech_to_text_from_wav(lang = 'ru-RU', file = 'tmp.wav'):

    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    
    # Reading Audio file as source
    # listening the audio file and store in audio_text variable
    
    with sr.AudioFile(file) as source:
        
        audio_text = r.listen(source)
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            return r.recognize_google(audio_text, language = lang)
        except Exception as e:
            print(e)
            return 'bad result of recognition'
             
             
def speech_to_text_from_micro(lang = 'ru-RU'):
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    
    with sr.Microphone() as source:
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, 0.5) 
        
        print(f"TALK ({lang[:2]})")
        audio_text = r.listen(source)
        print("Okay. Stop talking")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        return r.recognize_google(audio_text, language = lang)
    except Exception as e:
        print(e)
        return 'bad result of recognition'
             
             
speech_to_text_from_micro(lang='fa')
speech_to_text_from_wav()

speech_to_text_from_speaker(din,time=100000,lang = 'ru-RU')





from scipy.io.wavfile import write
samplerate = 100000; fs = 1000
t = np.linspace(0., 1., samplerate)
amplitude = np.iinfo(np.int16).max
data = amplitude * np.sin(2. * np.pi * fs * t)
write("example.wav", samplerate, data)


import numpy as np
from scipy.io.wavfile import write

data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('test.wav', 44100, scaled)


with din.recorder(samplerate=48000) as mic:
    print('Listen')
    dt = mic.record(100_000)
    dt = np.int16(dt/np.max(np.abs(dt)) * 32767)
    print('Okay')
    write("tmp.wav", 48000, dt)





dt = np.random.rand(50000,500)-0.5

%timeit r = np.int16(dt/np.max(np.abs(dt)) * 32767)

%timeit r = np.int16(dt * (32767/np.max(np.abs(dt))))

%timeit r = np.array(dt * (32767/np.max(np.abs(dt))),dtype='int16')

%timeit r = np.int16(dt * (32767/np.max(np.abs(np.array([dt.min(),dt.max()])))))


%timeit xmax = dt.flat[abs(dt).argmax()]

%timeit newdt=np.array([dt.min(),dt.max()])
%timeit xmax = newdt.flat[abs(newdt).argmax()]














