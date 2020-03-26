def fibonacci_sum(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

obj = fibonacci(3)
print(obj)