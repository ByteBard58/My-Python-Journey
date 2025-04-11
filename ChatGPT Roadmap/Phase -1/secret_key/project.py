import os
from dotenv import load_dotenv

load_dotenv()
print(f"The code is {os.getenv("nuke_code")}")

