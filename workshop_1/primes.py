# 1.Write a program to generate a list of all prime numbers lessthan 20.
# Before starting it is important to note what a primenumber is.
# 1.A prime number has to be a positive integer
# 2.Divisible by exactly 2 integers (1 and itself)
# 3.1 is not a prime number

#!/usr/bin/env python3
def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if(num % 2 == 0 or num % 3 == 0):
        return False
    i = 5
    while (i * i <= num) :
        if(num % i == 0 or num % (i + 2) == 0):
            return False
        i = i + 6
    return True

def generatePrimes(n):
    listOfPrimes = []
    for i in range(0, n):
        if isPrime(i) == True:
            listOfPrimes.append(i)
    return listOfPrimes

def main():
  print(generatePrimes(20))
  
if __name__ == '__main__': main()
