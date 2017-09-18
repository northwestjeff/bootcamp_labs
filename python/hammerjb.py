ampm_input = input("Is it AM or PM?: ")
ampm = ampm_input.lower()
print(ampm)

time_input = int(input("What time is it?: "))


#breakfast and dinner
if time_input >= 7 and time_input <= 9:
    if ampm == "am":
        print("{}{} is Breakfast Time".format(time_input, ampm))
    if ampm == "pm":
        print("{}{} is Dinner Time".format(time_input, ampm))
#lunch
elif ampm == "pm" and time_input == 12 or time_input == 1 or time_input == 2:
    print("{}{} is Lunch Time".format(time_input, ampm))
#hammertime
elif ampm == "pm" and time_input == 10 or time_input == 11:
    print("{}{} is Hammer Time".format(time_input, ampm))
elif ampm == "am" and time_input <= 4:
    print("{}{} is Hammer Time".format(time_input, ampm))
else:
    print("Nothing scheduled for this time :) ")





#breakfast 7AM-9AM
#lunch 12PM - 2PM
#dinner 7PM - 9PM
#hammer 10PM - 4AM
