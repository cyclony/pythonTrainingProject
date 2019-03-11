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


head = ListNode(0)
head.initial([1,2])
for i in head:
    print(i)
print(head)
print(Solution().removeNthFromEnd(head,1))



