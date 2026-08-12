class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)-1
        i = 0
        j = 1
        sm = 0
        while j<=n:
            asci_value = ord(s[j]) - ord(s[i])
            if asci_value<0:
                asci_value *=-1
            sm = sm + asci_value
            i+=1
            j+=1
        return sm
