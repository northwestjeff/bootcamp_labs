import random

print("I'm thinking of a number between 1 and 20.  I'll give you 5 guesses...")
print("")
user_choice = int(input("What's your guess?"))

rand_num = random.randint(1,20)

turn_counter = 0
winning = False

while turn_counter < 5:
    user_choice = int(input("What's your guess?"))
    if user_choice == rand_num:
        winning = True
        print("you got it! ")
        break
    elif user_choice > rand_num:
        print("too high! ")
    else:
        print("too low! ")
    turn_counter += 1

print("")
if winning == False:
    print("I win :) ")
