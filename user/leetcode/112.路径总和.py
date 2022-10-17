#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        # start BFS
        q = queue.Queue()
        q.put((root, root.val))
        while not q.empty():
            node, sum = q.get()
            if sum == targetSum and node.left is None and node.right is None:
                return True
            
            if node.left is not None:
                q.put((node.left, sum + node.left.val))
            
            if node.right is not None:
                q.put((node.right, sum + node.right.val))
        
        return False

# @lc code=end

