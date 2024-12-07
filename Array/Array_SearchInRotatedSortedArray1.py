# Brute Force: Linear Search
# def search(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1

# a = [4,5,6,7,0,1,2]
# print(search(a, 0))


# Optimized: Modified Optimized Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == target):
                return mid
            if (nums[low] <= nums[mid]):
                if (nums[low] <= target and target <= nums[mid]):
                    high = mid - 1
                else: 
                    low = mid + 1
            else:
                if (nums[mid] <= target and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

# Time Complexity: The time complexity of the code is 𝑂(log ⁡𝑛), because it uses binary search to halve the search space in each iteration.
# Space Complexity: The space complexity of the code is 𝑂(1), because it uses only a constant amount of extra space for variables.
