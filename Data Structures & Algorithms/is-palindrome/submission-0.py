class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphanumeric characters
        an_s = ""
        for i in range(len(s)):
            if s[i].isalnum():
                an_s += s[i]
        an_s = an_s.lower()
        return an_s == an_s[::-1]