class Solution:
    def isValid(self, s: str) -> bool:
        char_list = []
        pair = {'{':'}','(':')','[':']'}
        for num in range(len(s)):
            if s[num] in pair:
                char_list.append(s[num])
            elif char_list and s[num] == pair[char_list[-1]]:
                char_list.pop()
            else:
                return False
        if not char_list:
            return True
        else:
            return False