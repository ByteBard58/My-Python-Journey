# 🧹 Empty Folder Cleaner (Recursive) 

A simple and effective Python script to **automatically find and delete empty folders** (including those that contain only `.DS_Store` files) inside a target directory. Especially useful for macOS users who get cluttered `.DS_Store` files everywhere!

---

## 🔧 What It Does

- Recursively checks all subfolders inside the `target/` directory
- Deletes `.DS_Store` files if they exist
- Deletes folders **only if they are truly empty**
- Logs every action (deleted folders, skipped ones, etc.)

---

## 🐍 Technologies Used

- Python 3.x
- `pathlib` – For clean and modern path handling
- `shutil` – For removing folders

---

## 📁 Folder Structure Example

Before cleaning:
```
target/
├── Folder1/
│   └── .DS_Store
├── Folder2/
│   └── SubFolder/
│       └── .DS_Store
├── Folder3/
│   └── file.txt
```

After cleaning:
```
target/
├── Folder3/
│   └── file.txt
```


## 📜 Script

You can find the script in the **main.py** file.



## 💡 Notes

- It searches and deletes **.DS_Store** files which macOS creates as default.
- Modify the script to ignore or include other hidden files as needed.
- Can be extended to support full recursive cleanup (deep nested folders) with a custom function.


---

