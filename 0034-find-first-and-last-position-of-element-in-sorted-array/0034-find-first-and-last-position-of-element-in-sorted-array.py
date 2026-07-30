class Solution(object):
    def searchRange(self, nums, target):
        low,high=0,len(nums)-1
        start=-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                start=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        if start==-1:
            return (start,-1) 

        low,high=0,len(nums)-1
        end=-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                end=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return (start,end)        


        