# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:09:35 2017

@author: RealRobert
"""

import jap_text_processer 
import pickle

sentDumpPath = open('H:\\nihon_better_dump','rb')
wordDumpPath = open('H:\\nihon_better_dump_words_segregated','wb')


try:
    counter = 0
    while True:
        counter +=1
        sentence = pickle.load(sentDumpPath)
        for word in sentence:
            kanji_only = jap_text_processer.extract_unicode_block(jap_text_processer.kanji,word)
            if len(kanji_only) > 0:
                pickle.dump(kanji_only,wordDumpPath)
        if counter % 1000 == 0:
            print(counter)
except:
    print('FINITA LA COMEDIA')
            
wordDumpPath.close()