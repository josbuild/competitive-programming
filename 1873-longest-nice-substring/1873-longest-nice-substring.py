class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_length = 0
        start  = 0
        for i in range(len(s)):
            seen = set()
            miss = 0
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    if (s[j].lower() not in seen or s[j].upper() not in seen):
                        miss += 1
                    else:
                        miss -= 1
                if miss == 0 and (j - i + 1) > max_length:
                    max_length = j - i + 1
                    start = i
        return s[start: start + max_length]
        