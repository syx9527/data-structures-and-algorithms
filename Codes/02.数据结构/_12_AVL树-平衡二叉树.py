from _11_二叉搜索树 import BiTreeNode, BST


class AVLNode(BiTreeNode):

    def __init__(self, data):
        super().__init__(data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li=None):
        super().__init__(li)

    def rotate_left(self, p: AVLNode, c: AVLNode):
        """
        左旋
        """
        s2 = c.left_child
        p.right_child = s2
        if s2:
            s2.parent = p
        c.left_child = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p: AVLNode, c: AVLNode):
        """
        右旋
        """
        s2 = c.right_child
        p.left_child = s2
        if s2:
            s2.parent = p
        c.right_child = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p: AVLNode, c: AVLNode):
        """
        右旋->左旋
        """
        g = c.left_child
        s3 = g.right_child
        c.left_child = s3
        if s3:
            s3.parent = c
        g.right_child = c
        c.parent = g

        s2 = g.left_child
        p.right_child = s2

        if s2:
            s2.parent = p
        g.left_child = p
        p.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bg = 0
        elif g.bf < 0:
            p.bf = 0
            c.bg = 1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0

    def rotate_left_right(self, p: AVLNode, c: AVLNode):
        g = c.right_child

        s2 = g.left_child
        c.left_child = s2

        if s2:
            s2.parent = c
        g.left_child = c
        c.parent = g

        s3 = g.right_child
        p.left_child = s3
        if s3:
            s3.parent = p
        g.right_child = p
        p.parent = g

        # 更新bf
        if g.bg < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0

    def insert_no_rec(self, val):
        ...
