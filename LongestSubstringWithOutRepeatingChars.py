class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        Charset= set()
        Left =0 
        res = 0
        for r in range(len(s)):
            while s[r] in Charset:
                Charset.remove(s[Left])
                Left += 1
            Charset.add(s[r])
            res = max(res, r-Left+1)
        return res
        
  
