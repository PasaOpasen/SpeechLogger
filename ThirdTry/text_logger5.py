# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:44:49 2020

@author: qtckp

it`s text_logger4 with epytran transcriptions
"""

from textblob import TextBlob
import speech_recognition as sr
import soundcard as sc
from scipy.io.wavfile import write
import numpy as np

import epitran

import json

from termcolor import colored
#import colorama
#colorama.init()


my_speaker = None
epis = {}



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
    
def detect_languages(langs, trans):
    with open("./text_logger/languges.json", "r") as read_file:
        lg = json.load(read_file)
    
    with open("./text_logger/languges_for_transcription.json", "r") as read_file:
        tc = json.load(read_file)
    
    rs = []
    nd = []
    global epis
    
    def add_print(langu):
        print_on_magenta(f'---> added {langu} language')
    
    def add2_print(langu, is_not_sup):
        if is_not_sup:
            print(f'\tlanguage {langu} will be trancripted (with limited support)')
        else:
            print(f'\tlanguage {langu} will be trancripted')
    
    for lang, need in zip(langs,trans):
        
        f = False
        
        if lang in lg.values():
            rs.append(lang)
            f = True
            add_print(lang)
        elif lang in lg.keys():
            rs.append(lg[lang])
            f = True
            add_print(lang)
        else:
            for k in lg.keys():
                if k.startswith(lang):
                    rs.append(lg[k])
                    add_print(k)
                    f = True
                    break
        
        if not f:
            print_on_red(f"I donna this language: '{lang}'. See json file to correct it")
        else:
            nd.append(need)
            
            itlang = rs[len(rs)-1]
            epitran_lang = [key for key, _ in tc.items() if key.startswith(itlang)][0]
            
            if need:
                epis[itlang] = epitran.Epitran(epitran_lang)
                add2_print(*tc[epitran_lang])
            


    if len(rs) == 0:
        print_on_red('There are no correct languages in ur list. See json file to correct it')

    return rs, nd
    
    

def speech_to_text_from_speaker(speaker,time = 200_000,samplerate = 48000, lang = 'ru-RU'):
    with speaker.recorder(samplerate=samplerate) as mic:
        print_on_magenta(f'Listen (expected {lang})')
        dt = mic.record(time)        
        print_on_yellow('Okay. Wait')
        write("tmp.wav", 
              samplerate, 
              np.int16(dt * (32767/np.max(np.abs(np.array([dt.min(),dt.max()]))))))
    
    return speech_to_text_from_wav(lang)


def speech_to_text_from_wav(lang = 'ru', file = 'tmp.wav'):

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
             
def speech_to_text_from_micro(lang = 'ru'):
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    
    with sr.Microphone() as source:
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, 0.5) 
        
        print_on_magenta(f"TALK (expected {lang})")
        audio_text = r.listen(source)
        print_on_yellow("Okay. Stop talking")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        return r.recognize_google(audio_text, language = lang)
    except Exception as e:
        print(e)
        return 'bad result of recognition'

             

def log_text(text, lang_of_text=None, lang_list = ['en','ru'], trans_list = [True, True]):
    
    if len(text) < 3:
        print_on_yellow('too small text:',end=' ')
        print(text)
        return
    
    blob = TextBlob(text)
    if lang_of_text == None:
        lang_of_text = blob.detect_language()

    bool_list = [r != lang_of_text for r in lang_list]
    
    for lang, it, tc in zip(lang_list, bool_list, trans_list):
        print(colored(f'\t {lang}:', color = 'cyan', attrs=['bold']), end=' ')
        if it:
            txt = str(blob.translate(from_lang = lang_of_text, to = lang))
            print(txt)
        else:
            txt = text
            print(f'{text} (original text)')
        
        if tc:
            pron = epis[lang].transliterate(txt)
            print('\t\t\t',end=' ')
            print_on_magenta(f'[{pron}]')


def do_log(stop_word = 'break app', lang_list = ['en','ru','fa'], trans_list = [True, True,True]):
    
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
        log_text(text, lang_list = lang_list, trans_list = trans_list)
        counter+=1


def do_log_with_recognition(stop_word = '+', lang_list = ['en','ru','fa'], trans_list = [True, True,True], lang_repeat_step = 4, stop_repeat_step = 5):
    
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
                text = speech_to_text_from_micro(lang_list[number])
                print_on_cyan('You said:',end='')
                print_on_magenta(' '+text)
            except Exception as e:
                print(e)
                print_on_yellow('Something wrong...')

        log_text(text, lang_list = lang_list, trans_list = trans_list)
             
        counter+=1
        
        if counter%lang_repeat_step == 0:
            print_on_cyan("don't forget lang numbers:",end='')
            print_on_green(langs_string)
        
        if counter%stop_repeat_step == 0:
            print_on_magenta("to stop it write",end=' ')
            print_on_red(stop_word)

def do_log_with_recognition_both(speaker, listen_time = 200_000, stop_word = '+', lang_list = ['en','ru','fa'], trans_list = [True, True,True], lang_repeat_step = 4, stop_repeat_step = 5):
    
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
                text = speech_to_text_from_speaker(speaker = my_speaker, lang=lang_list[number], time = listen_time)
                print(colored('You listened:',on_color='on_cyan'),end='')
                print_on_magenta(' '+text)
            except Exception as e:
                print(e)
                print_on_yellow('Something wrong...')
        
        #if text is like 1 (should speak)
        elif text.isdigit():
            try:
                number = int(text)-1
                text = speech_to_text_from_micro(lang_list[number])
                print_on_cyan('You said:',end='')
                print_on_magenta(' '+text)
            except Exception as e:
                print(e)
                print_on_yellow('Something wrong...')

        log_text(text, lang_list = lang_list, trans_list = trans_list)
             
        counter+=1
        
        if counter%lang_repeat_step == 0:
            print_on_cyan("don't forget lang numbers:",end='')
            print_on_green(langs_string)
        
        if counter%stop_repeat_step == 0:
            print_on_magenta("to stop it write",end=' ')
            print_on_red(stop_word)

#do_log()





if __name__ == '__main__':
    
    with open("./text_logger/settings.json", "r") as read_file:
        settings = json.load(read_file)
    
    settings['languages'], settings['need_to_transcript'] = detect_languages(settings['languages'], settings['need_to_transcript'])
    
    print()
    print_on_blue(f'Your settings: {settings}')
    print()
    
    set_speaker()    
     
    stop_word = '+' 
    print_on_blue('Good! Write "',end='')
    print_on_red(str(stop_word),end='')    
    print_on_blue('" to stop logging')
    
    if my_speaker == None:
        do_log_with_recognition(lang_list=settings['languages'],
                                stop_word=settings['stop_word'],
                                trans_list = settings['need_to_transcript']
                                )
    else:
        do_log_with_recognition_both(speaker = my_speaker,
                                     lang_list=settings['languages'],
                                     stop_word=settings['stop_word'],
                                     listen_time = settings['listen_time'],
                                     trans_list = settings['need_to_transcript']
                                     )











