# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        def findthPeak():
            left = 0
            right = mountainArr.length() - 1
            while left<right:
                mid = (left+right)//2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left =  mid+1
                else:
                    right= mid
            return left
            
        def peakSearch(left,right, target, ascending=True):
            while left<=right:
                mid = (left+right)//2
                val = mountainArr.get(mid)
                if val==target:
                    return mid
                if ascending:
                    if val<target:
                        left = mid+1
                    else:
                        right = mid-1
                else:
                    if val>target:
                        left = mid+1
                    else:
                        right = mid-1
            return -1

        peak = findthPeak()
        result = peakSearch(0, peak, target, ascending=True)
        if result !=-1:
            return result
        return peakSearch(peak+1, mountainArr.length() - 1, target, ascending=False)


        