class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first = 0
        second = 0
        ans =''
        n1 = len(word1)
        n2 = len(word2)
        while first <n1  or second<n2:
            if first >=n1:
                ans = ans + word2[second:n2]
                return ans
            if second >= n2:
                ans = ans + word1[first:n1]
                return ans
            ans = ans + word1[first]+word2[second]
            first +=1
            second +=1

        return ans
            