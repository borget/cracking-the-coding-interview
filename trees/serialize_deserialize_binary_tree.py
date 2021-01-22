from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if not root:
            return None
        serialized_str = ''
        q = deque()
        q.append(root)
        while len(q) > 0:
            curr = q.popleft()
            serialized_str += f'{str(curr.val)},'
            if curr.left:
                q.append(curr.left)
            else:
                serialized_str += ','
            if curr.right:
                q.append(curr.right)
            else:
                serialized_str += ','
        return serialized_str


    def deserialize(self, data):
        if not data:
            return None
        data_len = len(data)
        pointer = 0
        while pointer < data_len:
            pass


if __name__ == '__main__':
    root = TreeNode(1)
    n2 = TreeNode(2)
    root.left = n2
    n3 = TreeNode(3)
    root.right = n3
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n3.left = n4
    n3.right = n5
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))

    root = None
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))

    root = TreeNode(1)
    n2 = TreeNode(2)
    root.right = n2
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))

    root = TreeNode(1)
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))


