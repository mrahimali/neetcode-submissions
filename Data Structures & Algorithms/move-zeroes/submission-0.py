class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        mid = 0
        n = len(nums)
        while mid<n:
            if nums[mid]==0:
                mid+=1
            else:
                nums[left], nums[mid]=nums[mid], nums[left]
                left +=1
                mid +=1
        