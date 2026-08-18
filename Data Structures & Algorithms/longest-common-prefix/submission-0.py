class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = len(strs)
        n1 = len(strs[0])
        i = 0
        st = ""

        while i < n1:
            st = st + strs[0][i]

            for j in range(1, n):
                if i >= len(strs[j]) or strs[j][i] != st[i]:
                    return st[:-1]

            i += 1

        return st
        