class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_str=Counter(s)
        t_str=Counter(t)
        for char in t_str:
            if t_str[char] > s_str[char]:
                return char
            
                
        

        