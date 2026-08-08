class Solution(object):
    def isDivisible(self,nums,divisor):
        total=0
        for num in nums:
            total+=(num+divisor-1)//divisor
        return total
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        ans=0

        while low<=high:
            mid=(low+high)//2
            if self.isDivisible(nums,mid)<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans            
        