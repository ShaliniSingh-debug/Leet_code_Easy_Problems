class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split()[-1]) space = O(n) time = O(n)

        # second approach

        # first calculate the length of the string
        i = len(s)-1
       

        # now check fron last to first until you get first " " this after a word
        while i >= 0 and s[i] == ' ':
            i -=1
        char_count =0 
        # now have to count the words char until you find first  " "
        while i >= 0 and s[i] != ' ':
            char_count +=1
            i -=1
        return char_count 
       
        