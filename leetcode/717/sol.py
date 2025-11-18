from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        length_bits = len(bits)
        last = True
        i = 0
        while i < length_bits:
            if bits[i] == 1:
                last = True
                i += 1 
            else:
                last = False
        
        return not last
            
                