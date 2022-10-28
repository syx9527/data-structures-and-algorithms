from typing import List


def select_sort_simple(li: List) -> List:
    """
    选择排序(不推荐)
    :param li: 无序列表
    :return: 有序列表
    """
    n = len(li)
    li_new = []
    for i in range(n):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li: List) -> None:
    """
    选择排序
    :param li: 无序列表
    :return: None
    """
    n = len(li)
    for i in range(n - 1):
        min_loc = i
        for j in range(i + 1, n):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


li = [9, 8, 7, 1, 2, 3, 4, 5, 6]
select_sort(li)
print("bubble_sort", li, )
