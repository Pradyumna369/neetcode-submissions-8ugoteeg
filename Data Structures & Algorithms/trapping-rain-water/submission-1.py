class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        curr = 0
        total = 0
        while curr < len(height):
            while stack and height[curr] > height[stack[-1]]:
                prev = stack.pop()
                if stack:
                    h = min(height[curr], height[stack[-1]])
                    vol = (h - height[prev]) * (curr - stack[-1] - 1)
                    total += vol
            stack.append(curr)
            curr += 1
        return total

            



