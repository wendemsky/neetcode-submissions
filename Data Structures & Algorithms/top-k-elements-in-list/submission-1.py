class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        sorted_map = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for key, value in sorted_map[:k]:
            ans.append(key)
        return ans

            