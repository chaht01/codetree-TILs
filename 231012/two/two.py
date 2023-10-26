n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))

ret = 0
for y in range(n-2):
    for x in range(n-2):
        ret = max(ret, 
        m[y][x] + m[y+1][x] + m[y+2][x] + m[y][x+1] + m[y+1][x+1] + m[y+2][x+1] + m[y][x+2] + m[y+1][x+2] + m[y+2][x+2])

print(ret)
