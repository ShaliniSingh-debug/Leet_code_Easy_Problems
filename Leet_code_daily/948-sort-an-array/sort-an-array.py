class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        n=len(nums)
        new_list=[0]*len(nums)
        for i in range(n):
            minn=heapq.heappop(nums)
            new_list[i]=minn
        return new_list
        
            
