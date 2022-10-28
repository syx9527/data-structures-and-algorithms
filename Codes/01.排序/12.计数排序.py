import copy
import random
from typing import List

from cal_time_tool import cal_time


@cal_time
def count_sort(li: List[int], max_count: int = 100) -> None:
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


@cal_time
def sys_sort(li: List):
    li.sort()


li = [random.randint(0, 100) for _ in range(1000000)]
max_li = max(li)
li_1 = copy.deepcopy(li)
li_2 = copy.deepcopy(li)
# print(li)
count_sort(li_1, max_li)
sys_sort(li_2)
# print(li)
