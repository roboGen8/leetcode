class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        ()
        ()() , (())
        
        '''
        output = {"()"}
        
        while n > 1:
            temp = set()
            for comb in output:
                for i in range(len(comb)):
                    curr = comb[:i] + "()" + comb[i:]
                    temp.add(curr)
            output = temp
            temp = {}
            
            n -= 1
            
        out = []
        for x in output:
            out.append(x)
            
        return out