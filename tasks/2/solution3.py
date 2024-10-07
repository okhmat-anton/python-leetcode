class Solution(object):
    def maxProfit(self, prices):
        minimal = -1
        maximal = -1
        max_profit = 0
        for i in prices:
            if minimal == -1 or minimal > i:
                minimal = i
                maximal = -1
                continue
            if maximal < i:
                maximal = i

            current_profit = maximal - minimal
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit




s = Solution()

print(s.maxProfit([2,4,1]))
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))