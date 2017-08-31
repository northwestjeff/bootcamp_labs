
def conversion(primary_distance, unit_given, target_unit ):
    #miles
    if unit_given == "mi" and target_unit == "ft":
        calculation = primary_distance * 5280
    if unit_given == "mi" and target_unit == "km":
        calculation = primary_distance * 1.6
    if unit_given == "mi" and target_unit == "mr":
        calculation = (primary_distance * 1.6) * 1000

    #kilometers
    if unit_given == "km" and target_unit == "ft":
        calculation = (primary_distance * 1000) * 3.28
    if unit_given == "km" and target_unit == "mi":
        calculation = primary_distance * 0.6
    if unit_given == "km" and target_unit == "mr":
        calculation = primary_distance * 1000

    #meters
    if unit_given == "mr" and target_unit == "ft":
        calculation = primary_distance * 3.28
    if unit_given == "mr" and target_unit == "mi":
        calculation = (primary_distance / 1000) * 0.6
    if unit_given == "mr" and target_unit == "km":
        calculation = primary_distance / 1000

    #feet
    if unit_given == "ft" and target_unit == "mr":
        calculation = primary_distance / 3.28
    if unit_given == "ft" and target_unit == "km":
        calculation = (primary_distance / 3.28) / 1000
    if unit_given == "ft" and target_unit == "mi":
        calculation = primary_distance / 5280

    calculation = str(calculation)
    primary_distance = str(primary_distance)

    if unit_given == "ft":
        unit_given = "feet"
    if unit_given == "mr":
        unit_given = "meters"
    if unit_given == "mi":
        unit_given = "miles"
    if unit_given == "km":
        unit_given = "kilometers"

    if target_unit == "ft":
        target_unit = "feet"
    if target_unit == "mr":
        target_unit = "meters"
    if target_unit == "mi":
        target_unit = "miles"
    if target_unit == "km":
        target_unit = "kilometers"


    return "There are " + calculation + " " + target_unit + " in " + primary_distance + " " + unit_given + ". "

print(conversion(float(input("what distance to convert?: ")), input("enter units ('mi' for miles, 'km' for kilometers, 'ft' for feet, 'mr' for meter): "), input("enter Target units ('mi' for miles, 'km' for kilometers, 'ft' for feet, 'mr' for meter): ")))
