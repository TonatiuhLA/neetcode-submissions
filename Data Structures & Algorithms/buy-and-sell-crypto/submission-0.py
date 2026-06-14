class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0

        for i in range(0, len(prices)):
            print(i)
            for j in range(0, i):
                diff = prices[i] - prices[j]
                if diff > max:
                    max = diff
        
        return max