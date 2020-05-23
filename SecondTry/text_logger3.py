# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:44:49 2020

@author: qtckp
"""

from textblob import TextBlob
import speech_recognition as sr
import soundcard as sc
from scipy.io.wavfile import write
import numpy as np

from termcolor import colored
#import colorama
#colorama.init()


my_speaker = None


def print_on_blue(text, end='\n'):
    return print(colored(text,on_color='on_blue'),end =end)
def print_on_red(text, end='\n'):
    return print(colored(text,on_color='on_red'),end =end)
def print_on_green(text, end='\n'):
    return print(colored(text,on_color='on_green'),end =end)
def print_on_magenta(text, end='\n'):
    return print(colored(text,on_color='on_magenta'),end =end)
def print_on_cyan(text, end='\n'):
    return print(colored(text,on_color='on_cyan'),end =end)
def print_on_yellow(text, end='\n'):
    return print(colored(text,on_color='on_yellow'),end =end)



def set_speaker():
    lst = sc.all_microphones(include_loopback=True)
    global my_speaker
    
    if len(lst)==0:
        print(colored('U have no callback-speakers thus u will not be able to recognize messages from speaker',on_color='on_yellow',attrs=['bold']))
        return
    if len(lst)==1:
        print(colored(f'Single speaker {lst[0]} was choosen',on_color='on_yellow',attrs=['bold']))
        my_speaker = lst[0]
        return
    
    print_on_blue('Hello! Please set the correct speaker from list or write 0 to disable speaker recognition:')
    for i, s in enumerate(lst):
        print(f"\t{i+1}) {s}")
    
    while True:
        res = input(f'Just write the number from {0} to {len(lst)} (0 to disable): ')
        if res.isdigit():
            number = int(res)
            
            if number == 0:
                print()
                print_on_blue('Speaker recognition was disabled')
                print()
                break
            
            if 1 <= number <= len(lst):
                print()
                print_on_blue(f'Speaker {lst[number-1]} was choosen')
                print()
                my_speaker = lst[number-1] 
                break
    

    
    

def speech_to_text_from_speaker(speaker,time = 100_000,samplerate = 48000,lang = 'ru-RU'):
    with speaker.recorder(samplerate=samplerate) as mic:
        print_on_magenta('Listen')
        dt = mic.record(time)        
        print_on_yellow('Okay. Wait')
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
        
        print_on_magenta(f"TALK ({lang[:2]})")
        audio_text = r.listen(source)
        print_on_yellow("Okay. Stop talking")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        return r.recognize_google(audio_text, language = lang)
    except Exception as e:
        print(e)
        return 'bad result of recognition'

             

def log_text(text, lang_of_text=None, lang_list = ['en','ru']):
    
    if len(text) < 3:
        print_on_yellow('too small text:',end=' ')
        print(text)
        return
    
    blob = TextBlob(text)
    if lang_of_text == None:
        lang_of_text = blob.detect_language()

    bool_list = [r != lang_of_text for r in lang_list]
    
    for lang, it in zip(lang_list, bool_list):
        print(colored(f'\t {lang}:', color = 'cyan', attrs=['bold']), end=' ')
        if it:
            print(str(blob.translate(from_lang = lang_of_text, to = lang)))
        else:
            print(f'{text} (original text)')


def do_log(stop_word = 'break app', lang_list = ['en','ru','fa']):
    
    counter = 1
    
    print(colored('Good! Write "','magenta'),end='')
    print(colored(str(stop_word),'red'),end='')    
    print(colored('" to stop logging','magenta'))
    
    print(colored('Output lang list: ','magenta'),end='')
    
    print(colored(str(lang_list),'cyan'),end='')  
    
    
    while True:
        text = input(f'({counter})--> ')
        if text == stop_word:
            break
        log_text(text, lang_list = lang_list)
        counter+=1


def do_log_with_recognition(stop_word = '+', lang_list = ['en','ru','fa'], ends=['US','RU','IR'], lang_repeat_step = 4, stop_repeat_step = 5):
    
    counter = 1
    
    print_on_blue('Output lang list: ',end='')
    
    choosen_list = [f'{number+1}) {lang}' for number, lang in zip(range(len(lang_list)),lang_list)]
    
    langs_string = ' '+' '.join(choosen_list)+' '
    
    print_on_green(langs_string)  
    
    print_on_blue('Choose a number of lang to start talking or -number to start listening')
    
    
    while True:
        text = input(f'({counter})--> ')
        if text == stop_word:
            break
        
        if text.isdigit():
            try:
                number = int(text)-1
                text = speech_to_text_from_micro(f'{lang_list[number]}-{ends[number]}')
                print_on_cyan('You said:',end='')
                print_on_magenta(' '+text)
            except Exception as e:
                print(e)
                print_on_yellow('Something wrong...')

        log_text(text, lang_list = lang_list)
             
        counter+=1
        
        if counter%lang_repeat_step == 0:
            print_on_cyan("don't forget lang numbers:",end='')
            print_on_green(langs_string)
        
        if counter%stop_repeat_step == 0:
            print_on_magenta("to stop it write",end=' ')
            print_on_red(stop_word)

def do_log_with_recognition_both(speaker, stop_word = '+', lang_list = ['en','ru','fa'], ends=['US','RU','IR'], lang_repeat_step = 4, stop_repeat_step = 5):
    
    counter = 1
    
    print_on_blue('Output lang list: ',end='')
    
    choosen_list = [f'{number+1}) {lang}' for number, lang in zip(range(len(lang_list)),lang_list)]
    
    langs_string = ' '+' '.join(choosen_list)+' '
    
    print_on_green(langs_string)  
    
    print_on_blue('Choose a number of lang to start talking or -number to start listening')
    
    
    while True:
        text = input(f'({counter})--> ')
        if text == stop_word:
            break
        
        # if text is like -1 (should listen)
        if text[1:].isdigit():
            try:
                number = int(text[1:])-1
                text = speech_to_text_from_speaker(speaker = my_speaker, lang=f'{lang_list[number]}-{ends[number]}')
                print(colored('You listened:',on_color='on_cyan'),end='')
                print_on_magenta(' '+text)
            except Exception as e:
                print(e)
                print_on_yellow('Something wrong...')
        
        #if text is like 1 (should speak)
        elif text.isdigit():
            try:
                number = int(text)-1
                text = speech_to_text_from_micro(f'{lang_list[number]}-{ends[number]}')
                print_on_cyan('You said:',end='')
                print_on_magenta(' '+text)
            except Exception as e:
                print(e)
                print_on_yellow('Something wrong...')

        log_text(text, lang_list = lang_list)
             
        counter+=1
        
        if counter%lang_repeat_step == 0:
            print_on_cyan("don't forget lang numbers:",end='')
            print_on_green(langs_string)
        
        if counter%stop_repeat_step == 0:
            print_on_magenta("to stop it write",end=' ')
            print_on_red(stop_word)

#do_log()





if __name__ == '__main__':
    
    
    set_speaker()    
     
    stop_word = '+' 
    print_on_blue('Good! Write "',end='')
    print_on_red(str(stop_word),end='')    
    print_on_blue('" to stop logging')
    
    if my_speaker == None:
        do_log_with_recognition(stop_word='+')
    else:
        do_log_with_recognition_both(speaker = my_speaker, stop_word='+')


#input('Press any key...')









