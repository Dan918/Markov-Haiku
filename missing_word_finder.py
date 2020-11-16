# -*- coding: utf-8 -*-
"""


@author: Dan
"""

import nltk
import sys
import json
import cmudict 
from string import punctuation
cmu=cmudict.dict()

path=(r'Desktop\python code')
file='txt cmu.txt'


f=open( r'C:\Users\Dan\Desktop\python code\zip\train.txt')
text=f.read()



def main():
    haiku= load_haiku(text)
    exceptions= cmuduct_missing(haiku)
    missing_words_dict= make_exceptions_dict(exceptions)
    save_exceptions(missing_words_dict)
    
def load_haiku(file):
    haiku=set(in_file.read().replace('-',' ').split())
    return haiku

def cmudict(word_set):
    exceptions=set()
    for word in word_set:
        word=word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word =word[:-2]
        
        if word not in cmudict:
            exceptions.add(word)
    print('exception')
    print('number of unique words in haiku={}'.format(len(word_set)))
    print('number of words in corpus not in cmudict ={}'.format(len(exceptions)))
    membership= (1-(len(exceptions)/len(word_set)))*100
    print('cmudict membership = {.1f}{}'.format(membership,'%'))
    return exceptions

def make_exceptions_dict(exceptions_set):
    missing_words={}
    print('input # of syllables in word')
    for word in exceptions_setL:
        while True:
            num_sylls = input('enter number of syllables in {}: '.format(word))
            if num_sylls.isdigit():
                break
            else:
                print(' not a valid answer!',file=sys.stderr)
        missing_words[word]=int(num_sylls)
    print()
    print(missing_words)
    print('Make Changes to Dictionary Before Saving?')
    print('''
    0 - Exit & Save
    1 - Add a Word or Change a Syllable Count 
    2 - Remove a Word
    ''')
    
    while True:
        choice = input('\nEnter choice: ')   
        if choice == '0':
            break
        elif choice == '1':
            word = input('\nWord to add or change: ')
            missing_words[word] = int(input("Enter number syllables in {}: '
                                            .format(word)))
        elif choice == '2':
            word = input('\nEnter word to delete: ')
            missing_words.pop(word, None)
            
    print('\nNew words or syllable changes:')
    print(missing_words)

    return missing_words
    
def save_exceptions(missing_words):
    json_string=json.dumps(missing_words)
    f=open('missing_words.json','w')
    f.write(json_string)
    f.close()
    print('file saves as missing_words.json')
    
    if __name__ == '__main__':
        main()