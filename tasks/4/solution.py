class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        letters = 'zxcvbnmasdfghjklqwertyuiop1234567890'

        end = len(s) - 1
        start = 0

        while start < end:
            while s[start] not in letters and start < end:
                start += 1
            currentFront = s[start]

            while s[end] not in letters and end > start:
                end -= 1
            currentEnd = s[end]

            if currentFront != currentEnd:
                return False
            start += 1
            end -= 1

        return True


s = Solution()
print(s.isPalindrome(".,"))
# print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome("race a car"))
# print(s.isPalindrome(" "))
