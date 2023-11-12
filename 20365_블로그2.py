import sys
input = sys.stdin.readline

N = int(input())
s = input().rstrip()
dict = {'B': 0,'R': 0}
dict[s[0]] += 1

for i in range(1,N):
    if s[i] != s[i-1]:
        dict[s[i]] += 1

answ = min(dict['B'],dict['R'])+1
print(answ)
