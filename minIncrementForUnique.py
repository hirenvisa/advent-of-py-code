class Solution(object):
    def minIncrementForUnique(self, nums):
        ans = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                d = nums[i-1] + 1                
                ans += d - nums[i]
                nums[i] = d
        return ans

class main():
    nums = [3,2,1,2,1,7]
    s = Solution()
    ans = s.minIncrementForUnique(nums)

    print (ans)