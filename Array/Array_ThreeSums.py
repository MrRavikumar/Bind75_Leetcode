# Three Sums

# Brute Force Approach: N^3
# def threeSum(nums):
#     nums.sort()
#     result = set()
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             for k in range(j + 1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     result.add((nums[i], nums[j], nums[k]))
#     return list(result)

# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))

# Better Approach: N^2  Formula: nums[i] + nums[j] + nums[k] = 0 => nums[k] = -(nums[i] + nums[j])
# def threeSum(nums):
#     nums.sort()
#     result = set()
#     for i in range(len(nums)):
#         hashSet = set()
#         for j in range(i+1, len(nums)):
#             k = -(nums[i] + nums[j])
#             if k in hashSet:
#                 result.add(tuple(sorted((nums[i], nums[j], k))))
#             hashSet.add(nums[j])
#     return list(result)

# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))

# Optimal Approach: 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sumOfTriplet = nums[i] + nums[j] + nums[k]
                if sumOfTriplet < 0:
                    j += 1
                elif sumOfTriplet > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1  
                    while j < k and nums[k] == nums[k+1]: 
                        k -= 1
        return result

# Time Complexity: The time complexity is 𝑂(𝑛^2) because the outer loop runs 𝑛 times and the inner two-pointer loop runs approximately 𝑛 times for each iteration, but sorting the array adds an initial 𝑂(𝑛log⁡𝑛), which is dominated by 𝑂(𝑛^2).
# Space Complexity: The space complexity is 𝑂(1) for the algorithm itself as it uses only a few pointers and variables, but the result list can take up to 𝑂(𝑘) space, where 𝑘 is the number of valid triplets found.