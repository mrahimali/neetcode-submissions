class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curEl = -1
        n = len(nums)

        for el in nums:
            if count == 0:
                curEl = el
                count =1
            elif el == curEl:
                count +=1
            else:
                count -=1
        count = 0
        for el in nums:
            if el == curEl :
                count+=1

        if count >= (n//2):
            return curEl
        return -1

        