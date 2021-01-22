class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            out = ""
            for c in s:
                out += c
            return out
        output = []
        for i in range(numRows):
            output.append([])
            
        # print(output)
        for i, c in enumerate(s):
            # print(i, c)
            # print(numRows)
            curr_index = i % (numRows * 2 - 2)
            if curr_index >= numRows:
                curr_index = numRows - (curr_index % numRows) - 2
                # 4 - 4 - 2  == 2
            output[curr_index].append(c)
            
        final_output = ""
        for arr in output:
            for c in arr:
                final_output += c
        return final_output