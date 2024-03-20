# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''if not preorder and not postorder:
            return None
        root=TreeNode(preorder[0])
       
        if len(preorder)==1:
            return root
        leftval=preorder[1]
        left_tree_size=postorder.index(leftval)+1
        self.left=self.constructFromPrePost(preorder[1:left_tree_size+1],postorder[:left_tree_size])
        self.right=self.constructFromPrePost(preorder[left_tree_size+1:],postorder[left_tree_size:-1])
        return root'''
        if not preorder and not postorder:
            return None
        root=TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        leftval=preorder[1]
        left_subtree_size=postorder.index(leftval)+1
        root.left=self.constructFromPrePost(preorder[1:left_subtree_size+1],postorder[0:left_subtree_size])
        root.right=self.constructFromPrePost(preorder[left_subtree_size+1:],postorder[left_subtree_size:-1])
        return root
        
