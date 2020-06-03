# program to determine if a command line argument passed is prime
import sys

def isPrime():
    num = int(sys.argv[1])
    if num > 3:
            if ((num % 2 == 0) or (num % 3 == 0)):
                print("not prime")
            else: 
                i = 5
                while i * i <= num try
                    if num % i == 0 or num % (i + 2) == 0:
                        print("not prime")
    else:
        print("prime")
    print(num)

isPrime()