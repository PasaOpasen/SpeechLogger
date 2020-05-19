# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:28:23 2020

@author: qtckp

source https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426

langs https://cloud.google.com/speech-to-text/docs/languages
"""

import speech_recognition as sr

def speech_to_text_from_wav():

    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    
    # Reading Audio file as source
    # listening the audio file and store in audio_text variable
    
    with sr.AudioFile('english.wav') as source:
        
        audio_text = r.listen(source)
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
         
        except:
             print('Sorry.. run again...')
             
             
def speech_to_text_from_micro():
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(audio_text))
        except:
             print("Sorry, I did not get that")
             
             
speech_to_text_from_micro()