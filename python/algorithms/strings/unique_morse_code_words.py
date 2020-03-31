# 804: Unique Morse Code Words
from typing import *

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        word_set = set()
        for word in words:
            unique_word = []
            for let in word:
                unique_word.append(morse_code_list[ord(let) - 97])
            word_set.add("".join(unique_word))
        return len(word_set)
        