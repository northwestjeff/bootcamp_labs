ft = 1

unit_dict = {"ft" : 1, "inch" : (ft * 0.083), "cm" : (ft * 0.03), "mr" : (ft * 3.28) , "km" : (ft * 3280), "mi" : (ft * 5280)}

distance = int(input("what distance would you like to convert?: "))
input_given = input("enter units ('mi' for miles, 'km' for kilometers, 'ft' for feet, 'mr' for meter, 'inch' for inches, 'cm' for centimeters: ")
target_unit = input("What unites would you like? ('mi' for miles, 'km' for kilometers, 'ft' for feet, 'mr' for meter, 'inch' for inches, 'cm' for centimeters: ")

#print(unit_dict[input_given])

total_distance = (distance * float(unit_dict[input_given]))
#print(total_distance)
converted_distance = (total_distance / float(unit_dict[target_unit]))
#print(converted_distance)

spelled_dict = {"ft": "feet", "inch": "inches", "cm": "centimeters", "mr": "meters", "km": "kilometers", "mi": "miles"}
print("{} {} is {} {}.".format(distance, spelled_dict[input_given], converted_distance, spelled_dict[target_unit]))
