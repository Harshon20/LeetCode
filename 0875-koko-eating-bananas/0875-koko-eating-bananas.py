class Solution(object):
    def countTotalHours(self,piles,speed):
        total_hour=0
        for banana in piles:
            total_hour+=(banana+speed-1)//speed
        return total_hour    
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        ans=max(piles)

        while low<=high:
            mid=(low+high)//2
            total_hour=self.countTotalHours(piles,mid)

            if total_hour<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans            
        
        