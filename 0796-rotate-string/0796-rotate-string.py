class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        concatenate_s = s+s
        return goal in concatenate_s    
        