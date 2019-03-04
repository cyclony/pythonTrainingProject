class Solution:
    def twoSum(self, nums, target: int):
        nums_pos = [(x,i) for x,i in zip(nums, range(len(nums)))]
        i = 0
        x,xi = nums_pos[i]
        while i<len(nums_pos)-1:
            for y, yi in nums_pos[i+1:]:
                if (x+y) == target:
                    return [xi, yi]
            i += 1
            x, xi = nums_pos[i]

print(Solution().twoSum([2,7], 9))