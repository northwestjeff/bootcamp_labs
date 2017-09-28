# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import urllib3
# import certifi
# import requests
# from lxml import html
#
# # http = urllib3.PoolManager(
# #     cert_reqs='CERT_REQUIRED',
# #     ca_certs=certifi.where())
#
# teams_page = "https://en.wikipedia.org/wiki/List_of_professional_sports_teams_in_the_United_States_and_Canada"
#
# page = urlopen(teams_page)
#
# soup = BeautifulSoup(page, 'html.parser')
#
# teams = soup.find_all('b')
#
# print(teams)
#

from wikitables import import_tables

teams = 'Major professional sports teams of the United States and Canada'
italy = 'List of cities in Italy'


teams_dict = import_tables(teams)

for row in teams_dict[0].rows:
    print(row)
    # print("{}, {}, {}".format(row["Team"], row["City"], row["League"]))



# italy_cities = import_tables(italy)
#
# for row in italy_cities[0].rows:
#     print("{}, population: {}".format(row["City"], row["2001 Census"]))
