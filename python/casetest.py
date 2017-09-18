import stringcase

def camel_test(user_input):
    if user_input[0].isupper() == True and "_" not in user_input:
        print("CamelCase")
    elif "_" in user_input and user_input[0].isupper() == False:
        print("snake_case")
    else:
        print("Neither snake_case, nor CamelCase. ")
    return

x = True
while x is True:
    camel_test(input("Give me a word and I'll tell you what case it's in: "))
    if input("again? y/n: ") == "n":
        x = False
    else:
        pass
