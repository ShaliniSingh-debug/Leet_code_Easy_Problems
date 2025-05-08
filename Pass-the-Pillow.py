class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        c = 2*(n-1)
        time %= c
        if time<n-1:
            return time+1
        return n-(time-(n-1))
            


        