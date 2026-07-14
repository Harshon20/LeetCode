class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)

        max_sum=nums[0]
        curr_sum=0

        for i in range(n):
            curr_sum+=nums[i]

            if max_sum<curr_sum:
                max_sum=curr_sum

            if curr_sum<0:
                curr_sum=0
        return max_sum            
        