class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #if len(s)!=len(goal):
        #    return False
        #concatenate_s = s+s
        #return goal in concatenate_s    
        
        return len(s) == len(goal) and goal in s+s