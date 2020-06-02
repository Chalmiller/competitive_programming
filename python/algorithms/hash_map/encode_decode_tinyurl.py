from typing import *
import string
import random

class Codec:

    def __init__(self):
        self.full_tiny = {}
        self.tiny_full = {}
        self.letters = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        def shorten():
          result = ''
          temp = ''
          for i in range(6):
              temp = random.choice(letters)
              result += temp
          return result
        
        if longUrl in full_tiny:
            return "http://tinyurl.com/" + full_tiny[longUrl]
        else:
            suffix = shorten()
            full_tiny[longUrl] = suffix
            tiny_full[suffix] = longUrl
            return "http://tinyurl.com/" + suffix

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))