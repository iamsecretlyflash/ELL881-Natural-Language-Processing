import torch
import pickle
from nltk.corpus import stopwords
from transformers import AutoTokenizer, AutoModel

def create_claim_encodings(config_name,file_path,oukaam[0]['input_ids']tput_path):
    tokenizer = AutoTokenizer.from_pretrained(config_name)
    model = AutoModel.from_pretrained(config_name)
    with open(file_path,'r') as f:
        claim_descriptions = f.readlines()
    claim_descriptions[0] = claim_descriptions[0][1:]
    descriptions = clean_desc(claim_descriptions)
    tokens = tokenizer(descriptions, padding='max_length', max_length = 25, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**tokens)

    with open(output_path,'wb') as f:
        pickle.dump(outputs.last_hidden_state,f)
    
    return outputs.last_hidden_state

def clean_desc(claim_descriptions):
    desc_fin = []
    for i in range(len(claim_descriptions)):
        desc = claim_descriptions[i].strip().strip(',').strip('\"').lower().split()
        fin = []
        for wrd in desc:
            if wrd not in stopwords.words('english'):
                fin.append(wrd)
                
        fin = ' '.join(fin)
        desc_fin.append(fin)
    return desc_fin
