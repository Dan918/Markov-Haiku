# -*- coding: utf-8 -*-
"""


@author: Dan
"""


import nltk
import sys
import cmudict 
from string import punctuation
import json
cmudict=cmudict.dict()

path=(r'Desktop\python code')
file='txt cmu.txt'


f=open( r'C:\Users\Dan\Desktop\python code\zip\train.txt')
text=f.read()

with open('missing_words.json') as f:
    missing_words = json.load(f)
    
def count_syllables(words):
    words=words.replace('-',' ')
    words=words.lower().split()
    num_sylls=0
    for word in words:
        word=word.strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word=word[:-2]
        if word in missing_words:
            num_sylls += missing_words[word]
        else:
            for phonemes in cmudict[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_sylls +=1
    return num_sylls
            

def main():
    while True:
        print("Syllable Counter")
        word = input("Enter word or phrase else press Enter to Exit: ")
        if word == '':
            sys.exit()
        try:
            num_syllables = count_syllables(word)
            print("number of syllables in {} is: {}"
                  .format(word, num_syllables))
            print()
        except KeyError:
            print("Word not found.  Try again.\n", file=sys.stderr)

if __name__ == '__main__':
    main()
