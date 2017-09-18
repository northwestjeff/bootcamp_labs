import string
from collections import Counter


def open_text():
    user_input = str(input("What text should I count?: "))
    #user_input = "metamorphasis"   # TEMOPRARY PLUG FOR USER INPUT so I don't have to type in metamorphasis while testing
    file = open("{}.txt".format(user_input), "r")
    file = file.read()
    file = file.lower()
    return file


def common_words_list():
    stop_words = open("common-english-words.txt", "r")
    stop_words = stop_words.read()
    stop_words_list = stop_words.split(",")
    stop_words_list[0] = "a "
    return stop_words_list


def scrub_text_puncuation_and_common(file):
    punct_list = set(string.punctuation)
    text_sans_punct = "".join(x for x in file if x not in punct_list).split()
    text_sans_punct_sans_common = " ".join(y for y in text_sans_punct if y not in stop_words_list)
    print(punct_list)
    return text_sans_punct_sans_common


def file_to_list(text_sans_punct_sans_common):
    file_list = text_sans_punct_sans_common.split()
    clean_text = Counter(file_list)
    clean_text.pop("a", "")
    return clean_text

def display(instances = 10):
    counter = 1
    print("Here are the {} most common words:".format(instances))
    print("")
    for k, v in clean_text.most_common(instances):
        print("{}) {}:  {} times.".format(counter, k, v))
        counter +=1


file = open_text()
stop_words_list = common_words_list()
text_sans_punct_sans_common = scrub_text_puncuation_and_common(file)
clean_text = file_to_list(text_sans_punct_sans_common)
display(int(input("How many of the most common words to dispaly?: ")))


# print("Printing Clean text: {}  ".format(clean_text))
# print(clean_text[0])




