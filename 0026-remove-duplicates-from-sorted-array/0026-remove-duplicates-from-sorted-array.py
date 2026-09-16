class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = []

        nums.sort()

        for i in range(len(nums)):
            if nums[i] not in k:
                k.append(nums[i])

        nums[:] = k

        return len(k)