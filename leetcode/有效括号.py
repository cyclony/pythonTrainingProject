class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        self.left_set = set(['{','[','('])
        self.right_set = set(['}',']',')'])
        dic = {'{':'}', '(':')', '[':']'}
        for a in s:
            if a in self.left_set:
                stack.insert(0,a)
            if a in self.right_set:
                if len(stack) == 0: return False
                b = stack.pop(0)
                if dic[b] !=a: return False
        if len(stack)!= 0 : return False
        return True

s = ''
print(Solution().isValid(s))
