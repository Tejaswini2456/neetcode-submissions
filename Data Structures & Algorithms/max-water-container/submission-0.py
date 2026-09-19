class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        start = 0
        end = len(heights) - 1

        while start < end:
            area = max(area,(end -                        start)*min(heights[start],heights[end]))
            if heights[start]<heights[end]:
                start += 1
            else:
                end -= 1
        return area

        