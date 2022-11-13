class BiTreeNode:
    """
    二叉树
    """

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

    def __str__(self):
        return str(self.data)


class BST:
    """
    二叉搜索树
    """

    def __init__(self, l_=None):
        self.root = None

        # 批量插入，初始化
        if l_:
            for val in l_:
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
        非递归插入
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

    def query(self, node: BiTreeNode, val):
        """
        递归查询
        """
        if not node:
            return None
        elif node.data < val:
            return self.query(node.right_child, val)

        elif node.data > val:
            return self.query(node.left_child, val)
        else:
            return node

    def query_no_rec(self, val):
        """
        非递归查询
        """
        p = self.root
        while p:
            if p.data < val:
                p = p.right_child
            elif p.data > val:
                p = p.left_child
            elif p.data == val:
                return p
        return None

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

    def __remove_node_1(self, node: BiTreeNode):
        # 情况1：node是叶子节点
        if not node.parent:
            self.root = None
        elif node == node.parent.left_child:  # node是他父亲的左节点
            node.parent.left_child = None
            node.parent = None
        elif node == node.parent.right_child:  # node是他父亲的左节点
            node.parent.right_child = None
            node.parent = None
        del node

    def __remove_node_21(self, node: BiTreeNode):
        # 情况2-1：node只有一个左孩子
        if not node.parent:
            self.root = node.left_child
            node.left_child.parent = None
        elif node == node.parent.left_child:  # node是他父亲的左节点
            node.parent.left_child = node.left_child
            node.left_child.parent = node.parent
        elif node == node.parent.right_child:  # node是他父亲的左节点
            node.parent.right_child = node.left_child
            node.right_child.parent = node.parent
        del node

    def __remove_node_22(self, node: BiTreeNode):
        # 情况2-1：node只有一个右边孩子
        if not node.parent:
            self.root = node.right_child
            node.right_child.parent = None
        elif node == node.parent.left_child:  # node是他父亲的左节点
            node.parent.left_child = node.right_child
            node.left_child.parent = node.parent
        elif node == node.parent.right_child:  # node是他父亲的左节点
            node.parent.right_child = node.right_child
            node.right_child.parent = node.parent
        del node

    def __remove_node_3(self, node: BiTreeNode):
        """
        有左孩子和右孩子
        """
        ...
        min_node = node.right_child
        while min_node.left_child:
            min_node = min_node.left_child
        node.data = min_node.data  # 替换

        # 删除min_node
        if min_node.right_child:
            self.__remove_node_22(min_node)
        else:
            self.__remove_node_1(min_node)

    def delete(self, val):
        """
        删除元素
        """
        if not self.root:
            return
        node = self.query_no_rec(val)
        if not node:  # 删除元素不存在
            return False
        if not node.left_child and not node.right_child:  # 叶子节点
            self.__remove_node_1(node)
        elif node.left_child and not node.right_child:  # 只有一个左孩子
            self.__remove_node_21(node)
        elif not node.left_child and node.right_child:  # 只有一个右孩子
            self.__remove_node_22(node)
        else:
            # 两个孩子都有
            self.__remove_node_3(node)


li = [1, 4, 2, 5, 3, 8, 6, 9, 7]

print(li)
tree = BST(li)

tree.pre_order(tree.root)
print()
tree.in_order(tree.root)
print()
tree.post_order(tree.root)
print()
print(tree.query_no_rec(3))
print("-" * 20)
tree.in_order(tree.root)
print()
tree.delete(5)
tree.in_order(tree.root)
print()
tree.delete(1)
tree.in_order(tree.root)
print()
tree.delete(8)
tree.in_order(tree.root)
print()
