# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:44:49 2020

@author: qtckp
"""

from textblob import TextBlob
from termcolor import colored

import speech_recognition as sr

             
def speech_to_text_from_micro(lang = 'ru-RU'):
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    
    with sr.Microphone() as source:
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, 0.5) 
        
        print(colored(f"TALK ({lang[:2]})",on_color='on_magenta'))
        audio_text = r.listen(source)
        print(colored("Time over. STOP",on_color = 'on_red'))
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        return r.recognize_google(audio_text, language = lang)
    except:
        return 'bad result'

             


def log_text(text, lang_of_text=None, lang_list = ['en','ru']):
    
    if len(text) < 3:
        print(f'too small text {text}')
        return
    
    blob = TextBlob(text)
    if lang_of_text == None:
        lang_of_text = blob.detect_language()

    bool_list = [r != lang_of_text for r in lang_list]
    
    for lang, it in zip(lang_list, bool_list):
        print(f'\t{lang}:', end=' ')
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



def do_log_with_recognition(stop_word = 'breakapp', lang_list = ['en','ru','fa'], ends=['US','RU','IR']):
    
    counter = 1
    
    print(colored('Good! Write "',on_color='on_blue'),end='')
    print(colored(str(stop_word),on_color='on_red'),end='')    
    print(colored('" to stop logging',on_color='on_blue'))
    
    print(colored('Output lang list: ',on_color='on_blue'),end='')
    
    choosen_list = [f'{number+1}) {lang}' for number, lang in zip(range(len(lang_list)),lang_list)]
    
    langs_string = ' '.join(choosen_list)+' '
    
    print(colored(langs_string,on_color = 'on_green'))  
    
    print(colored('Choose a number of lang to start talking',on_color='on_blue'))
    
    
    while True:
        text = input(f'({counter})--> ')
        if text == stop_word:
            break
        
        if text.isdigit():
            try:
                number = int(text)-1
                text = speech_to_text_from_micro(f'{lang_list[number]}-{ends[number]}')
            except:
                print('Something wrong...')

        log_text(text, lang_list = lang_list)
             
        counter+=1
        
        if counter%5 == 0:
            print("don't forget lang numbers:",end=' ')
            print(colored(langs_string,on_color = 'on_green'))


#do_log()

do_log_with_recognition()


#input('Press any key...')









