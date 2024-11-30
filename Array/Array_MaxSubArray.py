# Maximum Subarray
# What is SubArray?
# SubArray is a contiguous part of an array
# It can be empty or can have one element
# Formula to Calculate Possible SubArrays of an Array is: len(array) * (len(array) + 1) / 2
# Maximum Subarray is a Subarray with maximum sum

# Brute Force Approach
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # maxSum = 0
        # for i in range(n):
        #     currSum = 0
        #     for j in range(i, n):
        #         currSum += nums[j]
        #         maxSum = max(maxSum, currSum)
        # return maxSum


# Optimized: Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = 0
        maxSum = float('-inf')
        for i in range(n):
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum

# Time Complexity: 𝑂(𝑛), as the algorithm iterates through the list of size 𝑛 once.
# Space Complexity: 𝑂(1), as it uses a constant amount of additional space regardless of the input size.
