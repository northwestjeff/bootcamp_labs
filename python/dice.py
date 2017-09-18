import random

def dice_game(dice_number, dice_sides):
    run = 0
    while run < dice_number:
        print(str(random.randrange(1,dice_sides + 1)))
        run += 1

exit = ""

while exit != "n":
    dice_number = int(input("How many dice would you like to roll?: "))
    dice_sides = int(input("How many side are on the di?: "))
    dice_game(dice_number, dice_sides)
    if input("Roll again? (y/n): ") == "n":
        print("Thanks for playing. ")
        exit = "n"
    else:
        pass





