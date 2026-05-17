class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen = {}
        i = 0
        for s in strs:
            if str(sorted(s)) in seen:
                # print(seen)
                # print(seen[str(sorted(s))])
                ans[seen[str(sorted(s))]].append(s)
            else:
                ans.append([s])
                seen[str(sorted(s))] = i
                i += 1
        return ans