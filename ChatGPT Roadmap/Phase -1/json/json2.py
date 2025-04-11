import json

class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def showinfo(self):
    print(f"Name : {self.name}, Age : {self.age}")

class shit:
  def __init__(self, name):
    self.name = name

user1 = User("Shoccho", 69)
user2 = User("Zubayer", 17)
user3 = shit("Sakib")


def encoder(obj):
  if isinstance(obj, User):
    return {"name" : obj.name, "age" : obj.age, obj.__class__.__name__ : True}
  else:
    raise TypeError("The given object can not be decoded into JSON")

def encoder2(k):
  if isinstance(k, shit):
    return {"name" : k.name, k.__class__.__name__: True}
  else:
    raise TypeError("The given object can not be decoded into JSON")



data = json.dumps(user2, default=encoder,  indent=4)     ## Will use fixer decoder
print(data)

data2 = json.dumps(user3, default=encoder2, indent=4)    ## Will use fixer2 decoder
print(data2)


def decoder1(dick):
  if User.__name__ in dick:
    return User(name=dick["name"], age=dick["age"])

dick = json.loads(data, object_hook=decoder1)
print(dick.showinfo())
