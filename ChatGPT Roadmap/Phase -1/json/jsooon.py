import json

data = {
  "Name": "Zubayer",
  "Age" : 17,
  "Anime_fan" : True,
  "Btter_than_Sakib_in_almost_everything" : True,
  "Future_BUETian" : True,
  "Wife" : "Football (iykyk)",
  "G.O.A.T in" : "Programming, Anime, Physics, Math"
}


data_json = json.dumps(data, indent=4)
# print(data_json)

data_py = json.loads(data_json)                     ## json.dumps --> Coverts Python into JSON
# print(data_py)                                    ## json.loads --> Coverts JSON into Python

with open("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/GPT Roadmap/Phase 2/json/zub.json", "w+") as x:
  json.dump(data, x, indent=4)

with open("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/GPT Roadmap/Phase 2/json/sam.json", "r") as y:
  loaded_shit = json.load(y)

print(loaded_shit)
#Check the Output below !!!!

