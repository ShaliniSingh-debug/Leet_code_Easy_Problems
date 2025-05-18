class Solution:
    def trap(self, height: List[int]) -> int:
        l_max=0
        r_max=0
        total =0
        l=0
        r=len(height)-1
        while l<r:
            if height[l]<=height[r]:
                l_max = max(l_max,height[l])
                if height[l]<l_max:
                    total +=(l_max-height[l])
                else:
                    l_max = height[l]
                l +=1
            else:
                r_max = max(r_max,height[r])
                if height[r]<r_max:
                    total += (r_max-height[r])
                else:
                    r_max = height[r]
                r -=1
        return total


                
        