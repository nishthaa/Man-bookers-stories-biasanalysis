import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("Daniel is heading north. He is looking for someone. The simplicity of his early life with Daddy and Cathy has turned sour and fearful. They lived apart in the house that Daddy built for them with his bare hands. They foraged and hunted. When they were younger, Daniel and Cathy had gone to school. But they were not like the other children then, and they were even less like them now. Sometimes Daddy disappeared, and would return with a rage in his eyes. But when he was at home he was at peace. He told them that the little copse in Elmet was theirs alone. But that wasn't true. Local men, greedy and watchful, began to circle like vultures. All the while, the terrible violence in Daddy grew. Elmet is a lyrical commentary on contemporary English society and one family's precarious place in it, as well as an exploration of how deep the bond between father and child can go.")
for token in doc:
  if token.dep_ == "nsubj":
    head = token.head.text
    if token.head.pos_ == "VERB":
      print (token.text + " " + token.head.text)
