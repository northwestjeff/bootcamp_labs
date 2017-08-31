denominations = {"benjamin": 100, "jackson" : 20, "hamilton": 10, "lincoln": 5, "dollar_bill": 1, "quarter": 0.25, "dime": 0.10,
"nickel": 0.05, "penny": 0.01}

count_denom = []

def change_counter(balance):
    for key in denominations:
        count_denom.append(int(balance / denominations.get(key)))
        balance = balance - ((int(balance / denominations.get(key))) * denominations.get(key))
    bills = count_denom[0] + count_denom[1] + count_denom[2] + count_denom[3] + count_denom[4]
    coins = count_denom[5] + count_denom[6] + count_denom[7] + count_denom[8]
    print("I'll give you {} hundreds, {} twenties, {} tens, {} fives, {} singles, {} quarters, {} dimes,"
          " {} nickels, and {} pennies.".format(*count_denom))
    print("That's {} coins and {} bills.".format(coins, bills))
    return

change_counter(float(input("How much change do you need?: (protip: enter something like $5.45 as 5.45) ")))

