#Program to give sum, difference, product and quotient of two given numbers.

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))

def calculator(num1, num2):
    sum = num1+num2
    sub = num1 - num2
    mul = num1*num2

    if num2 == 0:
        div = "Can't divide by zero"
    else:
        div = num1/num2

    return "\nGiven numbers are: \n{} and {} \n\nFollowing Operations performed:\n Addition: {} \n Substraction: {} \n Multiplication: {} \n Divison: {} \n".format(num1,num2,sum,sub,mul,div)

    
print(calculator(num1, num2))
