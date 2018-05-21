import glob
import errno
import string

num = 2016
for i in range(0, 50):
    path = "C:\\Users\\Shravika\\Desktop\\4th sem\\Books Data\\" + str(num) + "\\*.txt"
    files = glob.glob(path)
    for f_name in files:
        try:
            with open(f_name, "r+", encoding = "utf8") as f:
                count = 0
                male_count = 0
                female_count = 0
                for l in f:
                    count = count + 1
                    if count>3:
                        list_words = l.split(" ")
                        print (l)
                        print (len(list_words))
                        print (list_words)
                        if len(list_words) >= 3:
                            if list_words[2].strip() == "M":
                                print (list_words[0])
                                male_count = male_count + 1
                            elif list_words[2].strip() == "F":
                                print (list_words[0])
                                female_count = female_count + 1
                            if(list_words[0] == "G:"):
                                if list_words[1] == "M":
                                    male_count = male_count + 1
                                elif list_words[1] == "F":
                                    female_count = female_count + 1
                f.write("\n")
                f.write("Mentions:" + "\n")
                f.write("Male: " + str(male_count) + "\n")
                f.write("Female: " + str(female_count) + "\n")
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    num = num - 1
