# User case 1: First player to dunk has an even number
# User case 2: Score at the end of the first quarter combines to be an even number


class User:
    def __init__(self, name):
        self.name = name  # user name
        self.balance = 0 # Total wages won/lost
        self.active_bet = None  # Are they in an active bet?
        self.position = None # bet, such as over/under or odd/even
        self.dict_key = 0


    def new_user(self):
        self.name = input("What is your username?")
        return self.name

    def add_user(self):
        self.us
        self.dict_key += 1

    def __str__(self):
        return "{}".format(self.name)


class Sport:
    def __init__(self):
        self.name = name
        self.team_one = team_one
        self.team_two = team_two


class Team:
    def __init__(self):
        self.team_name = team_name
        self.team_score = 0
        self.uni_color = None

class Player:
    def __init__(self):
        self.last_name = last_name
        self.first_name = first_name
        self.full_name = "{} {} ".format(first_name, last_name)
        self.uni_number = uni_number
        self.points_scored = 0




class Operator:
    def __init__(self):
        self.operator = None

    operater_list = {"basketball": [],
                     "football": [],
                     "soccer": [],
                     "baseball": [],
                     "hockey": [],
                     }

class Condition:
    def __init__(self):
        self.odd_even = False
        self.over_under = False


class Data:
    def __init__(self):
        self.users_list = ["Bozo", "Buddy"]
        self.sports_list = {"basketball": {"teams": {1:"blazers", 2:"bulls"}},
                     "football": {"teams": {1:"seahawks", 2:"panthers"}},
                     "soccer": {"teams": {1:"timbers", 2:"orlando"}},
                     "baseball": {"teams": {1:"mets", 2:"yankees"}},
                     "hockey": {"teams": {1:"kings", 2:"flyers"}},
                     }
        self.current_games = {"basketball": {"today": [self.sports_list["basketball"]["teams"].get(1), self.sports_list["basketball"]["teams"].get(2)]},
                     "football": {"today": {1:"seahawks", 2:"panthers"}},
                     "soccer": {"today": {1:"timbers", 2:"orlando"}},
                     "baseball": {"today": {1:"mets", 2:"yankees"}},
                     "hockey": {"today": {1:"kings", 2:"flyers"}},
                     }


class Interface:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.sport = None
        self.game = None
        self.condition = None


    def user_choice(self):
        running = True
        while running == True:
            menu_choice = input("Press 1 to add a new user, 2 to choose an existing user: ")
            if  menu_choice == "1":
                print("")
                return data.users_list.append(User(input("What's your new username?: ")))
            elif menu_choice == "2":
                counter = 0
                print("")
                print("Which user would you like to use?: ")
                for x in data.users_list:
                    print("{}) {} ".format(counter + 1, x))
                    counter += 1
                user_selection = input("")
                if user_selection in data.users_list:
                    return User(user_selection)
                else:
                    print("No such user. Please try again, with correct capitalization and spelling. ")

    def sport_choice(self):
        running = True
        while running == True:
            print("")
            print("What sport would you like to bet on? ")
            for keys in data.sports_list:
                print("  {}".format(keys))
            basketball = "basketball"   # TODO dummy input for testing
            return basketball    # TODO dummy input for testing
            # return input(">>> ")

    def game_choice(self):
        running = True
        while running == True:
            counter = 1
            print("")
            print("Here are the {} games today: ".format(self.sport))
            print("{})  {} vs {}".format(counter, data.current_games[self.sport].get("today")[0],
                                                                 data.current_games[self.sport].get("today")[1]))
            running = False

    def interface_menu(self):
        print("Please select Player One:")
        # self.player_one = self.user_choice()
        # print("")
        # print("Please select Player Two:")
        # self.player_two = self.user_choice()
        # print("")
        # print("{} vs. {}.  Let's make it interesting.".format(self.player_one, self.player_two))
        # print("")
        self.sport = self.sport_choice()
        self.game = self.game_choice()










data = Data()

run = Interface()
run.interface_menu()

