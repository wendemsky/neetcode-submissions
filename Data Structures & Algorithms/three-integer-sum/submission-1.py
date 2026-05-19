class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums): 
            if i > 0 and n == nums[i-1]:
                continue
            if n <= 0:
                target = -n
                j, k = i+1, len(nums)-1
                while(j < k):
                    if nums[j] + nums[k] == target:
                        res.append([n, nums[j], nums[k]])
                        while(j < k and nums[j] == nums[j+1]):
                            j += 1
                        j += 1
                        while(j < k and nums[k] == nums[k-1]):
                            k -= 1
                        k -= 1
                    elif nums[j] + nums[k] > target:
                        k -= 1
                    else:
                        j += 1
        return res

            