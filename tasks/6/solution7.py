# import cProfile
class Solution(object):
    def summaryRanges(self, nums):
        res = []

        if not nums:
            return res

        if len(nums) == 1:
            return [str(nums[0])]

        start = nums[0]
        lenNums = len(nums)
        for i in range(1, lenNums):
            if nums[i] - nums[i-1] != 1:
                if start == nums[i-1]:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(nums[i-1]))
                start = nums[i]

            if i == lenNums - 1:
                if start == nums[i]:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(nums[i]))

        return res


s = Solution()
# print('')
# print('---------------')
# cProfile.run(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
# print(s.summaryRanges([-1]))  # ["-1]
# print('---------------')
# print(s.summaryRanges([0, 1, 2, 4, 5, 7]))  # ["0->2","4->5","7"]
# print('---------------')
print(s.summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # ["0","2->4","6","8->9"]
# print('---------------')
