# CODE from:
#
# https://towardsdatascience.com/how-to-code-the-transformer-in-pytorch-24db27c8f9ec#3fa3
# http://peterbloem.nl/blog/transformers
# http://nlp.seas.harvard.edu/2018/04/03/attention

import math
import torch
import torch.nn as nn
import torch.nn.functional as F


def attention(queries, keys, values, mask=None):

    # queries:[..., SEQUENCE_DIM, KEY_DIM]
    # keys:   [..., SEQUENCE_DIM, KEY_DIM]
    # values: [..., SEQUENCE_DIM, VALUE_DIM]
    # output: [..., SEQUENCE_DIM, VALUE_DIM]

    KEY_DIM = queries.size()[-1]
    scores = torch.matmul(queries, keys.transpose(-1, -2))
    scores = scores / math.sqrt(KEY_DIM)
    if mask is not None:
        scores = scores.masked_fill(mask==0, -1e9)
    scores = F.softmax(scores, dim=-1)
        
    output = torch.matmul(scores, values)
    return output



class MultiHeadAttention(nn.Module):

    def __init__(self, inputEmb_dim, outputEmb_dim, num_heads, key_dim, value_dim):

        super().__init__()

        self.dim_heads = num_heads
        self.dim_keys  = key_dim
        self.dim_vals  = value_dim

        self.linear_q = nn.Linear(inputEmb_dim, num_heads * key_dim)
        self.linear_k = nn.Linear(inputEmb_dim, num_heads * key_dim)
        self.linear_v = nn.Linear(inputEmb_dim, num_heads * value_dim)
        self.linear_o = nn.Linear(num_heads * value_dim, outputEmb_dim)

    def forward(self, x, mask=None):

        # x: [BS, SEQUENCE_DIM, INPUT_EMBEDING_DIM]
        dim_bs  = x.size(0)
        dim_seq = x.size(1)

        q = self.linear_q(x) # [BS, SEQUENCE_DIM, HEAD_DIM * KEY_DIM]
        k = self.linear_k(x) # [BS, SEQUENCE_DIM, HEAD_DIM * KEY_DIM]
        v = self.linear_v(x) # [BS, SEQUENCE_DIM, HEAD_DIM * VALUE_DIM]

        q = q.view(dim_bs, dim_seq, self.dim_heads, self.dim_keys) # [BS, SEQUENCE_DIM, HEAD_DIM, KEY_DIM]
        k = k.view(dim_bs, dim_seq, self.dim_heads, self.dim_keys) # [BS, SEQUENCE_DIM, HEAD_DIM, KEY_DIM]
        v = v.view(dim_bs, dim_seq, self.dim_heads, self.dim_vals) # [BS, SEQUENCE_DIM, HEAD_DIM, VALUE_DIM]

        k = k.transpose(1,2) # [BS, HEAD_DIM, SEQUENCE_DIM, KEY_DIM]
        q = q.transpose(1,2) # [BS, HEAD_DIM, SEQUENCE_DIM, KEY_DIM]
        v = v.transpose(1,2) # [BS, HEAD_DIM, SEQUENCE_DIM, VALUE_DIM]

        out = attention(q, k, v, mask) # [BS, HEAD_DIM, SEQUENCE_DIM, VALUE_DIM]

        out = out.transpose(1,2) # [BS, SEQUENCE_DIM, HEAD_DIM, VALUE_DIM]
        out = out.contiguous()   # needed
        out = out.view(dim_bs, dim_seq, self.dim_heads * self.dim_vals) # [BS, SEQUENCE_DIM, HEAD_DIM * VALUE_DIM]
        out = self.linear_o(out) # [BS, SEQUENCE_DIM, OUTPUT_EMBEDING_DIM]

        return out



class FeedForward(nn.Module):

    def __init__(self, emb_dim, hidden_dim=2048, dropout=0.1):

        super().__init__() 
        self.linear_1 = nn.Linear(emb_dim, hidden_dim)
        self.dropout  = nn.Dropout(dropout)
        self.linear_2 = nn.Linear(hidden_dim, emb_dim)

    def forward(self, x):
        x = self.dropout(F.relu(self.linear_1(x)))
        x = F.relu(self.linear_2(x))
        return x



class LayerNorm(nn.Module):

    def __init__(self, emb_dim, eps=1e-6):
        super().__init__()
    
        self.emb_dim = emb_dim
        self.eps   = eps

        # Learnable parameters
        self.alpha = nn.Parameter(torch.ones(self.emb_dim))
        self.bias  = nn.Parameter(torch.zeros(self.emb_dim))

    def forward(self, x):

        # x: [BS, SEQUENCE_DIM, EMBEDING_DIM]

        mean = x.mean(dim=-1, keepdim=True) # [BS, SEQUENCE_DIM, 1]
        std  = x.std(dim=-1,  keepdim=True) # [BS, SEQUENCE_DIM, 1]

        return self.alpha * (x - mean) / (std + self.eps) + self.bias # [BS, SEQUENCE_DIM, EMBEDING_DIM]
        


class EncoderBlock(nn.Module):

    def __init__(self, emb_dim, num_heads):

        super().__init__()

        self.att    = MultiHeadAttention(inputEmb_dim=emb_dim,
                                         outputEmb_dim=emb_dim,
                                         num_heads=num_heads,
                                         key_dim=key_dim,
                                         value_dim=value_dim)
        self.norm1  = LayerNorm(emb_dim=emb_dim)
        self.ff     = FeedForward(emb_dim=emb_dim, hidden_dim=2048)
        self.norm   = LayerNorm(emb_dim=emb_dim)


    def forward(self, x):
        x = self.norm1(x + self.att(x))
        x = self.norm2(x + self.ff(x))
        return x



class Transformer(nn.Module):
    def __init__(self, k, heads, depth, seq_length, num_tokens, num_classes):
        super().__init__()

        self.num_tokens = num_tokens
        self.token_emb = nn.Embedding(num_tokens, k)
        self.pos_emb   = nn.Embedding(seq_length, k)

        # The sequence of transformer blocks that does all the 
        # heavy lifting
        encoder_blocks = []
        for i in range(depth):
            encoder_blocks.append(TransformerBlock(k=k, heads=heads))
        
        self.encoder_blocks = nn.Sequential(*encoder_blocks)

        # Maps the final output sequence to class logits
        self.toprobs = nn.Linear(k, num_classes)


    def forward(self, x):
        
        # x:       [BS, SEQUENCE_DIM] tensor of tokens (integer values representing words).
        # returns: [BS, ClASS_DIM]    tensor of log-probabilities over the  classes.
        
        
        # generate token embeddings
        tokens = self.token_emb(x)
        b, t, k = tokens.size()

        # generate position embeddings
        positions = torch.arange(t)
        positions = self.pos_emb(positions)[None, :, :].expand(b, t, k)
        
        x = tokens + positions
        
        # Transformer encoder
        x = self.encoder_blocks(x)
        
        # Average-pool over the t dimension and project to class 
        # probabilities
        x = self.toprobs(x.mean(dim=1))
        return F.log_softmax(x, dim=1)
