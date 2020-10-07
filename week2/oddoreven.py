import math

class oddOrEven():
    number = math.floor(int(input("please provide a number")))
    self def oddOrEven(newNumber):
        if newNumber % 2 == 0:
            print(f"{str(newNumber)} is even!")
        elif newNumber % 2 == 1:
            print(f"{str(newNumber)} is odd!")
    def multipleOfFour(newNumber):
        print(f"the number {str(newNumber)} is a multiple of 4" )
    if number % 4 == 0:
        multipleOfFour(number)
    elif number % 4 != 0:
        oddOrEven(number)

class oddOrEven2():
    number1 = math.floor(int(input("please provide the first number")))
    number2 = math.floor(int(input("please provide the second number")))
    def checkNum(check, num):
        if check % num == 0:
            print(f"{str(num)} divides evenly into {str(check)}")
        elif check % num != 0:
            print(f"{str(num)} does not divide evenly into {str(check)}")
    checkNum(number1, number2)