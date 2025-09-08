class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) ==1 and len(word2)==1:
            return word1+word2
        leftpt=0 
        rightpt=0
        output=""
        while leftpt<len(word1) or rightpt<len(word2):
            if leftpt<len(word1):
                output +=word1[leftpt]
                leftpt += 1
            if rightpt<len(word2):
                output += word2[rightpt]
                rightpt +=1
        return output
