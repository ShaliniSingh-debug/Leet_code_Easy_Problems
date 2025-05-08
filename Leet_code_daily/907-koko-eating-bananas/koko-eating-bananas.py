class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # check the hours devide by k banana eating from pile per hour 
        def k_works(k):
            hours = 0
            for p in piles:
                hours +=ceil(p/k)
            return hours<=h
        l =1
        r = max(piles) #the maximum value in pile is 11 

        while l<r:
            k = (l+r)//2
            
            if k_works(k): 
                r= k
            else:
                l = k+1
        return l


        

      

        