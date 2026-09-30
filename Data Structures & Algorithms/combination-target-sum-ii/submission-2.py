class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combination = []
        def dfs(start,total):
            if total == target:
                result.append(combination.copy())
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                combination.append(candidates[i])
                dfs(i+1,total+candidates[i])
                combination.pop()
        dfs(0,0)
        return result

            
        