class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        started = False
        sign = 1
        output = 0

        for char in s:
            if not started:
                if char == " ":
                    continue
                started = True
                if char == "+":
                    continue
                if char == "-":
                    sign = -1
                    continue

            if '0' <= char <= '9':
                output = output * 10 + int(char)
            else:
                break
            
        output = sign * output
        if output < INT_MIN:
            return INT_MIN
        if output > INT_MAX:
            return INT_MAX
        
        return output



        