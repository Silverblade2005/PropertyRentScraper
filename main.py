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

table_headers = [ "Title", "Num_Rooms", "Num_Baths", "Property_Type" ,"Suburb" ,"Price"]
table_data = []

tmp_table_row = []

for listing in listings_raw:
    tmp_table_row = []
    title = listing.find("a", class_="property-card-link")['title']
    price = listing.find("span", attrs={"itemprop":"price"}).text.strip()
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

    table_data.append(tmp_table_row)

print(table_data)