class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        bucket = [[] for i in range(len(nums)+1)]
        for n, c in freq.items():
            bucket[c].append(n)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


        return res

            