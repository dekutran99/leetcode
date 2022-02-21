# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if root == None:
            return result
        
        queue = []
        queue.insert(0, root)
        queue.insert(0, None)
        
        curLevel = []
        while len(queue) > 0:
            cur = queue.pop()
            
            if cur == None:
                result.append(curLevel)
                curLevel = []
                
                if len(queue) > 0:
                    queue.insert(0, None)
            else:
                curLevel.append(cur.val)
                
                if cur.left != None:
                    queue.insert(0, cur.left)
                if cur.right != None:
                    queue.insert(0, cur.right)
            
        return result