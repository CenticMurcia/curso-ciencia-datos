


################################# IMPORTS

import re
import html
import spacy


################################# SPECIAL TOKENS

UNK     = "xxunk"  # 0
PAD     = "xxpad"  # 1
BOS     = "xxbos"  # 3
EOS     = "xxeos"  # 4
TK_REP  = "xxrep"  # 5
TK_WREP = "xxwrep" # 6
TK_UP   = "xxup"   # 7
TK_MAJ  = "xxmaj"  # 8


################################# Pre-tokenization rules

def sub_br(t):
    "Replaces the <br /> by \n"
    re_br = re.compile(r'<\s*br\s*/?>', re.IGNORECASE)
    return re_br.sub("\n", t)

def spec_add_spaces(t):
    "Add spaces around / and #"
    return re.sub(r'([/#])', r' \1 ', t)

def rm_useless_spaces(t):
    "Remove multiple spaces"
    return re.sub(' {2,}', ' ', t)

def replace_rep(t):
    "Replace repetitions at the character level: cccc -> TK_REP 4 c"
    def _replace_rep(m) -> str:
        c,cc = m.groups()
        return f' {TK_REP} {len(cc)+1} {c} '
    re_rep = re.compile(r'(\S)(\1{3,})')
    return re_rep.sub(_replace_rep, t)
    
def replace_wrep(t):
    "Replace word repetitions: word word word -> TK_WREP 3 word"
    def _replace_wrep(m) -> str:
        c,cc = m.groups()
        return f' {TK_WREP} {len(cc.split())+1} {c} '
    re_wrep = re.compile(r'(\b\w+\W+)(\1{3,})')
    return re_wrep.sub(_replace_wrep, t)

def fixup_text(x):
    "Various messy things we've seen in documents"
    re1 = re.compile(r'  +')
    x = x.replace('#39;', "'").replace('amp;', '&').replace('#146;', "'").replace(
        'nbsp;', ' ').replace('#36;', '$').replace('\\n', "\n").replace('quot;', "'").replace(
        '<br />', "\n").replace('\\"', '"').replace('<unk>',UNK).replace(' @.@ ','.').replace(
        ' @-@ ','-').replace('\\', ' \\ ')
    return re1.sub(' ', html.unescape(x))



################################# Post-Tokenization rules
#
# These rules are applies after the tokenization on the list of tokens.

def replace_all_caps(x):
    "Replace tokens in ALL CAPS by their lower version and add `TK_UP` before."
    res = []
    for t in x:
        if t.isupper() and len(t) > 1: res.append(TK_UP); res.append(t.lower())
        else: res.append(t)
    return res

def deal_caps(x):
    "Replace all Capitalized tokens in by their lower version and add `TK_MAJ` before."
    res = []
    for t in x:
        if t == '': continue
        if t[0].isupper() and len(t) > 1 and t[1:].islower(): res.append(TK_MAJ)
        res.append(t.lower())
    return res

def add_eos_bos(x):
    return [BOS] + x + [EOS]


################################# Tokenizer

DEFAULT_SPEC_TOKS  = [UNK, PAD, BOS, EOS, TK_REP, TK_WREP, TK_UP, TK_MAJ]
DEFAULT_PRE_RULES  = [fixup_text, replace_rep, replace_wrep, spec_add_spaces, rm_useless_spaces, sub_br]
DEFAULT_POST_RULES = [deal_caps, replace_all_caps, add_eos_bos]
SPACY_EN_TOKENIZER = spacy.blank("en").tokenizer

def tokenize(text):
    
    ######### Apply pre rules
    for pre_rule in DEFAULT_PRE_RULES: text = pre_rule(text)
        
    ######### Apply Spacy English Tokenizer
    tokens = [str(token) for token in SPACY_EN_TOKENIZER(text)]
    
    ######### Apply post rules
    for post_rule in DEFAULT_POST_RULES: tokens = post_rule(tokens)
        
    return tokens




################################# Some tests

assert replace_rep('cccc')                       == ' xxrep 4 c '
assert replace_wrep('word word word word word ') == ' xxwrep 5 word  '
assert replace_all_caps(['I', 'AM', 'SHOUTING']) == ['I', 'xxup', 'am', 'xxup', 'shouting']
assert deal_caps(['My', 'name', 'is', 'Javi'])   == ['xxmaj', 'my', 'name', 'is', 'xxmaj', 'javi']
assert add_eos_bos(['My', 'name', 'is', 'Javi']) == ['xxbos', 'My', 'name', 'is', 'Javi', 'xxeos']


assert tokenize("Hello, my name is Javi!!!!") == ['xxbos','xxmaj','hello',',','my','name','is','xxmaj','javi','xxrep','4','!','xxeos']