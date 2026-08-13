class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0 
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        while i< n1 and j<n2:
            if nums1[i]<nums2[j]:
                ans.append(nums1[i])
                i+=1
            elif nums2[j]<nums1[i]:
                ans.append(nums2[j])
                j+=1
            else:
                ans.append(nums1[i])
                ans.append(nums2[j])
                i+=1
                j+=1
        
        ans.extend(nums1[i:])
        ans.extend(nums2[j:])

        n = len(ans)
        median = 0
        if (n % 2) ==0:
            median = (ans[(n//2)-1]+ans[(n//2)])/2
        else:
            median = ans[(n)//2]
        return median

        