import pickle
from collections import defaultdict
import math
class Ngram():

    def __init__(self,n):
        file = open('edited.txt','r')
        text = file.read()
        file.close()
        
        self.n = n
        self.occurences = defaultdict(list)
        self.occs_count = defaultdict(lambda:0)

        self.context_count = defaultdict(lambda:0)

        self.vocab = defaultdict(lambda: 0)
        self.train_vocab = defaultdict(lambda: 0)
        self.dev_vocab = defaultdict(lambda: 0)
        self.test_vocab = defaultdict(lambda: 0)

        self.sentences = []

        if n ==2: # for knesner-neys
            self.biprevs=defaultdict(lambda: 0)
            self.binexts=defaultdict(lambda: 0)
        
        text = text.split('.')

        for sent in text:
            sent = sent +' </s> '
            sent = sent.split()
            self.sentences.append(sent)
            for i in range(0,len(sent)-1):
                self.vocab[sent[i]]+=1
                if n==2:
                    self.biprevs[sent[i+1]]+=1
                    self.binexts[sent[i]]+=1
            self.vocab[sent[len(sent)-1]]+=1

        self.wrd_cnt = sum(self.vocab.values())

        len_sent = len(self.sentences)
        
        self.train = self.sentences[0:int(0.8*len_sent)]
        self.dev = self.sentences[int(len_sent*0.8):int(len_sent*0.9)]
        self.test = self.sentences[int(len_sent*0.9):]

        #building train,dev and test vocabs
        for sent in self.train:
            for i in range(0,len(sent)-1):
                self.train_vocab[sent[i]]+=1
            self.train_vocab[sent[len(sent)-1]]+=1
        for sent in self.dev:
            for i in range(0,len(sent)-1):
                self.dev_vocab[sent[i]]+=1
            self.dev_vocab[sent[len(sent)-1]]+=1
        for sent in self.test:
            for i in range(0,len(sent)-1):
                self.test_vocab[sent[i]]+=1
            self.test_vocab[sent[len(sent)-1]]+=1
    
        self.build_ngram()
        if n == 2:
            self.tot_bigrams=len(set(self.context_count.keys()))

    def build_ngram(self):
            # I'll build all ngrams from n = 1 to n = self.n
        n = self.n
        for sent in self.train:
                tojoin = (n-1)*['<s>'] if n >1 else ['<s>']
                tokens = tojoin + sent 
                cont = []
                st = 0; end = n-1
                if n == 1:
                    end = 0
            
                while end <=len(tokens)-1:
                    self.context_count[tuple(tokens[st:end+1])]+=1
                    self.occurences[tuple(tokens[st:end])].append(tokens[end])
                    st+=1;end+=1
        
        for key in list(self.occurences.keys()):
            self.occs_count[key]=len(self.occurences[key])
            self.occurences[key] = set(self.occurences[key])

