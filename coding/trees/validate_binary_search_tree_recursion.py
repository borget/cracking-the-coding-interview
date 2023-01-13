from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return TreeNode(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = insert(root.right, key)
            else:
                root.left = insert(root.left, key)
        return root


if __name__ == '__main__':
    root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    s = Solution()
    assert True == s.isValidBST(root=root)

    root = TreeNode(1, left=TreeNode(1))
    s = Solution()
    assert False == s.isValidBST(root=root)