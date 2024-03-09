import sys
input = sys.stdin.readline

# 도화지 100
# 색종이 10 고정

# 색종이 수
n = int(input())
lst = []
same = 0
for i in range(n):
    # x, y
    x, y = map(int, input().split())
    lst.append([x, y])

for a in range(0, n - 1):
    for b in range(a + 1, n):
        print("a : ", a, " / b : ", b)
        if -10 < lst[a][0] - lst[b][0] < 10 and -10 < lst[a][1] - lst[b][1] < 10:
            same = same + (lst[a][0] + 10 - lst[b][0]) * (lst[b][1] + 10 - lst[a][1])
            print(a+1, "try)", "same = ", same)
            # 음수 나오는지 확인

            # 2개 이상이 겹치는 경우

s = 100 * n - same
print(s)
