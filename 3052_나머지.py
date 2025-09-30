s = set()
l = list()

for i in range(10):
    data = int(input())
    s.add(data%42)

print(len(s))