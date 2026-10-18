class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robLine(houses):
            prev1,prev2 = 0,0
            for money in houses:
                current = max(money+prev1,prev2)
                prev1 = prev2
                prev2 = current
            return prev2
        return max(
            robLine(nums[:-1]),
            robLine(nums[1:])
        )
        