# Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]
    
# Time Complexity: 𝑂(𝑛⋅𝑘), where 𝑛 is the input number, and 𝑘 is the average number of bits in the binary representation of numbers from 0 to 𝑛, because the bit_count() function iterates over the bits of each number.
# Space Complexity: 𝑂(𝑛), as the function returns a list of size 𝑛+1.