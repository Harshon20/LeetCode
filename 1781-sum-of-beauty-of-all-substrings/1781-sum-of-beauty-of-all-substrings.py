class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        total=0

        for i in range(n):
            freq={}

            for j in range(i,n):
                freq[s[j]] = freq.get(s[j],0)+1

                value = freq.values()

                max_value = max(value)
                min_value = min(value)

                total+=(max_value - min_value)
        return total        
        