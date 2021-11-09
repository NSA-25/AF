def BFS(file, file2):              # 100 infoarena
    import collections
    f = open(file, "r")
    g = open(file2, "w")
    n, m, s = [int(n) for n in f.readline().split()]
    d = {}
    for i in range(1, n+1):
        d[i] = []
    for i in range(m):
        n1, n2 = [int(n) for n in f.readline().split()]
        d[n1].append(n2)
    q = collections.deque()
    q.append(s)
    r = (n+1)*[-1]
    r[s] = 0
    v = (n+1)*[False]
    v[s] = True
    while q:
        n = q.popleft()
        for i in d[n]:
            if v[i] is False:
                q.append(i)
                v[i] = True
                r[i] = r[n] + 1
    g.write(" ".join(str(n) for n in r[1:]))
    f.close()
    g.close()
BFS("bfs.in", "bfs.out")
