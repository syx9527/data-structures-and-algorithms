class Queue:
    """
    环形队列
    """

    def __init__(self, max_size: int = 10):
        """
        初始化
        :param max_size:队列最大长度
        """
        self.max_size = max_size
        self.queue = [None for _ in range(self.max_size)]
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element: object) -> dict:
        """
        队列入队操作
        :param element:入栈元素
        :return:{"rear": rear, "element": element}
        """
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = element
            return {"rear": self.rear, "element": element}
        else:
            raise IndexError("Queue is filled!")

    def pop(self, ) -> object:
        """
        队列出队操作
        :return:出队元素
        """
        if not self.is_empty():
            self.front = (self.front + 1) % self.max_size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty!")

    def is_empty(self) -> bool:
        """
        判断队空
        :return:
        """
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.max_size == self.front


q = Queue(5)
for i in range(4):
    q.push(i)
print(q.pop())
q.push(4)
