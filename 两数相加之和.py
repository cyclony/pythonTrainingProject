class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

     def __iter__(self):
         cur_node = self
         while cur_node != None:
             yield cur_node.val
             cur_node = cur_node.next

     def __repr__(self):
         return '->'.join(str(x) for x in self)



class Solution:
    carry = 0

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            if self.carry == 0: return None
            else: return ListNode(self.carry)
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)
        sum_val = l1.val + l2.val + self.carry
        self.carry = int(sum_val / 10)
        mod_no = sum_val % 10
        cur_node = ListNode(mod_no)
        cur_node.next = self.addTwoNumbers(l1.next, l2.next)
        return cur_node

def init(*xs):
    dumm_head = cur_node = ListNode(0)
    for x in xs:
        cur_node.next = ListNode(x)
        cur_node = cur_node.next
    return dumm_head.next

n1 = init(0)
n2 = init(0)
print(n1)
print(n2)
print(Solution().addTwoNumbers(n1, n2))



