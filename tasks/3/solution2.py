class Solution(object):
    def removeDuplicates(self, nums):
        wi = 2
        for i in range(2, len(nums)):
            if nums[wi - 1] != nums[i] or (nums[wi - 1] == nums[i] and nums[wi - 2] != nums[wi - 1]):
                nums[wi] = nums[i]
                wi += 1
        for i in range(wi, len(nums)):
            nums[i] = '_'
        print(nums)
        return wi


s = Solution()
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))

