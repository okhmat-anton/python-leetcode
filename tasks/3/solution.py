class Solution(object):
    def removeDuplicates(self, nums):
        # c = len(nums) - 1
        # while c > 0:
        #     if nums[c] == nums[c-1]:
        #         nums.pop(c)
        #     c -= 1
        # return len(nums)
        wi = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[wi] = nums[i]
                wi += 1
        return wi


s = Solution()
# print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))