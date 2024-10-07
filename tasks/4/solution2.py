class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.lower()
        letters = ' '

        c = len(s) - 1

        foundWord = False
        wordLen = 0
        while c >= 0:
            if not foundWord:
                if s[c] not in letters:
                    foundWord = True
                    wordLen = 1
            else:
                if s[c] not in letters:
                    wordLen += 1
                else:
                    break
            c -= 1

        return wordLen


s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))