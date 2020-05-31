import math

def largest_prime_factor(n):
  if n <= 1:
    return -1
  primes_end = int(math.sqrt(n)) - 1
  primes = [True for i in range(primes_end+1)]
  prime_res = []
  p = 2

  while (p*p <= primes_end):
    if primes[p] == True:
      for i in range(p*2, primes_end+1, p):
        primes[i] = False
    p += 1
  
  primes[0] = False
  primes[1] = False

  for i in range(len(primes)-1, -1, -1):
    if primes[i] and n%i == 0:
      return i

  # Faster most-awesome answer
  """
  factors = []
  d = 2
  while n > 1:
    while n  % d == 0:
      factors.append(d)
      n /= d
    d = d + 1
  return max(factors)
  """
  

print(largest_prime_factor(600851475143))