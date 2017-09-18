# class Car(object):
#
#     def __init__(self, make, model, horn_sound):
#         self.make = make
#         self.model = model
#         self.horn_sound = horn_sound
#
#
#     def __str__(self):
#         return "{} {}".format(self.make, self.model)
#
#     def honk(self):
#         return("{}".format(self.horn_sound))
#
#
# honda = Car("honda", "civic", "boooop")
# chevy = Car("chevy", "impala", "beeeep")
#
# class ParkingLot(object):
#
#     car_count = []
#
#     def entry(self, object):
#         car_count.append(object)
#         return car_count
#
#
#     def __str__(self):
#         return ("{} in the garage".format(car_count))
#
#
#
# print(honda)
# print(chevy)
#



# class Car(object):
#
#     def __init__(self, make, model, horn_sound):
#         self.make = make
#         self.model = model
#         self.horn_sound = horn_sound
#
#     def __str__(self):
#         return "{} {}".format(self.make, self.model)
#
#     def honk(self):
#         return "{}!".format(self.horn_sound)
import datetime

class User:
    """ A member of Friendface. Nmae and birhtday"""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of a user in years"""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) #date in birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)



user = User("Dave bowman", "19710315")
print(user.age())



help(User)

# print(user.name)
# print(user.first_name)
# print(user.last_name)
# print(user.birthday)
#
# help(User)