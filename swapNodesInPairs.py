# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, root: Optional[ListNode]) -> Optional[ListNode]:
        if root == None or root.next == None:
            return root
        
        result = root.next
        
        prevNode = None
        curNode = root
        while curNode != None and curNode.next != None:
            nextNode = curNode.next
            nextNextNode = nextNode.next
            
            # swap references
            curNode.next = nextNextNode
            nextNode.next = curNode
            if prevNode != None:
                prevNode.next = nextNode
            prevNode = curNode
            curNode = curNode.next
            
        return result