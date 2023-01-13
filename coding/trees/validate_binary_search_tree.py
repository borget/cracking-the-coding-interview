from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        left_q = deque()
        right_q = deque()
        if not root:
            return None
        root_val = root.val
        if root.left:
            left_q.append(root.left)
            while len(left_q) > 0:
                curr = left_q.popleft()
                if curr and curr.val >= root_val:
                    return False
                if curr and curr.left:
                    if curr.left.val < curr:
                        left_q.append(curr.left)
                    else:
                        return False
                if curr and curr.right:
                    if curr.right.val > curr and :
                        left_q.append(curr.left)
                    else:
                        return False




        return True


if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(1))
    s = Solution()
    assert False == s.isValidBST(root=root)

    root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    s = Solution()
    assert True == s.isValidBST(root=root)
