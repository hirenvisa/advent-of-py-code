class Solution(object):
    def heightChecker(self, heights):
        h = heights.copy()
        h.sort()

        ans = 0;
        for i in range(len(heights)):
            if h[i] != heights[i]: 
                ans += 1
        
        return ans
        

class main():
    heights = [1,1,4,2,1,3]
    s = Solution()

    ans = s.heightChecker(heights)
    print(ans)