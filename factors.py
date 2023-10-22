#!/usr/bin/python3
import sys

# get the file name from the command line argument
file_name = sys.argv[1]

# open the file and read the numbers
with open(file_name) as f:
    numbers = [int(line) for line in f]

# loop through each number
for n in numbers:
    # initialize p and q as 1
    p = 1
    q = n
    # loop from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # if n is divisible by i, update p and q
        if n % i == 0:
            p = i
            q = n // i
            # break the loop as soon as a factor is found
            break
    # print the factorization in the format n=p*q
    print(f"{n}={p}*{q}")

