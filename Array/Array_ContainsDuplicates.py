class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# Time Complexity: 𝑂(𝑛), as creating a set from the input list takes linear time, where 𝑛 is the length of nums.
# Space Complexity: 𝑂(𝑛), since the set requires additional space to store up to 𝑛 unique elements.