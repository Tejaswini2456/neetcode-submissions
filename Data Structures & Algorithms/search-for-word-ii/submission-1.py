class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        result = []
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c,node):
            char = board[r][c]
            if char not in node.children:
                return
            node = node.children[char]
            if node.word:
                result.append(node.word)
                node.word = None
            board[r][c] = "#"
            directions = {
                (1,0),
                (-1,0),
                (0,1),
                (0,-1)
            }
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if(
                    0<=nr<rows and
                    0<=nc<cols and
                    board[nr][nc]!="#"
                ):
                    dfs(nr,nc,node)
            board[r][c] = char
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return result         