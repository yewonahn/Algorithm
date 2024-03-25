import sys
input = sys.stdin.readline

k = int(input())

# 참외 밭의 넓이를 구하면 됨
length = []
check = []
for i in range(6):
    a, b = map(int, input().split())
    length.append([a, b])
    check.append(a)

# 전체 = 부분 + 부분 -> 부분의 변의 방향 같
# 쪼개진 부분인 경우 : 방향 count == 2
s = 0
c = True
i = 0

while c:
    for j in range(i+1, 6):
        if length[i][0] == length[j][0]:
            # first == 20
            if i + 4 == j:
                # first == 20
                if length[i+1][1] < length[i+3][1]:
                    s = length[i + 2][1] * length[i + 3][1] - length[i][1] * length[i + 5][1]
                    c = False
                # first == 100
                else:
                    s = length[i + 1][1] * length[i + 2][1] - length[i + 4][1] * length[i + 5][1]
                    c = False
            else:
                # first == 60
                if i == 0 and check.count(length[5][0]) == 2:
                    s = length[i + 3][1] * length[i + 4][1] - length[i][1] * length[i + 1][1]
                    c = False
                # first == 30
                else:
                    if i == 0:
                        s = length[4][1] * length[5][1] - length[1][1] * length[2][1]
                        c = False
                    elif i == 1:
                        s = length[0][1] * length[5][1] - length[2][1] * length[3][1]
                        c = False
                    else:
                        s = length[0][1] * length[1][1] - length[3][1] * length[4][1]
                        c = False
    i += 1
print(s*k)
