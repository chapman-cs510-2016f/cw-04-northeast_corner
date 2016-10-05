#!/usr/bin/env python3

def eratosthenes(n):
    """
    This function generates a list of all primes smaller than n using eratosthenes's algorithm
    """
    #generate a list of integers to filter
    integers = [x for x in range(2,n)]
    i = 0
    while i<len(integers):
        #remove all elements that are divisible by the largest prime that hasn't been checked yet
        #the condition statement is the condition for keeping the value (ie. primeness condition)
        #the first of these is that it must not be divisible by smaller primes
        #the second of these ensures that a prime is not removed for being divisible by itself
        integers = [x for x in integers if ((x%integers[i])!=0 or x==integers[i])]
        i+=1
    return integers

def gen_eratosthenes():
    """
    This is a generator of primes that works using eratosthenes's algorithm.
    Using next() on the generator yields the next prime.
    """
    prime = 2 #'prime' is the current largest prime
    primes = [] #'primes' is a list of all primes found so far
    while True:
        yield prime
        primes.append(prime)
        maybePrime = prime+1
        #this loop checks if maybePrime is prime then incriments and repeats if it is not prime
        while(True):
            isPrime = True #guilty until proven innocent
            for p in primes: #checking each prime found so far
                if (maybePrime%p==0):
                    isPrime = False
                    break #moves to the else statement of the outer while loop
            if (isPrime):
                prime = maybePrime
                break
            else:
                maybePrime+=1

def test_primes():
    assert eratosthenes(42) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

def main():
    from sys import argv
    print(eratosthenes(int(argv[1])))

if __name__ == '__main__':
    main()
