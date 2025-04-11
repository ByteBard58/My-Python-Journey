import requests

url ="https://httpbin.org/delay/10"   
z = requests.get(url, timeout=5)         ######
print(z)

## Use timeout in requests.get to avoid bugging out


