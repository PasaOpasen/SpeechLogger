# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:04:54 2020

@author: qtckp
"""



# Python program to print 
# red text with green background 

from colorama import Fore, Back, Style 
print(Fore.RED + 'some red text') 
print(Back.GREEN + 'and with a green background') 
print(Style.DIM + 'and in dim text') 
print(Style.RESET_ALL) 
print('back to normal now') 

input('')








