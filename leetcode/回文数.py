class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False #如果是负数，直接返回False
        nums = []            #构建一个各个位数的数组
        round_num = x
        while round_num>0:
            nums.append(round_num%10)
            round_num = int(round_num/10)
        for i in range(0 , int(len(nums)/2)):
            if nums[i] != nums[len(nums) - i -1]: #从头到中间遍历数组，依次比较尾到中间的数字，如果不相等，直接返回False
                return False
        return True

print(Solution().isPalindrome(-12))
