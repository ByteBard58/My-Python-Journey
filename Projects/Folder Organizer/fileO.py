import os
from pathlib import Path as path
import shutil

root = path(".")       # Replace the . with the path of your directory  

file_types ={
  "Images" : [".png", ".jpg", ".jpeg"],
  "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
  "Scripts": [".py", ".js", ".sh"],
  "Archived" : [".zip", ".tar"],
  "Videos": [".mp4",".mkv",".mov",".avi"]
}

for file in root.iterdir():
    if file.is_file():
        moved = False
        for name, extensions in file_types.items():
            if file.suffix.lower() in extensions:
                target_dir = root / name
                target_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(target_dir / file.name))
                moved = True
                break
        if not moved:
            others_dir = root / "Other files"
            others_dir.mkdir(exist_ok=True)
            shutil.move(str(file), str(others_dir / file.name))

    if file.is_dir() and file.name not in ["Images", "Documents", "Archived", "Scripts", "Other files", "Folders","Videos"]:
        put_it = root / "Folders"
        put_it.mkdir(exist_ok=True)
        shutil.move(str(file), str(put_it / file.name))

print("Files are organized !!")
