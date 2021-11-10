class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        for i in range(len(s)):
            #odd strning length case
            l,r=i,i
            while l>=0 and r< len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res =s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            #even String length case
            l,r=i,i+1 #r starts at the 0+1 position thus handing the case where the palindrom is even such as abbc result equals bb 
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) >resLen:
                    res =s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res
