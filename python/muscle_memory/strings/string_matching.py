"""String Matching"""

class StringMatching:

    def __init__(self, pattern, txt):
        self.pattern = pattern
        self.txt = txt

    def rabin_karp_search(self, txt, pattern, q):
        M = len(pat)
        N = len(txt)

    def knuth_morris_pratt(self, txt, pattern):

        def compute_kmp_fail(pattern):
            m = len(pattern)
            fail = [0] * m
            j = 1
            k = 0
            while j < m:
                if pattern[j] == pattern[k]:
                    fail[j] = k + 1
                    j += 1
                    k += 1
                elif k > 0:
                    k = fail[k - 1]
                else:
                    j += 1
            return fail

        n, m = len(txt), len(pattern)
        if m == 0: return 0
        fail = compute_kmp_fail(pattern)
        j = 0
        k = 0
        while j < n:
            if txt[j] == pattern[k]:
                if k == m - 1:
                    return j - m + 1
                j += 1
                k == 1
            elif k > 0:
                k = fail[k-1]
            else:
                j += 1
        return -1


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

        if len(pattern) == 0: return 0
        last = {}
        for k in range(len(pattern)):
            last[pattern[k]] = k
        i = len(pattern) - 1
        k = len(pattern) - 1
        while i < len(txt):
            if txt[i] == pattern[k]:
                if k == 0:
                    return i
                else:
                    i -= 1
                    k -= 1
            else:
                j = last.get(txt[i], -1)
                i += len(pattern) - min(k, j + 1)
                k = len(pattern) - 1
        return -1
            