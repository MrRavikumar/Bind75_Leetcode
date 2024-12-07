# Search in Rotated Sorted Array II

# Brute Force Approach: Linear Search
# def search(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return True
#     return False

# Optimized: Modified Optimized Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] == target):
                return True
            if (nums[low] == nums[mid] and nums[mid] == nums[high]):
                hight = high - 1
                low = low + 1
                continue
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
        return False
    
# Time Complexity: The time complexity is 𝑂(𝑛) in the worst case because of the scenario where duplicates make the algorithm reduce both low and high linearly, but 𝑂(log ⁡𝑛) in the average case for binary search in a rotated sorted array.
# Space Complexity: The space complexity is 𝑂(1), as the algorithm operates in-place with no additional data structures.