# -*- coding: utf8 -*-
import nltk
import glob
import errno
import string
import io

num = 1992
path = "C:\\Users\\Shravika\\Desktop\\4th sem\\Books Data\\" + str(num) + "\\*.txt"
files = glob.glob(path)
for f_name in files:
    print f_name
    try:
        with io.open(f_name, "r+", encoding = "UTF8") as f:
            count = 0
            verb_str = ""
            for l in f:
                count = count + 1
                if count>3:
                    verb_str = verb_str + "\n"
                    line = l
                    print line
                    tokens = nltk.word_tokenize(line)
                    tagged = nltk.pos_tag(tokens)
                    verbs = [word for word, pos in tagged \
                            if (pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ')]
                    for x in verbs:
                        x = x.lower()
                        verb_str = verb_str + "\n" + x
            print verb_str
            f.write(verb_str)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
