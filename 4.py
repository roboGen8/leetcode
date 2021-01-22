class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        left = 0
        mapping = dict()
        for i in range(len(s)):
            print(s[left:i+1])
            if s[i] in mapping and left <= mapping[s[i]]:
                left = mapping[s[i]] + 1
            else:
                output = max(output, i - left + 1)
            mapping[s[i]] = i
        return output