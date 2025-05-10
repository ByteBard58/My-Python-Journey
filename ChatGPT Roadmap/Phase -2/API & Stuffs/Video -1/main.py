import requests,json

url = "https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow"

response = requests.get(url)

# print(response.json())  ## Prints out the json data
# print(response.json()["items"])   ## Printts out the everything in "items"

# for data in response.json()["items"]:     ## Prints out the titles of each questions
#   print(data["title"])
# for data in response.json()["items"]:
#   print(data["link"])                     ## Prints out the links of each questions



## Creating a script which give you the link and title of every question is viewed for 0 times;
# for index, data in enumerate(response.json()["items"]):
#   if not data["is_answered"]:
#     print(f"Question no.{index}")
#     print(f"Title: {data["title"]}")
#     print(f"Link: {data["link"]}")
#     print("")
#   else:
#     print(f"Skipped Question no.{index}")
#     print("")



# with open("Video -1/main.json","w+") as x:       ## Dumping all the response into another json file
#   json.dump(response.json(),x,indent=4)