import sys
input = sys.stdin.readline

n = int(input())
# 빨 c / 파 p / 초 z / 노 y
board = [list(map(str, input().strip())) for _ in range(n)]
#print('**original board**')
#print(board)

# 먹을 수 있는 최대 개수
# 3 ≤ N ≤ 50 -> 완전 탐색

# 가로 확인
def check_w(x, y):
    global cnt
    if x + 1 < n and y < n and board[y][x] == board[y][x + 1]:
        cnt += 1
        check_w(x+1, y)

# 세로 확인
def check_l(x, y):
    global cnt
    if y + 1 < n and x < n and board[y][x] == board[y+1][x]:
        cnt += 1
        check_l(x, y+1)

def count():
    global max, cnt
    for a in range(n):
        for b in range(n-1):
            # (b, a) 현재 테스트 하는 점
            # 가로 확인
            #print('현재 테스트 하는 점 : ', b, ',', a)
            cnt = 1
            check_w(b, a)
            if cnt > max:
                #print('가로 확인 cnt > max : ', cnt, ',', max)
                max = cnt
            # 세로 확인
            cnt = 1
            check_l(b, a)
            if cnt > max:
                #print('check_l', b, a)
                #print('세로 확인 cnt > max : ', cnt, ',', max)
                max = cnt


max = 0
cnt = 0
for i in range(n):
    for j in range(n-1):
        # 가로 교환 (오른쪽)
        if j+1 < n and board[i][j] != board[i][j+1]:
            tmp = board[i][j]
            board[i][j] = board[i][j+1]
            board[i][j + 1] = tmp
            #print('--change board (가로)--')
            #print(board)
            count()
            # 원상 복귀
            tmp = board[i][j]
            board[i][j] = board[i][j + 1]
            board[i][j + 1] = tmp
            # 세로 교환 (아래)
        if i+1 < n and board[i][j] != board[i+1][j]:
            tmp = board[i][j]
            board[i][j] = board[i+1][j]
            board[i+1][j] = tmp
            #print('--change board (세로)--')
            #print(board)
            count()
            # 원상 복귀
            tmp = board[i][j]
            board[i][j] = board[i + 1][j]
            board[i + 1][j] = tmp

print(max)
