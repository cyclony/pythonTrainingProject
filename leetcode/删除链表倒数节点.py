# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
    def initial(self, nums):
         node = self
         node.val = nums[0]
         for i in nums[1:]:
             node.next = ListNode(i)
             node = node.next
    def __iter__(self):
        node = self
        yield str(node.val)
        while node.next != None:
            node = node.next
            yield str(node.val)

    def __repr__(self):
        return '->'.join(self)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        node = head
        if node.next == None: return None #只有一个元素的情况
        while node != None:
            l.insert(0, node)#将链表倒序放入list中，因为只保存引用，所以空间使用效率高，只遍历一边就可以按照list[n]方式访问任意元素
            node = node.next
        if n == len(l):#删除第一个节点
            head = head.next
        elif n == 1: #删除最后一个节点
            l[1].next = None
        else:#删除的节点在中间的,将两边节点对接起来即可
            prev_node = l[n]
            next_node = l[n-2]
            prev_node.next = next_node
        return head

    def removeNode(self, prev_node, current_node, n):#使用递归来处理，一遍就可以删掉
        if current_node.next != None:#
            self.removeNode(current_node, current_node.next, n)
        self.i += 1
        if self.i == n:
            prev_node.next = current_node.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        self.i = 0
        dummy_head = ListNode(0)#构建一个dummy头结点，减少代码量
        dummy_head.next = head
        self.removeNode(dummy_head, dummy_head.next, n)
        return dummy_head.next

        return head

head = ListNode(0)
head.initial([1,2])
print(head)
print(Solution().removeNthFromEnd2(head,2))



