class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countr = 0
        countw = 0
        countb = 0
        n = len(nums)
        for el in nums:
            if el == 0:
                countr += 1
            elif el == 1:
                countw += 1
            else:
                countb += 1
        
        for i in range(0, countr):
            nums[i] = 0
        
        for i in range(countr, countr+countw):
            nums[i]=1
        for i in range(countr+countw, countr+countw+countb):
            nums[i]=2