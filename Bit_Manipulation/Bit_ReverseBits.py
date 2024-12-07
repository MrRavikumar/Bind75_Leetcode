# Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            ans |= ((n >> i) & 1) << (31 - i)
        return ans


# Time Complexity: The time complexity of the code is O(32), as the loop runs a fixed number of 32 iterations, regardless of the input size.
# Space Complexity: The space complexity is O(1), as the algorithm uses a constant amount of space to store variables (ans and loop indices).