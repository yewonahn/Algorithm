import sys

def check(i):
    global word, count

    if word[i] == 'c':
        if word[i+1] == '=' or word[i+1] == '-':
            count -= 1
    elif word[i] == 'z' and word[i+1] == '=':
        if i >= 1:
            if word[i-1] == 'd':
                count -= 2
            else:
                count -= 1
        else:
            count -= 1
    elif word[i] == 'd' and word[i+1] == '-':
        count -= 1
    elif word[i+1] == 'j':
        if word[i] == 'l' or word[i] == 'n':
            count -= 1
    elif word[i] == 's' and word[i+1] == '=':
        count -= 1

    if i + 1 <= len(word) - 2:
        check(i+1)

input = sys.stdin.readline

word = list(input())
word.pop()
print(word)
count = len(word)

check(0)
print(count)
