import statistics
from timedfunction import timing

with open("kelly_school_rain.txt") as file:
    file = file.read().splitlines()

cleaned_file = (file[11:-1])  # Removes metadata from file.  not a solution for other files.

dataset = {}


def cleaning(lines_to_be_cleaned):
    line_no_space = lines_to_be_cleaned.replace("", "")
    line_no_space = line_no_space[:13] + " " + line_no_space[13:]
    line_no_space = line_no_space.replace("-", " ")
    line_list = line_no_space.split()
    return line_list


def make_primaryID(line_list):
    primaryid = "".join(line_list[0:3])
    return str(primaryid)


def create_dict(primaryid, dataset, line_list):
    dataset_values = {"day": "", "month": "", "year": "", "total_day": "", "0": "", "1": "", "2": "", "3": "", "4": "",
                      "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "",
                      "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": ""}
    dataset[primaryid] = dataset_values
    counter = 0
    for i in dataset_values:
        dataset_values[i] = line_list[counter]
        counter += 1
    return dataset


def user_interface():
    # Asks user to choose what data to look up
    user_category = input("Do you want to search by year, month, or day? (day as in 21 or 13 not Monday): ")
    user_category = user_category.lower()
    # Creates an empty set, displays the available options based on what the user input above ^
    set_of_day_month_year = set()
    print("Here are the available {}s to choose from: ".format(user_category))
    for i in dataset.values():
        set_of_day_month_year.add(i[user_category])
        # print(sorted(set_of_day_month_year))
    print(sorted((set_of_day_month_year)))
    # User chooses among the unique values within a cateogory
    category_selection = str(
        input("What {} do you want to see the total of?: (Day : xx, Month: XXX, Year: XXXX)  ".format(user_category)))
    category_selection = category_selection.upper()
    return user_category, category_selection, set_of_day_month_year


def tabulation(user_category, category_selection):
    summation = 0
    # day_month_year = dataset[key][user_category]
    for key in dataset:
        if dataset[key][user_category] == category_selection:
            summation += int((dataset[key]["total_day"]))
    summation = summation / 100
    return summation


# @timing
# def average(day_selection):
#     avg_rainfall = []
#     for key in dataset:
#         if dataset[key]["day"] == day_selection:
#             avg_rainfall.append(int(dataset[key]["total_day"]))
#             # print("ok")
#     return avg_rainfall



for line in cleaned_file:
    line_list = cleaning(line)
    primaryid = make_primaryID(line_list)
    dataset = create_dict(primaryid, dataset, line_list)

user_category, category_selection, set_of_day_month_year = user_interface()

# # day_selection = input("What day of the month would you like to know the average of?")
# day_selection = str(12)
# print("yes")
# avg_rainfall, delta = average(day_selection)
# print(avg_rainfall)
# print(statistics.mean(avg_rainfall))
# print("\n\n\n\n")
# print("this took {}.".format(delta))
#
# # print("The average rainfall is {}. ".format(statistics.mean(day)))

summation = tabulation(user_category, category_selection)
print("")
print("There were {} inches of rain in {} from the dataset. ".format(summation, category_selection))
