class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        for length in range(n,0,-1):
            for start in range(n-length+1):
                sub = s[start:start+length]
                if sub == sub[::-1]:
                    return sub
        return ''            
        