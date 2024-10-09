class Solution(object):

    def intToRoman(self, num):
        result = ''
        while num > 0:
            if num >= 1000:
                result += 'M'
                num -= 1000
                continue
            if 1000 > num >= 900:
                result += 'CM'
                num -= 900
                continue
            if 900 > num >= 500:
                result += 'D'
                num -= 500
                continue
            if 500 > num >= 400:
                result += 'CD'
                num -= 400
                continue
            if 400 > num >= 100:
                result += 'C'
                num -= 100
                continue
            if 100 > num >= 90:
                result += 'XC'
                num -= 90
                continue
            if 90 > num >= 50:
                result += 'L'
                num -= 50
                continue
            if 50 > num >= 40:
                result += 'XL'
                num -= 40
                continue
            if 40 > num >= 10:
                result += 'X'
                num -= 10
                continue
            if 10 > num >= 9:
                result += 'IX'
                num -= 9
                continue
            if 9 > num >= 5:
                result += 'V'
                num -= 5
                continue
            if 5 > num >= 4:
                result += 'IV'
                num -= 4
                continue
            if 4 > num >= 1:
                result += 'I'
                num -= 1
                continue

        return result


    def intToRoman2(self, num):
        val_to_sym = [
            (1000, 'M'),
            (900,  'CM'),
            (500,  'D'),
            (400,  'CD'),
            (100,  'C'),
            (90,   'XC'),
            (50,   'L'),
            (40,   'XL'),
            (10,   'X'),
            (9,    'IX'),
            (5,    'V'),
            (4,    'IV'),
            (1,    'I')
        ]

        result = ''
        for value, symbol in val_to_sym:
            count = num // value
            result += symbol * count
            num -= value * count

        return result

s = Solution()
print(s.intToRoman2(3))  # III
print('---------------')
print(s.intToRoman2(3749))  # MMMDCCXLIX
print('---------------')
print(s.intToRoman2(1994))  # MCMXCIV
