#Program to print string in forward direction and
# and in reverse direction.

str_input = input("Enter a word or anything: ")

print("Elements of list in Forward direction are ",end="")

for i in str_input:
        print(i, end=", ")

print()

print("Elements of list in reverse direction are ",end="")

for i in str_input[::-1]:
        print(i, end=", ")

