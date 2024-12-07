# Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor, (i ^ v for i, v in enumerate(nums, 1)))

# Time Complexity: The time complexity is 𝑂(𝑛), where 𝑛 is the length of the nums list, as we iterate through the list once to perform XOR operations.
# Space Complexity: The space complexity is 𝑂(1), as no additional space proportional to the input size is used beyond a few variables.