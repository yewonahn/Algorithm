import sys
input = sys.stdin.readline
s = input().rstrip()
answer = 0
pipe = 0
flag = False
for i in s:
    if i == '(':
        flag = True
        pipe += 1
    elif i == ')' and flag:
        pipe -= 1
        answer += pipe
        flag = False
    elif i == ')' and not flag:
        pipe -= 1
        answer += 1
print(answer)
