class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# Time Complexity: O(n log n) — sorting both strings
# Space Complexity: O(n) — storing sorted copies of strings
