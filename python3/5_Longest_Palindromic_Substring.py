class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        max_length = 0
        result = s
        for i in range(len(s)-1):
            if s[i+1] == s[i]:
                temp_str = self.get_maxsubstr(s,i,i+1)
                if len(temp_str) > max_length:
                    result = temp_str
                    max_length = len(temp_str)
                    
            temp_str = self.get_maxsubstr(s,i,i)
            if len(temp_str) > max_length:
                result = temp_str
                max_length = len(temp_str)
        return "".join(result)
                    
    def get_maxsubstr(self,s,i,j):
        substr = []
        while i>=0 and j < len(s):
            if i == j:
                substr.append(s[i])
            elif s[i] == s[j]:
                substr.insert(0,s[i])
                substr.append(s[j])
            else:
                return substr
            i-=1
            j+=1
        return substr