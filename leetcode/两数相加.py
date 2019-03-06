class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        #初始化一个cursor结点，作为游标移动
        cur_node = self
        while cur_node!= None:
            yield cur_node.val
            cur_node = cur_node.next

    def __repr__(self):
        return '->'.join(str(x) for x in self)


    @staticmethod
    def initial(*xs):
        dummy_head = cur_node = ListNode(0) #初始化一个头结点和游标
        for x in xs:
            cur_node.next = ListNode(x)
            cur_node = cur_node.next
        return dummy_head.next


class Solution:
    carry = 0
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: 
            l1 = ListNode(0)
        if l2 == None: 
            l2 = ListNode(0)
        sum_val= l1.val + l2.val + self.carry
        if sum_val == 0: return None
        self.carry = int(sum_val/10)
        mod_no =sum_val%10
        cur_node = ListNode(mod_no)
        cur_node.next = self.addTwoNumbers(l1.next, l2.next)
        return cur_node

n1 = ListNode(3)
n1.next = ListNode(5)
n1.next.next = ListNode(7)
n2 = ListNode(4)
n2.next = ListNode(6)
n2.next.next = ListNode(3)

node = Solution().addTwoNumbers(n1, n2)

n3 = ListNode(0)
n3 = ListNode.initial(0)
n4 = ListNode.initial(0)
print(n3)
print(n4)
print(Solution().addTwoNumbers(n3, n4))


