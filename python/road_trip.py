

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

menu_key = []

for key in city_to_accessible_cities:
    menu_key.append(key)


def user_menu(city_to_accessible_cities, menu_key):
    menu = True
    while menu == True:
        print("")
        print("The following cities are in your network: ")
        print("")
        for key in city_to_accessible_cities:
            print(key)
        print("")
        # city_lookup = input("What city would you like to look up?: ")
        city_lookup = "Boston"
        if city_lookup not in menu_key:
            print("")
            print("No such City found in network. Please choose from the list or check your spelling. ")
        else:
            break
    return city_lookup

def direct_access(city_to_accessible_cities, city_lookup):
    direct_cities = city_to_accessible_cities[city_lookup]
    return direct_cities

def indirect_access(city_to_accessible_cities, city_lookup, direct_cities):
    layover_set = set()
    for i in city_to_accessible_cities[city_lookup]:
        for x in city_to_accessible_cities[i]:
            if x != city_lookup:
                layover_set.add(x)
    layover_set.difference_update(direct_cities)
    return layover_set

def two_stops_cities(city_lookup, direct_cities, indirect_cities, menu_key):
    two_stop_cities = menu_key
    two_stop_cities.remove(city_lookup)
    for i in direct_cities:
        two_stop_cities.remove(i)
    for i in indirect_cities:
        two_stop_cities.remove(i)
    return two_stop_cities

def two_stop_check(two_stop_cities):
    if two_stop_cities != []:
        print("If with two connections, you can also travel to:  ")
        for i in two_stop_cities:
            print(i)
    else:
        pass

def travel_time(city_lookup, city_to_accessible_cities_with_travel_time, cities_list):
    list(cities_list)
    for i in cities_list:
        print("{} hours. ".format(city_to_accessible_cities_with_travel_time[city_lookup][i]))



def output_func(city_lookup, direct_cities, indirect_cities, two_stop_cities):
    print("")
    print("From {} you may directly travel to: ".format(city_lookup))
    for i in direct_cities:
        print(i)
    print("")
    print("From those cities, you may travel to: ")
    for e in indirect_cities:
        print(e)
    print("")
    two_stop_check(two_stop_cities)

def prog_execute(city_to_accessible_cities, menu_key):
    running = True
    while running == True:
        city_lookup = user_menu(city_to_accessible_cities, menu_key)

        direct_cities = direct_access(city_to_accessible_cities, city_lookup)
        print(travel_time(city_lookup, city_to_accessible_cities_with_travel_time, direct_cities))
        indirect_cities = indirect_access(city_to_accessible_cities, city_lookup, direct_cities)
        two_stop_cities = two_stops_cities(city_lookup, direct_cities, indirect_cities, menu_key)
        output_func(city_lookup, direct_cities, indirect_cities, two_stop_cities)
        print("")
        restart = input("Press 'y' to look up another city, or press any other key to quit. ")
        if restart != "y":
            print("")
            print("bye.")
            running = False

prog_execute(city_to_accessible_cities, menu_key)

