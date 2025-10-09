import sys
input = sys.stdin.readline

n = int(input())

cur_val = 1
cur_phase = list()
temp_list = list()
flag = True

for i in range(n):
    num = int(input())
    while cur_val <= num:
        temp_list.append(cur_val)
        cur_phase.append('+')
        cur_val += 1
    if temp_list[-1] == num:
        temp_list.pop()
        cur_phase.append('-')
    else:
        flag = False
        break
    
if(flag == False):
    print('NO')
else:
    for i in cur_phase:
        print(i)
    