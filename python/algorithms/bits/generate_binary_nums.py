def findBin(number):
  res = []
  queue = []

  queue.append(1)

  for i in range(number):
    res.append(queue.pop(0))
    s1 = res[i] + '0'
    s2 = res[i] + '1'
    queue.append(s1)
    queue.append(s2)

  return res