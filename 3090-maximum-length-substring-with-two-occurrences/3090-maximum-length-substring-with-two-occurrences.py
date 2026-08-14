class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        count={}
        j=0
        ans=0

        for i in range(n):
            ch=s[i]
            count[ch] = count.get(ch,0)+1
            while count[ch]>2:
                count[s[j]]-=1
                j+=1
            ans=max(ans,i-j+1)
        return ans        