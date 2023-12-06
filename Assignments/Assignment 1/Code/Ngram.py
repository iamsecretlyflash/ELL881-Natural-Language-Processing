import pickle
from collections import defaultdict
import math
class Ngram():

    def __init__(self,n):
        file = open('edited.txt','r')
        text = file.read()
        file.close()
        
        self.n = n
        self.occurences = defaultdict(list) # context + different words 
        self.occs_count = defaultdict(lambda:0) # number of times a context appears (N-1 grams)

        self.context_count = defaultdict(lambda:0) # Number of times a particular Ngram appears

        self.vocab = defaultdict(lambda: 0) # GENERAL VOCABULARY
        self.train_vocab = defaultdict(lambda: 0) 
        self.dev_vocab = defaultdict(lambda: 0)
        self.test_vocab = defaultdict(lambda: 0)

        self.sentences = [] # ALL SENTENCES IN THE TEXT

        if n ==2: # for knesner-neys
            # FOR KNESNER NEYS, WE NEED TO CALCULATE Pcontinuation. For it's efficient implementation I've stored all the bigram appearing for a particular word
            self.biprevs=defaultdict(lambda: set())
            self.binexts=defaultdict(lambda: set())
        
        text = text.split('.') # Splitting sentences at full stop.

        for sent in text:
            sent = sent +' </s> ' # adding sentence end tag
            sent = sent.split() # token level split
            self.sentences.append(sent) 
            for i in range(0,len(sent)-1):
                self.vocab[sent[i]]+=1
                if n == 2:
                    self.biprevs[sent[i+1]].add(sent[i])
                    self.binexts[sent[i]].add(sent[i+1])
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
        keys = list(self.context_count.keys())

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
            # should have used set and 'add'

def prob_nosmooth(model,cont,wrd):
        try:
            denom = float(model.occs_count[cont])
            temp = list(cont)
            temp.append(wrd)
            num = model.context_count[tuple(temp)]
            return num/denom
        except:
            return 0

def perplexity(model,sent):
        n = model.n
        sent = sent.split()
        context = ['<s>']*(n-1)
        res = [];i = 0;perp=0
        for wrd in sent:
            wrd_probs={}
            con = tuple(context)
            if wrd == '.':
                if n!=1:context = ['<s>']*(n-1)
            else:
                if n!=1:context.pop(0);context.append(wrd)
                perp+=math.log(prob_nosmooth(model,con,wrd))
                res.append(wrd)
                i+=1
        perp = math.exp(abs(perp/len(res)))
        return ' '.join(res),perp