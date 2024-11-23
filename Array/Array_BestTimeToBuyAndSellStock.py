# Best Time to Buy and Sell Stock

# Brute Force
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profits = []
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[j] - prices[i] > 0:
#                     profits.append(prices[j] - prices[i])
#         if profits == []:
#              return 0
#         return max(profits)

# Optimized
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        minPrice = float('inf')
        maxProfitVal = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfitVal = max(maxProfitVal, price - minPrice)
        return maxProfitVal
    
# Time Complexity: 𝑂(𝑛) because we traverse the list once.
# Space Complexity: 𝑂(1) since no additional space proportional to input size is used.



