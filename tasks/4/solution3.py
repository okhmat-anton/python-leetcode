class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ''
        end = False
        letterID = 0
        try:
            while not end:
                currentLetter = strs[0][letterID]
                for i in range(1, len(strs)):
                    if currentLetter != strs[i][letterID]:
                        return prefix
                prefix += currentLetter
                letterID += 1
        except:
            return prefix

        return prefix


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))