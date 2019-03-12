class BTreeNode: #构建一个反向的二叉树（子节点关联父节点），从叶子节点回溯，会生成所有的排列
    leaf_nodes = []
    def __init__(self,father, val, x_val, y_val, x_num, y_num):
        self.father = father
        self.x_num = x_num
        self.y_num = y_num
        self.val = val
        if x_num!= 0:
            leftChild = BTreeNode(self, x_val, x_val, y_val, x_num-1, y_num)
        if y_num!= 0:
            rightChild = BTreeNode(self, y_val, x_val, y_val, x_num, y_num-1)
        if x_num == 0 and y_num == 0:
            self.leaf_nodes.append(self)

    def __iter__(self):
        node = self
        while node.val != '':
            yield node.val
            node = node.father
    def __repr__(self):
        return ''.join(self)


class Solution:
    def generateParenthesis(self, n: int):
        BTreeNode.leaf_nodes = []
        root = BTreeNode(None, '', '(',')',n,n)
        result = [str(node) for node in root.leaf_nodes if self.isValid(str(node))]
        return result

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

print(Solution().generateParenthesis(1))
