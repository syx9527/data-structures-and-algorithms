import random
from typing import List

from Codes.Sorts import cal_time


@cal_time
def bucket_sort(li: List, n: int = 100, max_num: int = 10000) -> None:
    buckets = [[] for _ in range(n)]
    # 把元素放到不同桶里
    for val in li:
        # 0->0,86->0,100-1,
        i = min(val // (max_num // n), n - 1)  # i表示val放到几号桶
        buckets[i].append(val)
        # 对每个桶排序，保持桶内的顺序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    li.clear()
    for buc in buckets:
        li += buc





li = [random.randint(0, 10000) for _ in range(100000)]

print(li)
bucket_sort(li)
print(li)