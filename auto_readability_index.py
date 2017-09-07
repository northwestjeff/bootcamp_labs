import random
import string

# num_of_characters =
# num_of_words =
# num_of_sentances =


# number of characters / 4.17 + ((#words/#sentances)* 0.5) - 21.43

# def import_text():
#
# def number_chars():
#
# def words_per_sentance():
#
# def number_sentances():

ari_scale = {
         1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
         2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
         3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
         4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
         5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
         6: {'ages': '10-11', 'grade_level':    '5th Grade'},
         7: {'ages': '11-12', 'grade_level':    '6th Grade'},
         8: {'ages': '12-13', 'grade_level':    '7th Grade'},
         9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

speech_dict = {"1": "trump_speech.txt", "2": "mlk_letters.txt", "3": "obama_inaug.txt", "4": "gettysburg.txt"}
punct_list = [".", "!", "?", ",", ";", ":", "'", "-", '"'] # TODO need to add doublequote to this




def import_text(selection):
    file = open(speech_dict[selection], "r")
    file = file.read()
    return file

def remove_unnecessary_punct(file, punct_list):
    for punct in punct_list[3:-1]:
        file = file.replace(punct, "")
    file = file.replace("\n", " ")
    return file

def split_sentance(file, punc_list):
    for punct in punct_list[0:2]:
        split_file = file.split(punct)
        return split_file

def split_words(split_file):
    split_words = []
    for line in split_file:
        line_split = line.split(" ")
        split_words.append(line_split)
    return split_words

def words_in_sent(split_words):
    num_words_list = []
    for line in split_words:
        num_words_list = num_words_list.append(len(line))
    return num_words_list

def chars_in_words(split_words):
    char_in_words_list = []
    for line in split_words:
        for i in line:
            #print(len(i))
            char_in_words_list.append(len(i))
    return char_in_words_list

def sum_of_characters(char_in_words_list):
    sum_of_chars = 0
    for i in char_in_words_list:
        sum_of_chars += int(i)
    return sum_of_chars

def ari_scale_calc(ari_scale, formula):
    print("This text has an ARI rating of {}. ".format(str(formula)))
    print("")
    print("This corresponds to a {} reading level; appropriate for {} year-olds.".format(ari_scale[formula]["grade_level"], ari_scale[formula]["ages"]))
    print("")

def remove_space(split_words):
    for line in split_words:
        for i in line:
            if i == "":
                line.remove(i)
    return split_words

running = 0

while running == 0:
    print("")
    print("Please choose a number from the following menu:")
    print("1) Trump Speech")
    print("2) MLK Letters from Birmingham Jail")
    print("3) Obama Inauguration Speech")
    print("4) The Gettysburg Address")
    print("5) Quit")
    selection = str(input("->:  "))

    if selection == "5":
        running += 1

    file = import_text(selection)
    file = remove_unnecessary_punct(file, punct_list)

    split_file = split_sentance(file, punct_list)
    split_words = split_words(split_file)
    split_words = remove_space(split_words)

    char_in_words_list = chars_in_words(split_words)

    sum_of_chars = sum_of_characters(char_in_words_list)
    sum_of_words = len(char_in_words_list)
    sum_of_sent = len(split_words)

    formula = ((4.71 * (sum_of_chars/sum_of_words) + (0.5 * (sum_of_words/sum_of_sent)) - 21.43))

    if formula - round(formula, 0) > 0:
        formula = round(formula, 0) + 1

    print(formula)
    print("")
    ari_scale_calc(ari_scale, int(formula))



"""
#### Goal

Compute the ARI for a given body of text loaded in from a file.  The automated readability index (ARI) is a formula for
computing the U.S. grade level for a given block of text.

----------------------------------


##### Automated Readability Index Formula

The general formula to compute the ARI is as follows:

![ARI Formula](https://en.wikipedia.org/api/rest_v1/media/math/render/svg/878d1640d23781351133cad73bdf27bdf8bfe2fd)

In plain English, the score is computed by multiplying the number of characters divided by the number of words by 4.17,
adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal,
always round up.

Scores correspond to the following ages and grad levels:

```
    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
```

----------------------------------

#### Instructions


1. Create a new directory called `ari` in your code repo
1. Create a file called `main.py` file in the `ari` directory

When the user runs `main.py`, they should be presented with a menu of choices of the above files to choose from that looks something like the following:

    To compute its automated readability index,
    pick from one of the files below:

    1) geneology-of-morals.txt
    2) gettysburg-address.txt
    3) jack-and-jill.txt

    or

    q) Quit

The list of files should be generated from the files in the `ari` directory that have `.txt` for their extension.

After choosing one of the files, the output should look something like the following:

    --------------------------------------------------------

    The ARI for the file, gettysburg-address.txt, is 12.
    This corresponds to a 11th Grade level of difficulty
    that is suitable for an average person 16-17 years old.

    --------------------------------------------------------

Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level:

    ari_scale = {
         1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
         2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
         3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
         4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
         5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
         6: {'ages': '10-11', 'grade_level':    '5th Grade'},
         7: {'ages': '11-12', 'grade_level':    '6th Grade'},
         8: {'ages': '12-13', 'grade_level':    '7th Grade'},
         9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
"""