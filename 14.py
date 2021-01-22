class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""
        out = ""
        shortest_length = 9999999999999999999999999
        for s in strs:
            shortest_length = min(shortest_length, len(s))
        for i in range(shortest_length):
            curr = strs[0][i]
            for strin in strs:
                if curr != strin[i]:
                    return out
                
            out += curr
            
        return out
            
            