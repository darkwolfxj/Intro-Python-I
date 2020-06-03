# program to determine if a command line argument passed is prime
import sys

def isPrime():
    num = int(sys.argv[1])
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    if len(factors) > 2:
        print(f"{num} is not prime.")
    else:
        print(f"{num} is prime")
isPrime()