"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

示例 1：

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
通过次数239,460提交次数503,312
"""
from typing import List


# 方法一：逐行所搜
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            if target in line:
                return True
        return False


# 方法二：二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        left = 0
        right = w * h - 1

        while left <= right:
            mid = (left + right) // 2
            i = mid // w
            j = mid % w
            mid_val = matrix[i][j]
            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
res = Solution().searchMatrix(matrix=matrix, target=target)
print(res)
