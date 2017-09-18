import requests


package = {
    "APPID": "a4c0e8e842ba6b3f06d47fbb4dd5dab3"
}


user_input = input(str("Please enter a city or zip code:  "))

temp_type = input(str("Would you like to see temperatures in (f)ahrenheit or (c)elsius? (press f or c):  "))

if temp_type == "f":
    temp_type = "imperial"
elif temp_type == "c":
    temp_type = "celsius"
else:
    temp_type = "kelvin"

package["units"] = temp_type


# Test for user input as City or Zip.  Assigns a varable to be used in the URL.
if user_input.isdigit() == True:
    select_type = "zip"
else:
    select_type = "q" # for the url search. this is really should be something like "city_name"

# Adds the user selection to a dictionary.  Not sure this is necessary
package[select_type] = user_input

# Makes the Request
r = requests.post('http://api.openweathermap.org/data/2.5/weather?', params=package)
data = r.url

if temp_type == "imperial":
    temp_type = "fahrenheit"

weather_dict = r.json()
print("")
print("The current temperature in {} is {} degrees in {} units." .format(user_input.title(),
                                                                         round(weather_dict["main"]["temp"],),
                                                                         temp_type))