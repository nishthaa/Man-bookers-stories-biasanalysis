import spacy
import glob
import string

num = 1992
for i in range(0, 25):
    path = "/home/shravika/Desktop/Man-bookers-stories-biasanalysis/data/" + str(num) + "/*.txt"
    files = glob.glob(path)
    for f_name in files:
        with open(f_name, "r+", encoding = "utf8") as f:
            count = 0
            f.write("\n")
            for l in f:
                count = count + 1
                if count>3:
                    nlp = spacy.load('en_core_web_sm')
                    doc = nlp(l)
                    for token in doc:
                        if token.dep_ == "nsubj":
                            head = token.head.text
                            if token.head.pos_ == "VERB":
                                print (token.text + " " + token.head.text)
                                f.write("N: " + token.text.upper() + " " + "V: " + token.head.text.lower() + "\n")
    num = num - 1
