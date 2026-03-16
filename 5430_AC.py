import sys
input = sys.stdin.readline

from collections import deque

for tc in range(int(input())):

    p = input()
    n = int(input())
    arr = input().rstrip()[1:-1]  

    if n == 0 or arr == '':
        new_arr = deque()
    else:
        new_arr = deque(map(int, arr.split(',')))
    
    reverse_flag, flag = False, False

    for char in p:
        if char == 'R':
            reverse_flag = not reverse_flag
        elif char == 'D':
            if len(new_arr) == 0:
                flag = True
                break
                
            
            if reverse_flag:
                new_arr.pop()
            else:
                new_arr.popleft()
    
    if flag:
        print('error')
    else:
        if reverse_flag:
            print('[' + ','.join(map(str, reversed(new_arr))) + ']')
        else:
            print('[' + ','.join(map(str, new_arr)) + ']')