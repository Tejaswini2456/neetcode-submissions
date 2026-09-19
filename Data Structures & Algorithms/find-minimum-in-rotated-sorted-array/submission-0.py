class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float("inf")
        for num in nums:
            if num < minimum:
                minimum = num
        return int(minimum)

        