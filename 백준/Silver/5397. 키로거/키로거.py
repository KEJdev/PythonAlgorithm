from collections import deque
import sys

def process_input(operations):
    left = deque() 
    right = deque()  

    for op in operations:
        if op == '<':  
            if left:
                right.appendleft(left.pop())
        elif op == '>':
            if right:
                left.append(right.popleft())
        elif op == '-':
            if left:
                left.pop()
        else:
            left.append(op)

    return ''.join(left) + ''.join(right)

input = sys.stdin.read
data = input().splitlines()

test_cases = int(data[0])

results = []
for i in range(1, test_cases + 1):
    operations = data[i]
    results.append(process_input(operations))

# 결과 출력
sys.stdout.write('\n'.join(results) + '\n')
