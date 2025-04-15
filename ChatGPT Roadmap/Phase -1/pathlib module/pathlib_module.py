import os
from pathlib import Path

# print(os.environ["HOME"])   ## Inclding it for no reason

current_directory = Path.cwd()
# print(f"The current directory is {current_directory}")

home_folder = Path.home()
# print(f"User's home folder is in {home_folder}")

anime_folder = Path("/Users/Sakib/Movies/Anime")
# if Path.exists(anime_folder):
#   print(f"User's anime folder is in {anime_folder}")
## Path.exists() checks whether the path exists or doesn't, then returns True or False

## Use "/" to join paths
movies_dir = Path("/Movies")
anime_dir = movies_dir / "Animes"
AOT_dir  = anime_dir / "AOT"
ep2_path = AOT_dir / "ep2.mkv"
# print(f"User's Anime folder: {anime_dir}")
# print(f"AOT episode 2 path: {ep2_path}")

## You can add all folder, subfolder and file path at once too
martian_path = movies_dir / "Holywood" / "The Martian.mkv"
# print(f"You can find The Martian movie in {martian_path}")


## Accessing path components;
damn = Path("/usr/local/Downloads/Wallpaper/scenary.great.jpeg")

# print(f"Original Path: {damn}")
# print(f"Name of the file: {damn.name}")
# print(f"Name without last suffix: {damn.stem}")
# print(f"Suffix used at last: {damn.suffix}")
# print(f"All suffixes in use: {list(damn.suffixes)}")
# print(f"Logical Parent directory: {damn.parent}")
# print(f"The components: {damn.parts}")
# print(f"The part before the components: {damn.anchor}")

## Cheking Path Properties ;
## ("path").exists    --> Checks if the path exists (returns True) or not (returns False)
## ("path").is_file   --> Checks if the file is a regular file (returns True) or not (returns False)
## ("path").is_dir    --> Checks if the path leads to directory (returns True) or not (returns False)

## Path Manipulation ;
## ("path").absolute() --> Returns the absolute path of a relative path
## ("path").resolve()  --> Same as .absolute()
p = Path("shutil module/Attributes.png")
print(p.resolve())
print(p.exists())
print(p.is_relative_to("shutil module"))

## Path().mkdir()   --> Creates new file (only if it doesnt exist)
# Path("pathlib module").mkdir(exist_ok=True)     ## Avoids error
# Path("os module/shutil shit/damn").mkdir(parents=True, exist_ok=True)  ##Create nested directories in this way
## Path()touch()     --> Touches a file (if the file doesnt exist,it creates the file)
## Path().unlink()   --> Deletes a file
## Path().rmtree     --> Deletes an empty directory (for packed dirs, use shutil.rmtree)

## Iteration in a folder ;
# x = Path(".")       ## "." represnets the cwd
# for i in x.iterdir():
#   print(i)

## Glob and Reecursive Glob file search ;
y = Path("shutil module")     ## Glob search (Can only search in first level, can't dive into subdirectories)
for i in y.glob("*.py"):                    ## * looks for everything, ? looks for a single character only
  print(i)

y = Path(".")                 ## Recursive glob search (searches even through the subdirectories)
for i in y.rglob("*.png"):          
  print(i)


## File renaming ;
# z = Path("pathlib module/pathlib_mod.py")
# z.rename("pathlib module/pathlib_module.py")   ## You can also move a file to another path while renaming it
