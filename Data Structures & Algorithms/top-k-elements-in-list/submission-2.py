class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1
        ans =[]
        while k >0:
            max_freq=-1
            max_el = None
            for key in freq:
                if freq[key]>max_freq:
                    max_freq=freq[key]
                    max_el=key
            
            ans.append(max_el)
            del freq[max_el]
            k -=1
        return ans
                