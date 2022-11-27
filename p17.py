#Program to read a text file.

file = open('sample_text.txt','r')
str_in_file = file.read()
print(str_in_file)

file.close()
