class Solution:
    def minWindow(self, s: str, t: str) -> str:
        characters = {}

        for c in t:
            if c not in characters:
                characters[c] = 1
            else:
                characters[c] += 1
        
        min_window_size = len(t)

        if len(s) < min_window_size:
            return ""
        
        # init first window
        window = []
        for i in range(min_window_size):
            cur = s[i]
            if not window:
                
            if cur in characters:
                characters[cur] -= 1
            window.append(cur)
            
        # TODO: not implemented yet
        # check if window satisfies the condition


            
            