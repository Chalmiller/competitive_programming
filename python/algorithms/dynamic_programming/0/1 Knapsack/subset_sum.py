def can_partition(num, sum):
  n = len(num)
  dp = [[False for x in range(sum + 1)] for y in range(n)]

  for i in range(0, n):
    dp[i][0] = True

  for s in range(1, sum + 1):
    dp[0][s] = True if num[0] == s else False
  
  for i in range(1, n):
    for s in range(1, sum + 1):
      if dp[i - 1][s]:
        dp[i][s] = dp[i - 1][s]
      elif s >= num[i]:
        dp[i][s] = dp[i - 1][s - num[i]]
        
  return dp[n - 1][sum]