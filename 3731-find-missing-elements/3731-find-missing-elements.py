class Solution(object):
    def findMissingElements(self, nums):
        s=set(nums)
        minimum=min(nums)
        maximum=max(nums)

        ans=[]

        for i in range(minimum+1,maximum):
            if i not in s:
                ans.append(i)
        return ans        
        