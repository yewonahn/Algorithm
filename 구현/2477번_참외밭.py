import sys
input = sys.stdin.readline

k = int(input())

lst_x, lst_y, total = [], [], []
idx_max_x, idx_max_y = 0, 0
idx_total_x, idx_total_y = 0, 0

for i in range(6):
    dir, l = map(int, input().split())
    total.append(l)
    # dir == 1 / dir == 2 -> 평행
    if dir == 1 or dir == 2:
        lst_x.append(l)
        if max(lst_x) == l:
            idx_max_x = len(lst_x) - 1
            idx_total_x = i
    # dir == 3 / dir == 4 -> 평행
    else:
        lst_y.append(l)
        if max(lst_y) == l:
            idx_max_y = len(lst_y) - 1
            idx_total_y = i

min_x = abs(total[(idx_total_y - 1) % 6] - total[(idx_total_y + 1) % 6])
min_y = abs(total[(idx_total_x - 1) % 6] - total[(idx_total_x + 1) % 6])

s = max(lst_x) * max(lst_y) - min_x * min_y
print(s * k)
