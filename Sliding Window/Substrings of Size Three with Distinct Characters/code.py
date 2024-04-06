class Solution(object):
    def countGoodSubstrings(self, s):
        count=0
        for i in range(3,len(s)+1):
            sub=s[i-3:i]
            se=set(sub)
            if len(se)==3:
                
                count+=1
        return count
