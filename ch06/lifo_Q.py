from queue import LifoQueue
from queue import Full
from queue import Empty

# Demonstration of LIFO Queue which implements stack behavour

stack = LifoQueue(maxsize=3)
stack.put("one")
stack.put("two")
stack.put("three")
try:
    stack.put("four", block=False)
except Full as e:
    print("Stack is full")

print("stack.get() = {}".format(stack.get()))
print("stack.get() = {}".format(stack.get()))
print("stack.get() = {}".format(stack.get()))
print("stack.empty() = {}".format(stack.empty()))
try:
    stack.get(timeout=1)
except Empty as e:
    print("Stack is empty")
