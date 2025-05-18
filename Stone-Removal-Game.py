class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones=10
        count=0
        while n>=stones:
            n -=stones
            stones -=1
            count +=1
        return count%2==1
            
        