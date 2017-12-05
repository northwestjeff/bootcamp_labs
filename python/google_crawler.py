import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import requests, html5lib, time

from yogatest import directory_dict


def create_driver():
    driver = webdriver.Chrome()
    url = 'https://www.google.com'
    driver.get(url)
    return driver

def crawl():
    timeout = 10
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@class='q']")))
        print("found Q")
    except TimeoutException:
        print("Timed out waiting for page to loan")
        driver.quit()

def search(term):
    input_element = driver.find_element_by_name("q")
    print("found lower case q")
    input_element.send_keys(term)
    print("submitting " + term)
    submit = driver.find_element_by_name("btnK")
    print("found submit")
    submit.click()


def search_terms():
    for i in directory_dict.keys():
        city = directory_dict[i]["city"]
        name = directory_dict[i]["name"]
        phone = "phone number"
        keys_input = "{} {} {}".format(name, city, phone)
        print("search term".format(keys_input))


# "//div[@class='ya_school-address']"


def phone_element():
    time.sleep(7)
    parent_element = driver.find_element_by_xpath("//span[@data-local-attribute='d3ph']")
    child_element = parent_element.find_element_by_tag_name("span")
    phone_number = child_element.text
    print("phone number found: {}".format(phone_number))
    return phone_number


def scrape(keys_input):
        driver = webdriver.Chrome()
        url = 'http://www.google.com'
        driver.get(url)
        try:
            search(keys_input)
            directory_dict["phone"] = phone_element()
            print(directory_dict["phone"])
        except:
            pass



for i in directory_dict.keys():
    city = directory_dict[i]["city"]
    name = directory_dict[i]["name"]
    phone = "phone number"
    keys_input = "{} {} {}".format(name, city, phone)
    scrape(keys_input)

for x in directory_dict.items():
    print("after scrape item: {}".format(x))
