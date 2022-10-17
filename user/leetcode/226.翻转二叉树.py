#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root
        

# @lc code=end

