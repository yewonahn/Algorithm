# 풀이 참조 (discard 사용)
import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    con = list(input().split())
    # x = int(con[1]) -> all, empty 인 경우 KeyError

    if con[0] == "add":
        s.add(int(con[1]))
    elif con[0] == "remove":
        # remove() -> discard()
        s.discard(int(con[1]))
    elif con[0] == "check":
        if int(con[1]) in s:
            print(1)
        else:
            print(0)
    elif con[0] == "toggle":
        if int(con[1]) in s:
            s.remove(int(con[1]))
        else:
            s.add(int(con[1]))
    elif con[0] == "all":
        s.clear()
        s = {i for i in range(1, 21)}
    elif con[0] == "empty":
        s.clear()
