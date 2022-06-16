from collections import deque
from typing import List

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
]


def maze_path(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    深度优先
    :param x1:起点横坐标
    :param y1:起点纵坐标
    :param x2:终点横坐标
    :param y2:终点纵坐标
    :return: True or False
    """
    stack = []
    stack.append((x1, y1))
    while stack:
        cur_node = stack[-1]  # 当前的节点
        if cur_node[0] == x2 and cur_node[1] == y2:
            # 表示走到终点了
            for p in stack:
                print(p)
            return True
        # x,t 四个方向 上(x-1,y),下：(x+1,y),左(x,y-1),右(x,y+1)
        for dir_ in dirs:
            next_node = dir_(cur_node[0], cur_node[1])
            # 如果下一个节点能走：
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append((next_node))
                maze[next_node[0]][next_node[1]] = 2  # 标记已经走过了
                break
        else:
            maze[next_node[0]][next_node[1]] = 2
            stack.pop()

    else:
        print("没有路！")
        return False


def print_path(path_: List[int]):
    cur_node = path_[-1]
    real_path = []
    while cur_node[2] != -1:
        real_path.append(cur_node[:2])
        cur_node = path_[cur_node[2]]
    real_path.append(cur_node[:2])
    real_path.reverse()
    for node in real_path:
        print(node)


def maze_path_queue(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    广度优先
    :param x1:起点横坐标
    :param y1:起点纵坐标
    :param x2:终点横坐标
    :param y2:终点纵坐标
    :return: True or False
    """
    queue = deque()
    queue.append((x1, y1, -1))
    path_: List[int] = []
    while queue:
        cur_node = queue.popleft()
        path_.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            # 表示走到终点了
            print_path(path_)
            return True
        for dir_ in dirs:
            next_node = dir_(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0], next_node[1], len(path_) - 1))
                maze[next_node[0]][next_node[1]] = 2  # 标记为已经走过
    else:
        print("没有路！")
        return False


# 深度优先
# maze_path(1, 1, 8, 8)
maze_path_queue(1, 1, 8, 8)
