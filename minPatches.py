class Solution(object):
    def minPatches(self, nums, n):
        x = 1
        i = ans = 0

        while x <= n:
            if i < len(nums) and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                ans +=1
                x <<=1
            
        return ans


        

class main():
    nums = [1,5,10]
    n = 20

    s = Solution()
    ans =  s.minPatches(nums, n)
    print(ans)