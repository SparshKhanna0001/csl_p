#Program to print all even numbers between m and n.

num1 = int(input("Enter lower limit: "))
num2 = int(input("Enter upper limit: "))

if num1%2 ==0:
        list_of_even = list(range(num1,num2,2))
else:
        list_of_even = list(range(num1+1, num2, 2))


print("Even numbers between {} and {} are:- \n{}".format(num1, num2, list_of_even))
