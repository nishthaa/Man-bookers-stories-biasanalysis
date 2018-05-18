# -*- coding: utf8 -*-
import nltk
import glob
import errno
import string

num = 2007
path = "C:\\Users\\Shravika\\Desktop\\4th sem\\Books Data\\" + str(num) + "\\*.txt"
files = glob.glob(path)
for f_name in files:
    print f_name
    try:
        with open(f_name, "r+") as f:
            count = 0
            verb_str = ""
            for l in f:
                count = count + 1
                verb_str = verb_str + "\n"
                if count>3:
                    line = l
                    line.decode('utf8')
                    print line
                    tokens = nltk.word_tokenize(line)
                    tagged = nltk.pos_tag(tokens)
                    verbs = [word for word, pos in tagged \
                            if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN')]
                    downcased = [x.lower() for x in verbs]
                    verb_str = verb_str + "\n".join(downcased)
            print verb_str
            f.write(verb_str)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
