class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i == len(word):
                return node.isEnd
            char = word[i]
            if char != '.':
                if char not in node.children:
                    return False
                return dfs(i+1,node.children[char])
            else:
                for child in node.children.values():
                    if dfs(i+1,child):
                        return True
                return False
        return dfs(0,self.root)
        
