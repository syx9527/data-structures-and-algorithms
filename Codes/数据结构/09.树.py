"""
模仿操作系统中文件树
"""


class Node:

    def __init__(self, name, type_="dir"):
        self.name = name
        self.type = type_  # "dir" or "file"
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


"/root/"
"/var/"


class FileSystemTree:
    def __init__(self):
        self.root = Node(name="/")
        self.now = self.root

    def mkdir(self, name):
        # name以 / 结尾
        if name[-1] != "/":
            name += "/"

        node = Node(name=name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self, ):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        for child in self.now.children:
            if child.name == name:
                self.now = child
        else:
            raise ValueError("invalid dir")


tree = FileSystemTree()
tree.mkdir("var")
print(tree.root.children)
