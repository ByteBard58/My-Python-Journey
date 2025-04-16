
# Folder Organizer

A Python script that automatically organizes files and folders in a specified directory (e.g., Downloads) by moving files into categorized subfolders. It sorts files based on their extensions and moves them to predefined folders like "Images," "Documents," "Scripts," "Archived," and "Other files." Additionally, non-categorized folders are moved into a "Folders" directory.

## Features

- Sorts files into categories based on their extensions:
  - Images: `.png`, `.jpg`, `.jpeg`
  - Documents: `.pdf`, `.docx`, `.txt`, `.xlsx`
  - Scripts: `.py`, `.js`, `.sh`
  - Archived files: `.zip`, `.tar`
- Moves unknown file types into an "Other files" folder.
- Moves non-special folders into a "Folders" directory.
- Avoids creating duplicates, as the script checks for existing subfolders.
- Easy to customize and extend by adding more file categories.

## Requirements

- Python 3.x
- `os`, `shutil`, `pathlib` (Standard Python Libraries)


## Usage

1. Place the `folder_organizer.py` script in the directory you want to organize (e.g., your Downloads folder).
2. Run the script. It will create the following subdirectories if they don't exist:
   - Images
   - Videos
   - Documents
   - Scripts
   - Archived
   - Other files
   - Folders
3. The script will automatically move files and folders based on the predefined categories.

## Customization

You can easily customize the script by adding more file types and categories in the `file_types` dictionary. To do so, simply add more file extensions to the appropriate category.

Example:
```python
file_types = {
    "Images" : [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    ...
}
```
## Acknowledgments

- Thanks to Python's powerful standard libraries (`os`, `shutil`, and `pathlib`) for making this project easy to implement.
