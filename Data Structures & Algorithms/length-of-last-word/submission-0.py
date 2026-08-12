class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        aw = s.split()
        n = len(aw)-1
        return len(aw[n])
        