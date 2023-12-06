import torch
from torch import nn
import numpy as np
class prompt(nn.Module):

    def __init__(self,
                 wte : nn.Embedding,
                 prompt_length : int = 20,
                 rand_range : float = 0.5,
                 initialize_from_vocab : bool = True):

        super(prompt, self).__init__()
        self.wte = wte
        self.prompt_length = prompt_length
        self.learned_embedding = nn.Parameter(self.initialize_embedding(wte,
                                                                        prompt_length,
                                                                        rand_range,
                                                                        initialize_from_vocab))

    
    def initialize_embedding(self,
                             wte : nn.Embedding,
                             prompt_length : int =10,
                             random_range : float = 0.5,
                             initialize_from_vocab : bool = True):

        if initialize_from_vocab:
            return self.wte.weight[:prompt_length].clone().detach()

        return torch.FloatTensor(wte.weight.size(1),prompt_length).uniform_(-random_range,random_range)

    def forward(self,tokens):
        input_embedding = self.wte(tokens[:,self.prompt_length:])
        learned_embedding = self.learned_embedding.repeat(input_embedding.size(0),1,1)
        print(input_embedding)
        print(input_embedding.shape)
        print(learned_embedding)
        print(learned_embedding.shape)
        return torch.cat((learned_embedding,input_embedding),dim=1)
                    