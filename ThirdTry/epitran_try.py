# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:40:43 2020

@author: qtckp
"""



import epitran

epi = epitran.Epitran('fas-Arab')

epi.transliterate('سلام')



from epitran.backoff import Backoff

backoff = Backoff(['fas-Arab', 'rus-Cyrl'])
                  
backoff.transliterate('Привет дорогой друг пидор')

backoff.transliterate('queen')

backoff.transliterate('中文')

backoff.transliterate('سلام شادی من')


backoff.transliterate('ملکه')
