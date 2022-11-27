#program to check whether given number is zero, less than zero
#or greater than zero

num = int(input("Enter Number: "))
if num == 0:
    print("GIven number %d is zero."%num)
elif num > 0:
    print("GIven number %d is greater than zero."%num)
else:
    print("GIven number %d is less than zero."%num)
