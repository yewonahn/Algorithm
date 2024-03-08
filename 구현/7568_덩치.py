import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    # 몸무게, 키
    a, b = map(int, input().split())
    lst.append([a, b])
for i in range(n):
    count = 0
    # 덩치 등수 = 나보다 덩치 큰 사람 + 1
    for a in range(n):
        if i != a:
            if lst[i][0] < lst[a][0] and lst[i][1] < lst[a][1]:
                count += 1
    # 공백 문자로 분리해서 한 줄에 출력
    print(count + 1, end=" ")
