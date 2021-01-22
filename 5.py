class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        naive solution: O(n^2) choose each pivot then move outward
        '''
        out_left = 0
        out_right = 0
        # out_length = 0
        for i in range(2*(len(s)-1)):
            if i % 2 == 1:
                left = int(i / 2)
                right = int(i / 2) + 1
            else:
                left = int(i / 2)
                right = int(i / 2)

            if s[left] != s[right]:
                continue
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
                
                left -= 1
                right += 1
                
            if right - left + 1 > out_right - out_left + 1:
                out_left = left
                out_right = right
                
        return s[out_left:out_right + 1]