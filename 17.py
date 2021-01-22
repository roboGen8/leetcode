class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = {2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z'] }
        out = [""]
        for digit in digits:
            new_out = []
            for val in mapping[int(digit)]:
                for prev in out:
                    new_out.append(prev+val)
                    
            out = new_out
            
        return out