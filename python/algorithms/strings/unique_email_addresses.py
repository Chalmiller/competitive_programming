# 929: Unique Email Address
from typing import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_email = set()
        for email in emails:
            split_email = email.split("@")
            if "." in split_email[0] or "+" in split_email[0]:
                if "." in split_email[0]:
                    val_email = "".join(split_email[0].split("."))
                    if "+" in val_email:
                        val_email = "".join(val_email.split("+")[0])
                        valid_email.add(val_email + "@" + split_email[1])
                        continue
                    else:
                        valid_email.add(val_email + "@" + split_email[1])
                        continue
                if "+" in split_email[0]:
                    val_email = "".join(split_email[0].split("+")[0])
                    valid_email.add(val_email + "@" + split_email[1])
            else:
                valid_email.add(email)
        return len(valid_email)

obj = Solution()
val_emails = obj.numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"])
print(val_emails)
                