class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = ""
        for ch in s:
            if ch.isalnum():
                st += ch
        orgst = st
        st = list(st)
        left = 0
        right = len(st) - 1
        while left < right:
            st[left], st[right] = st[right], st[left]
            left += 1
            right -= 1
        return "".join(st) == orgst