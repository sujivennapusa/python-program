#deque-doubly entered queue
""" x=[1,2,3]
x.append(10)
print(x) """
import collections
x=collections.deque([1,2,3,4,5])
""" x.append(6)
x.appendleft(0) """
x.pop()
x.popleft()
print(x)