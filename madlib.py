import random

print("Let's play Mad Libs.")

#word_list = []
play = True

while play == True:

    team_input = input("Give me two names of sports teams, seperated by commas: ")
    team_list = team_input.split(",")

    adj_input = input("Give me three adjectives, seperated by commas: ")
    adj_list = adj_input.split(",")

    name_input = input("Give me the name of three athletes, seperated by commas: ")
    name_list = name_input.split(",")

    print("On Friday, the {} got a needed 2-0 win at home over the {}, despite it being a {} match. ".format(team_list[0], team_list[1], random.choice(adj_list)))
    print("Both sides remained {} through the first 65 minutes until {} got a goal courtesy of a {} cross. ".format(random.choice(adj_list), random.choice(name_list), random.choice(name_list)))
    print("For the remainder of the match, {} withstood sustained pressure from {}, and even managed a game-clinching goal after {} goalkeeper {} went forward for a set piece. ".format(team_list[0], team_list[1], team_list[1], name_list[2]))
    print("{} scored into a {} net after being set up by {}. ".format(random.choice(name_list), random.choice(adj_list), random.choice(name_list)))
    print("")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "n" :
        play = False
