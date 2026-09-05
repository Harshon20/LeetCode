class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)            
        if n<2:
            return s

        start=0
        end=0

        for i in range(n):
            left1,right1=i,i

            while left1>=0 and right1<n and s[left1]==s[right1]:
                left1-=1
                right1+=1

            left2,right2=i,i+1

            while left2>=0 and right2<n and s[left2]==s[right2]:
                left2-=1
                right2+=1

            if right1-left1>end-start:
                start=left1+1
                end=right1
            if right2-left2>end-start:
                start=left2+1
                end=right2
        return s[start:end]                        