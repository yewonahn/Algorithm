import sys
input = sys.stdin.readline
 
n = int(input().rstrip())
 
tip = []
for i in range(n):
    tip.append(int(input().rstrip()))
 
tip.sort(reverse=True)
 
total = 0
for i in range(n):
    tmp = tip[i] - i
    if tmp > 0:
        total += tmp
 
print(total)
