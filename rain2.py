import string

file = open("kelly_school_rain.txt").readlines()

cleaned_file = (file[11:-1])

dataset = {"PrimaryID": {"day": "", "month": "","year": "", "total_day": "", "0": "", "1": "", "2": "", "3": "","4": "",
                         "5": "", "6": "", "7": "", "8": "", "9":"","10": "", "11": "", "12": "", "13": "", "14": "",
                         "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "","23": "" }}

# Day, Month, Year, Total, 0 , 1, 2, 3, 4.... etc.

example = (file[11])


def cleaning(lines_to_be_cleaned):
    example_no_space = lines_to_be_cleaned.replace("  ", "")
    example_no_space = example_no_space[:13] + " " + example_no_space[13:]
    #print(example_no_space)
    example_no_space = example_no_space.replace("-", " ")
    line_list = example_no_space.split()
    return line_list

def make_primaryID(line_list):
    primaryid = "".join(line_list[0:3])
    return primaryid

# def create_dict(primaryid, line_list):



line_list = cleaning(example)
primaryid = make_primaryID(line_list)
print(example)
print(line_list)
print(primaryid)
print(dataset)



#{primaryID: {day: "", "month": }}\

# FROM CHRIS
# diction = {'some_key': 'nothing'}
# main_key = '30-08-2017'
# total = 10
# # diction[main_key] = {'Date': main_key, 'Total': total, 0: 0, 1: 5}
# # diction['30-08-2018'] = {'Date': '30-08-2018', 'Total': 22, 0: 10, 1: 12}
# diction.update(some_key={'some': 'value'})
# print(diction)





# dict = {}
# dict[variablex] = {30Aug2017}

#print(example_no_space.split[1](""))

# example_no_space = example.("   ")
# print()
# example_no_space_no_dash = example_no_space[0].split("-")
# print(example_no_space_no_dash)
# example2 = "".join(example.split("  "))
# print(example2)
# example = [x for x in example.split("  ") if x != "  "]
# print(example)


"""
>>> a = [1, 2, 3, 4, 2, 3, 4, 2, 7, 2]
>>> a = [x for x in a if x != 2]
>>> print a
[1, 3, 4, 3, 4, 7]

"""