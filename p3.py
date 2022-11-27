#Program to take input in numeric data and give output in words.

numeric_to_words = {
        0:"Zero",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine"
        }

num = int(input("Enter Number: "))
print(numeric_to_words[num])
