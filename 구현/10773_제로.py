import sys
input = sys.stdin.readline

k = int(input())
say = []

for i in range(k):
    n = int(input())
    if n == 0:
        say.pop()
    else:
        say.append(n)

result = 0
for i in say:
    result += i

print(result)
