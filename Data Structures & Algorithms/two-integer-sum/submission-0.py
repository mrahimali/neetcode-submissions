class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, n in enumerate(nums):
            dif = target-n
            if dif in mydict:
                return [mydict[dif],i]
            else:
                mydict[n]=i  
        