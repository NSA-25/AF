def Bellman(file, file2):
    from collections import deque
    f = open(file, "r")
    g = open(file2, "w")
    n, m = [int(n) for n in f.readline().split()]
    L = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, c = [int(n) for n in f.readline().split()]
        L[u].append([c, v])
    d = (n+1)*[float('inf')]
    d[1] = 0
    q = deque()
    q.append([0, 1])
    stop = 0
    flag = True
    while q:
        if stop == n*m:
            flag = False
            break
        stop += 1
        u = q.popleft()[1]
        for l in L[u]:
            c, v = l
            if d[u] + c < d[v]:
                d[v] = d[u] + c
                q.append(l)
    if flag:
        g.write(" ".join(['0' if n == float('inf') else str(n) for n in d[2:]]))
    else:
        g.write("Ciclu negativ!")
Bellman("bellmanford.in", "bellmanford.out")
