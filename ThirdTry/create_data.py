# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:40:25 2020

@author: qtckp
"""


import os, shutil
import json
import googletrans


directory='./text_logger'

def copy(filename):
    shutil.copyfile(filename,os.path.join(directory,filename))


if os.path.exists(directory):
    shutil.rmtree(directory)

os.makedirs(directory)


copy('text_logger5.py')
copy("languges_for_transcription.json")



langs = {value: key for key, value in googletrans.LANGUAGES.items()}

with open(os.path.join(directory,"languges.json"), "w") as write_file:
    json.dump(langs, write_file, indent=4)


settings = {
    'languages':['ru','en','fa'],
    'need_to_transcript':[True,False,True],
    'listen_time':220_000,
    'stop_word':'+'
    }

with open(os.path.join(directory,"settings.json"), "w") as write_file:
    json.dump(settings, write_file, indent=4)