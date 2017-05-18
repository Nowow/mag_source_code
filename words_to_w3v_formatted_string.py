#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 21:22:00 2017

@author: robert
"""

import pickle

wordDumpPath = open('/media/robert/Kingston SSD/nihon_better_dump','rb')
word_adagram = open('/media/robert/Kingston SSD/sentences_for_adagram','w',encoding = 'utf-8')

counter = 0
while True:
    counter +=1
    sentence = pickle.load(wordDumpPath)
    for word in sentence:
        word_adagram.write(word + ' ')
    if counter % 10000 == 0:
        print(counter, word)
        word_adagram.close()
        word_adagram = open('/media/robert/Kingston SSD/sentences_for_adagram','a',encoding = 'utf-8')
        

            
wordDumpPath.close()