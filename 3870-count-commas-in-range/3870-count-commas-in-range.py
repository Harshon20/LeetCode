class Solution:
    def countCommas(self, n: int) -> int:
        count = n - 999
        commacount = max(count,0)
        return commacount
        