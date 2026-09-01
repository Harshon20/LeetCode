class Solution:
    def maxDepth(self, s: str) -> int:
        n=len(s)
        count=0
        max_count=0
        for i in range(n):
            if s[i]=="(":
                count+=1
                max_count=max(max_count,count)
            elif s[i]==")":
                count-=1
        return max_count            
        