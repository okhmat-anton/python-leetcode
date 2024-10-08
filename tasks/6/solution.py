class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        map = {}

        for letter in ransomNote:
            if letter in map:
                map[letter] += 1
            else:
                map[letter] = 1

        for letter in magazine:
            if letter in map:
                map[letter] -= 1
                if map[letter] == 0:
                    map.pop(letter)
                    if map == {}:
                        return True

        res = 0
        for m in map.values():
            res += m

        if res > 0:
            return False
        else:
            return True


s = Solution()
print(s.canConstruct('a','b'))
print(s.canConstruct('aa','ab'))
print(s.canConstruct('aa','aab'))