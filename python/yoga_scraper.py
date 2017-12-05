from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import requests, html5lib, time

#  Oregon search in the Directory
url = 'https://www.yogaalliance.org/Directory-Registrants?type=School&location=Oregon,%20United%20States'
# url = "https://www.yogaalliance.org/Directory-Registrants?type=School&location=Eugene,%20OR,%20United%20States"

# create new instance of chrome
driver = webdriver.Chrome()

# Direct driver to site of interest
driver.get(url)

list_directory = []
file = open("yogaresults.txt", 'w')

crawl_criteria = "//div[@class='ya_school-name']"


def crawl():
    timeout = 10
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='ya_school-name']")))
    except TimeoutException:
        print("Timed out waiting for page to loan")
        driver.quit()
        # Get all the names of yoga schools


def get_names():
    address_parent = driver.find_elements_by_xpath("//div[@class='ya_school-address']")
    addresses = [x.text for x in address_parent]
    addresses = [str(i) for i in addresses]
    addresses = [each.replace("\n", " ") for each in addresses]
    print("address: {}".format(addresses))

    # Creates list of yoga names on the page
    link_parent = driver.find_elements_by_xpath("//h3[@class='ya_school-location-name']//a")
    link_name = [x.text for x in link_parent]
    print("link name: {}".format(link_name))

    # link_url = [x.get_attribute('href') for x in link_parent]
    #
    # for x, y, z in (zip(link_name, link_url, addresses)):
    #     directory[x] = y, z
    # print("directory: {}".format(directory))
    make_list(zip(link_name, addresses))

    with open("yogafile.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerows(list_directory)


def remove_n(list):
    for i in list:
        if "\n" in i[1]:
            i[1].split("\n")


def next_page():
    try:
        # next_button = driver.find_element_by_xpath("//a[@title='Go to the next page'][contains(@class, 'k-pager-nav')]")
        next_not_disabled = driver.find_element_by_xpath(
            "//a[@title='Go to the next page'][not(contains(@class, 'k-state-disabled'))]")
        next_button = driver.find_element_by_xpath("//span[contains(@class, 'k-i-arrow-e')]")
        print("found next button")
        next_button.click()
        return True
    except NoSuchElementException:
        print('no element')
        return False
    except StaleElementReferenceException:
        print("stale")
        return False


def google_name(name_to_search):
    url = 'http://www.google.com'
    google_driver = webdriver.Chrome()
    google_driver.get(url)
    timeout = 5
    try:
        WebDriverWait(google_driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='btnI']")))
        print("successful try google")
    except TimeoutException:
        print("timeout!!!")
        google_driver.quit()
    search = google_driver.find_element_by_name('q')
    search.send_keys(name_to_search + " facebook")
    google_driver.find_element_by_name("btnI").click()
    time.sleep(8)  # sleep for 8 seconds so you can see the results
    phone = google_driver.find_element_by_class_name("_4bl9")
    phone = phone.find_element_by_tag_name("div")
    print("phone number: {}".format(phone))

    google_driver.quit()


def make_list(zipped):
    for x in zipped:
        list_directory.append(list(x))


def writer(list):
    for i in list:
        file.writelines(i)


# LOOP through pages
next_enabled = True
while next_enabled == True:
    crawl()
    get_names()
    next_enabled = next_page()
    time.sleep(7)
