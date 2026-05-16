class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i, j = 0, len(nums)-1
        while i<j:
            if sorted_nums[i] + sorted_nums[j] == target:
                break
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            else:
                j -= 1
        if (sorted_nums[i] != sorted_nums[j]):
            i, j = nums.index(sorted_nums[i]), nums.index(sorted_nums[j])
        else:
            i = nums.index(sorted_nums[i]) 
            j = nums.index(sorted_nums[j], i + 1)
        return sorted([i, j])
        