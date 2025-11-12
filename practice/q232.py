class MyQueue:

    def __init__(self):
        self.stack_in = []   # 入栈
        self.stack_out = []  # 出栈        

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        # 如果 stack_out 为空，则把 stack_in 的元素倒入 stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # 弹出 stack_out 的栈顶元素
        return self.stack_out.pop()        

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]        

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out       


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# 测试
if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)  # queue is: [1]
    myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
    print(myQueue.peek())  # return 1
    print(myQueue.pop())   # return 1, queue is [2]
    print(myQueue.empty()) # return false