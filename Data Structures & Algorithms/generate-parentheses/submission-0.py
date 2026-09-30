class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def dfs(openN,closeN):
            if openN == n and closeN == n:
                result.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                dfs(openN+1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                dfs(openN,closeN+1)
                stack.pop()
        dfs(0,0)
        return result
        