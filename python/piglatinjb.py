vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
user_input = str(input("Give me a word and I'll translate it to pig latin: "))
user_input[:1].isupper()


vowel_check = (user_input.split()[0][0])

vowel_suff = "yay"
const_suff = "ay"

if vowel_check.lower() in vowel_list:
    if user_input[:1].isupper() == True:
        print(user_input.title() + vowel_suff)
    else:
        print(user_input + vowel_suff)
else:
    const_letter = (user_input.split()[0][0])
    if user_input[:1].isupper() == True:
        print(user_input.split()[0][1:].title() + const_letter.lower() + const_suff)
    else:
        print(user_input.split()[0][1:] + const_letter + const_suff)
