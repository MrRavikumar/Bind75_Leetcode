# Maximum Product Subarray
# What is SubArray?
# SubArray is a contiguous part of an array
# It can be empty or can have one element
# Formula to Calculate Possible SubArrays of an Array is: len(array) * (len(array) + 1) / 2
# Maximum Product Subarray is a Subarray with maximum product

# Brute Force Approach
# class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     maxProduct = 0
    #     for i in range(n):
    #         currProduct = 1
    #         for j in range(i, n):
    #             currProduct *= nums[j]
    #             maxProduct = max(maxProduct, currProduct)
    #     return maxProduct

# Optimized: Observation Logic Prefix and Suffix Approach
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suffix = 1
        prefix = 1
        maxProd = float('-inf')
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if suffix == 0: 
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[len(nums) - i - 1]
            maxProd = max(maxProd, max(prefix, suffix))
        return maxProd 

# Time Complexity: The algorithm runs in 𝑂(𝑛) time because it iterates through the array of length 𝑛 twice—once from left to right (prefix) and once from right to left (suffix).
# Space Complexity: The algorithm uses 𝑂(1) space as it employs only a constant number of variables for computation, irrespective of the input size.
