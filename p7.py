#Program to print elements of the Fibnacci Series till a limit.

limit = int(input("Enter number of elements of fibonacci series that are to be displayed: \n>"))

series = [0,1]

for i  in range(limit):
    print(series[0],  end=" ,")
    series.append(series[0] + series[1])
    series.remove(series[0])
    

