from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_elem = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return top_elem

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_elem = self.q1.popleft()
        self.q2.append(top_elem)  # 放回栈顶元素
        self.q1, self.q2 = self.q2, self.q1
        return top_elem        

    def empty(self) -> bool:
        return not self.q1



# 测试  
if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())   # 返回 2
    print(stack.pop())   # 返回 2
    print(stack.empty()) # 返回 False