class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        n = len(details)
        i = 0
        while i < n:
            if int(details[i][11:13])>60:
                count+=1
            i+=1
        return count