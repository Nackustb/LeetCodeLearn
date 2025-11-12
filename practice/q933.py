from collections import deque
class RecentCounter:

    def __init__(self):
         self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
    
# 测试  
if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))     # 返回 1
    print(rc.ping(100))   # 返回 2
    print(rc.ping(3001))  # 返回 3
    print(rc.ping(3002))  # 返回 3
    