class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        count = 0
        for el in nums:
            if el == 1:
                count+=1
                m = max(count, m)
            elif el != 1:
                count = 0
        return m
        