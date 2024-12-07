# Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count
    

# Time Complexity: The time complexity is O(k), where 𝑘 is the number of bits in the binary representation of 𝑛, as the loop iterates once for each bit until 𝑛 becomes 0.
# Space Complexity: The space complexity is O(1), as the function uses a constant amount of additional memory regardless of the input size.