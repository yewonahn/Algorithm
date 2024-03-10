import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    con = list(input().split())
    x = con[1]

    if con[0] == "add":
        s.add(x)
    elif con[0] == "remove":
        s.remove(x)
    elif con[0] == "check":
        if x in s:
            print(1)
        else:
            print(0)
    elif con[0] == "toggle":
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif con[0] == "all":
        s.clear()
        s = {i for i in range(1, 21)}
    elif con[0] == "empty":
        s.clear()