import unicodedata
import os
import tinysegmenter
import ast
import re
import nltk
import pickle
from nltk.tokenize import RegexpTokenizer

jp_sent_tokenizer = nltk.RegexpTokenizer('[^ 「」!?。．]*[!?。]')

segmenter = tinysegmenter.TinySegmenter()

puncts = ['，', '&', 
'「', '；', '#', '〔', '❳', '》', '⟩', '］', '•', '\\', '＿', "'", '¡', '‚', '{', ':',
 '⟨', '〘', '－', '‒', '※', ']', '‣', '・', '›', '‡', '―', '［', ')', '་', '」', '：', '〕', 
 '）', '%', '»', '‹', '･', '‟', '@', '[', '％', '†', '‧', '"', '﹑', '︰', '､', '·', '＼', 
 '｢', '«', '_', '‼', '’', '〈', '＠', '』', '′', '﹐', '§', '‑', '゠', '（', '¿', '＃', '!', '-', '｡',
 '｝', '〝', '／', '〙', '།', '*', '〃', '？', '【', '＆', '《', '?', '.', '〞', ';', '—', '(', ',', '″', '】',
'｛', '。', '〟', '‰', '”', '/', '、', '⁉', '‘', '｣', '}', '＊', '“', '！', '〉', '．', '〜', '–', '‵', '„', '＂', '…', '『', '‐', 'っ','\n']

with open('/home/robert/Documents/stemtokstop/ja_stopword.txt','r') as stps:

    stopwords = stps.read().split('\n')

stopwords+= '\n'
'''
def get_punct(path):
    a = []
    with open(path,'r') as fdf:
        for i in fdf.read():
            if unicodedata.category(i).startswith('P'):
                a.append(i)
    return list(set(a))
'''

#nihon_dump = open('/home/robert/Documents/nihon_dump','wb')

def walkover(rootdir):

    for rt,dirs,files in os.walk(rootdir):
        for f in files:
            nihon_dump = open('/home/robert/Documents/nihon_dump2','ab')
            print(rt+f)
#            with open('/home/robert/Documents/nihon_dump','wb') as nihon_dump:
            try:
                compl = cycle_over_txt(rt+'/'+f)
            except:
                continue
            #print(len(compl))
            #print(compl[:10])
            for x in compl:
                pickle.dump(x,nihon_dump)
            nihon_dump.close()
    

def purify(heretic):
    pf = []
    
    for x in heretic:
        forcebreak = False
        for i in puncts:
            x = x.replace(i,'')
        if len(x) < 1:
            continue
           
        else:
            for i in stopwords:
                if x == i:
#                    print('DA',i,x)
                    forcebreak = True
                    
                    
                    
            if not forcebreak:
                pf.append(x)
    return pf



def cycle_over_txt(path):
    qwe = ['\\n','\n']
    cyclo = []
    with open(path,'r') as txt:
        for line in txt:
            for x in qwe:
                line = line.replace(x,'')

            dictcash = ast.literal_eval(line)
            separated_text = jp_sent_tokenizer.tokenize(dictcash['text'])
            #print(separated_text)
            for x in separated_text:
                x = re.sub('(0|[1-9][0-9]*)','specialtokenfornumbers', x)
                cyclo.append(purify(segmenter.tokenize(x)))
            #cyclo += purify(tokenized)
    return(cyclo)
        
def cycle_over_txt2(path):
    qwe = ['\\n','\n']
    cyclo = []
    counter = 0
    with open(path,'r') as txt:
        for line in txt:
            for x in qwe:
                line = line.replace(x,'')

            dictcash = ast.literal_eval(line)
            separated_text = jp_sent_tokenizer.tokenize(dictcash['text'])
            sent_dump = open('/run/media/robert/Kingston SSD/sent_dump.txt','a', encoding = 'utf-8')
            for x in separated_text:
                counter += 1
                x = re.sub('(0|[1-9][0-9]*)','specialtokenfornumbers', x)
                sent_dump.write(x+'\n')
                if counter % 1000 == 0:
                    print(counter)
            sent_dump.close()

def walkover2(rootdir):

    for rt,dirs,files in os.walk(rootdir):
        for f in files:

            print(rt+f)
#            with open('/home/robert/Documents/nihon_dump','wb') as nihon_dump:
            try:
                cycle_over_txt2(rt+'/'+f)
            except:
                continue
            #print(len(compl))
            #print(compl[:10])
          

def kuromoji_to_pickle(path):
    nihon_better_dump = open('/run/media/robert/Kingston SSD/nihon_better_dump','ab')
    counter = 0
    with open(path,'r',encoding='utf-8') as kmj:
        for line in kmj:
            counter += 1
            sent_cash = purify(line.split(' '))
            #print(sent_cash)
            pickle.dump(sent_cash,nihon_better_dump)
            if counter % 1000 == 0:
                print(counter)