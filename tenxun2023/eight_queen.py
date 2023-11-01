import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#str = input()

n = 4
pos = [None] * n

cnt = 0

def backtrack(pos, row):
    global cnt
    if row == n:
        cnt += 1
        print("HHH", pos)
        return
    for i in range(n):
        pos[row] = i
        print(pos, no_conflict(pos, row))
        if no_conflict(pos, row):
            backtrack(pos, row+1)
        pos[row] = None

def no_conflict(pos, row):
    for i in range(len(pos)):
        if i == row or pos[i] is None:
            continue
        if pos[row] == pos[i] or \
            pos[row] - row == pos[i] - i or \
            pos[row] + row == pos[i] + i:
            return False
    return True

backtrack(pos, 0)

print(cnt)