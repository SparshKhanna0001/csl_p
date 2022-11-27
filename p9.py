#To check whether the given number is prime or not.

num = int(input("Enter Number: "))

def prime_or_not(num):
    if num == 1:
        return "Given number %d is neither a prime number nor a composite number."%num
    else:
        if num in (2,3):
            return "Given number %d is a prime number."%num
        else:
            factors = 2
            while True:
                for i in range(2, num):
                    if num % i == 0:
                        factors += 1x
                        break
                break
            
            if factors == 2:
                return "Given number %d is a prime number."%num
            else:
                return "Given number %d is a composite number."%num

print(prime_or_not(num))
