from math import sqrt

class Solution(object):
    def judgeSquareSum(self, c):
        a = 0
        b = int(sqrt(c))

        while a <= b:
            s = a**2 + b **2
            if s == c:
                return True
            if s < c:
                a += 1
            else:
                b -= 1
        
        return False

class main():
    c = 5
    s = Solution()
    ans = s.judgeSquareSum(c)

    print(ans)