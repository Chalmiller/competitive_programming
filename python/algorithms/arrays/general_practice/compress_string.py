from typing import *
import collections

def compress(chars: List[str]) -> int:
    char_set = OrderedSet(chars)
    return_list = []
    if len(chars) == 1:
        return 1

    for i in char_set:
        return_list.append(i)
        count = str(chars.count(i))
        if int(count) == 1:
            continue
        else:
            for j in count:
                return_list.append(j)
    print(return_list)
    return len(return_list)

listy = ["a","a","b","b","c","c","c"]
compress(listy)