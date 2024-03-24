import sys
input = sys.stdin.readline

n, m = map(int, input().split())
first = []
for i in range(n):
    first.append(list(map(int, input().strip().split())))

second = []
# p = m
p, k = map(int, input().split())
for i in range(m):
    second.append(list(map(int, input().strip().split())))

cnt = k * m
for i in range(m):
    cnt -= second[i].count(0)
#print(cnt)
result = [[0] * cnt for _ in range(n)]
#print(result)

# first : [m][n] / second : [m][k]
x = 0
for a in range(m):
    for b in range(k):
        if second[a][b] != 0:
            #print('second[a][b] : ', second[a][b])
            for c in range(n):
                #p = first[c][a] * second[a][b]
                #print(first[c][a] * second[a][b])
                result[c][x] = first[c][a] * second[a][b]
            x += 1

for i in result:
    for j in i:
        print(j, end=' ')
    print()
