# A.-United-We-Stand
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    _min = min(a)
    for i in a:
        if i == _min:
            b.append(i)
        elif _min == i and _min % i == 0:
            b.append(i)
        else:
            c.append(i)
    lenght = [len(b), len(c)]
    if len(b) == 0 or len(c) == 0:
        print(-1)
    else:
        print(*lenght)
        print(*b)
        print(*c)
