from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str):
        cur = self
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.isWord = True
            



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        out = []

        for word in words:
            root.addWord(word)

        for i in range(len(board)):
            for j in range(len(board[0])):

                def dfs(trieNode: Optional[TrieNode], i: int, j: int, str):
                    if not trieNode or i < 0 or i > len(board) - 1 or j < 0 or j < len(board[0]) - 1:
                        return
                    
                    if trieNode.isWord:
                        out.append(str)
                    
                    cur_character = board[i][j]

                    if cur_character not in trieNode:
                        return
                    
                    dfs(trieNode.children[cur_character], i + 1, j, str + cur_character)
                    dfs(trieNode.children[cur_character], i - 1, j, str + cur_character)
                    dfs(trieNode.children[cur_character], i, j + 1, str + cur_character)
                    dfs(trieNode.children[cur_character], i, j - 1, str + cur_character)

        return out



