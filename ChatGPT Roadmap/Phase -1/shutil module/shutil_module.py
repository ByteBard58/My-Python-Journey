# Shutil stands for shell utilities, which means that it can do tasks like file/folder copy, paste, move etc.

import os 
import shutil


shutil.copy2(
    "/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/shutil module/demo.txt",
    "/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2//shutil module/demo files/demo1.txt"
)

# shutil.copyfile(
#     "/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/shutil module/demo.txt",
#     "/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2//shutil module/demo files/"
# )        ## Retruns an error

# shutil.move("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/shutil module/demo.x.txt",
#             "/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/shutil module/demo files/")


# shutil.copy allows us to copy a file from one path to another. If the dst path is a folder, it creates a file of the same name of the src in the dst folder (shown in the example)
# shutil.copy2 does the same, the diffrence is that it saves the meta data of the src file too.
# shutil.copyfile does the same, it just doesn't accept a folder as dst path
# shutil.move moves a file form path src to path dst


# shutil.rmtree("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/ISRAEL")
# shutil.rmtree levels an entire directory with everything in it ! Be cautious while using it !!

# shutil.make_archive("demo files", "zip", "/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/shutil module/demo files")
# shutil.make_archive creates archived folderin formats like .zip, .tar etc

# shutil.unpack_archive("demo files.zip", "Demoooooooooo")
# shutil.unpack_archive unpacks a zipped or archived folder

a = shutil.disk_usage("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/shutil module")
print(a)
#shutil.disk_usage prints out the storage statistics of a specified folder

# shutil.copytree("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/shutil module", "/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/ChatGPT Roadmap/Phase -2/shutil module -2")
#shutil.copytree copies an entire directory into another directory (dst must NOT exist)

