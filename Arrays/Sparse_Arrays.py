n = int(input())
x = []
for i in range(n):
    x.append(raw_input().strip())
m = int(input())
y = []
for j in range(m):
    y.append(raw_input().strip())
for k in y:
    print x.count(k)