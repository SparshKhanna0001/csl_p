#Program to calculate square of a number using lambda function.

num  = int(input("Enter number: "))
sq_num = (lambda x: x*x)(num)
print(sq_num)
