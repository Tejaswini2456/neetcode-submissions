class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        result = []
        combination = []
        def dfs(i):
            if i == len(digits):
                result.append("".join(combination))
                return
            letters = phone[digits[i]]
            for letter in letters:
                combination.append(letter)
                dfs(i+1)
                combination.pop()
        dfs(0)
        return result