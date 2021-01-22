class Solution:
    def myAtoi(self, s: str) -> int:
        output = 0
        lead_white = True
        sign_reveal = False
        num_reveal = False
        i = 0
        sign = 1
        num_set = set()
        for j in range(10):
            num_set.add(str(j))
        print(num_set)
        # print(num_set)
        while i < len(s):
            print(s[i], i)
            # print('helolo')
            if s[i] == '-' or s[i] == '+':
                if num_reveal:
                    break
                if sign_reveal:
                    break
                lead_white = False
                if s[i] == '-':
                    sign *= -1
                # sign = -1 if s[i] == '-' else 1
                i += 1
                sign_reveal = True
                continue

            
            if s[i] in num_set:
                num_reveal = True
                lead_white = False
                # print('helolo')
                if not (output == 0 and s[i] == '0'):
                    print(output)
                    output = 10 * output + int(s[i])
                    # print('helolo')
                
                
            else:
                if not (s[i] == ' ' and lead_white): 
                    break
            i += 1
        
                    
        output *= sign
        # print(output)
        if output < -1 * 2 ** 31:
            output = -1 * 2 ** 31
        if output > 2 ** 31 - 1:
            output = 2 ** 31 - 1
        return output
                
                