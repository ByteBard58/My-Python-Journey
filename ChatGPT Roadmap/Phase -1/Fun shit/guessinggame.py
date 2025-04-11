import random
xx = random.randint(1,20)
print('I have a number within 1 to 20, try to guess it. You have 10 attempts')

try:
    for i in range(1,11):
        num = int(input("The Number is: "))
        if num == xx :
            print(f"DAMN, You got it right!; You took {i} attempts")
            break
        elif num > xx:
            print(f"Your number is too more. You have {10-i} attempts left")
        elif num < xx:
            print(f"Your number is too less. You have {10-i} attempts left")
        if i == 10:
            print(f"You failed. The correct anser was {xx}")
except ValueError:
    print("You can only enter integers")
except Exception:
    print("something went wrong")
finally:
    print("Just a demo")

# Not in the roadmap, found it somewhere, tried to create myself