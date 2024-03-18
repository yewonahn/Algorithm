# 태그 <> - 알파벳만
# 단어 - 알파벳, 숫자로만
# 태그 단어 사이에 공백 없음

# 단어만 뒤집어서 출력

import sys
input = sys.stdin.readline

s = list(input().strip())
print(s)
lst = []

i = 0
while i < len(s):
    save = []
    if s[i] == "<":
        save.append("<")
        for a in range(i+1, len(s)):
            save.append(s[a])
            if s[a] == ">":
                save.append(">")
                i = a + 1
                lst.append(save)
                break
    else:
        while s[i] != " ":
            save.append(s[i])
            i += 1
        i += 1
        save.reverse()
        lst.append(save)
