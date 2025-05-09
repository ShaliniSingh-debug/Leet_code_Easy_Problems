class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=0
        n=len(nums)
# here first we will run through k where k is 4 
        for i in range(k):
            max_sum +=nums[i]
# we will get the avg of the sum 

        max_avg= max_sum / k

# we have to check from k to n so we will run the loop from k to till len of list
        for i in range(k,n):
# since we are add i value means coming next value and our len should be fixed =4= k so we will minus the k from i tokeep the fixed len 4
            max_sum += nums[i]
            max_sum -= nums[i-k]
            avg = max_sum / k # get avg
            max_avg = max(max_avg,avg) # comparing the max
        return max_avg # returning the max
    
    
        