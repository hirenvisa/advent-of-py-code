class Solution(object):
    def sortColors(self, nums):
        
        n = len(nums)
        for i in range(0, n):
            j = i+1
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    self.swap(nums, i , j)
                    break
        return nums

    def swap(self, nums, i ,j):
        m = j
        for m in range(j, 0, -1):
            if nums[m] < nums[m-1]:
                a = nums[m-1]
                nums[m-1] = nums[m]
                nums[m] = a
            else:
                break 

    def sortColorUsingFrequncy(self, nums):
        freq = [0] * 3
        for i in nums:
            freq[i] += 1
        
        ans = []
        for j in range(0, len(freq)):
            for m in range(0, freq[j]):
                ans.append(j)

        return ans 

class main():
    nums = [2,0,2,1,1,0]
    s = Solution()
    ans = s.sortColorUsingFrequncy(nums)
    print(ans)