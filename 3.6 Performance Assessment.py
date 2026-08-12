import math


def functionOne():
    print("My studentID is hunhar4916")


def functionTwo():
    num1 = int(input("Please enter a whole number: "))
    num2 = int(input("Please enter another whole number: "))

    sum = num1 + num2

    print(f"The sum of {num1} and {num2} is {sum}")

    return sum



def functionThree(sum):
    if sum <= 5:
        print(f"{sum} is less than or equal to 5")
    else:
        print(f"{sum} is greater than 5")


    return 4916

def main():
    #functionOne is displaying my studentID
    functionOne()
    #functionTwo asks the user for 2 numbers and adds those numbers together than
    #returns the sum
    sum = functionTwo()

    #functionThree uses an if else statement to check if the sum is greater or less
    #than 5
    
    functionThree(sum)



    print(f"functionThree returned the value of 4916")

main()
