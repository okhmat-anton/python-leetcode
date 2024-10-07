class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


s = Solution()
print(s.majorityElement([6,5,5]))
print(s.majorityElement([3,3,4]))
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))
