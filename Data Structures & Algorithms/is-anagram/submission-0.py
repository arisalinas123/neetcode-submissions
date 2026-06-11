class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        for i in s:
            count1[i] = count1.get(i,0) + 1 
        count2 = {}
        for c in t:
            count2[c] = count2.get(c,0) + 1
        if count1 == count2:
            return True
        else: 
            return False
