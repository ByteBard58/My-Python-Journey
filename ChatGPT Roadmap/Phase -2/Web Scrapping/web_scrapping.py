from bs4 import BeautifulSoup as bsoup
import lxml
import requests


url = "https://books.toscrape.com/index.html"
x = requests.get(url)

# if x.status_code == 200 :
#   print("You are good to go!")
# else: 
#   print(f"Something went south!! Status code: {x.status_code}")

data = bsoup(x.content, "lxml")
header_data = data.find("header")
print(header_data)