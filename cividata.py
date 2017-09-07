import requests

package = {
    "count": 100,
    "restaurant_name": "",
    # "since": "1980-01-01"
}


# rest_choice = input("What restaurant do you want to research?:  ")
rest_choice = "foster burger"
package["restaurant_name"] = rest_choice

r = requests.get("http://api.civicapps.org/restaurant-inspections", params=package)

data = r.json()

data_log = []

for line in data["results"]:
    data_log.append(line["inspection_number"])

# print(data_log)

violations_log = {}

for i in data_log:
    r = requests.get("http://api.civicapps.org/restaurant-inspections/inspection/{}".format(i))
    data_new = r.json()
    violations_log[i] = {}
    violations_log[i]["date"] = data_new["results"]["date"]
    violations_log[i]["inspection_number"] = i
    violations_log[i]["violations"] = data_new["results"]["violations"]

# print(len(violations_log))
# print(violations_log)
for i in violations_log:
    for x in violations_log[i]["violations"]:
        print(x["violation_comments"])


# for i in data_log:
#     r = requests.get("http://api.civicapps.org/restaurant-inspections/inspections/{}".format(i))
#     print(r.json())
