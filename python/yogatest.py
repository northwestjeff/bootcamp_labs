import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import requests, html5lib, time

directory_dict = {}

file = open("yogafile.csv")
filereader = csv.reader(file, delimiter=",")

yoga_dir = [row for row in filereader]
print("top: {}".format(yoga_dir))

#remove "map" in the location.  The last five characters pulled in from the scrape
def remove_map():
    for i in yoga_dir:
        i[1] = i[1][:-5]


def zip_strip():
    for i in yoga_dir:
        if i[1][-1].isnumeric():
            i[1] = i[1][:-6]


# Two types of locations, some say USA others say United States.  This normalizes
def usa_normalize():
    for i in yoga_dir:
        key_string = i[1]
        check = "United States"
        if check in key_string:
            i[1] = key_string[:-15]
        else:
            i[1] = key_string[:-5]

# splices location and pulls the City as the last item in the index
def split_state():
    for i in yoga_dir:
        i[1] = i[1].split(" ")
        i.append(i[1][-2])

def make_dict():
    for i in yoga_dir:
        directory_dict[i[0]] = {"name": i[0],
                                "address": i[1],
                                'city': i[2]
        }



remove_map()
usa_normalize()
zip_strip()
split_state()
make_dict()
x = 0
for i in yoga_dir:
    print(i)
    x += 1
    print(x)
print(directory_dict)
print(directory_dict.keys())

# Todo convert these lists to a dictionary: w/ names, city, state
#




