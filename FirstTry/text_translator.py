# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:56:22 2020

@author: qtckp
"""

from textblob import TextBlob

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

blob = TextBlob(text)

blob


# Section 11.2.2 snippets
blob.sentences

blob.words


# Section 11.2.3 snippets
blob

blob.tags


# Getting the polarity and subjectivity from the Sentiment Object
%precision 3

blob.sentiment.polarity

blob.sentiment.subjectivity

# Getting the Sentiment of a Sentence 
for sentence in blob.sentences:
    print(sentence.sentiment)

    

# Section 11.2.7 snippets
blob

blob.detect_language()

spanish = blob.translate(to='es')

spanish

spanish.detect_language()

chinese = blob.translate(to='zh')

chinese

chinese.detect_language()

spanish.translate()

chinese.translate() 






from textblob import Word

word = Word('theyr')

word.spellcheck()

word.correct()  # chooses word with the highest confidence value

from textblob import TextBlob

sentence = TextBlob('Ths sentense has missplled wrds.')

sentence.correct()








#https://dev-gang.ru/article/perevod-teksta-s-pomosczu-google-translate-api-v-python-ahgm88wx1k/

from googletrans import Translator

translator = Translator()
result = translator.translate('Hello', src='en', dest='ru')

print(result.src)
print(result.dest)
print(result.text)
print(result.pronunciation)



translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])



import pronouncing
pronouncing.rhymes("climbing")
pronouncing.phones_for_word('Привет')



import os
from gtts import gTTS

tts = gTTS('hello')

tts.save('hello.mp3')
os.system("hello.mp3")



# это позднее где-то пригодится

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Hello World сука")
speak.Speak("Привет пидор")
#speak.Speak("Ich will")




import pyttsx3
engine = pyttsx3.init()
engine.say('Good morning.')
engine.runAndWait()





from google_speech import Speech # sox too

# say "Hello World"
text = "Hello World"
lang = "en"
speech = Speech(text, lang)
speech.play()

# you can also apply audio effects while playing (using SoX)
# see http://sox.sourceforge.net/sox.html#EFFECTS for full effect documentation
sox_effects = ("speed", "1.5")
speech.play(sox_effects)


























