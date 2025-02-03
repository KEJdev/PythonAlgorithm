import sys
input_fast = sys.stdin.readline

n = int(input_fast().strip())
q = []

for _ in range(n):
    temp = input_fast().strip().split()
    if temp[0] == 'push':
        q.append(int(temp[1]))
    elif temp[0] == 'pop':
        print(q.pop(0) if q else -1)
    elif temp[0] == 'size':
        print(len(q))
    elif temp[0] == 'empty':
        print(1 if not q else 0)
    elif temp[0] == 'front':
        print(q[0] if q else -1)
    elif temp[0] == 'back':
        print(q[-1] if q else -1)
