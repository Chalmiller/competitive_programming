def power_power(a, b, n):

  def power(b, n):
    if n == 0: return 1
    return b * power(b, n-1)
  
  if b == 0: return 1
  return a * power(a, power(b, n) - 1)

print(power_power(3, 2, 2))
