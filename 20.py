class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = {'(','{','['}
        mapping = {')':'(','}':'{',']':'['}
        # right = {')','}',']'}
        while len(s) > 0:
            curr = s[0]
            s = s[1:]
            if curr in left:
                stack.append(curr)
            else:
                if len(stack) == 0:
                    return False
                if mapping[curr] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
                    
        if len(stack) == 0:
            return True