class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums)
        return not len(nums) == len(hashSet)