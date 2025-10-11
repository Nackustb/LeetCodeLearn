## Python 常用数据类型和基本用法总结



Python 提供了丰富的内置数据类型，同时也可以通过标准库或自定义类来实现更复杂的数据结构。以下是 Python 中常用的数据类型和数据结构的总结，以 Markdown 格式呈现。



### 一、 基本数据类型





#### 1. Number (数字)



Python 支持多种数字类型，主要包括整数、浮点数和复数。

- **Integer (整数 `int`)**: 表示整数，可以是正数、负数或零。Python 3.x 中的整数没有大小限制。
- **Float (浮点数 `float`)**: 表示带有小数点的数字。
- **Complex (复数 `complex`)**: 由实部和虚部组成，例如 `3 + 5j`。

**基本用法:**

Python

```
# 整数
a = 10
print(type(a))  # <class 'int'>

# 浮点数
b = 3.14
print(type(b))  # <class 'float'>

# 复数
c = 1 + 2j
print(type(c))  # <class 'complex'>

# 数学运算
sum_val = a + b
product_val = a * 2
print(sum_val)
print(product_val)

#除法
3/2 =1.5
5//2 =2 # 整除
5 % 2 =1 # 取余
```



#### 2. String (字符串)



字符串是用于表示文本数据的字符序列，不可变。

**基本用法:**

Python

```
# 创建字符串
s1 = 'Hello, World!'
s2 = "Python"

# 字符串拼接
s3 = s1 + ' ' + s2
print(s3)

# 字符串索引和切片
print(s1[0])      # 'H'
print(s1[7:12])   # 'World'

# 常用方法
print(s1.upper()) # 'HELLO, WORLD!'
print(s1.lower()) # 'hello, world!'
print(s1.split(',')) # ['Hello', ' World!']
```



### 二、 复合数据类型 (内置)





#### 3. List (列表)



列表是一个有序、可变的元素集合，可以包含不同类型的元素。

**基本用法:**

Python

```
# 创建列表
my_list = [1, 'apple', 3.14, True]

# 访问元素
print(my_list[1])  # 'apple'

# 修改元素
my_list[0] = 'one'
print(my_list) # ['one', 'apple', 3.14, True]

# 添加元素
my_list.append('new_item')
print(my_list)

# 删除元素
my_list.pop(0)# 删除第一个元素
my_list.pop() # 删除最后一个元素
del my_list[1] # 删除指定索引的元素
print(my_list)

# 列表推导式
squares = [x**2 for x in range(5)]
print(squares) # [0, 1, 4, 9, 16]

#常用函数
len(my_list) #长度
my_list.clear #删除
my_list.reverse #反转

```



#### 4. Tuple (元组)



元组是一个有序、不可变的元素集合。由于其不可变性，通常用于存储不希望被修改的数据。

**基本用法:**

Python

```
# 创建元组
my_tuple = (1, 'apple', 3.14, True)

# 访问元素
print(my_tuple[1]) # 'apple'

# 元组不可修改，以下操作会报错
# my_tuple[0] = 'one' # TypeError

# 元组解包
a, b, c, d = my_tuple
print(a, b, c, d)
```



#### 5. Set (集合)



集合是一个无序、不重复的元素集合。主要用于成员测试和去重。

**基本用法:**

Python

```
# 创建集合
my_set = {1, 2, 3, 2, 'apple'}
print(my_set) # {1, 2, 3, 'apple'}

# 添加元素
my_set.add(4)
print(my_set)

# 删除元素
my_set.remove(2)
print(my_set)

# 集合运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2) # 并集: {1, 2, 3, 4, 5}
print(set1 & set2) # 交集: {3}
print(set1 - set2) # 差集: {1, 2}
```



#### 6. Dictionary (字典)



字典是一个无序的键值对 (key-value) 集合，键必须是唯一的且不可变的。

**基本用法:**

Python

```
# 创建字典
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 访问值
print(my_dict['name']) # 'Alice'
print(my_dict.get('age')) # 25

# 修改值
my_dict['age'] = 26
print(my_dict)

# 添加键值对
my_dict['gender'] = 'Female'
print(my_dict)

# 删除键值对
my_dict.pop('city')
print(my_dict)

# 遍历字典
for key in my_dict:
for value in my_dict.values()
for key, value in my_dict.items():
    print(f"{key}: {value}")
```



### 三、 数据结构 (标准库及实现)





#### 7. Array (数组)



Python 的 `array` 模块提供了一种比列表更节省空间的数组，它要求所有元素必须是同一类型。

读很快。

**基本用法:**

Python

```
import array

# 创建一个整数数组
my_array = array.array('i', [1, 2, 3, 4, 5])

print(my_array[0]) # 1

# 只能添加相同类型的元素
my_array.append(6)
print(my_array)

# my_array.append('a') # TypeError
```



#### 8. Linked List (链表)



链表是一种线性数据结构，由一系列节点组成，每个节点包含数据和指向下一个节点的引用。Python 中没有内置的链表类型，通常需要自定义实现。

**基本用法 (概念实现):**

Python

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 使用
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display() # 1 -> 2 -> 3 -> None
```



#### 9. Hash Table (哈希表)



Python 的字典 (`dict`) 类型就是基于哈希表实现的。哈希表通过哈希函数将键映射到存储位置，以实现快速的查找、插入和删除操作。



#### 10. Queue (队列)



队列是一种先进先出 (FIFO, First-In-First-Out) 的数据结构。在 Python 中，推荐使用 `collections.deque` 来实现高效的队列操作。

**基本用法:**

Python

```
from collections import deque

# 创建队列
my_queue = deque(['a', 'b', 'c'])

# 入队 (在右侧添加)
my_queue.append('d')
print(my_queue) # deque(['a', 'b', 'c', 'd'])

# 出队 (从左侧移除)
element = my_queue.popleft()
print(element)      # 'a'
print(my_queue) # deque(['b', 'c', 'd'])
```



#### 11. Stack (栈)



栈是一种后进先出 (LIFO, Last-In-First-Out) 的数据结构。Python 的列表 `list` 可以很方便地用作栈。

**基本用法:**

Python

```
# 创建栈
my_stack = [1, 2, 3]

# 入栈 (在列表末尾添加)
my_stack.append(4)
print(my_stack) # [1, 2, 3, 4]

# 出栈 (从列表末尾移除)
element = my_stack.pop()
print(element)   # 4
print(my_stack) # [1, 2, 3]
```



#### 12. Heap (堆)



堆是一种特殊的树形数据结构，其任意节点的值都大于或等于 (大顶堆) 或小于或等于 (小顶堆) 其子节点的值。Python 的 `heapq` 模块提供了小顶堆的实现。

**基本用法:**

Python

```
import heapq

# 创建一个列表作为堆
my_heap = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(my_heap) # 将列表转换为堆
print(my_heap) # [1, 1, 2, 3, 5, 9, 4] (不一定是排序的，但满足堆的性质)

# 入堆
heapq.heappush(my_heap, 0)
print(my_heap)

# 出堆 (总是弹出最小的元素)
smallest = heapq.heappop(my_heap)
print(smallest) # 0
```



#### 13. Tree (树)



树是一种非线性的分层数据结构，由节点和连接节点的边组成。Python 中没有内置的树类型，通常需要自定义实现，例如二叉树。

**基本用法 (二叉树概念实现):**

Python

```
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# 创建一个简单的树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 树的遍历等操作需要通过递归或迭代函数实现
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

inorder_traversal(root) # 4 2 5 1 3
```