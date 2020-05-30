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


epi = epitran.Epitran('eng-Latn')

epi.transliterate('Hello')



epi=epitran.Epitran('deu-Latn')
epi.transliterate('Du hast mich')




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

isletool.LexicalTool('ISLEdict.txt').lookup('cat')

from pysle import pronunciationtools

pronunciationtools.findClosestPronunciation(isleDict, 'cat', ['k', 'æ',])



tl = isletool.LexicalTool()

tl.lookup('cat')








from phonemizer.phonemize import phonemize


phonemize("hello", language = 'en-us', backend = 'espeak')
phonemize("hello my queen", language = 'en-us', backend = 'espeak')


phonemize("ich will", language = 'de', backend = 'espeak')

phonemize("bonjour le monde", language = 'fr-fr', backend = 'espeak')


phonemize("konnichiwa", language = 'japanese', backend = 'espeak')

phonemize("привет", language = 'ru', backend = 'espeak')
phonemize("salam", language = 'fa', backend = 'espeak')
phonemize("انتساب", language = 'fa', backend = 'espeak')
phonemize("انتساب", language = 'fa-latn', backend = 'espeak')





from espeakng import ESpeakNG

esng = ESpeakNG()

esng.g2p('Hello World!', ipa=2)







from g2p import make_g2p

















































