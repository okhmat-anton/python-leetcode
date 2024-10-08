class Solution(object):
    def romanToInt(self, s):
        result = 0
        c = len(s) - 1
        letters = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        while c >= 0:
            if s[c] in letters:
                result += letters[s[c]]
                while c > 0 and s[c] in letters and letters[s[c]] > letters[s[c-1]]:
                    result -= letters[s[c-1]]
                    c -= 1
            c -= 1
        return result


s = Solution()
print(s.romanToInt("III"))  # 3
print('---------------')
print(s.romanToInt("LVIII"))  # 58
print('---------------')
print(s.romanToInt("MCMXCIV"))  # 1994
