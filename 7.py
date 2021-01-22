class Solution:
    def reverse(self, x: int) -> int:
        if x < -1 * 2**31 or x > 2**31 + 1:
            return 0
        sign = -1 if x < 0 else 1
        # print(sign)
        x = abs(x)
        output = 0
        while x > 0:
            curr = x % 10
            x = int(x / 10)
            output = output * 10 + curr
        output *= sign
        if output < -1 * 2**31 or output > 2**31 + 1:
            return 0
        return output