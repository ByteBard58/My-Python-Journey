import requests
from bs4 import BeautifulSoup as bsoup

url = "https://www.scrapethissite.com/lessons/sign-up/"

damn = requests.get(url)
# print(damn.text)      
# print(damn.headers)     ## Prints out the headers of that request (general, request and response headers, all in one)       

pretty = bsoup(damn.content, "lxml") 
# print(pretty)                           ##Beautiful soup 

url2 = "https://scontent.fdac31-1.fna.fbcdn.net/v/t39.30808-6/476158239_1843084426519753_6974734325811164366_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeEtr9TeidFDDO_2_VpSnLIqLG0dEZmY55ksbR0RmZjnmS_p1IOSjXqXm3suNafHKj0Ecd2VRpfUwR6QkKQjgAgU&_nc_ohc=cd0ITnxzIQUQ7kNvgEK43NR&_nc_oc=AdjmbwTkdfacIc156DZujS83Llu2sXgtijK1c9TBeaJGpUKv18ASerGC93wbfR6LS30&_nc_zt=23&_nc_ht=scontent.fdac31-1.fna&_nc_gid=AUa-pp9OWp3XeScDUpFLdB4&oh=00_AYF3HSKSQVYjoCvYtCZ42G5MkX3GqFPQF-mTx5k4cwCA7A&oe=67D80111"
x = requests.get(url2, timeout=12)
with open("random_pic.png", "wb") as file:
  file.write(x.content)
