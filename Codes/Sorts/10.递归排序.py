import random
from typing import List


def merge(li: List, low: int, mid: int, high: int) -> None:
    """
    归并
    :param li:
    :param low:
    :param mid:
    :param high:
    :return:
    """

    i = low
    j = mid + 1
    temp_list = []
    while i <= mid and j <= high:  # 只要左右两边都有数
        if li[i] < li[j]:
            temp_list.append(li[i])
            i += 1
        else:
            temp_list.append(li[j])
            j += 1
    # while 执行完，肯定有一部分没数了
    while i <= mid:
        temp_list.append(li[i])
        i += 1
    while j <= high:
        temp_list.append(li[j])
        j += 1
    li[low: high + 1] = temp_list


def _merge_sort(li: List, low: int, high: int) -> None:
    """
    :param li:
    :param low:
    :param high:
    :return: None
    """
    if low < high:  # 至少有两个元素，递归：
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)
        print(li[low:high + 1])


def merge_sort(li: List):
    """
    递归排序
    :param li:
    :return:
    """
    _merge_sort(li, 0, len(li) - 1)


li = list(range(16))
random.shuffle(li)
print(li)
merge_sort(li)
print(li)
