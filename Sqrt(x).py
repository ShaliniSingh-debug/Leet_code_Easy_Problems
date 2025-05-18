class Solution:
    def mySqrt(self, x: int) -> int:

        if x<=1:
            return x
        # ans=0
        left ,right = 1,x//2 #create the pointers 
        while left<=right: #check if left pointer is less than right
            mid = (left+right) //2 # find the mid
            if floor(mid*mid)==x: #check mid into mid is equal to x
                return mid
            elif floor(mid*mid) <x: #agar nahi to left to bdhao
                left = mid+1
                # ans = mid
            elif floor(mid*mid)>x:
                right = mid - 1 # nahi to right ko badhao
        return right # right ko return kro kyuki right might be the perfect one

        
        


        