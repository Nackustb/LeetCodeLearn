class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: 
                stack.append(c)
            elif dic[stack.pop()] != c: 
                return False 
        return len(stack) == 1

# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))          # True
    print(s.isValid("()[]{}"))      # True
    print(s.isValid("(]"))          # False
    print(s.isValid("([)]"))        # False
    print(s.isValid("{[]}"))        # True
    print(s.isValid(""))            # True