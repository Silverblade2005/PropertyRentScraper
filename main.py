from bs4 import BeautifulSoup
import requests
import pandas as pd

province = input("Enter a province: ").lower()
city = input("Enter a city: ").lower()
bedroom_amt = input("Enter a bedroom amount: ")
bathroom_amt = input("Enter a bathroom amount: ")
get_pages = int(input("Enter amount of pages to get: "))
page = 1

table_headers = [ "Title", "Num_Rooms", "Num_Baths", "Property_Type" ,"Suburb" ,"Price"]
df = pd.DataFrame(columns=table_headers)

def scrape(page):
    url = f"https://www.remax.co.za/property/to-rent/south-africa/{province}/{city}/?bd={bedroom_amt}&bh={bathroom_amt}&page={page}"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    listings_raw = soup.find_all('div', class_ ="property-card-info")

    for listing in listings_raw:
        tmp_table_row = []
        title = listing.find("a", class_="property-card-link")['title']
        price = int(listing.find("span", attrs={"itemprop":"price"}).text[1:].strip().replace(" ", ""))
        num_rooms = listing.find("span", attrs={"itemprop":"numberOfRooms"}).text
        num_baths = listing.find("span", attrs={"itemprop":"amenityFeature"}).text
        suburb_string = listing.find("div", class_="property-card-info__suburb").text
        property_type = suburb_string.split(" ")[2]
        suburb = suburb_string[suburb_string.find("in")+3:]

        tmp_table_row.append(title)
        tmp_table_row.append(num_rooms)
        tmp_table_row.append(num_baths)
        tmp_table_row.append(property_type)
        tmp_table_row.append(suburb)
        tmp_table_row.append(price)

        length = len(df)
        df.loc[length] = tmp_table_row

while page < get_pages + 1:
    print(f"Doing page: {page}")
    scrape(page)
    page += 1

print(df)
print(f'Average Property Rent in {city}: R{df["Price"].mean()}')
