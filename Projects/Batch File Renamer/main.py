import os
from pathlib import Path as path

def main_shit(root, prefix, file_type):
  files = [f for f in root.iterdir() 
           if f.suffix.lower() == file_type.lower() and not f.stem.startswith(prefix)]
  counter =1
  for filename in files:
    ext = filename.suffix.lower()
    while True:
      new_name = root/ f"{prefix}_{counter}{ext}"
      if not new_name.exists():
        filename.rename(new_name)
        break
      counter += 1

main_shit(path("Testing"),"Lecture",".txt")
## Replace "Testing" with the path to the folder where you want to apple this
## Replace "Lecture" with the name you want to rename into
## Replace ".txt" with the extension of the files which you want to rename