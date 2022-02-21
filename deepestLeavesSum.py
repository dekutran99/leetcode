# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return self.deepestLeavesSumHelper(root, 0)[0]
    
    def deepestLeavesSumHelper(self, root, depth):
        if root == None:
            return (0,0)
        elif root.left == None and root.right == None:
            return (root.val, depth)
        
        left = root.left
        right = root.right

        leftDeepestLeavesSumAndDepth = self.deepestLeavesSumHelper(left, depth + 1)
        rightDeepestLeavesSumAndDepth = self.deepestLeavesSumHelper(right, depth + 1)
        
        leftDeepestLeavesSum = leftDeepestLeavesSumAndDepth[0]
        leftDeepestLeavesDepth = leftDeepestLeavesSumAndDepth[1]
        rightDeepestLeavesSum = rightDeepestLeavesSumAndDepth[0]
        rightDeepestLeavesDepth = rightDeepestLeavesSumAndDepth[1]
        

        if leftDeepestLeavesDepth == rightDeepestLeavesDepth:
            return (leftDeepestLeavesSum + rightDeepestLeavesSum, leftDeepestLeavesDepth)
        elif leftDeepestLeavesDepth > rightDeepestLeavesDepth:
            return (leftDeepestLeavesSum, leftDeepestLeavesDepth)
        elif rightDeepestLeavesDepth > leftDeepestLeavesDepth:
            return (rightDeepestLeavesSum, rightDeepestLeavesDepth)
