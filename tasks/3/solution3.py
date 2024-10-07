class Solution(object):
    def removeElement(self, nums, val):
        wi = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[wi] = nums[i]
                wi += 1
        return wi


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
