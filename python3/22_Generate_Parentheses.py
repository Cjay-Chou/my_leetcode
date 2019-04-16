class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return ''
        result = ['()']
        for i in range(n-1):
            result = self.insert_plus(result)
            
        return result
    
    def insert_plus(self,list_pair):
        added_list = []
        for pairs in list_pair:
            for i in range(len(pairs)):
                if i == 0:
                    new_pair = '()'+pairs
                else:
                    new_pair = pairs[:i]+'()'+pairs[i:]
                    print(new_pair)
                    
                if new_pair not in added_list:
                    added_list.append(new_pair)
                    
        return added_list
                