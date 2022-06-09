import random
from typing import List

from Codes.Sorts import cal_time


@cal_time
def radix_sort(li: List) -> None:
    """
    基数排序
    :param li: 无序列表
    :return:None
    """
    max_num = max(li)  # 最大值
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for val in li:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1


li = list(range(100000))
random.shuffle(li)
print(li)
radix_sort(li)
print(li)
