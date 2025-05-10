def fibon(n):
    series = [0,1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    while len(series)<n:
        series.append(series[-1]+series[-2])
    return series
def analysis(fiboseries):
    print(f"The series = {fiboseries}")
    print(f"Sum = {sum(fiboseries)}")
    print(f"Average= {sum(fiboseries)/len(fiboseries)}")
    if len(fiboseries)>2:
        print(f"The golden ratio = {fiboseries[-1]/fiboseries[-2]}") 


try:
    n = int(input("How many numbers do you want?"))
    if n<0:
        print("Fuck You, Provide positive integer")
    else:
        analysis(fibon(n))
except ValueError:
    print("Provide valid integer!!!!!!!!!!")


## Seccond approach
# def fibon(n):
#   series = [0,1]
#   for i in range(0,n):
#     series.append(series[-1]+series[-2])
#   return series
# print(fibon(10))
