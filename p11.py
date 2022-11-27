#Program to give factorial of a given number using recursion

num  = int(input("Enter number: "))
pointer = num

def fac(num, pointer):
    if num == 0:
        return num
    elif num < 0:
        return "Factorial of negative number cannot be calculated."
    else:
        if pointer == 1:
            return num
        else:
            pointer = pointer - 1
            num = num * pointer
            return fac(num, pointer)

print(fac(num, pointer))
