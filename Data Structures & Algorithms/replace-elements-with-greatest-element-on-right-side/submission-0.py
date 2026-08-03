class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(0, n):
            greatest = float('-inf')
            for j in range(i+1, n):
                if arr[j]>greatest:
                    greatest = arr[j]
            arr[i] = greatest

        arr[n - 1] = -1
        return arr
        