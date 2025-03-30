from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        out = []
        idx = 0
        start = 0
        end = 0
        while idx < len(s):
            if idx > end:
                out.append(end - start + 1)
                start = idx
            cur = s[idx]
            last = s.rfind(cur)
            if end < last:
                end = last
            idx += 1

        if idx > end:
            out.append(end - start + 1)
        return out