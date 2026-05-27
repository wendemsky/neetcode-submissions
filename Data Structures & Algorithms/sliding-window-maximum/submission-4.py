class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k 
        hashMap = {}
        res = []
        for i in range(l, r):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        print(hashMap)
        res.append(max(hashMap.keys()))
        print(res)
        for i in range(r, len(nums)):
            # remove from beg
            if hashMap[nums[l]]:
                hashMap[nums[l]] -= 1
            if hashMap[nums[l]] == 0:
                hashMap.pop(nums[l])
            
            # add from end
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)

            res.append(max(hashMap.keys()))
            l += 1
        return res