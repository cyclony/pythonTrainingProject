# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
     def initial(self, nums):
        node = self
        for num in nums:
            node.next = ListNode(num)
            node = node.next

     def __iter__(self):
         node = self
         while node != None:
             yield node.val
             node = node.next

     def __repr__(self):
         return '->'.join(str(i) for i in self)

     def __ge__(self, other):
         if self.val >= other.val: return True
         else: return False


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        head = ListNode(0)
        p = head
        while p1!= None or p2!= None:
            if p1 == None :
                p.next = p2
                p = p.next
                p2 = p2.next
                continue
            if p2 == None:
                p.next = p1
                p = p.next
                p1 = p1.next
                continue
            if p1>=p2:
                p.next= p2
                p = p2
                p2 = p2.next
            else:
                p.next = p1
                p = p1
                p1 = p1.next
        return head.next

nums1 = [1,2,4]
nums2 = [1,3,4]
h1 = p = ListNode(nums1[0])
for n in nums1[1:]:
    p.next = ListNode(n)
    p = p.next

h2 = p = ListNode(nums2[0])
for n in nums2[1:]:
    p.next = ListNode(n)
    p = p.next


print(Solution().mergeTwoLists(h1,h2))
