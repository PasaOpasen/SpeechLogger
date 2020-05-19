# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:44:49 2020

@author: qtckp
"""

from textblob import TextBlob


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
    
    text = f'Good! Write "{stop_word}" to stop logging'
    print(text)
    print(f'Output lang list: {lang_list}')
    
    
    while text != stop_word:
        text = input(f'({counter})--> ')
        log_text(text, lang_list = lang_list)
        counter+=1



do_log()














