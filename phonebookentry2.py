"""
Create a program that uses a dictionary to store phonebook
entries. Must have user interaction.
Include ability to:
1. Search
2. Add Entry
3. Chage Entry
4. Delete Entry
5. Exit Program
"""

#dictionary in dictionary?
#not as complicated as it might seem?
#return 1 to search press 2 to Add Entry press 3 to change entry press 4 to delete entry press 5 to exit

#selection = str(input("Phonebook.  Press 1 to search, 2 to Add Entry, 3 to Change Entry, 4 to Delete Entry, 5 to exit"))

phone_book = {
    }


#print(phone_book.keys())
#print(phone_book.values())

def search():
    name_search = input("What's the last name of the person you're looking for?: ")
    for i in list(phone_book.keys()):
        if name_search in phone_book.values():
            print("Result: {}'s phone number is: {}.".format(phone_book[name_search]["full_name"], phone_book[name_search]["phonenumber"]))
        else:
            print("I couldn't find anyone named {}.".format(name_search))

def add_entry():
    running = True
    while running == True:
        entry_name = input("Who do you want to add to the phone book?: ")
        entry_number = str(input("What's their number?: "))
        phone_book[entry_name + entry_number[-4:]] = {"full_name": entry_name, "phonenumber": entry_number}
        (phone_book)
        if input("Would you like to add anyone else? (y/n): ") == "n":
            running = False


#    my_dict['address'] = 'Downtown'

def change_entry():
    running = True
    print(phone_book)
    while running == True:
        change_search = input("Whose number do you want to change?: ")
        change_number = str(input("What do you want their number to be?"))
        phone_book[change_search + change_number[-4:]] = {"full_name": change_search, "phonenumber": change_number }
        if input("Would you like to change any other entries? (y/n): ") == "n":
            running = False

def delete_entry():
    running = True
    print(phone_book)
    while running == True:
        delete_search = input("Whose number do you want to delete?: ")




        # for key, value in phone_book.items():
        #     for k, v in value.items():
        #         if change_search in v:
        #             phone_book.pop(k)
        #         else:
        #             print("no")
        #         print(phone_book)

                # if change_search == v:
                #     phone_book.pop(change_search + change_number[-4:])
                # else:
                #     print("NO")
# # remove a particular item
# # Output: 16
# print(squares.pop(4))


#



# phone_book = {
#     "concat_name": {"full_name": "FULL NAME", "phonenumber": "33333333"}
# }

# person = {'name': 'Phill', 'age': 22}
#
# print('Name: ', person.get('name'))
# print('Age: ', person.get('age'))
#
# # value is not provided
# print('Salary: ', person.get('salary'))
#
# # value is provided
# print('Salary: ', person.get('salary', 0.0))


search()
print(phone_book)
#print(phone_book)
