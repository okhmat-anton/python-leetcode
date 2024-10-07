class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]

        return profit




s = Solution()

print(s.maxProfit([1,2,3,4,5]))
# print(s.maxProfit([7,1,5,3,6,4]))