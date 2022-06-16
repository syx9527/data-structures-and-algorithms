from typing import List


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


def create_linklist_head(li: List[int]) -> Node:
    """
    头插法
    :param li:
    :return:
    """
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_linklist_tail(li: List[int]) -> Node:
    """
    尾插法
    :param li:
    :return:
    """
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk: Node):
    while lk:
        print(lk.item, end=', ')
        lk = lk.next


li = [1, 2, 3, 4, 5, 6, 7, 8]
lk = create_linklist_tail(li=li)
print_linklist(lk)
