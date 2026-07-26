class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(0, n):
            prod = 1
            for j in range(0, n):
                if i==j:
                    continue
                else:
                    prod = prod * nums[j]

            ans.append(prod)
        return ans

        