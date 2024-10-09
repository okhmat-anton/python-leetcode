class Solution(object):
    def strStr(self, haystack, needle):
        position = -1
        haystackLen = len(haystack)
        needleLen = len(needle)

        if haystackLen < needleLen:
            return -1

        if needleLen == haystackLen:
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(haystackLen-needleLen+1):
            for j in range(needleLen):
                if haystack[i+j] != needle[j]:
                    break
                else:
                    if j == needleLen - 1:
                        position = i
                        return position

        return position

s = Solution()
print(s.strStr('mississippi','issipi'))  # -1
print('---------------')
print(s.strStr('aaa','aaaa'))  # -1
print('---------------')
print(s.strStr('sadbutsad','sad'))  # 0
print('---------------')
print(s.strStr('leetcode','leeto'))  # -1
print('---------------')
print(s.strStr('aaanton','anton'))  # 2
