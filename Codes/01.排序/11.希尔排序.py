import copy
import random
from typing import List

from cal_time_tool import cal_time


def insert_sort_gap(li: List, gap) -> None:
    """
    插入排序(修改后)
    :param li: 无序列表
    :return: None
    """
    n = len(li)
    for i in range(gap, n):  # i 表示摸到的牌的下标
        temp = li[i]
        j = i - gap  # 手里的牌的下标
        while li[j] > temp and j >= 0:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = temp


@cal_time
def shell_sort(li: List) -> None:
    """
    希尔排序
    :param li: 无序列表
    :return:  None
    """
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


@cal_time
def insert_sort(li: List) -> None:
    """
    插入排序
    :param li: 无序列表
    :return: None
    """
    n = len(li)
    for i in range(1, n):  # i 表示摸到的牌的下标
        temp = li[i]
        j = i - 1  # 手里的牌的下标
        while li[j] > temp and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp


# 堆排序
def sift(li: List, low: int, high: int) -> None:
    """
    向下调整
    :param li: 列表
    :param low: 堆的堆顶位置（根节点位置）
    :param high: 堆的最后一个元素的位置（用于查找最后一个非叶子节点）
    :return: None
    """
    i = low  # 最开始指向根节点
    j = i * 2 + 1  # j开始使左孩子
    temp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数（没有越界）
        if j + 1 <= high and li[j + 1] < li[j]:  # 右节点存在且比左节点大
            j += 1
        if li[j] < temp:
            li[i] = li[j]
            i = j  # 往下走一层，更新i,j
            j = 2 * i + 1
        else:  # temp更大，把temp放到i的位置
            break
        li[i] = temp


def topk(li: List, k: int) -> List:
    heaq = li[0:k]
    n = len(li)
    for i in range((k - 2) // 2, -1, -1):
        sift(heaq, low=i, high=k - 1)
    # 1.建堆
    for i in range(k, n):
        if li[i] > heaq[0]:
            heaq[0] = li[i]
            sift(heaq, 0, k - 1)
    for i in range(k - 1, -1, -1):
        # i指向堆的最后一个元素
        heaq[0], heaq[i] = heaq[i], heaq[0]
        sift(heaq, low=0, high=i - 1)
    return heaq


@cal_time
def heap_sort(li: List) -> None:
    n = len(li)
    # 建堆
    for i in range((n - 2) // 2, -1, -1):
        sift(li, low=i, high=n - 1)
    # 建堆完成
    # 逐个出数
    for i in range(n - 1, -1, -1):
        # i指向堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, low=0, high=i - 1)


li = list(range(100000))

random.shuffle(li)
li_1 = copy.deepcopy(li)
li_2 = copy.deepcopy(li)
li_3 = copy.deepcopy(li)

shell_sort(li_1)
# insert_sort(li_2)
heap_sort(li_3)
# print(li)
