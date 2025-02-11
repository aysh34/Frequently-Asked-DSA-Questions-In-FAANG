class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        num = 0
        res = 0
        sign = 1 # for +ve
        st = []

        for i in range(n):
            # i could either be a digit or + or - or ( or )
            if s[i].isdigit():
                num = num * 10 + int(s[i]) #  form a multi-digit number

            elif s[i] == '+': # no has formed already
                res += (sign*num)
                num = 0
                sign = 1
            elif s[i] == '-':
                res += (sign*num)
                num = 0
                sign = -1

            elif s[i] == '(':
                # bracket k andar new res aye ga so phele wala stack mei store krlo
                st.append(res)
                st.append(sign)
                res = 0
                num = 0
                sign = 1
            elif s[i] == ')': 
                res += num*sign # res inside bracket
                num = 0
                st_sign = st.pop()
                last_res = st.pop()
                res *= st_sign
                res += last_res

        res += (num*sign)
        return res