from typing import List

from Codes.cal_time_tool import cal_time


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
        print(li)



end = "\n" + "=" * 40 + "\n"
# li = [random.randint(0, 10000) for i in range(10)]
li = [9, 8, 7, 1, 2, 3, 4, 5, 6]
bubble_sort(li=[9, 8, 7, 1, 2, 3, 4, 5, 6])
print("bubble_sort", li, end=end)


