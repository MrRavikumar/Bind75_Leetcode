# Sum of Two Integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b & mask) != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry 
        return a & mask if b > 0 else a

# Time Complexity: The time complexity is 𝑂(1) in the worst-case scenario as the number of iterations in the while loop is limited to the number of bits in an integer (e.g., 32 bits for typical systems).
# Space Complexity: The space complexity is 𝑂(1) as the algorithm uses a constant amount of additional space for variables.