class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #heapsort sollution
        # heapq.heapify(nums)
        # n=len(nums)
        # new_list=[0]*len(nums)
        # for i in range(n):
        #     minn=heapq.heappop(nums)
        #     new_list[i]=minn
        # return new_list


    # merge sort sollution
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return merge_sort(nums)