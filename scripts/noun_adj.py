import spacy
nlp = spacy.load('en')
doc = nlp(u'The elderly Bruno knows he is not far from death. One of his last wishes is to contact his estranged son, Miles, whose marriage to an Indian woman drove a decades-long wedge between father and son. When Miles comes back into his father’s life, Bruno must confront his guilt, and his family must overcome the tension that grew during his long absence. Set against an enchanting London backdrop, Murdoch’s complex family drama is a poignant exploration of love, remorse, and the power of emotional redemption.Mark and John are sincere employees at Google.')
noun_adj_pairs = []
for i,token in enumerate(doc):
    if token.pos_ not in ('PROPN'):
        continue
    for j in range(i+1,len(doc)):
        if doc[j].pos_ == 'ADJ':
            noun_adj_pairs.append((token,doc[j]))
            break
print (noun_adj_pairs)

