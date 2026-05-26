class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = defaultdict(int)
        charMap[s[0]] += 1
        replacements = 0
        i = 0
        res = 1
        for j in range(1, len(s)):
            charMap[s[j]] += 1
            maxFreq = max(charMap.values())
            lenSubstr = j - i + 1
            replacements = lenSubstr - maxFreq # Len of substr - max frequency in map
            if replacements <= k:
                res = max(res, lenSubstr)
            else:
                charMap[s[i]] -= 1
                i += 1
        return res
            

