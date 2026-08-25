class Solution:
    def largestOddNumber(self, num: str) -> str:
        i=len(num)-1
        ind=-1
        
        while i>=0:
            if int(num[i])%2==1:
                ind=i
                break
            i-=1
        i=0    
        if num[0]=="0":
            i=1
        return num[i:ind+1]            
        