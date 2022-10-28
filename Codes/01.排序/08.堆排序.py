import random
from typing import List

from cal_time_tool import cal_time


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


li = list(range(10))
random.shuffle(li)
print(li)
heaq = topk(li, 5)
print(heaq)
