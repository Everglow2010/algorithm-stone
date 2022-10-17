#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None :
            return ans
        
        q = queue.Queue()
        q.put(root, 1)
        while not q.empty :
            n, lv = q.get()
            if len(ans) < lv:
                ans.append([])
            
            ans[lv - 1].append(n.val)
            if lv % 2 == 1 :
                if n.right is not None:
                    q.put(n.right, lv + 1)
                if n.left is not None:
                    q.put(n.left, lv + 1)
            else:
                if n.left is not None:
                    q.put(n.left, lv + 1)
                if n.right is not None:
                    q.put(n.right, lv + 1)
        
        return ans
# @lc code=end 

