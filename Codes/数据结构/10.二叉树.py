from collections import deque


class BiTreeNode:
    """二叉树"""

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.data


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.left_child = a
e.right_child = g
a.right_child = c
c.left_child = b
c.right_child = d
g.right_child = f

root = e


# 前序遍历
def pre_order(root: BiTreeNode):
    if root:
        print(root.data, end=",")
        pre_order(root.left_child)
        pre_order(root.right_child)


# 中序遍历
def in_order(root: BiTreeNode):
    if root:
        in_order(root.left_child)
        print(root.data, end=",")
        in_order(root.right_child)


# 后续遍历
def post_order(root: BiTreeNode):
    if root:
        post_order(root.left_child)
        post_order(root.right_child)
        print(root.data, end=",")


# 层次遍历
# def fl_order(root: BiTreeNode, res: list, temp: list) -> list or None:
#     if temp:
#         op = []
#         for i in temp:
#             if i:
#                 res.append(i)
#                 op.append(i.left_child)
#                 op.append(i.right_child)
#         temp = op
#
#         fl_order(root, res=res, temp=temp)
def level_order(root: BiTreeNode):
    queue = deque()
    queue.append(root)
    while len((queue)) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.left_child:
            queue.append(node.left_child)
        if node.right_child:
            queue.append(node.right_child)


pre_order(root)
print("\n")
in_order(root)
print("\n")
post_order(root)
print("\n")
level_order(root)
