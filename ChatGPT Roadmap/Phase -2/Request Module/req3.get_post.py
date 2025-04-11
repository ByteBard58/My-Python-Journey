import requests

url = "https://httpbin.org/post"
payload = {"name" : "Sakib", "age":20}
x = requests.post(url, data=payload)
x.py = x.json()
# print(x.py["form"])

url2 ="https://httpbin.org/get"
payloax = {"page": 2, "count" : 25}
dd = requests.get(url2, params=payloax)
# print(dd.text)
