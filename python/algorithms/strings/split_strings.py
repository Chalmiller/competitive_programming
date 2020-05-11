def solution(s):
    res = []
    while len(s) > 1:
        res.append(s[0:2])
        s = s[2:]
        print(res)
    if s:
      res.append(s + '_')
    return res

print(solution('abc'))