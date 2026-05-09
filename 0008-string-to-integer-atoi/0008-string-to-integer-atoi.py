class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        if not s:
            return 0
        # Remove white spaces at first
        while i < n and s[i] == " ":
            i += 1
        if i == n:
            return 0
        #find the sign
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        res = 0
        while i < n and s[i].isdigit():
            res = res*10 + int(s[i])
            if res*sign >= INT_MAX:
                return INT_MAX
            if res*sign <= INT_MIN:
                return INT_MIN
            i += 1
        return sign*res

        
        