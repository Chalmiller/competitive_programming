import math  
from Queue import PriorityQueue 

def KMaxCombinations(a, b, n, k):
    pq = PriorityQueue()

    for i in range(0, n):
        for j in range(0, n):
            a = a[i] + b[j]
            pq.put((-a, a))
    count = 0
    while (count < k):
        print(pq.get()[1])
        count += 1
