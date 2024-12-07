# Find Minimum in Rotated Sorted Array

# Brute Force: Linear Search
# def findMin(nums):
#     min = nums[0]
#     for i in range(1, len(nums)):
#         if nums[i] < min:
#             min = nums[i]
#     return min

# Optimized: Modified Binary Search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minNum = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                minNum = min(minNum, nums[low])
                low = mid + 1
            else:
                minNum = min(minNum, nums[mid])
                high = mid - 1
        return minNum
    
# Time Complexity: The time complexity is 𝑂(log ⁡𝑛) because the algorithm uses a binary search approach, halving the search range in each iteration.
# Space Complexity: The space complexity is 𝑂(1) as the algorithm uses a constant amount of extra space.

# Python Cheese : Believe me It gets the minimum number in log n
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         minVal = min(nums)
#         return minVal