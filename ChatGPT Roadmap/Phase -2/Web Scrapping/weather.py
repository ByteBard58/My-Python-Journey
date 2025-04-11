from bs4 import BeautifulSoup as bsoup
import requests

url = "https://www.daraz.com.bd/products/goodknight-liquid-mosquito-repellant-refill-45ml-i161128162-s1093022216.html?scm=1007.51610.379274.0&pvid=bfc0606c-8a12-4d58-81f4-a249754b58a8&search=flashsale"
target = requests.get(url)
tarx = bsoup(target.content , "lxml")
product = tarx.find("h1", class_="pdp-mod-product-badge-title")
price = tarx.find("span", class_="notranslate pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl")

print(f"Source: {url} \nProduct: {product} \nPrice: {price}")