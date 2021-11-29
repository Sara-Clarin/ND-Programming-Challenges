#!/usr/bin/env python3


# Carmichael numbers: program to check if numbers are prime, and to perform modular exponentiation
# Author : Sara Clarin
# 29 November 2021

import sys, math


def is_prime( number ):
    '''
    Determine if a number is prime by testing divisibility to facturs up to sqrt(n)
    '''
    if number <= 1:
        return False

    end = math.ceil(math.sqrt( number) )
    for i in range( 2, end):
        if number % i == 0:
            return False

    return True

def is_carmichael( a, n, modulus):
    '''
    Tests if a^n mod n = a
    Number: Composite number
    Performs recursive modular exponentiation 
    '''
    # Base case
    if n == 0:   # a^0 mod m = 1 mod m
        return 1 % modulus

    # Recursive Case
    res = is_carmichael( a, n//2, modulus)
    res = pow( res, 2, modulus)

    if n % 2:    # odd case: multiply by an extra factor of a (mod m?)
        res = (res * a) % modulus

    return res

def main():

    for number in map(int, sys.stdin):
        a = 3              # anything less than number - 1

        if not is_prime(number):
            if is_carmichael(a, number, number ) == a:
                print(f'The number {number} is a Carmichael number.' )
            else:
                print(f'{number} is normal.')
        else:
            print(f'{number} is normal.')


if __name__ == "__main__":
    main()