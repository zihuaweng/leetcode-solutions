#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

import math

# 最大公约数   Greatest common divisor
def get_gcd(a, b):
    if b == 0:
        return a
    print(a, b)
    return get_gcd(b, a % b)

get_gcd(48, 30)

# 计算约数个数
# 时间复杂度 O(n)
def divisor1(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return count


# count prime， 
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i + i, n, i):   # delete all its multiples
                    primes[j] = False
        return sum(primes)


# Use upper limit of (n**0.5)+1, because:
#  (a) the smallest factor of a non-prime number will not be > sqrt(n).
#      Ex. non-prime = 100,
#           5*20
#           10*10,
#           20*5   # !! we have seen 5 before.



# 判断prime，因为所有prime都是6n+1或者6n-1，同时我们只需要计算到sqrt(n)就可以
def find_primer(n):
    if n <= 3:
        return n > 1
    if n%6 != 1 and n%6 != 5:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n%i == 0 or n %(i+2) == 0:
            return False
    return True


# 计算约数个数
# 时间复杂度 O( sqrt(n) )
def divisor2(num):
    count = 0
    sqrt = int(num ** 0.5)
    for x in range(1, sqrt + 1):
        if num % x == 0:
            count += 2
            print(x, num // x)
    return count - (sqrt ** 2 == num)


# power of 4
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0 and n & 0xAAAAAAAA == 0


# power of 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


# power of 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(2)) % 1 == 0


# devide
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        a / b = c
        
        keep subtracting b, a faster way is to -2*b, -4*b, -1024*b

        if a > 2 * b  => c should be bigger than 2 (1<<1)
        if a > 4 * b  => c should be bigger than 4 (1<<2)
        if a > 1024 * b  => c should be bigger than 1024 (1<<10)

        a might == 1024*b + 4*b + 2*b
        c = (1024+4+2)

        2 * b == b << 1
        1024 * b == b << 10
        
        """
        sig = (dividend < 0) == (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            shift = 0
            while a >= b << (shift + 1):
                print(a, res)
                shift += 1
            res += 1 << shift
            a -= b << shift
        return min(res if sig else -res, (1 << 31) - 1)


# power
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        if n & 1 == 0:
            return self.myPow(x * x, n >> 1)
        else:
            return x * self.myPow(x * x, n >> 1)

# sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            # print(l,r)
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1

        return r


# root of number, x is the number and n is the root
def root(x, n):
  if x == 0:
    return 0
  
  low = 0
  hi = max(1, x)
  root = (low+hi) / 2.0
  
  while root - low >= 0.001:
    if root**n > x:
      hi = root
    elif root**n < x:
      low = root
    else:
      break
    root = (low+hi) / 2.0
    
  return root