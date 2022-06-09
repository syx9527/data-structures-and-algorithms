from typing import List

from Codes.cal_time_tool import cal_time


@cal_time
def binary_search(li: List, val) -> int or None:
    """
    二分查找
    :param li:有序列表
    :param val: 需要查找的元素
    :return:
    """
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = li[mid]
        if mid_val == val:
            return mid
        elif mid_val > val:
            right = mid - 1
        else:
            left = mid + 1
    return


@cal_time
def linear_search(li: List, val) -> int or None:
    """
    顺序查找
    :param li:需要查找的列表
    :param val: 需要查找的元素
    :return:
    """
    for ind, v in enumerate(li):
        if v == val:
            return ind
    return


li = list(range(10000))
linear_search(li, 3890)
binary_search(li, 3890)
