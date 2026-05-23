class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEatingRate = max(piles)
        print("maxEatingRate: ", maxEatingRate)
        eatingRate = -1
        l, r = 1, maxEatingRate
        while l <= r:
            mid = (l + r) // 2
            print("mid: ", mid)
            print(sum(math.ceil(bananas / mid) for bananas in piles))
            if sum(math.ceil(bananas / mid) for bananas in piles) <= h:
                eatingRate = mid
                r = mid - 1
            else: 
                l = mid + 1

        return eatingRate