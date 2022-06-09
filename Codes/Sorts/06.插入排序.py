import random
from typing import List

from cal_time_tool import cal_time


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
        # print(li)


# li = [random.randint(0, 10) for i in range(10)]
li = list(range(10000))
random.shuffle(li)
# print(li)
insert_sort(li)
# print(li)
