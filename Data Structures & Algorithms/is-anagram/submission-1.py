class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted([char for char in s])
        list_t = sorted([char for char in t])
        return list_s == list_t