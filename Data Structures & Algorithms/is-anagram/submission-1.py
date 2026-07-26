class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict={}
        if len(s) != len(t):
            return False

        for w in s :
            if w in mydict:
                mydict[w]+=1
            else:
                mydict[w]=1
            
        for t in t:
            if t in mydict:
                mydict[t]-=1
            else:
                mydict[t]=1
        
        for el in mydict:
            if mydict[el]!=0:
                return False
            
        return True
        