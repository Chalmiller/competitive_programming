# 359: Logger Rate Limiter
from typing import *
from collections import defaultdict

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.msg.get(message) == None:
            self.msg[message] = timestamp
            return True
        else:
            if abs(self.msg[message] - timestamp) >= 10:
                self.msg[message] = timestamp
                return True
            else:
                return False
        


# Your Logger object will be instantiated and called as such:
obj = Logger()
param_1 = obj.shouldPrintMessage(1, "foo")
param_2 = obj.shouldPrintMessage(2, "foo")
param_4 = obj.shouldPrintMessage(2, "bar")
param_3 = obj.shouldPrintMessage(11, "foo")
print(param_3)