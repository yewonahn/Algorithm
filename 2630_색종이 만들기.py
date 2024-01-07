import sys
input = sys.stdin.readline
 
n = int(input())
arr = []
w,b = 0,0
for i in range(n):
    arr.append(list(map(int,input().split())))
 
def solution(x,y,N) :
    global w,b
    color = arr[y][x]
    d = N//2
    for i in range(y,y+N) :
        for j in range(x,x+N) :
            if color != arr[i][j] :
                solution(x,y,d)
                solution(x+d,y,d)
                solution(x,y+d,d)
                solution(x+d,y+d,d)
                return 
    if color :
        b += 1
    else :
        w += 1
 
solution(0,0,n)
print(w,b,sep='\n')
