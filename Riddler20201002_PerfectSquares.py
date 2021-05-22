# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 08:31:38 2021
Riddler Express 02/10/2020
Benjamin likes numbers that can be written as the difference between two perfect squares. He thinks they’re hip.
For example, the number 40 is hip, since it equals 72−32, or 49−9. But hold the phone, 40 is doubly hip, because it also equals 112−92, or 121−81.

With apologies to Douglas Adams, 42 is not particularly hip. Go ahead and try finding two perfect squares whose difference is 42. I’ll wait.

Now, Benjamin is upping the stakes. He wants to know just how hip 1,400 might be. Can you do him a favor,
and figure out how many ways 1,400 can be written as the difference of two perfect squares? Benjamin will really appreciate it.

@author: tae8858
"""
#%%
# Create function to list prime factors
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return set(primfac)

#%%
import numpy as np

# Create square matrix looking at difference of squares of each index
sims = 1000
matrix  = np.matrix([[x**2 - y**2 for x in range(sims)] for y in range(sims)])
matrix[matrix < 0] = 0
matrix[:1] = 0

# Check values of concern (confirm 42 doesn't match)
value = 42
result = np.where(matrix == value)
print("For ", value, ":\t\t", list(zip(result[0], result[1])))
# Result : For  42 :		 []

# Check values of concern (confirm 40 has (3, 7) and (9, 11) pairs)
value = 40
result = np.where(matrix == value)
print("For ", value, ":\t\t", list(zip(result[0], result[1])))
# Result : For  40 :		 [(3, 7), (9, 11)]

# Check values of concern (test question - 1,400)
value = 1400
result = np.where(matrix == value)
print("For ", value, ":\t", list(zip(result[0], result[1])))
# Result : For  1400 :	 [(11, 39), (25, 45), (43, 57), (65, 75), (173, 177), (349, 351)]

#%%
"""
Extra credit: Can you find a general formula or approach for counting the number of ways any whole number can be written as the difference between two perfect squares?
(Your approach might be a function of whether the number is even or odd, its prime factorization, etc.)
"""
# This is not the full solution, but creates list  of the prime factors and possible square combinations from 1 to 99
for x in range(1, 100):
    value = x
    result = np.where(matrix == value)
    print("For ", value, ":\t", primes(value), "\t\t", list(zip(result[0], result[1])))