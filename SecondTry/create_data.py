# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:40:25 2020

@author: qtckp
"""


import os, shutil
import json
import googletrans



directory='./text_logger'
file_name='text_logger3.py'

if os.path.exists(directory):
    shutil.rmtree(directory)

os.makedirs(directory)

shutil.copyfile(file_name,os.path.join(directory,file_name))



langs = {value: key for key, value in googletrans.LANGUAGES.items()}

with open(os.path.join(directory,"languges.json"), "w") as write_file:
    json.dump(langs, write_file, indent=4)

