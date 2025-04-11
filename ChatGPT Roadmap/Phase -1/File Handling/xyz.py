import os

file = open("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/GPT Roadmap/Phase 1/File Handling/first.txt", "r")
# print(file.read(10))
# print(file.readline())
# print(file.readline())
for i in file:
  print(i)

file.close()


# file = open("bank.py", "x")

## Or

# if os.path.exists("bank.py"):
#   file = open("bank.py", "x")
# else:
#   print("fuck off")