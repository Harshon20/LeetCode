class Solution(object):
    def findKthPositive(self, arr, k):
        low=0
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]-(mid+1)>=k:
                high=mid-1
            else:
                low=mid+1
        return high+k+1            
        