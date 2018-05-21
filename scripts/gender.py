import glob
import errno
import string

num = 2017
for i in range(0, 25):
    path = "C:\\Users\\Shravika\\Desktop\\4th sem\\Books Data\\" + str(num) + "\\*.txt"
    files = glob.glob(path)
    for f_name in files:
        try:
            with open(f_name, "r+", encoding = "utf8") as f:
                count = 0
                for l in f:
                    count = count + 1
                    if count>3:
                        list_words = l.split(" ")
                        for word in list_words:
                            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
                            word_p = ""
                            for char in word:
                               if char not in punctuations:
                                   word_p = word_p + char
                            with open("f.txt") as female:
                                for fem_name in female:
                                    if fem_name.strip() == word_p.lower():
                                        f.write(word_p.upper() + " - " + "F" + "\n")
                            with open("m.txt") as male:
                                for m_name in male:
                                    if m_name.strip() == word_p.lower():
                                        f.write(word_p.upper() + " - " + "M" + "\n")
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    num = num - 1
