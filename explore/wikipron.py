# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:54:44 2020

@author: qtckp
"""



import wikipron
import os
import json



dic = {}

config = wikipron.Config(key="en") 

t = 0
for word, pron in wikipron.scrape(config):
    t+=1
    if t%100 ==0:
        print(f'{t} {word} {pron}')
    if len(word)>1:
        dic[word]=pron


with open("english.json", "w") as write_file:
    json.dump(dic, write_file, indent=4)


