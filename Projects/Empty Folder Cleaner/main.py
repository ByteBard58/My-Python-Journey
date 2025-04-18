from  pathlib import Path
import shutil

def main_shit(root):
  for folder in root.iterdir():
    if folder.is_dir():
      contents = list(folder.iterdir())
      
      for more in folder.iterdir():             ## Cheking inside folders (Recursive action)
        if more.is_dir():
          conts = list(more.iterdir())
          for more_files in conts:
            if more_files.name == ".DS_Store":
                more_files.unlink()
          if not any(more.iterdir()):
            shutil.rmtree(more)

      for file in contents:                     ## Cheking inside the parent folders
        if file.name == ".DS_Store":
          file.unlink()
      if not any(folder.iterdir()):
        shutil.rmtree(folder)
        
main_shit(Path("target"))        ### Replace "target" with the path of the folder where you want to perform it