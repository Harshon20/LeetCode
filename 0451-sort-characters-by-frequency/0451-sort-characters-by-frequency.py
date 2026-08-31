class Solution:
    def frequencySort(self, s: str) -> str:
        freq=[0]*256

        for ch in s:
            freq[ord(ch)]+=1

        def get_sorted(ascii_code):
            return -freq[ascii_code]

        order = sorted(range(256),key=get_sorted)
        t=""
        for i in order:
            t+=chr(i)*freq[i]
        return t    
        