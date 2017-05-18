# -*- coding: utf-8 -*-

from gensim.models import word2vec
import operator

model = word2vec.Word2Vec.load('/media/robert/1TB-1/linuxfolder/gitlair/mag/kuromoji_five_window_100_min')
#model = word2vec.Word2Vec.load('I:\\linuxfolder\\gitlair\\mag\\kuromoji_solo_kanji_last_only_min_20')

class VocabManager():
    model = model
    vocab = model.vocab
    solo_kanji = []
    
    def __init__(self,n=100):	# upon initialization creates a list of top-n frequently used solo kanji, available at .solo_kanji
        if n > 1000:
            n = 1000
        counter = -1
        while len(self.solo_kanji) < n:
            counter += 1
            if len(self.model.index2word[counter]) == 1:
                self.solo_kanji.append(self.model.index2word[counter])
    
    def top_kanji_everywhere(self,kanji,n=100): # returns a list of of top-n frequently used words containing specified kanji
        raw_list = []
        counter = -1
        counter_success = 0
        while (counter_success < n)&(counter < len(model.vocab)):
            counter += 1
            try:
                if (kanji in model.index2word[counter])&(kanji != model.index2word[counter]):
                    raw_list.append(model.index2word[counter])
                    counter_success += 1 # len!
            except IndexError:
                print(counter)
        self.last_raw_list = raw_list
        return raw_list
        
    def endswith_top_kanji_everywhere(self,kanji,n=100):  # returns a list of of top-n frequently used words ending with specified kanji
        raw_list = []
        counter = -1
        counter_success = 0
        while (counter_success < n)&(counter < len(model.vocab)):
            counter += 1
            try:
                if (model.index2word[counter].endswith(kanji))&(kanji != model.index2word[counter]):
                    raw_list.append(model.index2word[counter])
                    counter_success += 1 # len!
            except IndexError:
                print(counter)
        self.last_raw_list = raw_list
        return raw_list
    
    def kanji_everywhere(self,kanji): # depr
        raw_list = []
        for item in self.vocab:
            if kanji in item:
                raw_list.append(item)
        return raw_list

    def estimate_convergention(self,kanji,n = 100,mode = None): # returns list of neighbours of top-n frequently used words with kanji list
								# either "kanji in word" or "word ends with kanji"
        if not mode:
            return model.most_similar(self.top_kanji_everywhere(kanji,n))
        else:
            if mode == 'endswith':
                print(mode)
                return model.most_similar(self.endswith_top_kanji_everywhere(kanji,n), topn = 10)
    
    
mng = VocabManager()

#long_dict = {}
#for i in model.vocab:
#    if len(i) > 1:
#        long_dict[i] = model.vocab[i].count
#        
#sorted_x = sorted(long_dict.items(), key=operator.itemgetter(1))
