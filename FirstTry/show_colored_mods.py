# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:54:14 2020

@author: qtckp
"""

from termcolor import colored

def show_color_mods():
    
    cols = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    cols2=['on_'+c for c in cols]
    
    cols.append(None)
    cols2.append(None)
    
    for color in cols:
        for on_color in cols2:
            
            r = (color==None) + (on_color == None)
            
            p=False
            if r < 2:
                if r==1:
                    p = True
                else:
                    p = color != on_color[3:]                                      
            
            if p:
                for attr in ['bold', 'underline', 'blink']:
                    print(colored(f'{color} {on_color} {attr}',color,on_color,attrs=[attr]))


show_color_mods()


