class Solution:
    def permute(self, nums):
        result = []
        if nums == None: return result
        if len(nums) == 0: return result
        if len(nums) == 1:
            result.append(nums)
            return result
        a = nums[:1]
        for perm in self.permute(nums[1:]):
            result += [perm[:i] + a + perm[i:] for i in range(len(perm)+1)]
        return result

    def permuteUnique(self, nums):
        result = self.permute(nums)
        s = {tuple(x) for x in result} # 先把unhashable的list转化为hashable的tuple，从而可以用set去除重复的list
        return [list(x) for x in s]


nums = [1,2,3,4]
result = Solution().permute(nums)
print(len(result))
print(Solution().permute(nums))

num = [1,1,3]
print(Solution().permuteUnique(num))
