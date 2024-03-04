import sys

def checker(word):
    check = []
    last = ' '
    isGroup = True
    for i in word:
        # 처음 나온 경우
        if i not in check:
            check.append(i)
            last = i
        # 떨어져서 나온 경우
        elif i in check and last != i:
            isGroup = False
            break
    return isGroup


input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    word = list(input())
    if (checker(word)):
        count += 1

print(count)