

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import pathlib
from collections import Counter
import pickle

import spacy_english_word_tokenizer as tokenizer




def read_file(text_file): 
    with open(text_file, 'r', encoding='utf8') as f:
        return f.read()

def parallel_map(func, array):
    
    cpu_cores = multiprocessing.cpu_count()
    array_len = len(array)
    chunksize = array_len // 100
    
    if cpu_cores<2:
        return list(tqdm(map(func, arr), total=array_len))
    else:
        with ProcessPoolExecutor(max_workers=cpu_cores) as ex:
            return list(tqdm(ex.map(func, array, chunksize=chunksize), total=array_len))

def readfile_and_tokenize(filename):
    return tokenizer.tokenize(read_file(filename))

def create_vocab(texts_toks, max_vocab=60000, min_freq=2):
    
    # Count number of occurrences for each token
    token_counts = Counter(p for o in texts_toks for p in o)
    
    print("Found", len(token_counts), "different tokens.")
    print( len([t for t in token_counts if token_counts[t]>=2]), "appears at least 2 times")
    print( len([t for t in token_counts if token_counts[t]>=3]), "appears at least 3 times")
    print( len([t for t in token_counts if token_counts[t]>=5]), "appears at least 5 times")
    
    # Create vocab limiting some words
    vocab = [t for t,c in token_counts.most_common(max_vocab) if c >= min_freq]
    
    # Put special tokens (xxTOKEN) at the begining of the list
    for o in tokenizer.DEFAULT_SPEC_TOKS[::-1]:
        if o in vocab:
            vocab.remove(o)
        vocab.insert(0, o)
        
    return vocab


data_path  = pathlib.Path("../../Datasets/NLP/IMBd")
filenames  = list( (data_path).glob('**/*.txt') )

print("Reading texts for discover tokens...")
texts_toks = parallel_map(func=readfile_and_tokenize, array=filenames)

print("Building vocab...")
vocab      = create_vocab(texts_toks, max_vocab=60000, min_freq=2)

vocab_file = open(data_path/'vocab.pkl','wb')
pickle.dump(vocab, vocab_file)
print("Vocab saved on", str(data_path/'vocab.pkl'))

######################## Test for reading vocab file 
vocab_file = open(data_path/'vocab.pkl','rb')
assert pickle.load(vocab_file) == vocab