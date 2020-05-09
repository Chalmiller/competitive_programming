def count_ways(n):
  dp = [0 for x in range(n+1)]
  return count_ways_recursive(dp, n)


def count_ways_recursive(dp, n):
  if n == 0:
    return 1  # base case, we don't need to take any step, so there is only one way

  if n == 1:
    return 1  # we can take one step to reach the end, and that is the only way

  if n == 2:
    return 2  # we can take one step twice or jump two steps to reach at the top

  if dp[n] == 0:
    # if we take 1 step, we are left with 'n-1' steps;
    take1Step = count_ways_recursive(dp, n - 1)
    # similarly, if we took 2 steps, we are left with 'n-2' steps;
    take2Step = count_ways_recursive(dp, n - 2)
    # if we took 3 steps, we are left with 'n-3' steps;
    take3Step = count_ways_recursive(dp, n - 3)

    dp[n] = take1Step + take2Step + take3Step
    print(dp)

  return dp[n]


def main():

  # print(count_ways(3))
  # print(count_ways(4))
  print(count_ways(5))


main()