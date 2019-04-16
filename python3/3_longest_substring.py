class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = {}
        front = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]]=i
            else:
                for char in list(temp.keys()):
                    if temp[char] < temp[s[i]]:
                        del temp[char]
                front = temp[s[i]]+1
                temp[s[i]]=i
                
            if max_length< (i-front+1):
                max_length = (i-front+1)
        return max_length
                