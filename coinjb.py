
dollar_bill = 1
quarter = 25
dime = 10
nickel = 5
penny = 1

user_input = int(input("How much change do you need?: (protip: enter something like $0.45 as 45) "))
#print(user_input)

num_quarters = int(user_input / quarter)
# print(num_quarters)
after_quarter = user_input - (quarter * num_quarters)
# print(after_quarter)
num_dime = int(after_quarter / dime)
# print(num_dime)
after_dime = after_quarter - (dime * num_dime)
# print(after_dime)
num_nickel = int(after_dime / nickel)
# print(num_nickel)
after_nickel = after_dime - (nickel * num_nickel)
# print(num_nickel)
num_penny = int(after_nickel / penny)
# print(num_penny)

print("I'll give you {} quarters, {} dimes, {} nickels, and {} pennies.".format(num_quarters, num_dime, num_nickel, num_penny))
