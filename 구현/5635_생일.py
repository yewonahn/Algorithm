import sys
input = sys.stdin.readline

def check(l):
    global max, min
# 학생수
n = int(input())

old = 20110101 # 제일 많은
young = 0  # 제일 적은
old_name = ""
young_name = ""

for a in range(n):
    con = list(input().strip().split(" "))
    # print(con)
    for i in range(1, 3):
        if int(con[i]) < 10:
            con[i] = '0' + con[i]
            # print(con[i])
    s = [con[0], int(con[3]+con[2]+con[1])]
    # print(s)
    if s[1] > young:
        young = s[1]
        young_name = s[0]
    elif s[1] < old:
        old = s[1]
        old_name = s[0]
    # print(a, " : ")
    # print(young_name)
    # print(old_name)

print(young_name)
print(old_name)
