class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        words = S.split()
        for i, word in enumerate(words):
          if word[0].lower() in vowels:
            words[i] = word + 'ma'
          elif word[0] not in vowels:
            words[i] = word[1:] + word[0] + 'ma'
          words[i] = words[i] + 'a' * (i + 1)
        return " ".join(words)