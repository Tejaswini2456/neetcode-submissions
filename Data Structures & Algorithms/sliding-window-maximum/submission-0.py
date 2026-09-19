from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        left = 0

        for right in range(len(nums)):

            # Remove smaller values from the back
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            # Remove indexes that are outside the window
            if dq[0] < left:
                dq.popleft()

            # Once the window reaches size k
            if right - left + 1 >= k:
                result.append(nums[dq[0]])
                left += 1

        return result
        