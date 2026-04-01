class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []  

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):   # We have encountered 
                # right limit for the rectangle, whether when we hit the right boundary
                # or when we find a rectangle of smaller height on the right
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1   # the left boundary of the rectangle,
                # which is till the next smaller rectangle to the left or if none, then extending till 0
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea