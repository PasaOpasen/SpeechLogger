# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:54:12 2020

@author: qtckp
"""


import json

def to_pair(lst):
    return lst[0], lst[1]

with open('./epitran tables/all_supported.txt','r') as fl:
    pairs = [to_pair(s[2:].split('|')) for s in fl.readlines()]
    all_langs = {key.strip(): value.strip() for key, value in pairs}


with open('./epitran tables/limited_supported.txt','r') as fl:
    arr = [s.split('|')[1].strip() for s in fl.readlines()]


for key, val in all_langs.items():
    if key in arr:
        all_langs[key]= (val, True)
    else:
        all_langs[key]= (val, False)



with open("languges_for_transcription.json", "w") as write_file:
    json.dump(all_langs, write_file, indent=4)









