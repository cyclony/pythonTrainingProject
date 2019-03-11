from collections import Counter
class Solution:
    def fourSum(self, nums, target: int):
        nums = sorted(nums)
        c = Counter(nums)
        matched_set = set()
        result = []

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    remainder = target - (nums[i] + nums[j] + nums[k])
                    if remainder in c:
                        matched_set.add(tuple(sorted([nums[i], nums[j], nums[k], remainder])))

        for four in matched_set:
            four_counter = Counter(four)
            if all([four_counter[key] <= c[key] for key in four_counter]):
                result.append(list(four))
        return result


nums = [1, 0, -1, 0, -2, 2]
print(Solution().fourSum(nums, 0))



