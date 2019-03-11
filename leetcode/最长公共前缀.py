class trieNode:
    def __init__(self, a):
        self.a = a
        self.children = []
    def addNodes(self, strs):
        if len(strs) == 0: return
        a = strs[0]
        finded = False
        for node in self.children:
            if node.a == a:
                node.addNodes(strs[1:])
                finded = True
        if not finded:
            newNode = trieNode(a)
            self.children.append(newNode)
            newNode.addNodes(strs[1:])

    def commonPrefix(self):
        result = ''
        cur_node = self
        while len(cur_node.children) == 1:
            result +=cur_node.children[0].a
            cur_node = cur_node.children[0]
        return result

    def __str__(self, level=0):
        result = '\t'*level + self.a + '\n'
        for child in self.children:
            result += child.__str__(level+1)
        return result

    def treeShow(self):
        print(self)



class Solution:
    def eq(self, x, items):
        for item in items:
            if x != item: return False
        return True

    def longestCommonPrefix(self, strs) -> str:
        zipped_list = zip(*strs)
        result = ''
        for x,*items in zipped_list:
            if self.eq(x,items): result += x
            else: break
        return result

    def longestCommonPrefix2(self, strs) -> str:
        root = trieNode('')
        for str in strs:
            root.addNodes(str)
        return root.commonPrefix()




strs = ['spow','spoer','spowlish']
root = trieNode('root')
for str in strs:
    root.addNodes(str)
root.treeShow()
print(Solution().longestCommonPrefix(strs))
print(Solution().longestCommonPrefix2(strs))

