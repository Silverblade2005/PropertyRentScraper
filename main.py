from bs4 import BeautifulSoup
import requests

province = input("Enter a province: ")
city = input("Enter a city: ")
bedroom_amt = input("Enter a bedroom amount: ")
bathroom_amt = input("Enter a bathroom amount: ")
page = 1

url = f"https://www.remax.co.za/property/to-rent/south-africa/{province}/{city}/?bd={bedroom_amt}&bh={bathroom_amt}&page={page}"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

listings_raw = soup.find_all('div', class_ ="property-card-info")
print(listings_raw)
