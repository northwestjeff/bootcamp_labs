import string

file = open("kelly_school_rain.txt").readlines()

cleaned_file = (file[11:-1])

example = (file[11])


# def cleaning(lines_to_be_cleaned):

print(example)
example_no_space = example.replace("  ", "")
example_no_space = example_no_space[:13] + " " + example_no_space[13:]
print(example_no_space)
example_no_space = example_no_space.replace("-", " ")
print(example_no_space.split())


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