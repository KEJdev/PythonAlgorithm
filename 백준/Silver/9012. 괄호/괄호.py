n = int(input())
answer = []

for i in range(n):
    temp = input()
    vps_ck = []
    for idx, j in enumerate(temp):
        if j == '(':
            vps_ck.append(j)
        elif j == ')':
            if len(vps_ck) != 0 :
                vps_ck.pop()
            else:
                vps_ck.append(')')
                break
    if len(vps_ck) != 0:
        answer.append("NO")
    else:
        answer.append("YES")

for i in answer:
    print(i)
