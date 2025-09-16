
import math
import os
import random
import re
import sys


def nonDivisibleSubset(k, s):
    remainders = [0] * k
    for i in s:
        remainders[i%k] += 1
    max_val = 0
    max_val += min(remainders[0], 1)
    if k % 2 == 0:
        max_val += min(remainders[k//2], 1)
    for i in range(1, k//2+ 1):
        if i != k -i:
            max_val += max(remainders[i], remainders[k-i])
    return max_val
    
  
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
