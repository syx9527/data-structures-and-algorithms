class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self, ):
        return self.stack.pop()

    def get_top(self, ):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0


# 应用--括号匹配问题
def brace_match(s: str) -> bool:
    match = {
        ')': '(',
        "]": "[",
        "}": "{",
    }
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('{'))
