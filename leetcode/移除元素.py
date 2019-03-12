class Solution:
    def removeElement(self, nums, val: int) -> int:
        rp = len(nums)-1
        for i in range(len(nums)):
            while nums[rp] == val: 
            if i == rp: break
            while nums[i] == val:
                nums[i] = nums[rp]
                rp -=1
        return