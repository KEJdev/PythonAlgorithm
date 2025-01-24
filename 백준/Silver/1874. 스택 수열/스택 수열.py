n = int(input())
target = [int(input()) for _ in range(n)]

current = 1
temp = []
result = []

for num in target:
    while current <= num:
        temp.append(current)
        result.append("+")
        current += 1
    if temp and temp[-1] == num:
        temp.pop()
        result.append("-")
    else:
        print("NO")
        exit()
print("\n".join(result))
