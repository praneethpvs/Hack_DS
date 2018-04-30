n = int(input())
x = []
for i in range(n):
    x.append(input().strip())
m = int(input())
y = []
for j in range(m):
    y.append(input().strip())
for k in y:
    print(x.count(k))
