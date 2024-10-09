class Solution(object):
    def reverseWords(self, s):

        return ' '.join(reversed(s.split()))

        # c = len(s) - 1
        # result = ''
        # currentWord = ''
        #
        # while c >= 0:
        #     if s[c] != ' ':
        #         currentWord = s[c] + currentWord
        #     else:
        #         if currentWord != '':
        #             if result == '':
        #                 result = currentWord
        #             else:
        #                 result += ' ' + currentWord
        #             currentWord = ''
        #     c -= 1
        #
        # if currentWord != '':
        #     if result == '':
        #         result = currentWord
        #     else:
        #         result += ' ' + currentWord
        #
        # return result


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
