from typing import List

from Codes.cal_time_tool import cal_time


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



