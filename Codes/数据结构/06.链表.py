from typing import List


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


def create_linklist_head(_list: List[int]) -> Node:
    """
    头插法
    :param _list:
    :return:
    """
    if not _list:
        return Node(None)
    head = Node(_list[0])
    for element in _list[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_linklist_tail(_list: List[int]) -> Node:
    """
    尾插法
    :param _list:
    :return:
    """
    if not _list:
        return Node(None)
    head = Node(_list[0])
    tail = head
    for element in _list[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk: Node):
    while lk:
        print(lk.item, end=', ')
        lk = lk.next


_list = [1, 2, 3, 4, 5, 6, 7, 8]
lk = create_linklist_tail(_list=_list)
print_linklist(lk)
