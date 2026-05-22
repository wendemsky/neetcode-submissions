class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionMap = {}
        for i, pos in enumerate(position):
            positionMap[pos] = i
        sortedPositionMap = dict(sorted(positionMap.items()))
        time = []
        for pos, i in sortedPositionMap.items():
            time.append(float((target - pos) / speed[i]))
        fleets = 1
        stack = []
        for t in time[::-1]:
            if stack and t > stack[-1]:
                fleets += 1
                stack.append(t)
            else: 
                if not stack:
                    stack.append(t)
                    
        return fleets