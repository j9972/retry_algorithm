import sys
input = sys.stdin.read

line = input().splitlines()
i = 0

while i < len(line):
    data = line[i]
    i += 1

    if data == '.':
        break

    st = []
    flag = True

    for c in data:
        if c == '(' or c == '[':
            st.append(c)
        elif c == ')':
            if not st or st[-1] != '(':
                flag = False
                break
            st.pop()
        elif c == ']':
            if not st or st[-1] != '[':
                flag = False
                break
            st.pop()
    
    if(flag and not st):
        print('yes')
    else:
        print('no')

    
