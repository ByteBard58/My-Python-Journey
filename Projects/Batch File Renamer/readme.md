# 🔁 Batch File Renamer

This is a simple batch file renaming tool written in Python. It allows you to rename multiple files in a folder based on file type and apply a custom naming pattern.

---

## 📁 What It Does

- Renames all files of a given type (e.g. `.txt`) in a folder
- Applies a new prefix with numbered sequence (e.g. `Lecture_1.txt`, `Lecture_2.txt`, etc.)
- Skips files that are already renamed using the same prefix (no double-renaming)
- Ensures no existing files are overwritten

---

## 🧠 How It Works

1. Scans the folder for files with the given extension.
2. Filters out files that already start with the provided prefix.
3. Renames matching files with the new prefix + number.
4. Skips existing filenames to avoid overwriting.

---

## 🧾 Example Usage

Suppose you have a folder named `Testing/` with these files:

```
note1.txt
note2.txt
note3.txt
```

And you run the code (of **main.py** file )

Now the folder becomes:

```
Lecture_1.txt
Lecture_2.txt
Lecture_3.txt
```

Run the script again? It won’t mess with those files — already done.

---

## 📦 Requirements

- Python 3.6+
- Uses only the built-in `pathlib` module (no external dependencies)

---

## ⚠️ Notes

- You can modify the prefix, file type, or folder as needed.
- Check the **main.py** file, that's where the main script is written
