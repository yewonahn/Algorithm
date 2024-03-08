import sys
input = sys.stdin.readline

# 인덱스 2를 기준으로,
# 뒤 요소들 저장 -> 앞에 요소들 저장
def remove(table):
    global order
    new = []
    if len(table) - 1 >= k:
        order.append(table[k])
        for i in range(k, len(table)):
            new.append(table[i])
    else:
        order.append(table[k-len(new)-1])
    if k != 1 and len(table) >= k-1:
        for j in range(0, k - 1):
            new.append(table[j])
    if len(table) < k-1:
        for q in range(0, len(table)-1):
            new.append(table[q])
    if len(order) != n:
        print(new)
        remove(new)

n, k = map(int, input().split())

first = []
order = []

for i in range(n):
    first.append(i+1)

remove(first)
print(order)

# for p in range(k):