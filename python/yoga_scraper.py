from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import requests, html5lib, time

# TODO create list for URL lookup for more states/cities
# TODO create crawler that looks into each URL and pulls phone number



#  Oregon search in the Directory
url = 'https://www.yogaalliance.org/Directory-Registrants?type=School&location=Oregon,%20United%20States'
#
# create new instance of chrome
driver = webdriver.Chrome()
#
# Site of interest
driver.get(url)

directory = {}


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
    school_names = driver.find_elements_by_xpath("//div[@class='ya_school-name']")
    names = [x.text for x in school_names]
    #
    # studio_pages = driver.find_elements_by_xpath("//div[@class='ya_school-location-name']/a")
    #
    address_parent = driver.find_elements_by_xpath("//div[@class='ya_school-address']")
    addresses = [x.text for x in address_parent]
    print("address: {}".format(addresses))
    #
    link_parent = driver.find_elements_by_xpath("//h3[@class='ya_school-location-name']//a")  # .get_attribute("href")
    link_name = [x.text for x in link_parent]
    link_url = [x.get_attribute('href') for x in link_parent]
    #
    for x, y, z in (zip(link_name, link_url, addresses)):
        directory[x] = y, z

    return directory


def next_page():
    try:
        # next_button = driver.find_element_by_xpath("//a[@title='Go to the next page'][contains(@class, 'k-pager-nav')]")
        next_not_disabled = driver.find_element_by_xpath(
            "//a[@title='Go to the next page'][not(contains(@class, 'k-state-disabled'))]")
        next_button = driver.find_element_by_xpath("//span[contains(@class, 'k-i-arrow-e')]")
        next_button.click()
        return True
    except NoSuchElementException:
        print('no element')
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
    time.sleep(8)  # sleep for 5 seconds so you can see the results
    phone = google_driver.find_element_by_class_name("_4bl9")
    phone = phone.find_element_by_tag_name("div")
    print("phone number: {}".format(phone))



    google_driver.quit()







# def next_page_click(next_button):
#     next_button.click()


# next_enabled = True
# while next_enabled == True:
#     crawl()
#     get_names()
#     time.sleep(10)
#     next_enabled = next_page()


# get_phone_number(single_page)

#
# crawl()
# get_names()
# next_page()
search = "Asmi Yoga Bend"
google_name(search)
# names = []
# for x in school_names:
#     names.append(x.text)

print(directory)
