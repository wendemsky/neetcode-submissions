class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        charMap1 = defaultdict(int)
        charMap2 = defaultdict(int)
        for i in range(len(s1)):
            charMap1[s1[i]] += 1
            charMap2[s2[i]] += 1
        if charMap1 == charMap2:
            return True
        i = 0
        for j in range(len(s1), len(s2)):
            charMap2[s2[j]] += 1
            charMap2[s2[i]] -= 1
            if charMap2[s2[i]] <= 0:
                charMap2.pop(s2[i])
            if charMap1 == charMap2:
                return True
            i += 1
        return False
            
