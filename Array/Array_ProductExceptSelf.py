# Product of Array Except Self

#Brute Force
# import math
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in nums:
#             expectList = nums[:]
#             expectList.remove(i)
#             c = math.prod(expectList)
#             result.append(c)
#         return result

#Optimized Using Division Operator
# import math
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         listProduct = math.prod(nums)
#         result = []
#         for i in nums:
#             result.append(listProduct // i)
#         return result

#Optimized Without Using Division Operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result

# Time Complexity: The time complexity is O(n), as the code iterates through the input list nums twice, once for the prefix products and once for the postfix products.
# Space Complexity: The space complexity is O(1) (excluding the output array), since no additional space proportional to the input size is used; the computation is done in-place using the result array.


