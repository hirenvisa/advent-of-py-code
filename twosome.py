from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        
        for i in range(0, len(nums) - 1):
           j = i + 1
           for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:                    
                    return [i, j]
            

class Main():
    nums = [0] * 4
    nums[0] = [2, 7, 11, 15]
    nums[1] = [3, 2, 4]
    nums[2] = [3, 3]
    nums[3] = [3, 2, 3]
    target = [9,6,6,6]
    obj = Solution()
    for i in range(0, 4):
        print(obj.twoSum(nums[i], target[i]))
    