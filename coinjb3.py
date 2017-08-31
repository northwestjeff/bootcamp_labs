
benjamin = 100
jackson = 20
hamilton = 10
lincoln = 5
dollar_bill = 1
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

#denominations = (benjamin, jackson, hamilton, lincoln, dollar_bill, quarter, dime, nickel, penny)


user_input = float(input("How much change do you need?: (protip: enter something like $5.45 as 5.45) "))
print(user_input)

#Bills
num_ben = int(user_input / benjamin)
print(num_ben)
after_ben = user_input - (benjamin * num_ben)
print(after_ben)
num_jack = int(after_ben / jackson)
print(num_jack)
after_jack = after_ben - (jackson * num_jack)
print(after_jack)
num_ham = int(after_jack / hamilton)
print(num_ham)
after_ham = after_jack - (hamilton * num_ham)
num_linc = int(after_ham / lincoln)
print(num_linc)
after_linc = after_ham - (num_linc * lincoln)
print(after_linc)
num_dollar = int(after_linc / dollar_bill)
print(num_dollar)
after_dollar = after_linc - (dollar_bill * num_dollar)
#Coins
num_quarters = int(after_dollar / quarter)
print(num_quarters)
after_quarter = after_dollar - (quarter * num_quarters)
print(after_quarter)
num_dime = int(after_quarter / dime)
print(num_dime)
after_dime = after_quarter - (dime * num_dime)
print(after_dime)
num_nickel = int(after_dime / nickel)
print(num_nickel)
after_nickel = after_dime - (nickel * num_nickel)
print(num_nickel)
num_penny = int(after_nickel / penny)
print(num_penny)

bills = num_ben + num_jack + num_ham + num_linc + num_dollar
coins = num_quarters + num_dime + num_nickel + num_penny

print("$" + str(user_input))
print("I'll give you {} hundreds, {}, twenties, {} tens, {} fives, {} singles, {} quarters, {} dimes, {} nickels, and {} pennies.".format(num_ben, num_jack, num_ham, num_linc, num_dollar, num_quarters, num_dime, num_nickel, num_penny))
print("That's " + str(coins) + " coins and " + str(bills) + " bills.")
