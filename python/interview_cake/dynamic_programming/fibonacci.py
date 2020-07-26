import unittest

class Fibonacci:

  def __init__(self):
    self.memo = {}


  def fibonacci_recursive(self, n):

    if n  < 2:
      return n
    else:
      return self.fibonacci_recursive(n-1) + self.fibonacci_recursive(n-2)

  def dynamic_fibonacci(self, n ):

    if n < 0:
      raise Exception('The number cannot be lower than 0')

    if n < 2:
      return n

    elif n in self.memo:
      return self.memo[n]

    else:
      result = self.dynamic_fibonacci(n-1) + self.dynamic_fibonacci(n-2)

      self.memo[n] = result

      return result

class FibonacciTestSuite(unittest.TestCase):

  def test_recursive_fibonacci(self):
    input = 5
    self.assertEquals(input, Fibonacci().fibonacci_recursive(input))

  def test_dynamic_fibonacci(self):
    input = 5
    self.assertEquals(input, Fibonacci().dynamic_fibonacci(input))

  def test_functions_are_equal(self):
    input = 5
    self.assertEquals(Fibonacci().dynamic_fibonacci(input), Fibonacci().fibonacci_recursive(input))
    
unittest.main(verbosity=2)
      