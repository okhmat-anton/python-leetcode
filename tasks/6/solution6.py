class Solution(object):
    def isSubsequence(self, s, t):
        c1 = len(s)
        current = 0

        if s == '':
            return True

        for letter in t:
            if letter == s[current]:
                current += 1
            if current == c1:
                return True
        return False


s = Solution()
print('')
print('---------------')
print(s.isSubsequence('', 'ahbgdc'))
print('---------------')
print(s.isSubsequence('abc', 'ahbgdc'))
print('---------------')
print(s.isSubsequence('axc', 'ahbgdc'))
print('---------------')
