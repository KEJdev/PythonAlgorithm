int_x = int(input())
temp_list = list()

for i in range(int_x):
    temp = input().split(' ')

    if temp[0] == 'push':
        temp_list.append(temp[1])

    elif temp[0] == 'pop':
        if temp_list:
            print(temp_list.pop(-1))
        else:
            print(-1)

    elif temp[0] == 'size':
        print(len(temp_list))

    elif temp[0] == 'top':
        if len(temp_list) != 0:
            print(temp_list[-1])
        else:
            print(-1)

    elif temp[0] == 'empty':
        if not temp_list:
            print(1)
        else:
            print(0)
