class Solution(object):
    def lengthOfLongestSubstring(self, s):
        y=max_length=0
        char_set=set()
    
        for x in range(len(s)):
            while s[x] in char_set:
                char_set.remove(s[y])
                y+=1

            char_set.add(s[x])
            max_length=max(max_length , x-y+1)
        
        return(max_length)
    #new try    