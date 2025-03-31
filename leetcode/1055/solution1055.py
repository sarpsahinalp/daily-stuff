import re

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cur: str = ""
        out: int = 0
        idx = 0
        while idx < len(target):
            if cur == "":
                cur += ".*" + target[idx] + ".*"
            else:
                cur += target[idx] + ".*"

            res = re.search(cur, source)
            
            if not res and len(cur) == 5:
                return -1
            
            if not res:
                out += 1
                cur = ""
                continue

            if idx == len(target) - 1:
                out += 1

            idx += 1
        return out