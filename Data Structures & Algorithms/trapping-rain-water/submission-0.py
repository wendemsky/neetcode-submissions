class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxLeft = 0
        maxRight = 0
        l, r = 0, len(height)-1
        i = 0
        while(l < r):
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            if height[l] < height[r]:
                l += 1
                if maxLeft - height[l] > 0:
                    res += maxLeft - height[l]
            else:
                r -= 1
                if maxRight - height[r] > 0:
                    res += maxRight - height[r]
        return res
            

