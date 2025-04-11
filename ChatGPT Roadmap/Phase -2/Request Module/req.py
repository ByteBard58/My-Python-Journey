import requests
from bs4 import BeautifulSoup as bsoup

url = "https://pypi.org/project/numpy/"

fetch = requests.get(url)
data = fetch.content

gg_data = bsoup(data, "html.parser")
# print(gg_data)

pack_name = gg_data.find("h1", class_="package-header__name").text.strip()
pip_code = gg_data.find("span", id="pip-command").text.strip()
# print(f"Package : {pack_name}\nPip Code (copy and paste in terminal to install) : {pip_code}")

