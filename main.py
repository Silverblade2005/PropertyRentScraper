from bs4 import BeautifulSoup
import requests

province = "limpopo"#input("Enter a province: ")
city = "polokwane"#input("Enter a city: ")
bedroom_amt = "2"#input("Enter a bedroom amount: ")
bathroom_amt = "1"#input("Enter a bathroom amount: ")
page = 1

url = f"https://www.remax.co.za/property/to-rent/south-africa/{province}/{city}/?bd={bedroom_amt}&bh={bathroom_amt}&page={page}"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

listings_raw = soup.find_all('div', class_ ="property-card-info")

for listing in listings_raw:
    print("_________________________________________________________________________________")
    #print(listing.prettify())
    print(listing.find("div", class_="property-card-info__suburb").text)
    print("_________________________________________________________________________________")
