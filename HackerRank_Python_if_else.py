Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1

n = 24
n > 26 and n is even, so it is not weird.

#!/bin/python3

import math
import os
import random
import re
import sys




n = int(input()) 

if n % 2 != 0: 
    print("Weird") 
elif n % 2 == 0 and n in range(2,6): 
    print("Not Weird") 
elif n % 2 == 0 and n in range(6,21): 
    print("Weird") 
else: 
    print("Not Weird")
