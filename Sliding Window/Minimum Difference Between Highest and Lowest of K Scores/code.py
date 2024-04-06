class Solution(object):
    def minimumDifference(self, nums, k):
        m=float('inf')
        if k==1:
            return 0
        nums.sort()
        for i in range(k,len(nums)+1):
            sub=nums[i-k:i]
            diff=abs(max(sub)-min(sub))
            print(diff)
            m=min(diff,m)
        return m
