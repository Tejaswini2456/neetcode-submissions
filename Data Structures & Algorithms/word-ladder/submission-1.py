class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord,1)])
        visited = {beginWord}
        while queue:
            word,Length = queue.popleft()
            if word == endWord:
                return Length
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord,Length+1))
        return 0
         