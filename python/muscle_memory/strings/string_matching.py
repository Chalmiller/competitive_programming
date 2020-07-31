"""String Matching"""

class StringMatching:

    def __init__(self, pattern, txt):
        self.pattern = pattern
        self.txt = txt

    def rabin_karp_search(self, txt, pattern, q):
        M = len(pat)
        N = len(txt)

    def brute_forc_pattern_match(self, txt, pattern):
        txt_len, pattern_len = len(txt), len(pattern)
        for i in range(txt_len - pattern_len + 1):
            k = 0
            while k < pattern_len and txt[i + k] == pattern[k]:
                k += 1
            if k == pattern_len:
                return i
        return -1

    def boyer_moore_pattern_matching(self, txt, pattern):
        n, m = len(txt), len(pattern)
        if m == 0: return 0
        last = {}
        for k in range(m):
            last[pattern[k]] = k
        i = m - 1
        k = m - 1
        while i < n:
            if txt[i] == pattern[k]:
                if k == 0:
                    return i
                else:
                    i -= 1
                    k -= 1
            else:
                j = last.get(txt[i], -1)
                i += m - min(k, j + 1)
                k = m - 1
        return -1
            