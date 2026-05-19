class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphanumeric characters and check reverse
        # an_s = ""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         an_s += s[i]
        # an_s = an_s.lower()
        # return an_s == an_s[::-1]

        # two pointer
        i, j = 0, len(s)-1
        while(i<j):
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif s[i].isalnum() and not s[j].isalnum():
                j -= 1
            elif not s[i].isalnum() and s[j].isalnum():
                i += 1
            else:
                i += 1
                j -= 1
        return True