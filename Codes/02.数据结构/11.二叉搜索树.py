import random


class BiTreeNode:
    """二叉树"""

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

    def __str__(self):
        return self.data


class BST:
    def __init__(self, li=None):
        self.root = None

        # 批量插入，初始化
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node: BiTreeNode, val):
        """
        递归插入
        """
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.left_child = self.insert(node.left_child, val)
            node.left_child.parent = node
        elif val > node.data:
            node.right_child = self.insert(node.right_child, val)
            node.right_child.parent = node
        else:
            ...

        return node

    def insert_no_rec(self, val):
        """
        非递擦插入
        """
        p = self.root
        if not p:  # 空树特殊处理一下
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.left_child:
                    p = p.left_child
                else:
                    p.left_child = BiTreeNode(val)
                    p.left_child.parent = p
                    return
            elif val > p.data:
                if p.right_child:
                    p = p.right_child
                else:
                    p.right_child = BiTreeNode(val)
                    p.right_child.parent = p
                    return
            else:
                return

    # 前序遍历
    def pre_order(self, root: BiTreeNode):

        if root:
            print(root.data, end=",")
            self.pre_order(root.left_child)
            self.pre_order(root.right_child)

    # 中序遍历
    def in_order(self, root: BiTreeNode):
        if root:
            self.in_order(root.left_child)
            print(root.data, end=",")
            self.in_order(root.right_child)

    # 后续遍历
    def post_order(self, root: BiTreeNode):
        if root:
            self.post_order(root.left_child)
            self.post_order(root.right_child)
            print(root.data, end=",")


li = list(range(1, 20 + 1))
print(li)
random.shuffle(li)
tree = BST(li)

tree.pre_order(tree.root)
print()
tree.in_order(tree.root)
print()
tree.post_order(tree.root)
