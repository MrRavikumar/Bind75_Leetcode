# Container With Most Water

#Brute Force
# def maxArea(height):
#     maxArea = float('-inf')
#     for i in range(len(height)):
#         for j in range(i + 1, len(height)):
#             maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
#     return maxArea

# height = [1,8,6,2,5,4,8,3,7]
# print(maxArea(height))

# Optimized: Two Pointer Approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = float('-inf')
        rp = len(height) - 1
        lp = 0
        while (lp < rp):
            containerHeight = min(height[lp], height[rp])
            containerWidth = rp - lp
            currentArea = containerWidth * containerHeight
            maxArea = max(maxArea, currentArea)
            if (height[lp] < height[rp]):
                lp += 1
            else:
                rp -= 1
        return maxArea
    
# Time Complexity: The time complexity of the given code is O(n) because the two-pointer approach ensures each element in the list is processed at most once.
# Space Complexity: The space complexity of the given code is O(1) because it uses a constant amount of extra space regardless of the input size.