# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    # carry is set as static var to use specifically for recursion
    # carry = 0
    
	# # solution using recursion
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     # dummy head
    #     sm = ListNode()
        
    #     # base case
    #     if not (l1 or l2):
    #         if self.carry == 0:
    #             return None
    #         else:
    #             return ListNode(val=self.carry)
    #     # other cases
    #     else:
    #         sm.val = (0 if l1 == None else l1.val) + (0 if l2 == None else l2.val) + self.carry
    #         if sm.val >= 0:
    #             self.carry, sm.val = int(sm.val / 10), sm.val % 10
    #         else:
    #             self.carry = 0
    #         sm.next = self.addTwoNumbers((l1.next if l1 else None), (l2.next if l2 else None))
        
    #     return sm
    
	# solution using iteration
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sm = ListNode()
        carry = 0
        
        cur = sm
        p = l1
        q = l2
        while p or q or carry:
            if cur.next == None:
                cur.next = ListNode()
                cur = cur.next
            cur.val = ( 0 if p == None else p.val) + (0 if q == None else q.val) + carry
            
            if cur.val >= 10:
                carry, cur.val = int(cur.val /10), cur.val % 10
            else:
                carry = 0
            
            p = None if p == None else p.next
            q = None if q == None else q.next
            
        return sm.next