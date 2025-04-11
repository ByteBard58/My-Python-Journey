# Couldn't write a file for the questions, sorry for that :(


# 1.
# x = "abcDefig"

# print(len(x))    #length
# print(x.upper())  #upper
# print(x.lower())  #lower
# y = x
# print(y)
# for i in range(7,-1,-1):
#   print(x[i], end="")
# print()

# 2.
# x = 'abCdEfiG'
# for i in x:
#   if i.islower():
#     print(i)
# for i in x:
#   if i.isupper():
#     print(i)

# 3.
# x = input('Gimme the string')
# Letters = 0
# Digits = 0
# Special_Characters = 0
# spaces = 0

# for i in x:
#   if i.isalpha():
#     Letters += 1
#   elif i.isdigit():
#     Digits += 1
#   elif i.isspace():
#     spaces += 1
#   else :
#     Special_Characters += 1

# print(f"Number of letters: {Letters}")
# print(f"Number of Digits: {Digits}")
# print(f"Number of Speial Characters: {Special_Characters}")
# print(f"Number of spaces: {spaces}")

# 4.
# d = input('Gimme a string')
# vowels = 0
# for i in d:
#   if i in "aeiouAEIOU":
#     vowels += 1

# print(f"Number of vowles: {vowels}")

# 5.
# str1 = input("Gimme a string")
# str2 = ""
# for i in range(len(str1)-1,-1,-1):
#   str2 += str1[i]
# if str1 == str2:
#   print("It is a palindrome string")
# else:
#   print("It is not a palindrome string")


# Lists
# 1.
# x = []
# num = int(input('How many numbers should be in the list'))
# for i in range(num):
#   y = int(input('Input the element (in integer)'))
#   x.append(y)
# print(x)

# 2.
# x = [1,2,3,4,5]
# rev = []
# for i in range(len(x)-1,-1,-1):
#   rev.append(x[i])
# print(rev)

# 3. 
# x = [6,4,0,3,-3,-10,100]
# pos = []
# neg = []
# for i in x:
#   if i<0:
#     neg.append(i)
#   elif i>0:
#     pos.append(i)
# print(pos)
# print(neg)

# 4.
# x = [1001,100,120,12,11,6,72,907,240,427]
# z = max(x)
# print(f"Greatest number: {z}, Index: {x.index(z)}")

# 5.
# x = [1000,1001,100,120,12,11,6,72,907,240,427,1000.5]
# x.remove(max(x))
# z = max(x)
# if x.index(z) == 0:
#   print(f"2nd Greatest number: {z}, Index: {x.index(z)}")
# elif x.index(z)>0:
#   print(f"2nd Greatest number: {z}, Index: {x.index(z)+1}")

# 6.
# x = [55,56,57,65,58]
# for i in range(len(x)-1):
#   if x[i] <= x[i+1]:
#     continue
#   else:
#     print("The list isn't sorted")
#     break
# else:
#   print("Your list is sorted")            
#Note: The word "sorted" represents both ascending and descending order, 
# But this code only works in case of ascending order. 
# It will still print "not sorted" for descending ordered lists

# 7.
# x = ["radar","level","radar"]
# y = []
# for i in range(len(x)-1,-1,-1):
#   y.append(x[i])
# if x == y:
#   print("It's a palindromic list")
# elif x != y:
#   print("It's not a palindromic list")

# 8.
# x = [1,2,3,3,3,4,5,5,5,5]
# y = []
# num = 0
# for i in x:
#   if i in y:
#     pass 
#   else :
#     num += 1
#   y.append(i)
# print(num)

