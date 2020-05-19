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




































