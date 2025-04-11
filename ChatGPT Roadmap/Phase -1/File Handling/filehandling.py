# damn = open("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/GPT Roadmap/Phase 1/norm.txt", "a+")
# damn.write(f"\nGreat")
# damn.close()


# with open("/Users/Sakib/CODE Stuffs /Sakib's Stuffs/PYTHON/GPT Roadmap/Phase 1/norm.txt", "a+") as x:
#   x.write(" I hope you are all good :)")
#   print(x.read())   
# #  Best Practice, because you wont need to close it manually


# with open("x.txt", "w+") as newfile:                 ##Creates new file
#   newfile.write("Hey there")



## RAWX = Read, Append, Write, X


## "r" – Read mode (default). Opens the file for reading. If the file does not exist, it raises a FileNotFoundError.

## "w" – Write mode. Opens the file for writing. If the file exists, it overwrites (deletes) the existing content. If the file does not exist, it creates a new one.

## "a" – Append mode. Opens the file for writing, but does not erase existing content. Instead, new content is added at the end of the file. If the file does not exist, it creates a new one.

## "x" – Exclusive creation mode. Creates a new file, but if the file already exists, it raises a FileExistsError.

## "r+" – Read and write mode. Opens the file for both reading and writing. The file must exist, or it raises a FileNotFoundError.

## "w+" – Write and read mode. Opens the file for both writing and reading. If the file exists, it is overwritten. If the file does not exist, it creates a new one.

## "a+" – Append and read mode. Opens the file for both appending and reading. Content can only be added at the end, and existing content cannot be modified. If the file does not exist, it creates a new one.
