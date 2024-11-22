class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []

# Space Complexity: 𝑂(𝑛), as the dictionary (seen) grows proportionally with the number of elements in nums in the worst case.
# Time Complexity: 𝑂(𝑛), as each element is processed once, and dictionary operations (lookup and insert) are 𝑂(1) on average.
