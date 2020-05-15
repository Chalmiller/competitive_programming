def diamond(n):
  for i in range(n):
    print(i, n - i, i * 2 + 1)
    print(" " * (n - i), "*"*(i * 2 + 1))

diamond(5)
    