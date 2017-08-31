# 7 columns
# dictionaries for each line
# append a 'token' to the lowest column allowable
#calculate four-in a row: horizontal, diagonal, vertical

line5 = ["0" , "0" , "0" , "0" , "0" , "0" , "0"]
line4 = ["0" , "0" , "0" , "0" , "0" , "0" , "0"]
line3 = ["0" , "0" , "0" , "0" , "0" , "0" , "0"]
line2 = ["0" , "0" , "0" , "0" , "0" , "0" , "0"]
line1 = ["0" , "0" , "0" , "0" , "0" , "0" , "0"]
board = [line1, line2, line3, line4, line5]

column_1 = 0
column_2 = 0
column_3 = 0
column_4 = 0
column_5 = 0
column_6 = 0
column_7 = 0
column_list = [column_1, column_2, column_3, column_4, column_5, column_6, column_7]

winner = ""

def column_select(user_choice):
    print(column_list)
    for line_x in list(board):
        if line_x[user_choice - 1] == "0":
            line_x[user_choice - 1] = "R"
            column_list[user_choice - 1] +=1
            break
    return


def hor_four_in_a_row():
    global winner
    for i in board:
        print(i.count("R"))
        # for a in i:
        if i.count("R") > 3 and i[3] == "R":
            print("winner")
            winner = "R"
            break
    return


def ver_four_in_a_row(user_choice):
    global winner
    for i in list(column_list):
        if i > 3 and line3[user_choice - 1] != 0:
            print("")
            print("winner!")
            winner = "R"


def diagonal():
    


while winner != "R":
    user_choice = int(input("Red: select a column: "))
    column_select(user_choice)
    print("")
    print(line5)
    print(line4)
    print(line3)
    print(line2)
    print(line1)
    print("")
    hor_four_in_a_row()
    ver_four_in_a_row(user_choice)
    print("")




