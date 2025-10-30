from functools import cmp_to_key
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        dig_logs = []

        for log in logs:
            if not log[-1].isdigit():
                let_logs.append(log)
            else:
                dig_logs.append(log)
        
        let_logs.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))

        let_logs.extend(dig_logs)

        return let_logs