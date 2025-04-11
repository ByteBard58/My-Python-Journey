# Special Palidrome checker 

# def checker(number):
#   x = number
#   return x == x[::-1]
# target = input('Gimme something')
# if checker(target):
#   print(f"{target} is a palindrome")
# else :
#   print(f"{target} is not a palindrome")


#1
# num = int(input("The Number"))
# for i in range(1,num+1,1):
#   if num%i==0:
#     print(i)

#2
# num = int(input("The Number"))
# sum = 0
# for i in range(1,num+1,1):
#   if num%i==0 and i != num:
#     sum = sum + i
# if sum == num:
#   print("The number you provided is a perfect number")
# else :
#   print("The number you provided is not a perfect number")

#3 (my approach, not standard)
# num = int(input('The Number'))
# sum = 0
# for i in range(1,num+1,1):
#   if num%i==0:
#     sum = sum + i
# if sum == num+1 and num>=2:
#   print('It is a prime number')
# if sum != num+1 and num>=2:
#   print('It is a composite number')
# if num<2:
#   print('It is neither prime nor composite')

#3 (standard)
# num = int(input('The Number'))
# sum = 0
# for i in range(1, num + 1, 1):
#     if num % i == 0:
#         sum = sum + 1
# if sum == 2 and num >= 2:
#     print('It is a prime number')
# if sum != 2 and num >= 2:
#     print('It is a composite number')
# if num < 2:
#     print('It is neither prime nor composite')

#4
# y = int(input("Enter the number"))
# while y>0:
#   print(y%10)
#   y = y//10

#5
# y = int(input("Enter the number"))
# x=y
# z = 0
# while y>0:
#   z = z*10+y%10
#   y = y//10
# if z == x:
#   print("It's a palindromic number")
# else :
#   print("It's not a palindromic number")


#Dictionay problems
# 1.
# x = {22:11,33:22,44:33}
# y = {55:44,66:55}
# x.update(y)
# print(x)

# 2.
# x = {1:10,2:7,3:39,4:13}
# sum = 0
# for i in x.values():
#   sum += i
# print(f"The sum of dictionay x is {sum}")

# 3.
# x = int(input('Which element do you want to check?'))
# list = [1,2,3,3,4,4,5,6]
# print(f"It is {list.count(x)} times in the list")

# 4.
# x = {1:22, 3:3333, 4: 4444, 5:654, 6:342}
# y = {34:12221, 4:111, 5:346, 8:89,  2:222, 4335: 778}
# for i in x.keys():
#   if i in y.keys():
#     y[i] = y[i] + x[i]
#   else:
#     y[i] = x[i]
# print(y)


