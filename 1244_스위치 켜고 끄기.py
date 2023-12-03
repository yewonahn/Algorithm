n = int(input())
switch = [0] + list(map(int, input().split()))

def change(x):
    global switch
    switch[x] = abs(switch[x]-1)


for _ in range(int(input())):
    gender, no = map(int, input().split())
    i = 1
    # 남자
    if gender == 1:
        while no * i <= n:
            change(no * i)
            i += 1
    # 여자
    elif gender == 2:
        change(no)
        while 1 <= no-i and no+i <= n and switch[no-i] == switch[no+i]:
            change(no-i)
            change(no+i)
            i += 1

for i in range(1, n+1):
    print(switch[i], end=" ")
    if not i % 20:
        print()
