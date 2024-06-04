class Solution(object):
    def longestPalindrome(self, s):
        lst = [None] * 123

        for i in range(0,len(s)):
            if lst[ord(s[i])] == None:
                lst[ord(s[i])] = 1
            else:               
                lst[ord(s[i])] += 1

        ans = 0
        for j in range(65, 123):
            if lst[j] is not None:
                print(f"{j} {chr(j)} ==> {lst[j]}")
                ans += lst[j] // 2 * 2
        
        if ans < len(s):
            ans += 1
            

        return ans

    

class main():
    s = Solution()
    print(s.longestPalindrome("zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"))
