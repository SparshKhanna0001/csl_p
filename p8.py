#To print factorial of the given number using function.

num = int(input("Enter number: "))

def fac(num):
    if num < 0:
        return "Factorial of negative number cannot be calculated."
    elif num == 0:
        return "Factorial of the given number is %d."%num
    else:
        for i in range(2, num):
            num *= i
        return num

print(fac(num))
