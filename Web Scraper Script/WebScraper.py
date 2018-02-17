# Import libraries
from bs4 import BeautifulSoup
import csv
import requests

# A simple practice Web Scraper made with Python

# Collect first page of artists’ list
page = requests.get('https://en.wikipedia.org/wiki/Main_Page.html')
print(page)     # prints response code to see if properly downloaded
                # 200 = success, 400/500 = failure

# print(page.content) # prints out html content to console

soup = BeautifulSoup(page.content, 'html.parser')   # init beautiful soup
print(soup.prettify())      # formats html to prettify tags

print() # space between elements printed
list(soup.children)  # lists all children
# print([type(item) for item in list(soup.children)])  # loop through object types
print()

# print("Children listed: ")
html = list(soup.children)[2]   # take third item in list
# print(list(html.children))  # find children in html tag

# searching for tags by class and id:

page = requests.get("https://en.wikipedia.org/wiki/Science.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p', class_='outer-text')

# print(soup.find_all(class_="outer-text"))  # find all by outer text
# print(soup.find_all(id="first"))          # find all by id

# finding css:
print(soup.select("div p"))     # find all p tags inside of div

# download forecast: below:
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

# download page, make class to parse, find div with seven day forecast
# find each item inside forecast
# extract and print
# http://www.bbc.co.uk/weather/2643743




