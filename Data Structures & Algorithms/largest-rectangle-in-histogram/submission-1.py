class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = 0

        for i in range(len(heights) + 1):

            current = heights[i] if i < len(heights) else 0

            while stack and current < heights[stack[-1]]:

                height = heights[stack.pop()]

                left = stack[-1] if stack else -1

                width = i - left - 1

                area = height * width

                maxArea = max(maxArea, area)

            stack.append(i)

        return maxArea
        