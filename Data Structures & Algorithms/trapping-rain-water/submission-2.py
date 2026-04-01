class Solution:
    def trap(self, height: List[int]) -> int:
        # stack = []
        # curr = 0
        # total = 0
        # while curr < len(height):
        #     while stack and height[curr] > height[stack[-1]]:
        #         prev = stack.pop()
        #         if stack:
        #             h = min(height[curr], height[stack[-1]])
        #             vol = (h - height[prev]) * (curr - stack[-1] - 1)
        #             total += vol
        #     stack.append(curr)
        #     curr += 1
        # return total

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        return res




            



