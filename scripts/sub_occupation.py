import glob
import errno
import string

num = 1969
for i in range(0, 23):
    path = "C:\\Users\\Ashima\\Desktop\\Books Data\\" + str(num) + "\\*.txt"
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
                                    with open("occupations.txt") as occupation:
                                        for fem_occ in occupation:
                                         if fem_name.strip() == word_p.lower():
                                            if fem_pcc.strip()== word_p.lower():
                                                f.write(word_p.lower())
                            with open("m.txt") as male:
                                for m_name in male:
                                    with open("occupations.txt") as occupation:
                                         for m_occ in occupation:
                                               if m_name.strip() == word_p.lower():
                                                   if m_occ.strip()== word_p.lower():
                                                        f.write(word_p.lower())
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    num = num - 1
