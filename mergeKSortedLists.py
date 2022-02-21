# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKSortedLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # initialize resulting merged sorted list with dummy node
        result = ListNode()
        cur = result
        
        itrs = list(filter(None, lists.copy()))
        while len(itrs) != 0:
            minItrIdx = 0
            for i in range(len(itrs)):
                if itrs[i].val < itrs[minItrIdx].val:
                    minItrIdx = i
            
            cur.next = itrs[minItrIdx]
            cur = cur.next
            itrs[minItrIdx] = itrs[minItrIdx].next
            if itrs[minItrIdx] == None:
                itrs.pop(minItrIdx)
        
        # skip dummy node
        result = result.next
        return result