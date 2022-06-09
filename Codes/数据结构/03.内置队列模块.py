from collections import deque


# q = deque(iterable=[1, 2, 3, ], maxlen=5)
# q.append(4)  # 队尾进队
# print(q.popleft())  # 队首出队
# print(q)
# # 用于双向队列
# print(q.popleft())
# q.appendleft(1)  # 队首进队
# q.pop()  # 队尾出队
def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='')
