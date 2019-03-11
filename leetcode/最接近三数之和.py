import bisect
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums = sorted(nums)
        result = sum(nums[0:3])
        distance = abs(result - target)
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                thrdNum = target - (nums[i] + nums[j])
                p = bisect.bisect_left(nums[j+1:], thrdNum)
                if p == 0:
                    temp = nums[j+1]
                elif p == len(nums[j+1:]):
                    temp = nums[len(nums)-1]
                else:#插入点左边和右边的数哪一个离目标值近
                    temp = nums[j+1:][p] if nums[j+1:][p]-thrdNum <= thrdNum - nums[j+1:][p-1] else nums[j+1:][p-1]
                threeSum = temp + nums[i] + nums[j]
                current_distance = abs(threeSum - target)
                if current_distance < distance:
                    distance = current_distance
                    result = threeSum
        return result

#nums = [-7,-10,-1,3,0,-7,-9,-1,10,8,-6,4,14,-8,9,-15,0,-4,-5,9,11,3,-5,-8,2,-6,-14,7,-14,10,5,-6,7,11,4,-7,11,11,7,7,-4,-14,-12,-13,-14,4,-13,1,-15,-2,-12,11,-14,-2,10,3,-1,11,-5,1,-2,7,2,-10,-5,-8,-10,14,10,13,-2,-9,6,-7,-7,7,12,-5,-14,4,0,-11,-8,2,-6,-13,12,0,5,-15,8,-12,-1,-4,-15,2,-5,-9,-7,12,11,6,10,-6,14,-12,9,3,-10,10,-8,-2,6,-9,7,7,-7,4,-8,5,-4,8,0,3,11,0,-10,-9]
nums = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]


print(Solution().threeSumClosest(nums, 0))





