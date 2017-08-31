import wikipedia

def ie_test(string):
    if "ie" in string:
        if "cie" in string:
            print("Does not follow rule.")
        else:
            print("you gave me an ie without a C ")
    elif "ei" in string:
        if "cei" in string:
            print("Exception! E & I after C ")
        else:
            print("Normal E & I. ")
    else:
        print("no ie or ei.  ")

x = True
while x == True:
    string = input("gimmie a string: ")
    ie_test(string)
    if input("another word? y/n: ") == "n":
        x = False
    else:
        pass
print(wikipedia.page())

