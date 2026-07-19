class Solution(object):
    def subarraySum(self, nums, k):
        n=len(nums)
        count=0
        pre_sum=0
        sum_freq={0:1}

        for num in nums:
            pre_sum+=num
            target=pre_sum-k

            if target in sum_freq:
                count+=sum_freq[target]
            if pre_sum in sum_freq:
                sum_freq[pre_sum]+=1
            else:
                sum_freq[pre_sum]=1
        return count                