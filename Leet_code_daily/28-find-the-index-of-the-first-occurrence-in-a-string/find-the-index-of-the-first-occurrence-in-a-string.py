class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1
        #another approach

        i = j = 0
        while i<len(haystack) and j<len(needle):
            if haystack[i]==needle[j]:
                i += 1
                j += 1
                if j == len(needle): 
                    return i-j
            else:
                i= i-j+1
                j=0
            
        return -1
            

        