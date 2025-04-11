import os 

os.chdir("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2")
print(f"Current working directory: {os.getcwd()}")
print(os.listdir())

# os.getcwd() --> Prints the current working directrory
# os.chdir("Path") --> Changes the cwd to the given path 
# os.listdir --> Prints all of the directories stored inside cwd

path = os.path.join("Users","Bill Gates","idk","idgaf","PYTHON", "shit.py")
# print(path)
if os.path.exists(path):
  print("Green")
elif not os.path.exists(path):
  print("Red")

#os.path.join("Folder", "Subfolder", "Files") --> Creates new path, just path 
#os.path.exists("Path") --> Returns true if the given path exists, false for the opposite

print(os.environ.get('HOME'))
os.environ["Treadstone"] = "1082919"
print(os.environ.get("Treadstone"))

# Environment variables are some system-wide variables created by the OS and it is accessed by various programms 
# os.environ.get("HOME") --> Returns the path where the user directory is stored
# New environment variable can be created temporarily by using dictionary indexing. (Line 22)


## os.makedirs("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/os module")

# Check "os fnc.png" to get more info on mkdir, makedirs, rmdir, remove

# os.chdir("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/os module")
# os.rename("shit.png", "Attributes.png")
# # os.rename() --> Renames file or directory

