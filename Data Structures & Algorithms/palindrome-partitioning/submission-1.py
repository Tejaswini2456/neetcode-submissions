class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []
        def dfs(start):
            if start == len(s):
                result.append(partition.copy())
                return
            for end in range(start,len(s)):
                if self.isPalindrome(s,start,end):
                    partition.append(s[start:end+1])
                    dfs(end+1)
                    partition.pop()
        dfs(0)
        return result
    
    def isPalindrome(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

        