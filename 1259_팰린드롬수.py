arr = []

while True:
    val = input()
    if val == '0':
        break
    arr.append(val)

for i in arr:
    if i == i[::-1]:
        print('yes')
    else:
        print('no')