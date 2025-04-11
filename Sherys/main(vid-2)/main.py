# def hlw(y,z,x=89):           #default parameter
#   print('Hello World', x)
#   print(y,z)
# hlw(z=23,y=78)               #keyword argument  #normal arguement = default argument


# def ulf(b=3):
#   print('You mom is pregnant')
#   for i in range(1,b):
#     print(i)
#     if i == 6:
#       break

# ulf(4)

# def checker(s):
#   if s%2==0:
#     return('It is an even number')
#   else:
#     return('It is an odd number')

#x = "abcdefig"       #Index --> a=-8,b=-7,c=-6,d=-5,e=-4,f=-3,i=-2,g=-1
# print(x[-1:-9:-1]) 

# a = checker(78)
# print(a)

# x = "abcdefig"       
# for i in range(len(x)):
#   print(x[i])           #Output: a b c d e f i g
# s = [1,2,3,4,5]
# x = s
# s[2]=33
# print(x)

  # Output: [1, 2, 3, 4, 5] (unchanged)

# tuple = ('Dr',100,'Engineer')
# set = set(tuple)
# print(set)                       #Output:  {'Engineer', 100, 'Dr'}

# b = {12,12,23,'GG'}
# for i in b:
#   print(i)            #Output:  12 GG 23

# a = [1,3,1,1,4,4,6,6,2,8,9,5,3,34,5]
# print(a.count(1))

#What is Dictionary 
#Keys & Values 
#Targetting using keys 
#Dictionay Iteration 
# #Dictionary Methods 
# z = {1:10,5:50,7:70}
# for key in z.keys():
#   print(key)
# for value in z.values():
#   print(value)

# #To iritate over both keys and values;
# for key, value in z.items():
#   print(f"{key}:{value}")

c = {11:200,1:100}
c[111]=300
print(c)    #Output:  {11: 200, 1: 100, 111: 300}

for i in c:
  print(i)

_tt = 'gh'
print(_tt)

