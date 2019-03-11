alpha_str = ''.join([chr(x) for x in range(97,123)])
sep = 3
grouped_strlist = [alpha_str[sep*i:i*sep+sep] for i in range(9)]
dic = {str(a):l for a,l in zip(range(2,10), grouped_strlist)}
dic['7'] = 'pqrs'
dic['8'] = 'tuv'
dic['9'] = 'wxyz'

class Solution:
    def letterCombinations(self, digits: str):
        if digits == '' : return []
        result = list(dic[digits[0]])
        for a in digits[1:]:
            result = [x+y for x in result for y in dic[a]]
        return result

str = '234567'
print(Solution().letterCombinations(str))

