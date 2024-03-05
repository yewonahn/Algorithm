import sys

def push(n):
    global stack
    stack.append(n)

def pop():
    global stack
    if len(stack) == 0:
        return -1
    else:
        result = stack.pop()
        return result

def size():
    global stack
    result = len(stack)
    return result

def empty():
    global stack
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    global stack
    if len(stack) == 0:
        return -1
    else:
        result = stack[len(stack) - 1]
        return result

input = sys.stdin.readline
N = int(input())
stack = []

for i in range(N):
    order = input().split()
    if order[0] == 'pop':
        result = pop()
        print(result)
    elif order[0] == 'size':
        result = size()
        print(result)
    elif order[0] == 'empty':
        result = empty()
        print(result)
    elif order[0] == 'top':
        result = top()
        print(result)
    elif order[0] == 'push':
        n = order[1]
        push(n)