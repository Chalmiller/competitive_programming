from typing import *

class StringIterator:

    def __init__(self, compressedString: str):
        
        self.compressed_str = compressedString
        self.pointer = 0
        self.counter = 0
        self.current_char = ""
        self.length = len(compressedString)
        

    def next(self) -> str:
        
        if not self.hasNext():
            return " "
        
        if self.counter == 0:
            ptr = self.pointer
            
            ch = ""
            while not self.compressed_str[ptr].isdigit():
                ch = ch+self.compressed_str[ptr]
                ptr += 1
                
            self.current_char = ch
                
            self.counter = 0
            while ptr < self.length and  self.compressed_str[ptr].isdigit():
                self.counter = self.counter*10 + int(self.compressed_str[ptr])
                ptr += 1
            
            self.pointer = ptr
            
        self.counter -= 1
        return self.current_char
        

    def hasNext(self) -> bool:
        if self.counter > 0 or self.pointer < self.length:
            return True
        
        return False