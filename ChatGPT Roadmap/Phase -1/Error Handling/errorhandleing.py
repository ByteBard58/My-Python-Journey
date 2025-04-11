try :
  f = open("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/GPT Roadmap/Phase 1/norm.txt")
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print("Something went wrong")
else:
  print(f.read())
  f.close

