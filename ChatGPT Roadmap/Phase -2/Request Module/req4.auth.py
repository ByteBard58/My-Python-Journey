import requests
from bs4 import BeautifulSoup as bsoup

url ="https://httpbin.org/basic-auth/{user}/{passwd}"
x = requests.get(url, auth=("Sakib","1348"))
print(x)

# That passowrd is just a demo, nothing serious 
