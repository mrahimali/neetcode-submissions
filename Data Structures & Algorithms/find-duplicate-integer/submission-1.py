class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mydict = {}
        for i in range(len(nums)) :
            if nums[i] in mydict:
                return nums[i]
            else:
                mydict[nums[i]] = i 
        