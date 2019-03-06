class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_list = ['']
        position = 0
        for x in s:
            if substr_list[position].find(x) == -1:
                substr_list[position] += x
            else:
                substr_list.append(x)
                position += 1
        print(substr_list)
        max_size = 0
        for substr in substr_list:
            if len(substr)>max_size: max_size = len(substr)
        return max_size


print(Solution().lengthOfLongestSubstring('pwwkew'))
