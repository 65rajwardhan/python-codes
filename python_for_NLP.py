# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:14:51 2024

@author: rajwa
"""

#we want to replace words in string
#.replace(new,old)
sentence2="i visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY", "Malaysia").replace("IND", "India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

####################################
#we want auto correct in the sentence
from autocorrect import Speller
spell=Speller(lang='en')
spell("Engilish")

######################################
#correct whole sentence

import nltk
nltk.download("punkt")
from nltk import word_tokenize
sentence="naturel languuage processin deals withh the aart of extrct"
sentence=word_tokenize(sentence)
corrected_sentence=" ".join([spell(word)for word in sentence])
corrected_sentence

#################################################
#stemming
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("jumping")
stemmer.stem("jumped")

##############################
#lamatize
nltk.download("wornet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
stemmer.stem("programed")
stemmer.stem("programs")
stemmer.stem("battling")    
stemmer.stem("amazing")

##########################################
#chunking
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence1="we are learning NLP in python by sanivani"
nltk.download('average_perceptron_tagger')
words=word_tokenize(sentence1)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]

####################################
#sentence tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning python. from naik sir")
sent

##############################################

from nltk.wsd import lesk
sentence1="keep your saving in the bank"
print(lesk(word_tokenize(sentence1),'bank'))

sentence2="it is risky to drive over banks of rivers"
print(lesk(word_tokenize(sentence1),'bank'))
