class Solution(object):
    def possibleDays(self,weights,capacity):
        days=1
        currLoad=0
        for w in weights:
            if currLoad+w > capacity:
                days+=1
                currLoad=w
            else:
                currLoad+=w
        return days            
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)

        while low<high:
            mid=(low+high)//2

            if self.possibleDays(weights,mid)<=days:
                high=mid
            else:
                low=mid+1
        return low            

        