my_list = ['cat', 'dog', 'monkey']

# for pet in my_list:
#     print(pet)
#
# for pet in my_list:
# #nested for loop
#     for char in pet:
#         print(char)
#     #after printing each character within pet it prints a space
#     print()

# while True:
#     print('This is the song that never ends...')


#Capitalize
# text = "happy happy joy joy"
# cap_text = text.capitalize()
#
# # print(text)
# # print(text.capitalize())
# # print(cap_text.swapcase())
# # print(cap_text)
# print(cap_text.islower())
#
# print(text.title())

name = input("What is your name?: ")

if name == "Chris":
    print("uh, hi {}".format(name))
elif name == "Chelsea":
    print("It's {}".format(name))
else:
    print("hello {}".format(name))
