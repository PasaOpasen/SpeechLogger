# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:40:43 2020

@author: qtckp
"""



import epitran

epi = epitran.Epitran('fas-Arab')

epi.transliterate('سلام')


epi = epitran.Epitran('rus-Cyrl')

epi.transliterate('Привет дорогой друг пидор')



# standardize farsi
from farsi_tools import standardize_persian_text
text = standardize_persian_text('سلام خوبي؟ کمك ﻧميخواي؟')
epi.transliterate(text)




from epitran.backoff import Backoff

backoff = Backoff(['fas-Arab', 'rus-Cyrl'])
                  
backoff.transliterate('Привет дорогой друг пидор')

backoff.transliterate('queen')

backoff.transliterate('中文')

backoff.transliterate('سلام شادی من')


backoff.transliterate('ملکه')





from pysle import isletool

tl = isletool.LexicalTool()

tl.lookup('cat')

from pysle import pronunciationtools



from phonemizer.phonemize import phonemize


phonemize("hello my queen", language = 'en-us', backend = 'espeak')


phonemize("hello my queen", language = 'en-us', backend = 'segments')


from espeakng import ESpeakNG

esng = ESpeakNG()

esng.g2p('Hello World!', ipa=2)







from g2p import make_g2p

















































