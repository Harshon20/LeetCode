class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)
        count=0
        longest=1
        st=set()

        if n==0:
            return 0

        for num in nums:
            st.add(num)

        for lt in st:
            if lt-1 not in st:
                count=1
                x=lt

                while x+1 in st:
                    count+=1

                    x=x+1
                longest=max(longest,count)
        return longest

        