class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        out = 0
        
        hash_map_first_last = dict(list())
        
        for i in range(len(s)):
            char = s[i]
            
            if char in hash_map_first_last:
                hash_map_first_last[char][1] = i
            else:
                hash_map_first_last[char] = [i, i]
        
        for char, indexes in hash_map_first_last.items():
            elems = set()

            for i in range(indexes[0] + 1, indexes[1]):
                elems.add(s[i])
            
            out += len(elems)

        return out