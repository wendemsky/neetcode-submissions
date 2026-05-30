class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # can't modify array
        # no extra space -> no set or map
        # O(n2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
        return -1