class Solution(object):
    def climbStairs(self, n):
        if n <= 1: return 1
        f = 1
        se = 1
        for _ in range(2, n + 1):
            t = f + se
            f, se = se, t

        return se


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(5))
