from typing import *
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
          return -1

        primes = [True for i in range(n + 1)]
        p = 2

        while (p * p <= n):
          if (primes[p] == True):
            for i in range(p*2, n + 1, p):
              primes[i] = False
          p += 1

        primes[0] = False
        primes[1] = False

        count = 0
        for p in range(n + 1):
          if primes[p]:
            count += 1

        return count