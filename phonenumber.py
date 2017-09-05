user_phone = input("Please enter all the digits in your phone number: ")

area_code = user_phone[0:3]
mid_code = user_phone[3:6]
last_four = user_phone[6:]

print(f"{area_code}-{mid_code}-{last_four}")
