import string

"""
with open(filename) as f:
    mylist = f.read().splitlines() 
"""


with open("kelly_school_rain.txt") as file:
    file = file.read().splitlines()

#file = open("kelly_school_rain.txt").readlines()

cleaned_file = (file[11:-1])  #removes metadata from file.  not a solution for other files.

dataset = {}

example = (file[11])

def cleaning(lines_to_be_cleaned):
    example_no_space = lines_to_be_cleaned.replace("", "")
    #example_no_space = example_no_space[:13] + " " + example_no_space[13:]
    #print(example_no_space)
    example_no_space = example_no_space.replace("-", " ")
    line_list = example_no_space.split()
    return line_list

def make_primaryID(line_list):
    primaryid = "".join(line_list[0:3])
    return str(primaryid)
    #need to split the list and append the remainder to the new primaryid

def create_dict(primaryid, dataset, line_list):
    dataset_values = {"day": "", "month": "", "year": "", "total_day": "", "0": "", "1": "", "2": "", "3": "", "4": "",
              "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": "", "13": "", "14": "",
              "15": "", "16": "", "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": ""}
    dataset[primaryid] = dataset_values
    #print(dataset_values)
    counter = 0
    for i in dataset_values:
        dataset_values[i] = line_list[counter]
        counter += 1
        # print(counter)
        # print(i)
    return dataset

# for line in example:
#     line_list = cleaning(line)
#     primaryid = make_primaryID(line_list)
#     dataset = create_dict(primaryid, dataset, line_list)
"""
for line in cleaned_file:
    line_list = cleaning(line)
    print(line_list)
    primaryid = make_primaryID(line_list)
    print(primaryid)
    dataset = create_dict(primaryid,dataset, line_list)  # DOUBLE DIGIT VALUES ARE THROWING OFF THE SPACING
"""



# print(dataset)


line_list = cleaning(example)
print(line_list)

# print(line_list)
# primaryid = make_primaryID(line_list)
# # print(primaryid)
# dataset = create_dict(primaryid, dataset, line_list)
# # print(dataset)
# # print(line_list)
# print(dataset)
#


#print(dataset(primaryid, line_list))


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



# >>> a = [1, 2, 3, 4, 2, 3, 4, 2, 7, 2]
# >>> a = [x for x in a if x != 2]
# >>> print a
# [1, 3, 4, 3, 4, 7]
