import sys
from typing import List

from Codes.cal_time_tool import cal_time

sys.setrecursionlimit(100000000)


def partition(li: List, left: int, right: int) -> int:
    """
    对分区排序
    :param li:
    :param left:
    :param right:
    :return:
    """
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:  # 右边找比temp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写道左边的空位上
        # print(li, "right")
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]
        # print(li, "left")
    li[left] = temp
    return left


def _quick_sort(li: List, left: int, right: int) -> None:
    """
    递归P归位
    :param li:
    :param left:
    :param right:
    :return:
    """
    if left < right:  # 至少两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@cal_time
def quick_sort(li: List) -> None:
    """
    快速排序
    :param li:
    :return:
    """
    _quick_sort(li, left=0, right=len(li) - 1)


# li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
@cal_time
def bubble_sort(li: List[int]) -> None:
    """
    冒泡排序
    :param li:无序列表
    :return: None
    """
    n = len(li)
    for i in range(n - 1):
        exchange = False
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break


@cal_time
def oo(li: List):
    li.sort()


# li = list(range(10000, 0, -1))
# random.shuffle(li)
# li_new = copy.deepcopy(li)
# li_new_two = copy.deepcopy(li)
# quick_sort(li)
# bubble_sort(li_new)
# oo(li_new_two)
li = [ 8,9, 7, 6, 5, 4, 3, 2, 1]
quick_sort(li)
# print(li)
