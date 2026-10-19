class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin,res = nums[0],nums[0],nums[0]
        for n in nums[1:]:
            candidates = (n,n*curMax,n*curMin)
            curMax = max(candidates)
            curMin = min(candidates)
            res = max(res,curMax)
        return res
        